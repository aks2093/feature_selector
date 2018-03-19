# -*- coding: utf-8 -*-
"""
| **@created on:** 13/03/2018,
| **@author:** Amit Kumar Sharma,
| **@version:** v0.0.2
|
| **Description:**
| Feature Selector Class
| **Sphinx Documentation Status:** Complete
|
..todo::

"""

import random
from configs.ConfigDef import ConfigDef
from typeguard import typechecked
import json
from typing import Union


class FeatureSelector(object):
    """
    | **@author:** Amit Kumar Sharma
    |
    | Used to select features
    """

    @typechecked
    def __init__(self, columns: dict, probabilities: dict, number_of_models: int, save_path: Union[None, str] = None):
        """
        :param path_config: contains path to all JSONs required
        :param number_of_models: number of models
        """
        self.columns = columns
        self.probabilities = probabilities
        self.model_column_config = {}
        self.model_file_column_config = {}
        self.model_file_columnRange_config = {}
        self.number_of_models = number_of_models
        self.___validate_columns()
        self.__validate_probabilities()
        self.configDef = ConfigDef(columns= self.columns, probabilities= self.probabilities)
        self.save_path = save_path

    def get_columns(self):
        """
        Used to get columns,file-column,file-columnRange for the model

        :return: A tuple containing model_column_config, model_file_column_config, model_file_columnRange_config
                 all in dictionary format

        """
        for model_index in range(self.number_of_models):
            var1, var2, var3 = {}, {}, {}
            for cn in self.configDef.columnConfigs:
                var1[cn] = self.__probability_check(self.configDef.columnConfigs[cn].probability)
                if var1[cn]:
                    if not self.configDef.columnConfigs[cn].file in var2:
                        var2[self.configDef.columnConfigs[cn].file] = []
                    var2[self.configDef.columnConfigs[cn].file] += [{self.configDef.columnConfigs[cn].name:
                                                                    self.configDef.columnConfigs[cn].column_range}]

                    if not self.configDef.columnConfigs[cn].file in var3:
                        var3[self.configDef.columnConfigs[cn].file] = []
                    var3[self.configDef.columnConfigs[cn].file] += [self.configDef.columnConfigs[cn].column_range]

            self.model_column_config[model_index] = var1
            self.model_file_column_config[model_index] = var2
            self.model_file_columnRange_config[model_index] = var3

            if self.save_path:
                self.__save_to_file()

        return self.model_column_config, self.model_file_column_config, self.model_file_columnRange_config

    @typechecked
    def __probability_check(self, probability: float) -> bool:
        """
        | **@author:** Amit Kumar Sharma,
        |
        | Used to check given probability with randomly generated values from uniform distribution(0-1)

        :param probability: probability attached to column(feature)
        :return: boolean value for a column(feature) getting selected
        """
        random_probability = random.uniform(0, 1.0)
        if random_probability < probability:
            return True
        else:
            return False

    def __save_to_file(self):
        """
        | **@author:** Amit Kumar Sharma,
        |
        | Used to save column configurations for models in a JSON file

        :return: None
        """
        with open(self.save_path+"model_column_config.json", "w") as fd:
            fd.write(json.dumps(self.model_column_config, indent=2))

        with open(self.save_path+"model_file_column_config.json", "w") as fd:
            fd.write(json.dumps(self.model_file_column_config, indent=2))

        with open(self.save_path+"model_file_columnRange_config.json", "w") as fd:
            fd.write(json.dumps(self.model_file_columnRange_config, indent=2))

    def ___validate_columns(self):
        """
        | **@author:** Amit Kumar Sharma,
        |
        | Used to validate the structure of the columns.

        :return:
        """
        if self.__is_empty(self.columns):
            raise Exception("Columns dictionary should not be empty.")
        else:
            for file_key in self.columns.keys():
                if self.__is_empty(self.columns[file_key]):
                    raise Exception("for file_key: {} in columns dictionary the value"
                                    " should not be an empty structure.".format(file_key))
                elif not isinstance(self.columns[file_key],dict):
                    raise Exception("value of file_key: {} in column_dictionary the value should"
                                    " be a dictionary.".format(file_key))
                else:
                    for column_key in self.columns[file_key].keys():
                        if self.__is_empty(self.columns[file_key][column_key]):
                            raise Exception("value mapped to column_key: {} for file_key: {} can"
                                            " not left empty".format(column_key, file_key))
                        if not isinstance(self.columns[file_key][column_key], list):
                            raise Exception("value Attached to column_key: {} for file_key: {}"
                                            " should be a list ".format(column_key, file_key))

    def __validate_probabilities(self):
        """
        | **@author:** Amit Kumar Sharma,
        |
        | Used to validate the structure of the column's probability

        :return:
        """
        if self.__is_empty(self.probabilities):
            raise Exception("Probabilities dictionary should not be empty.")
        else:
            if "COLUMN_CONFIG" not in self.probabilities.keys():
                raise Exception("COLUMN_CONFIG key should be there in probabilities dictionary.")
            elif self.__is_empty(self.probabilities["COLUMN_CONFIG"]):
                raise Exception("value mapped to 'COLUMN_CONFIG' should not be left empty.")
            elif not isinstance(self.probabilities["COLUMN_CONFIG"],list):
                raise Exception("values mapped to 'COLUMN_CONFIG' should be list.")
            else:
                for element in self.probabilities["COLUMN_CONFIG"]:
                    if not isinstance(element, dict):
                        raise Exception("All elements in the list mapped to 'COLUMN_CONFIG'"
                                        " should be dictionary.")
                    elif self.__is_empty(element):
                        raise Exception("Any element in the list mapped to 'COLUMN_CONFIG'"
                                        "should not be left empty.")
                    elif "FILE" not in element.keys() or "COLUMNS" not in element.keys():
                        raise Exception("'FILE' and 'COLUMNS' should be the keys "
                                        "in elements of the the list mapped to 'COLUMN_CONFIG'.")
                    elif not isinstance(element['COLUMNS'], dict):
                        raise Exception("value of key 'COLUMNS' in elements of"
                                        " the list mapped to 'COLUMN_CONFIG' should be dictionary.")
                    elif self.__is_empty(element['COLUMNS']):
                        raise Exception("value of key 'COLUMNS' in elements of the "
                                        "list mapped to 'COLUMN_CONFIG' should not be left empty")

    @staticmethod
    @typechecked
    def __is_empty(any_structure: Union[list,dict,set,str]) -> bool:
        """
        | **@author:** Amit Kumar Sharma,
        |
        | Used to check a empty structure

        :param any_structure: like lists, dictionaries etc.
        :return: Boolean
        """
        if any_structure:
            return False
        else:
            return True




