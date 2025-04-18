#pylint: disable=line-too-long
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
import logging
from PyQt6 import QtWidgets


class QPlainTextEditLogger(logging.Handler):
    widget : QtWidgets.QPlainTextEdit
    def __init__(self, parent):
        super().__init__()
        self.widget = parent
        self.setLevel(logging.INFO)
        self.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(message)s","%H:%M:%S"))

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)


class QStatusBarLogger(logging.Handler):
    widget : QtWidgets.QStatusBar
    def __init__(self, parent):
        super().__init__()
        self.widget = parent
        self.setLevel(logging.INFO)
        self.setFormatter(logging.Formatter("Status: %(message)s"))

    def emit(self, record):
        msg = self.format(record)
        self.widget.showMessage(msg)
