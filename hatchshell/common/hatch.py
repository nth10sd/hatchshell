# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Define objects common to all shells."""

from __future__ import annotations

from pathlib import Path


class HatchedShellError(Exception):
    """Error class unique to HatchedShell objects."""


class HatchedShell:
    """This object represents an actual compiled JS shell.
    :param shell_type: type of shell, can be spidermonkey or javascriptcore
    :raise HatchedShellError: When an unsupported js shell is specified
    """

    def __init__(self, shell_type: str):
        self.shell_path = Path()
        self.shell_type = shell_type
        if self.shell_type not in self.get_supported():
            raise HatchedShellError(
                "Other js shells, e.g. V8 and Edge Chromium are not yet supported",
            )

    def get_absolute_path(self) -> Path:
        """Get the absolute path of the newly compiled JavaScript shell.
        :returns: Absolute path to the shell
        """
        return self.shell_path

    @staticmethod
    def get_supported() -> list[str]:
        """Get a list of supported JavaScript shells.
        :returns: Supported shells
        """
        return ["spidermonkey", "javascriptcore"]

    # @classmethod
    # def main(cls) -> None:
    #     """Main function of HatchedShell class.
    #     """

    # @staticmethod
    # def compile() -> None:
    #     """Build a shell
    #     """
