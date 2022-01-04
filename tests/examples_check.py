from os import path
from subprocess import Popen, PIPE
import time

examples = path.dirname(path.realpath(__file__)).replace('tests', 'examples')
tab = "\t"
ret = "\r\n"
KILL = -9

class Pyrun:
	def __init__(self, p, args=None) -> None:
		if args is None:
			args = []
		self.name = p
		print(f"starting {self.name}")
		self.process: Popen = Popen(["python3", path.join(examples, p), *args], stdin=PIPE, stdout=PIPE, stderr=PIPE)
		self.start = time.time()
		self.end = None
		self._stdouts = []
		self._stderrs = []
	def dbg(self):
		self.wait()
		print("stdout:")
		print(f"{tab}{tab.join(self.stdout)}")
		print("stderr:")
		print(f"{tab}{tab.join(self.stderr)}")
	def status(self, expecting=0, do_print=True):
		status = self.wait()
		formatted = f"{self.name}: returned {status} (expected {expecting}) - {self.time:.2}s"
		if do_print:
			print(formatted)
		return formatted if status != expecting else None
	def wait(self):
		code = self.process.wait()
		if self.end is None:
			self.end = time.time()
		return code
	@property
	def stdout(self):
		self._stdouts.extend(line.decode('utf8') for line in self.process.stdout.readlines())
		return self._stdouts
	@property
	def stderr(self):
		self._stderrs.extend(line.decode('utf8') for line in self.process.stderr.readlines())
		return self._stderrs
	@property
	def time(self):
		return None if self.end is None else (self.end - self.start)

errors = []

info = Pyrun("j_info.py")
if info.status():
	info.dbg()
	errors.append(info.status())
scout = Pyrun("j_scout.py")
if scout.status():
	scout.dbg()
	errors.append(scout.status())

storage = Pyrun("j_storage.py")
sub = Pyrun("j_sub.py")
pull = Pyrun("j_pull.py")
time.sleep(1)
put = Pyrun("j_put.py")
if put.status():
	put.dbg()
	errors.append(put.status())
time.sleep(1)
pub = Pyrun("j_pub.py", ["--iter=2"])
time.sleep(3)
try:
	pull.process.stdin.write(b"\n")
	pull.process.stdin.flush()
	time.sleep(1)
	pull.process.stdin.write(b"q\n")
	pull.process.stdin.flush()
	pull.process.stdin.close()
except Exception as e:
	pull.dbg()
	errors.append(f"pull stdin sequence failed: {e}")
if pub.status():
	pub.dbg()
	errors.append(pub.status())
if pull.status():
	pull.dbg()
	errors.append(pull.status())
subout = "".join(pull.stdout)
if not ("Received PUT ('/demo/example/janu-python-put': 'Put from Python!')" in subout):
	errors.append("j_pull didn't catch put")
if not ("Received PUT ('/demo/example/janu-python-pub': '[   1] Pub from Python!')" in subout):
	errors.append("j_pull didn't catch second j_pub")
if any(("j_pull" in error) for error in errors):
	pull.dbg()

eval = Pyrun("j_eval.py", ["-k=/demo/example/janu-python-eval"])
time.sleep(1)
get = Pyrun("j_get.py", ["-s=/demo/example/janu-python-eval"])
if get.status():
	get.dbg()
	errors.append(get.status())
if not ("Received ('/demo/example/janu-python-eval': 'Eval from Python!')" in "".join(get.stdout)):
	get.dbg()
	eval.dbg()
	errors.append("j_get didn't get a response from j_eval")

try:
	eval.process.stdin.write(b"q\n")
	eval.process.stdin.flush()
	eval.process.stdin.close()
except Exception as e:
	errors.append(f"eval stdin sequence failed: {e}")
if eval.status():
	eval.dbg()
	errors.append(eval.status())
evalout = "".join(eval.stdout)
if not ("Received Query '/demo/example/janu-python-eval'" in evalout):
	errors.append("j_eval didn't catch query")
if any(("j_eval" in error) for error in errors):
	eval.dbg()

time.sleep(1)
get = Pyrun("j_get.py", ["-s=/demo/example/janu-python-put"])
if get.status():
	get.dbg()
	errors.append(get.status())
if not ("Received ('/demo/example/janu-python-put': 'Put from Python!')" in "".join(get.stdout)):
	storage.dbg()
	errors.append("j_get didn't get a response from j_storage about put")
if not ("Received ('/demo/example/janu-python-put': 'Put from Python!')" in "".join(get.stdout)):
	storage.dbg()
	errors.append("j_get didn't get a response from j_storage about put")
if any(("j_get" in error) for error in errors):
	get.dbg()

time.sleep(1)
delete = Pyrun("j_delete.py")
if delete.status():
	delete.dbg()
	errors.append(delete.status())

time.sleep(1)
get = Pyrun("j_get.py", ["-s=/demo/example/janu-python-put"])
if get.status():
	get.dbg()
	errors.append(get.status())
if ("Received ('/demo/example/janu-python-put': 'Put from Python!')" in "".join(get.stdout)):
	storage.dbg()
	errors.append("j_get did get a response from j_storage about put after delete")
if any(("j_get" in error) for error in errors):
	get.dbg()

time.sleep(1)
put_float = Pyrun("j_put_float.py")
if put_float.status():
	put_float.dbg()
	errors.append(put_float.status())

try:
	sub.process.stdin.write(b"q\n")
	sub.process.stdin.flush()
	sub.process.stdin.close()
except Exception as e:
	errors.append(f"pub stdin sequence failed: {e}")
if sub.status():
	sub.dbg()
	errors.append(sub.status())
subout = "".join(sub.stdout)
if not ("Received PUT ('/demo/example/janu-python-put': 'Put from Python!')" in subout):
	errors.append("j_sub didn't catch put")
if not ("Received PUT ('/demo/example/janu-python-pub': '[   1] Pub from Python!')" in subout):
	errors.append("j_sub didn't catch second j_pub")
if not ("Received DELETE ('/demo/example/janu-python-put': '')" in subout):
	errors.append("j_sub didn't catch delete")
if not ("Received PUT ('/demo/example/janu-python-put': '3.141592653589793')" in subout):
	errors.append("j_sub didn't catch put float")
if any(("j_sub" in error) for error in errors):
	sub.dbg()

try:
	storage.process.stdin.write(b"q\n")
	storage.process.stdin.flush()
	storage.process.stdin.close()
except Exception as e:
	errors.append(f"storage stdin sequence failed: {e}")
if storage.status():
	storage.dbg()
	errors.append(storage.status())
storageout = "".join(storage.stdout)
if not ("Received PUT ('/demo/example/janu-python-put': 'Put from Python!')" in storageout):
	errors.append("j_storage didn't catch put")
if not ("Received PUT ('/demo/example/janu-python-pub': '[   1] Pub from Python!')" in storageout):
	errors.append("j_storage didn't catch second j_pub")
if not ("Received DELETE ('/demo/example/janu-python-put': '')" in storageout):
	errors.append("j_storage didn't catch delete")
if not ("Received PUT ('/demo/example/janu-python-put': '3.141592653589793')" in storageout):
	errors.append("j_storage didn't catch put float")
if not ("Received Query '/demo/example/janu-python-put'" in storageout):
	errors.append("j_storage didn't catch query")
if any(("j_storage" in error) for error in errors):
	storage.dbg()

sub_thr = Pyrun("j_sub_thr.py")
pub_thr = Pyrun("j_pub_thr.py", ["128"])
time.sleep(5)
sub_thr.process.kill()
pub_thr.process.kill()
if sub_thr.status(KILL):
	sub_thr.dbg()
	errors.append(sub_thr.status())
if pub_thr.status(KILL):
	pub_thr.dbg()
	errors.append(pub_thr.status())


if len(errors):
	message = f"Found {len(errors)} errors: {(ret+tab) + (ret+tab).join(errors)}"
	raise Exception(message)