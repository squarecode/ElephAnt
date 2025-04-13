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
"""This module handles the Elephant setup and how to save and retrieve it from a file"""

import logging
import configparser
import os

logger = logging.getLogger("ElephantLogger")

# Default setup values are configured here
DEFAULT_SETUP = {
    "general": {
        "setup_name": "New Setup",
        "setup_comment": "",
        "last_modified": "---",
        "aut_name": "No AUT Name"
    },
    "hardware": {
        "some_hw_attr": "12321"
    }
}

class SectionWrapper:
    """Wrapper for the Sections of the Setup"""
    def __init__(self, section_name: str, config: configparser.ConfigParser, section_dirty_callback):
        self._section_name = section_name
        self._config = config
        self._mark_dirty = section_dirty_callback

    def __getattr__(self, item):
        return self._config.get(self._section_name, item, fallback="")

    def __setattr__(self, key, value):
        if key in {"_section_name", "_config", "_mark_dirty"}:
            super().__setattr__(key, value)
        else:
            if not self._config.has_section(self._section_name):
                self._config.add_section(self._section_name)
            self._config.set(self._section_name, key, value)
            logger.debug("Set [%s] %s = %s", self._section_name, key, value)
            self._mark_dirty()


class ElephantSetup:
    """Stores the setup information"""
    def __init__(self, setup_is_dirty_callback=None):
        self._config = configparser.ConfigParser()
        logger.info("Initializing new setup with defaults")
        self._load_defaults()

        self.expected_sections = ["general", "hardware"]
        self.general  = SectionWrapper("general",  self._config, self._set_dirty)
        self.hardware = SectionWrapper("hardware", self._config, self._set_dirty)

        self.path = None
        self._dirty = False

        self._is_dirty_callback = setup_is_dirty_callback

    def _set_dirty(self):
        self._dirty = True
        logger.debug("Setup marked as dirty")
        # Issue a callback. Setup has been modified
        if self._is_dirty_callback is not None:
            self._is_dirty_callback()

    def _set_clean(self):
        self._dirty = False
        logger.debug("Setup marked as clean")
        # Issue a callback. Setup is now clean
        if self._is_dirty_callback is not None:
            self._is_dirty_callback()
    @property
    def is_dirty(self):
        """Returns the dirty status flag of the setup. `True` indicates unsaved changes"""
        return self._dirty

    def _load_defaults(self):
        for section, keys in DEFAULT_SETUP.items():
            if not self._config.has_section(section):
                self._config.add_section(section)
            for key, default_value in keys.items():
                self._config.set(section, key, default_value)
                logger.debug("Loaded default [%s] %s = %s", section, key, default_value)

    def load_setup_file(self, path: str):
        """Function to load a setup from a setup file
        Args:
            path (str): Path to the setup file
        Returns:
            bool: `True` if loading was successful. `False` otherwise
        """
        logger.info("Loading setup from %s", path)
        if not os.path.isfile(path):
            logger.error("Loading setup failed! isfile failed")
            return False

        self.path = path
        self._config.read(path)

        # Inject defaults if missing
        for section, keys in DEFAULT_SETUP.items():
            if not self._config.has_section(section):
                self._config.add_section(section)
                logger.warning("Section [%s] missing in file. Added with defaults.", section)
            for key, default_value in keys.items():
                if not self._config.has_option(section, key):
                    self._config.set(section, key, default_value)
                    logger.warning("Missing [%s] %s in file. Set to default: %s", section, key, default_value)
        self._set_clean()
        logger.debug("Setup loaded and marked as clean")

    def save_setup_file(self, path: str = None) -> bool:
        """Function to save a setup to a file. The setup can be save to it`s load
            from location by leaving path set to `None`
        Args:
            path (str, optional): Can be a setup save path or None. Defaults to None.
                                    which will save the setup to it`s load from location
        Returns:
            bool: `True` if saving was successful. `False` otherwise
        """
        logger.info("Saving setup")
        if path:
            logger.debug("Using the specified path for saving: %s", path)
            self.path = path
            save_path = path
        elif self.path:
            logger.debug("Using the path from load from location")
            save_path = self.path
        else:
            logger.error("No path specified for saving setup")
            return False

        try:
            with open(save_path, 'w', encoding='utf8') as configfile:
                self._config.write(configfile)
                logger.info("Saved setup to %s", save_path)
                self._set_clean()
                logger.debug("Setup saved and marked as clean")
        except OSError as err:
            logger.error("Failed to write setup! %s", str(err))
            return False
        logger.info("Setup has been saved!")
        return True

# testing read write of setups
if __name__ == "__main__":
    setup = ElephantSetup()
    setup.load_setup_file("setup.toml")
    # do stuff
    setup.save_setup_file("setup.toml")
