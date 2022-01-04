# Cak Nyut

import sys
import time
from datetime import datetime
import argparse
import janu
from janu import Reliability, SubMode

# --- Command line argument parsing --- --- --- --- --- ---
parser = argparse.ArgumentParser(
    prog='j_pull',
    description='janu pull example')
parser.add_argument('--mode', '-m', dest='mode',
                    choices=['peer', 'client'],
                    type=str,
                    help='The janu session mode.')
parser.add_argument('--peer', '-e', dest='peer',
                    metavar='LOCATOR',
                    action='append',
                    type=str,
                    help='Peer locators used to initiate the janu session.')
parser.add_argument('--listener', '-l', dest='listener',
                    metavar='LOCATOR',
                    action='append',
                    type=str,
                    help='Locators to listen on.')
parser.add_argument('--key', '-k', dest='key',
                    default='/demo/example/**',
                    type=str,
                    help='The key expression matching resources to pull.')
parser.add_argument('--config', '-c', dest='config',
                    metavar='FILE',
                    type=str,
                    help='A configuration file.')

args = parser.parse_args()
conf = janu.config_from_file(args.config) if args.config is not None else janu.Config()
if args.mode is not None:
    conf.insert_json5("mode", args.mode)
if args.peer is not None:
    conf.insert_json5("peers", f"[{','.join(args.peer)}]")
if args.listener is not None:
    conf.insert_json5("listeners", f"[{','.join(args.listener)}]")
key = args.key

# janu-net code  --- --- --- --- --- --- --- --- --- --- ---


def listener(sample):
    time = '(not specified)' if sample.source_info is None or sample.timestamp is None else datetime.fromtimestamp(
        sample.timestamp.time)
    print(">> [Subscriber] Received {} ('{}': '{}')"
          .format(sample.kind, sample.key_expr, sample.payload.decode("utf-8"), time))


# initiate logging
janu.init_logger()

print("Openning session...")
session = janu.open(conf)

print("Creating Subscriber on '{}'...".format(key))

sub = session.subscribe(key, listener, reliability=Reliability.Reliable, mode=SubMode.Pull)

print("Press <enter> to pull data...")
c = '\0'
while c != 'q':
    c = sys.stdin.read(1)
    if c == '':
        time.sleep(1)
    else:
        sub.pull()

sub.close()
session.close()
