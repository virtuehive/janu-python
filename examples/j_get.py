# Cak Nyut

import sys
import time
import argparse
import janu
from janu import config, queryable, QueryTarget, Target

# --- Command line argument parsing --- --- --- --- --- ---
parser = argparse.ArgumentParser(
    prog='j_get',
    description='janu get example')
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
parser.add_argument('--selector', '-s', dest='selector',
                    default='/demo/example/**',
                    type=str,
                    help='The selection of resources to query.')
parser.add_argument('--kind', '-k', dest='kind',
                    choices=['ALL_KINDS', 'STORAGE', 'EVAL'],
                    default='ALL_KINDS',
                    type=str,
                    help='The KIND of queryables to query.')
parser.add_argument('--target', '-t', dest='target',
                    choices=['ALL', 'BEST_MATCHING', 'ALL_COMPLETE', 'NONE'],
                    default='ALL',
                    type=str,
                    help='The target queryables of the query.')
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
selector = args.selector
kind = {
    'ALL_KINDS': queryable.ALL_KINDS,
    'STORAGE': queryable.STORAGE,
    'EVAL': queryable.EVAL}.get(args.kind)
target = {
    'ALL': Target.All(),
    'BEST_MATCHING': Target.BestMatching(),
    'ALL_COMPLETE': Target.AllComplete(),
    'NONE': Target.No()}.get(args.target)

# janu-net code  --- --- --- --- --- --- --- --- --- --- ---

# initiate logging
janu.init_logger()

print("Openning session...")
session = janu.open(conf)

print("Sending Query '{}'...".format(selector))
replies = session.get_collect(selector, target=QueryTarget(kind, target))
for reply in replies:
    print(">> Received ('{}': '{}')"
          .format(reply.data.key_expr, reply.data.payload.decode("utf-8")))

session.close()
