# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Test hatching a common shell."""

from __future__ import annotations

from pathlib import Path

from hatchshell.common import hatch


def test_hatchedshell() -> None:
    """Test a common HatchedShell."""
    hsh = hatch.HatchedShell("spidermonkey")
    assert hsh.get_absolute_path() == Path()
