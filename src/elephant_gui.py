#pylint: disable=line-too-long, c-extension-no-member
#
# Created on Fri Mar 21 2025
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
"""This module handles the GUI of ElephAnt"""

import sys
import logging

from PyQt6 import QtWidgets
from elephant_ui_form import Ui_ElephAnt
from ui_logger import QPlainTextEditLogger, QStatusBarLogger

from elephant import ElephantLogic, setup_logging
from elephant_setup import ElephantSetup
from elephant_setup_binder import SetupBinder

logger = logging.getLogger("ElephantLogger")

setup_list: list[ElephantSetup]

class MainWindow(QtWidgets.QMainWindow):
    """Main Window of the GUI handling user input/output"""
    _logic: ElephantLogic
    def __init__(self, ui_logic: ElephantLogic, *args, **kwargs):
        """Init of the main windows of the GUI handling user input/output
        Args:
            ui_logic (ElephantLogic): `ElephantLogic` backend to attach to
        """
        super().__init__(*args, **kwargs)
        self._logic = ui_logic
        self._ui = Ui_ElephAnt()
        self._ui.setupUi(self)

        self._binder = SetupBinder(self._ui)

        ui_log_box = QPlainTextEditLogger(self._ui.logDisplayArea)
        ui_status = QStatusBarLogger(self._ui.statusbar)
        logger.addHandler(ui_log_box)
        logger.addHandler(ui_status)

        self._ui.actionNew_Setup.triggered.connect(self.new_setup)
        self._ui.actionExit.triggered.connect(self.close)
        self._ui.actionSave_Setup.triggered.connect(self.save_setup)
        self._ui.actionSave_Setup_As.triggered.connect(self.save_setup_dialog)
        self._ui.actionOpen_Setup.triggered.connect(self.open_setup_dialog)
        self._ui.actionClose_Setup.triggered.connect(self.close_setup)

        self._ui.treeWidget.itemDoubleClicked.connect(self.setup_double_clicked)

        self._ui.treeWidget.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        self.update_ui_setup_list()

        logger.info("UI init finished")

    #pylint: disable=C0103:invalid-name
    def closeEvent(self, event):
        """This function handles the closing process"""
        logger.info("Application is closing!")
        setup_list_len = len(setup_list)
        while setup_list_len > 0:
            self.close_setup()
            if setup_list_len == len(setup_list):
                # no setup was closed. Stop closing process
                logger.info("Stopped closing of the application")
                event.ignore()
                return
            setup_list_len = len(setup_list)
        logger.debug("All setups are closed")
        event.accept()

    def query_msgbox(self, title: str, message: str) -> bool:
        """Generates a query box and captures the result
        Args:
            title (str): Title of the query box
            message (str): Message of the query box
        Returns:
            bool: Returns `True` if yes was selected. `False` otherwise
        """
        query_box = QtWidgets.QMessageBox(self)
        query_box.setIcon(QtWidgets.QMessageBox.Icon.Question)
        query_box.setWindowTitle(title)
        query_box.setText(message)
        query_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        query_box.show()
        return bool(query_box.exec() == QtWidgets.QMessageBox.StandardButton.Yes)

    def error_msgbox(self, title: str, message: str):
        """Generates an error message box
        Args:
            title (str): Title for the title bar of the error message
            message (str): Content of the error message
        """
        error_msg = QtWidgets.QMessageBox(self)
        error_msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        error_msg.setWindowTitle(title)
        error_msg.setText(message)
        error_msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        error_msg.show()

    def update_setup_status(self):
        """When the is_dirty flag of a setup is set, this function is called back"""
        self.update_ui_setup_list()

    def open_setup_dialog(self):
        """Opens a `Open Setup` file dialog.
        This will add a ElephantSetup to the list of setups
        and set it as the current setup in the logic back-end.
        """
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setWindowTitle("Open Setup")
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptOpen)
        file_dialog.setViewMode(QtWidgets.QFileDialog.ViewMode.Detail)
        file_dialog.setNameFilter("ElephAnt Setup (*.toml)")

        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            logger.info("Selected a setup file for opening", extra={'file': selected_file})
            if any(setup.path == selected_file for setup in setup_list):
                logger.error("Selected setup file is already part of the loaded setups!")
                self.error_msgbox("Error", "Selected setup file is already part of the loaded setups!")
                return
            setup = ElephantSetup(self.update_setup_status)

            if setup.load_setup_file(selected_file) is False:
                logger.error("Failed to load setup")
                self.error_msgbox("Error", "Failed to load setup!")
            else:
                setup_list.append(setup)
                self.change_active_setup(setup_list[-1])
                logger.info("Loaded setup successfully")

    def setup_double_clicked(self, item: QtWidgets.QTreeWidgetItem, col: int):
        """Action to follow when a setup from the list is double clicked
        Args:
            item (QtWidgets.QTreeWidgetItem): Signal information on which item was clicked
            col (int): Column of the TreeWidget which was clicked
        """
        # filter top level elements in tree
        if item.parent():
            return
        for setup in setup_list:
            if setup.general.setup_name == item.text(0).replace('*',''):
                self.change_active_setup(setup)
                break

    def update_ui_setup_list(self):
        """Updates the setup tree widget containing the setups in the main window"""
        tree = self._ui.treeWidget
        tree.clear()

        icon_open = self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DirOpenIcon)
        icon_closed = self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DirClosedIcon)
        icon_section = self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_FileIcon)

        for setup in setup_list:
            setup_itm = QtWidgets.QTreeWidgetItem(tree)
            if setup == self._logic.current_setup:
                setup_itm.setIcon(0, icon_open)
                for section in self._logic.current_setup.expected_sections:
                    child_itm = QtWidgets.QTreeWidgetItem(setup_itm)
                    child_itm.setText(0, section)
                    child_itm.setIcon(0, icon_section)
                    setup_itm.addChild(child_itm)
                    setup_itm.setExpanded(True)
                    if setup.is_dirty:
                        setup_itm.setText(0, setup.general.setup_name + '* - Active')
                    else:
                        setup_itm.setText(0, setup.general.setup_name + ' - Active')
            else:
                setup_itm.setIcon(0, icon_closed)
                if setup.is_dirty:
                    setup_itm.setText(0, setup.general.setup_name + '*')
                else:
                    setup_itm.setText(0, setup.general.setup_name)


    def change_active_setup(self, new_setup: ElephantSetup):
        """Used to have a single place where to switch setups with the GUI
        Args:
            new_setup (ElephantSetup): Setup to switch to. Can be `None`
        """
        self._logic.current_setup = new_setup
        if new_setup is not None:
            logger.info("Switched active setup to: %s", new_setup.general.setup_name, extra={'new_setup': new_setup})
            self._binder.set_setup(self._logic.current_setup)
        self.update_ui_setup_list()

    def new_setup(self):
        """Adds a new setup file to the list of active setups and prompts to save it"""
        logger.info("Generating a new setup")
        new_setup = ElephantSetup(self.update_setup_status)
        new_setup.general.setup_name = 'Blank Setup'
        setup_list.append(new_setup)
        self.change_active_setup(new_setup)
        self.save_setup_dialog()

    def save_setup(self):
        """Saves a setup in it`s load from location"""
        if self._logic.current_setup is None:
            logger.error("Current setup is None. Cannot save setup")
            self.error_msgbox("Error", "There is no active setup!")
            return
        if self._logic.current_setup.save_setup_file() is False:
            self.error_msgbox("Error", "Failed to save setup!")

    def save_setup_dialog(self):
        """Opens a `Save Setup` file dialog.
        This will store the currently active setup of the logic back-end
        to a file.
        """
        file_dialog = QtWidgets.QFileDialog(self)
        file_dialog.setWindowTitle("Save Setup")
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptSave)
        file_dialog.setViewMode(QtWidgets.QFileDialog.ViewMode.Detail)
        file_dialog.setNameFilter("ElephAnt Setup (*.toml)")
        file_dialog.setDefaultSuffix('toml')
        setup_to_save = self._logic.current_setup
        if setup_to_save is None:
            logger.error("Current setup is None. Cannot save setup")
            self.error_msgbox("Error", "There is no active setup!")
            return

        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]
            logger.info("Selected a setup file for saving", extra={'file': selected_file})
            if not setup_to_save.save_setup_file(selected_file):
                self.error_msgbox("Error", "Failed to save setup!")

    def close_setup(self):
        """Closes the current setup and removes it from the list of active setups"""
        if len(setup_list) == 0:
            logger.info("Nothing to close. No active setups")
            return
        try:
            if self._logic.current_setup.is_dirty:
                setup_name = self._logic.current_setup.general.setup_name
                if not self.query_msgbox("Closing setup with unsaved changes?",
                                         f"Do you really want to close the setup \"{setup_name}\" without saving changes?"):
                    logger.info("Aborted closing setup with unsaved changes")
                    return
                logger.info("Closing setup with unsaved changes!")
            setup_list.remove(self._logic.current_setup)
        except ValueError:
            logger.error("Here is something fishy going on! Active setup not found in the setup list!", extra={'current_setup': self._logic.current_setup})

        if len(setup_list) == 0:
            self.change_active_setup(None)
            logger.debug("There is no setup left to switch to from the setup_list!")
        else:
            self.change_active_setup(setup_list[-1])


if __name__ == "__main__":
    setup_logging()
    setup_list = []
    app = QtWidgets.QApplication(sys.argv)

    logic = ElephantLogic()
    window = MainWindow(logic)
    window.show()
    app.exec()
    logger.info("Closing")
