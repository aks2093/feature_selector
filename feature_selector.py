# -*- coding: utf-8 -*-
"""
| **@created on:** 13/03/2018,
| **@author:** Amit Kumar Sharma,
| **@version:** v0.0.1
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
    def __init__(self, path_config: str, number_of_models: int, save_path: Union[None, str] = None):
        """
        :param path_config: contains path to all JSONs required
        :param number_of_models: number of models
        """
        self.model_column_config = {}
        self.model_file_column_config = {}
        self.model_file_columnRange_config = {}
        self.number_of_models = number_of_models
        self.configDef = ConfigDef(config_json=path_config)
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
        | Used to check given probability with randomly generated values from uniform distribution(0-1)
        |
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
        Used to save column configurations for models in a JSON file

        :return: None
        """
        with open(self.save_path+"model_column_config.json", "w") as fd:
            fd.write(json.dumps(self.model_column_config, indent=2))

        with open(self.save_path+"model_file_column_config.json", "w") as fd:
            fd.write(json.dumps(self.model_file_column_config, indent=2))

        with open(self.save_path+"model_file_columnRange_config.json", "w") as fd:
            fd.write(json.dumps(self.model_file_columnRange_config, indent=2))



