import logging


from sawtooth_sdk.processor.handler import TransactionHandler
from sawtooth_sdk.processor.exceptions import InvalidTransaction
from sawtooth_sdk.processor.exceptions import InternalError

from hw_payload import HwPayload
from hw_state import Item
from hw_state import HwState
from hw_state import HW_NAMESPACE


LOGGER = logging.getLogger(__name__)






class HwTransHand(TransactionHandler):


	@property
	def family_name(self):
		return 'hw'

	@property
	def family_versions(self):
		return ['1.0']

	@property
	def namespaces(self):
		return [HW_NAMESPACE]

	#apply method will be calledd by the validator probably ??

	def apply(self,transaction,context):
		header = transaction.header
		signer = header.signer_public_key

		hwpayload = HwPayload.from_bytes(transaction.payload)
		hwstate = HwState(context)

		if hwpayload.action == 'delete':

			item = hwstate.get_item(hwpayload.name)

			if item is None:
				raise InvalidTransaction('Invalid Action')

			hwstate.delete_item(hwpayload.name)

		elif hwpayload.action == 'create' :
			if hwstate.get_item(hwpayload.name) is not None:
				raise InvalidTransaction('Invalid Item Exists')

			item = Item(name = hwpayload.name,check = "-" * 2 ,
						c_addr = hwpayload.cu_add , p_addr = None)
			hwstate.set_item(hwpayload.name,item)
			_display("Item {} created by {}".format(hwpayload.name,hwpayload.cu_add))



		elif hwpayload.action == 'send' :
			item = hwstate.get_item(hwpayload.name)
			if item is None:
				raise InvalidTransaction('Item not yet created')

			if hwstate.vldt_item(hwpayload.name,hwpayload.cu_add):

				item.p_addr = hwpayload.cu_add
				item.c_addr = hwpayload.nxt_add

				hwstate.set_item(hwpayload.name,item)
				_display("Item {} sent to {} by {}".format(hwpayload.name,hwpayload.nxt_add,hwpayload.cu_add))
			else:
				print("Invalid transaction")


def _display(msg):
	n = msg.count("\n")

	if n>0:
		msg = msg.split("\n")
		length = max(len(line) for line in msg)
	else:
		length = len(msg)
		msg = [msg]

	LOGGER.debug("+"+(length+2)*"-"+"+")
	for line in msg:
		LOGGER.debug("+"+line.center(length)+"+")

	LOGGER.debug("+"+(length+2)*"-"+"+")





