from sawtooth_sdk.processor.exceptions import InvalidTransaction

class HwPayload(object):

	def __init__(self,payload):

		try:
			name,action,cu_add,nxt_add = payload.decode().split(",")
		except ValueError:
			raise InvalidTransaction("Invalid payload serialization")

		#Add different type of exceptions
		self._name = name
		self._action = action
		self._cu_add = cu_add
		self._nxt_add = nxt_add

	@staticmethod
	def from_bytes(payload):
		return HwPayload(payload=payload)

	@property
	def name(self):
		return self._name
	
	@property
	def action(self):
		return self._action

	@property
	def cu_add(self):
		return self._cu_add
	
	@property
	def nxt_add(self):
		return self._nxt_add