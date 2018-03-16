# -*- coding: utf-8 -*-
"""
| **@created on:** 13/03/2018,
| **@author:** Amit Kumar Sharma,
| **@version:** v0.0.1
|
| **Description:**
| Class to get column configurations
| **Sphinx Documentation Status:** Complete
|
..todo::

"""
import json
from configs.path_config import PathConfig
from typeguard import typechecked


class ColumnConfig():
    """
    | **@author:** Amit Kumar Sharma
    |
    | Used to get an object of column(feature) configuration
    """

    @typechecked
    def __init__(self, name: str, file: str, prob: float, column_range: list):
        """

        :param name: column name
        :param file: file name
        :param prob: probability
        :param column_range: column range of a feature
        """
        self.name = name
        self.file = file
        self.column_range = column_range
        self.probability = prob


class ConfigDef():
    """
    | **@author:** Amit Kumar Sharma
    |
    | Used to get configuration definition of the columns(features)
    """

    @typechecked
    def __init__(self,config_json: str):
        """

        :param config_json:
        """
        self.columnConfigs = {}
        probabilities = json.load(open(PathConfig(config_json).PROBABILITY_PATH))
        columns_def = json.load(open(PathConfig(config_json).COLUMNS_PATH))
        for column_configs in probabilities["COLUMN_CONFIG"]:
            file = column_configs["FILE"]
            for col in column_configs["COLUMNS"]:
                if file in columns_def:
                    column_range = columns_def[file][col]
                    self.columnConfigs[file + "." + col] = ColumnConfig(col, file, column_configs["COLUMNS"][col],
                                                                        column_range)
