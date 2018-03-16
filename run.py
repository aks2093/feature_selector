# -*- coding: utf-8 -*-
"""
| **@created on:** 13/03/2018,
| **@author:** Amit Kumar Sharma,
| **@version:** v0.0.1
|
| **Description:**
| Script to get column(features) configs for given number of models
| **Sphinx Documentation Status:** Complete
|
..todo::

"""
from feature_selector import FeatureSelector
from pprint import pprint

fs = FeatureSelector(path_config="./samples/config_files/path_config.json", number_of_models=2)

d = fs.get_columns()
pprint(d)
exit()
