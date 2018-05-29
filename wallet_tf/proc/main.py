from sawtooth_sdk.processor.core import TransactionProcessor
from wal_transhand import WalTransHand

#add a processor handler

def main():
	processor = TransactionProcessor(url='tcp://127.0.0.1:4004')
	handler = WalTransHand()
	processor.add_handler(handler)
	print("I am in")
	processor.start()

main()	