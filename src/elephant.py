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
"""This module handles the elephant application.
    Start from here for a custom console application"""

import json
import pathlib
import logging.config
import logging.handlers

from elephant_setup import ElephantSetup

logger = logging.getLogger("ElephantLogger")

class ElephantLogic:
    """Main logic block of the application
    """
    def __init__(self):
        self._current_setup = None

    @property
    def current_setup(self) -> ElephantSetup:
        """`current_setup` property.
        Used to set or get the current `ElephantSetup` of the logic.
        Returns:
            ElephantSetup: The currently active setup of the logic
        """
        logger.debug("Logic returns it's current setup")
        return self._current_setup

    @current_setup.setter
    def current_setup(self, new_setup):
        logger.debug("Logic got a new setup")
        self._current_setup = new_setup


def setup_logging():
    """ Sets logging up according to the json config """
    config_file = pathlib.Path("./logging_configs/log_config_stderr_file.json")
    with open(config_file, encoding='utf8') as f_in:
        config = json.load(f_in)

    logging.config.dictConfig(config)
    logging.basicConfig(level="INFO")




if __name__ == '__main__':
    setup_logging()
    print("This is the command line version of the tool.")
    print("To start the GUI run \'elephant_ui.py\'")

    logic = ElephantLogic()
    setup = ElephantSetup()
    setup.load_setup_file("setup.toml")
    logic.current_setup = setup

    # do something

    current_setup = logic.current_setup
    # save to read from file
    current_setup.save_setup_file()
    # save to another file
    current_setup.save_setup_file("setup2.toml")
