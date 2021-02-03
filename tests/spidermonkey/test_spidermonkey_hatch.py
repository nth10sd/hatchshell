# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Test hatching a SpiderMonkeyShell."""

from __future__ import annotations

import pytest

from hatchshell.spidermonkey import hatch


def test_spidermonkeyshell() -> None:
    """Test a SpiderMonkeyShell."""
    with pytest.raises(AssertionError):
        # SpiderMonkeyShell hardcoded to set shell_type as empty string ""
        hatch.SpiderMonkeyShell()
