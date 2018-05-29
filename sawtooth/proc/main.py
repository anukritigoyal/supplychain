from sawtooth_sdk.processor.core import TransactionProcessor
from hw_transhand import HwTransHand

#add a processor handler

def main():
	processor = TransactionProcessor(url='tcp://127.0.0.1:4004')
	handler = HwTransHand()
	processor.add_handler(handler)
	print("I am in")
	processor.start()

main()
