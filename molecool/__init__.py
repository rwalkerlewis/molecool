"""
molecool
meh
"""

# Add imports here
from .molecool import *
from .measure import *
from .molecule import *
from .visualize import *
from .atom_data import *

import molecool.IO

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
