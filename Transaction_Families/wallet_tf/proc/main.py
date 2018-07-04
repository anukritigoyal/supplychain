from sawtooth_sdk.processor.core import TransactionProcessor
from wal_transhand import WalTransHand
import argparse
#add a processor handler

parser = argparse.ArgumentParser()
parser.add_argument("url")
args = parser.parse_args()
processor = TransactionProcessor(url=args.url)
handler = WalTransHand()
processor.add_handler(handler)
processor.start()
