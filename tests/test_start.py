# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Tests for start.py"""

import pytest

from hatchshell import start


def test_main() -> None:
    """Test the main() function."""
    with pytest.raises(AssertionError):
        start.main()  # SpiderMonkeyShell hardcoded to set shell_type as empty string ""