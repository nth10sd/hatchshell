# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Test hatching a JavaScriptCoreShell."""

import pytest

from hatchshell.javascriptcore import hatch


def test_javascriptcoreshell() -> None:
    """Test a JavaScriptCoreShell."""
    with pytest.raises(AssertionError):
        hatch.JavaScriptCoreShell()  # JavaScriptCoreShell hardcoded to set shell_type as empty string ""
