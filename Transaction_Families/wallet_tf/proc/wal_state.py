import hashlib
from sawtooth_sdk.processor.exceptions import InternalError

WAL_NAMESPACE = hashlib.sha512('wal'.encode("utf-8")).hexdigest()[0:6]

def _make_wal_address(name):
	return WAL_NAMESPACE + \
		hashlib.sha512(name.encode('utf-8')).hexdigest()[:64]

class Pair(object):
	def __init__(self,name,pubkey,prof):
		self.name = name
		self.pubkey = pubkey
		self.prof = prof

class WalState(object):
	TIMEOUT = 3
	def __init__(self,context):
		self._context = context
		self._address_cache = {}

	def delete_pair(self,pair_name):
		pairs = self._load_pairs(pair_name= pair_name)

		del pairs[pair_name]
		if pairs:
			self._store_pair(pair_name,pairs = pairs)
		else:
			self._delete_pair(pair_name)

	def set_pair(self,pair_name,pair):
		pairs = self._load_pairs(pair_name= pair_name)
		pairs[pair_name] = pair
		self._store_pair(pair_name,pairs = pairs)

	def get_pair(self,pair_name):
		return self._load_pairs(pair_name=pair_name).get(pair_name)

	def _store_pair(self,pair_name,pairs):

		address = _make_wal_address(pair_name)
		state_data = self._serialize(pairs)
		self._address_cache[address] = state_data
		self._context.set_state({address: state_data},timeout=self.TIMEOUT)
		



	def _delete_pair(self,pair_name):
		address = _make_wal_address(pair_name)
		self._context.delete_state([address],timeout=self.TIMEOUT)
		self._address_cache[address] = None

	def _load_pairs(self,pair_name):
		address = _make_wal_address(pair_name)
		if address in self._address_cache:
			if self._address_cache[address]:
				serialized_pairs = self._address_cache[address]
				pairs = self._deserialize(serialized_pairs)
			else:
				pairs = {}
		else:
			state_entries = self._context.get_state([address],timeout=self.TIMEOUT)
			
			if state_entries :
				self._address_cache[address] = state_entries[0].data
				
				pairs = self._deserialize(data=state_entries[0].data)

			else:
				self._address_cache[address] = None
				pairs = {}

		return pairs

	def _deserialize(self,data):
		pairs = {}
		try:
			for pair in data.decode().split("|"):
				name,pubkey,prof = pair.split(",")
				pairs[name] = Pair(name,pubkey,prof)

		except ValueError:
			raise InternalError("Failed to deserialize pairs data")

		return pairs

	def _serialize(self, pairs):
		pair_strs =[]
		for name,g in pairs.items():
			pair_str = ",".join(
				[name,g.pubkey,g.prof])

			pair_strs.append(pair_str)

		return "|".join(sorted(pair_strs)).encode()