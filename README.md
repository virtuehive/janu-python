![janu banner](./janu-dragon.png)

[![CI](https://github.com/virtuehive/janu-python/workflows/CI/badge.svg)](https://github.com/virtuehive/janu-python/actions?query=workflow%3A%22CI%22)
[![Documentation Status](https://readthedocs.org/projects/janu-python/badge/?version=latest)](https://janu-python.readthedocs.io/en/latest/?badge=latest)
[![Gitter](https://badges.gitter.im/atolab/janu.svg)](https://gitter.im/atolab/janu?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![License](https://img.shields.io/badge/License-EPL%202.0-blue)](https://choosealicense.com/licenses/epl-2.0/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Eclipse janu Python API

[Eclipse janu](http://janu.io) is an extremely efficient and fault-tolerant [Named Data Networking](http://named-data.net) (NDN) protocol 
that is able to scale down to extremely constrainded devices and networks.

-------------------------------
## How to install it

The Eclipse janu-python library is available on [Pypi.org](https://pypi.org/project/virtuehive/).  
Install the latest available version using `pip`:
```
pip install virtuehive
```

:warning:WARNING:warning: janu-python is developped in Rust.
On Pypi.org we provide binary wheels for the most common platforms (MacOS, Linux x86). But also a source distribution package for other platforms.  
However, for `pip` to be able to build this source distribution, there some prerequisites:
 - `pip` version 19.3.1 minimum (for full support of PEP 517).  
   (if necessary upgrade it with command: `'sudo pip install --upgrade pip'` )
 - Have a Rust toolchain installed (instructions at https://rustup.rs/)

### Supported Python versions and platforms

janu-python has been tested with Python 3.6, 3.7, 3.8 and 3.9.

It relies on the [janu](https://github.com/virtuehive/janu/tree/master/janu) Rust API which require the full `std` library. See the list Rust supported platforms here: https://doc.rust-lang.org/nightly/rustc/platform-support.html .


-------------------------------
## How to build it

Requirements:
 * Python >= 3.6
 * pip >= 19.3.1
 * [Rust and Cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html).

Steps:
 * Install developments requirements:
   ```bash
   pip install -r requirements-dev.txt
   ```
 * Build janu-python
   ```bash
   python setup.py develop
   ```

This will automatically build the janu Rust API, as well as the janu-python API and install it in your Python environement.

-------------------------------
## Running the Examples

The simplest way to run some of the example is to get a Docker image of the **janu** network router (see https://github.com/virtuehive/janu#how-to-test-it) and then to run the examples on your machine.

Then, run the janu-python examples following the instructions in [examples/janu/README.md](https://github.com/virtuehive/janu-python/blob/master/examples/janu/README.md)
