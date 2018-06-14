from sawtooth_sdk.processor.exceptions import InvalidTransaction

class WalPayload(object):

	def __init__(self,payload):

		try:
			name,action,pubkey = payload.decode().split(",")
		except ValueError:
			raise InvalidTransaction("Invalid payload serialization")

		#Add different type of exceptions

		self._name = name
		self._action = action
		self._pubkey = pubkey

	@staticmethod
	def from_bytes(payload):
		return WalPayload(payload=payload)

	@property
	def name(self):
		return self._name
	
	@property
	def action(self):
		return self._action

	@property
	def pubkey(self):
		return self._pubkey