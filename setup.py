#!/usr/bin/env python
from distutils.core import setup

setup(
    name="couch-named-python",
    version="0.2.2",
    author="Daniel Richman",
    author_email="main@danielrichman.co.uk",
    url="https://github.com/danielrichman/couch-named-python",
    description="CouchDB view server that executes functions "
                "on the python path by name",
    packages=["couch_named_python"],
    install_requires=["PyYAML", "couchdbkit"],
    license="GNU General Public License Version 3",
    scripts=["bin/couch-named-python", "bin/cnp-upload"]
)
