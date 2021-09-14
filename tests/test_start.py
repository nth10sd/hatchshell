# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Tests for start.py"""

from __future__ import annotations

import pytest

from hatchshell import start
from hatchshell.common.hatch import HatchedShellError


def test_main() -> None:
    """Test the main() function."""
    with pytest.raises(HatchedShellError):
        start.main()  # SpiderMonkeyShell hardcoded to set shell_type as empty string ""
