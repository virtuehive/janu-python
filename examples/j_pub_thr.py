# Cak Nyut

import sys
import time
import argparse
import janu
from janu import config, CongestionControl

# --- Command line argument parsing --- --- --- --- --- ---
parser = argparse.ArgumentParser(
    prog='j_pub_thr',
    description='janu throughput pub example')
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
parser.add_argument('payload_size',
                    type=int,
                    help='Sets the size of the payload to publish.')
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
size = args.payload_size

# janu-net code  --- --- --- --- --- --- --- --- --- --- ---

# initiate logging
janu.init_logger()

data = bytearray()
for i in range(0, size):
    data.append(i % 10)
data = bytes(data)
congestion_control = CongestionControl.Drop

session = janu.open(conf)

rid = session.declare_expr('/test/thr')

pub = session.declare_publication(rid)

while True:
    session.put(rid, data, congestion_control=congestion_control)
