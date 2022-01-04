# Cak Nyut

import sys
import time
import datetime
import argparse
import janu
from janu import  Reliability, SubMode

# --- Command line argument parsing --- --- --- --- --- ---
parser = argparse.ArgumentParser(
    prog='j_sub_thr',
    description='janu throughput sub example')
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
parser.add_argument('--samples', '-s', dest='samples',
                    default=10,
                    metavar='NUMBER',
                    action='append',
                    type=int,
                    help='Number of throughput measurements.')
parser.add_argument('--number', '-n', dest='number',
                    default=50000,
                    metavar='NUMBER',
                    action='append',
                    type=int,
                    help='Number of messages in each throughput measurements.')
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
m = args.samples
n = args.number

# janu-net code  --- --- --- --- --- --- --- --- --- --- ---


def print_stats(start):
    stop = datetime.datetime.now()
    print("{:.6f} msgs/sec".format(n / (stop - start).total_seconds()))


count = 0
start = None
nm = 0


def listener(sample):
    global n, m, count, start, nm
    if count == 0:
        start = datetime.datetime.now()
        count += 1
    elif count < n:
        count += 1
    else:
        print_stats(start)
        nm += 1
        count = 0
        if nm >= m:
            sys.exit(0)


# initiate logging
janu.init_logger()

session = janu.open(conf)

rid = session.declare_expr('/test/thr')

sub = session.subscribe(rid, listener, reliablity=Reliability.Reliable, mode=SubMode.Push)

time.sleep(600)

session.undeclare_expr(rid)
session.close()