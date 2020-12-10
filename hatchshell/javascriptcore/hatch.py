# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Hatch a JavaScriptCore shell."""

from __future__ import annotations

from hatchshell.common.hatch import HatchedShell


class JavaScriptCoreShellError(Exception):
    """Error class unique to JavaScriptCoreShell objects."""


class JavaScriptCoreShell(HatchedShell):
    """An actual compiled JavaScriptCore shell."""

    def __init__(self) -> None:
        super().__init__("")

    # @classmethod
    # def main(cls) -> None:
    #     """Main function of JavaScriptCoreShell class.
    #     """

    # @staticmethod
    # def compile() -> None:
    #     """Build a shell
    #     """
