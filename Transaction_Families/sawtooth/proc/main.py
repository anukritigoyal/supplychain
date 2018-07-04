from sawtooth_sdk.processor.core import TransactionProcessor
from hw_transhand import HwTransHand
import argparse

#add a processor handler

parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()
processor = TransactionProcessor(url=args.url)
handler = HwTransHand()
processor.add_handler(handler)
processor.start()
