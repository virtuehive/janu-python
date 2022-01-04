# Cak Nyut

import sys
import time
import argparse
import itertools
import janu
from janu import config

# --- Command line argument parsing --- --- --- --- --- ---
parser = argparse.ArgumentParser(
    prog='j_pub',
    description='janu pub example')
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
                    default='/demo/example/janu-python-pub',
                    type=str,
                    help='The key expression to publish onto.')
parser.add_argument('--value', '-v', dest='value',
                    default='Pub from Python!',
                    type=str,
                    help='The value to publish.')
parser.add_argument("--iter", dest="iter", type=int, help="How many puts to perform")
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
value = args.value

# janu-net code  --- --- --- --- --- --- --- --- --- --- ---

# initiate logging
janu.init_logger()

print("Openning session...")
session = janu.open(conf)

print("Declaring key expression '{}'...".format(key), end='')
rid = session.declare_expr(key)
print(" => RId {}".format(rid))

print("Declaring publication on '{}'...".format(rid))
session.declare_publication(rid)

for idx in itertools.count() if args.iter is None else range(args.iter):
    time.sleep(1)
    buf = "[{:4d}] {}".format(idx, value)
    print("Putting Data ('{}': '{}')...".format(rid, buf))
    session.put(rid, bytes(buf, encoding='utf8'))

session.undeclare_publication(rid)
session.undeclare_expr(rid)
session.close()
