# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Hatch a SpiderMonkey shell."""

from hatchshell.common.hatch import HatchedShell


class SpiderMonkeyShellError(Exception):
    """Error class unique to SpiderMonkeyShell objects."""


class SpiderMonkeyShell(HatchedShell):
    """An actual compiled SpiderMonkey shell."""

    def __init__(self) -> None:
        super().__init__("")

    # @classmethod
    # def main(cls) -> None:
    #     """Main function of SpiderMonkeyShell class.
    #     """

    # @staticmethod
    # def compile() -> None:
    #     """Build a shell
    #     """
