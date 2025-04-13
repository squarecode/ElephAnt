#pylint: disable=line-too-long, c-extension-no-member
#
# Created on Sun Apr 13 2025
#
# The MIT License (MIT)
# Copyright (c) 2025 Stefan Voigt <stefan.voigt@rwth-aachen.de>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

"""This module handles the binding of an Elephant setup to the GUI elements"""

import logging

from PyQt6 import QtWidgets, QtCore
from elephant_setup import ElephantSetup

logger = logging.getLogger("ElephantLogger")

class SetupBinder(QtCore.QObject):
    """SetupBinder to bind a setup to the GUI elements by prefix.
        The GUI elements are prefixed with e.g. tb_ for a QLineEdit.
        This enables the Binder to automatically bind setup information to the GUI.
    Args:
        QtWidgets (QObject): Usually just the MainWindow
        setup (ElephantSetup, optional): Optional setup to bind to during init. Defaults to None.
    """
    value_changed = QtCore.pyqtSignal()

    def __init__(self, parent_widget: QtWidgets.QWidget, setup: ElephantSetup = None):
        super().__init__()
        self.parent = parent_widget
        if setup is not None:
            self.setup = setup
            self.bind_widgets()

    def unbind_widgets(self):
        """Unbinds the widgets from a setup"""
        for name, widget in self.parent.__dict__.items():
            if isinstance(widget, QtWidgets.QLineEdit) and name.startswith("tb_"):
                try:
                    widget.disconnect()
                except TypeError as te:
                    logger.debug("Could not disconnect from %s. %s", name, str(te))
            elif isinstance(widget, QtWidgets.QLabel) and name.startswith("l_"):
                try:
                    widget.disconnect()
                except TypeError as te:
                    logger.debug("Could not disconnect from %s. %s", name, str(te))

    def set_setup(self, new_setup: ElephantSetup):
        """Used to change the setup bound to the GUI"""
        logger.info("Changing setup bound to widgets")
        self.setup = new_setup
        self.unbind_widgets()
        self.bind_widgets()

    def bind_widgets(self):
        """This method containt the prefix removal and binding"""
        for name, widget in self.parent.__dict__.items():
            if isinstance(widget, QtWidgets.QLineEdit) and name.startswith("tb_"):
                setup_path = name[3:]  # remove 'tb_' to find object to bind to
                self.bind_line_edit(widget, setup_path)
            elif isinstance(widget, QtWidgets.QLabel) and name.startswith("l_"):
                setup_path = name[2:]  # remove 'l_' to find object to bind to
                self.bind_label(widget, setup_path)

    def bind_line_edit(self, line_edit: QtWidgets.QLineEdit, path: str):
        """Bi-Directional bind method for QLineEdit"""
        # Find a match in the setup and bind to it
        for section_name in self.setup.expected_sections:
            section = getattr(self.setup, section_name)
            if hasattr(section, path):
                line_edit.setText(getattr(section, path))
                logger.debug("Bound line edit '%s' to setup [%s] %s", line_edit.objectName(), section_name, path)

                def update_setup(text: str="", section=section, path=path, section_name=section_name):
                    setattr(section, path, text)
                    self.value_changed.emit()
                    logger.debug("Updated setup [%s] %s from line edit: %s", section_name, path, line_edit.text())

                line_edit.textChanged.connect(update_setup)
                break

    def bind_label(self, label: QtWidgets.QLabel, path: str):
        """Unidirectional bind method for QLabel"""
        for section_name in self.setup.expected_sections:
            section = getattr(self.setup, section_name)
            if hasattr(section, path):
                label.setText(getattr(section, path))
                logger.debug("Bound label '%s' to setup [%s] %s", label.objectName(), section_name, path)
                break
