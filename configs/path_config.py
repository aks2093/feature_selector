# -*- coding: utf-8 -*-

"""
| **@created on:** 13/03/18,
| **@author:** Amit Kumar Sharma,
| **@version:** v0.0.1
|
| **Description:**
| Class to get required paths
| **Sphinx Documentation Status:** Complete
|
..todo::
"""
import json
from typeguard import typechecked


class PathConfig():
    """
    | **@author:** Amit Kumar Sharma
    |
    | Used to get the paths of required JSONs
    """
    @typechecked
    def __init__(self, config_json: str):
        """

        :param config_json: path to config_json(containing all required paths) file
        """
        try:
            if isinstance(config_json,str):
                self.config = json.load(open(config_json))
            else:
                self.config = config_json
            self.PROBABILITY_PATH = self.config["PROBABILITY_PATH"]
            self.COLUMNS_PATH  = self.config["COLUMNS_PATH"]
        except Exception as e:
            raise Exception(e)

