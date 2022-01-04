# Cak Nyut

import sys
import time
import argparse
import janu
from janu import WhatAmI

# initiate logging
janu.init_logger()

print("Scouting...")
hellos = janu.scout(WhatAmI.Peer | WhatAmI.Router, 1.0)

for hello in hellos:
    print(hello)
