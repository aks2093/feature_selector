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
    def __init__(self,columns: dict, probabilities: dict):
        """

        :param columns: A Dictionary, contains columns name and their range.
        :param probabilities: A Dictionary, contains probabilities for each column.
        """
        self.columnConfigs = {}
        for column_configs in probabilities["COLUMN_CONFIG"]:
            file = column_configs["FILE"]
            for col in column_configs["COLUMNS"]:
                if file in columns:
                    column_range = columns[file][col]
                    self.columnConfigs[file + "." + col] = ColumnConfig(col, file, column_configs["COLUMNS"][col],
                                                                        column_range)
