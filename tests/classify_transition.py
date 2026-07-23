"""Compatibility entrypoint for the Transition Diagnosis v0.1 evaluator.

The reusable command and implementation now live at
``tools/capability_diagnostic.py``. This wrapper preserves historical commands
and imports used by the repository's regression fixtures.
"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.capability_diagnostic import *  # noqa: F401,F403,E402
from tools.capability_diagnostic import main  # noqa: E402


if __name__ == "__main__":
    sys.exit(main())
