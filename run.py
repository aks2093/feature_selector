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

columns = {
    "TRANSACTION_COUNTS":{
        "LOAN": [181, 193],
        "CCPMT": [169, 181],
        "CHEQUE": [25, 37],
        "DEBIT": [205, 217],
        "DDPO": [97, 109],
        "FT": [37, 49],
        "ECS": [133, 145],
        "NEFT": [109, 121],
        "CREDIT": [193, 205],
        "SALARY": [61, 73],
        "TAXPMT": [85, 97],
        "RTGS": [13, 25],
        "INTEREST": [49, 61],
        "CHARGES": [1, 13],
        "LOCKER": [121, 133],
        "OFFLINE": [145, 157],
        "FD": [157, 169],
        "SI": [73, 85]
    },
    "TRANSACTIONS": {
        "AUTO_Channel_Amount": [241, 253],
        "CHEQUE": [25, 37],
        "DEBIT": [217, 229],
        "FT": [37, 49],
        "AUTO_Channel_Count": [337, 349],
        "ECS": [145, 157],
        "NEFT": [121, 133],
        "BNA_Channel_Count": [409, 421],
        "FD": [169, 181],
        "RTGS": [13, 25],
        "CHARGES": [1, 13],
        "BRN_Channel_Count": [349, 361],
        "NI_Channel_Amount": [277, 289],
        "POS_Channel_Count": [361, 373],
        "OFFLINE": [157, 169],
        "BRN_Channel_Amount": [253, 265],
        "LOCKER": [133, 145],
        "LOAN": [193, 205],
        "CCPMT": [181, 193],
        "NI_Channel_Count": [373, 385],
        "DDPO": [109, 121],
        "CREDIT": [205, 217],
        "BNA_Channel_Amount": [313, 325],
        "SALARY": [61, 73],
        "TAXPMT": [97, 109],
        "monthly_daily_average_balance": [73, 85],
        "INTEREST": [49, 61],
        "POS_Channel_Amount": [265, 277],
        "ATM_Channel_Amount": [229, 241],
        "ATM_Channel_Count": [325, 337],
        "MB_Channel_Count": [397, 409],
        "INB_Channel_Count": [385, 397],
        "INB_Channel_Amount": [289, 301],
        "SI": [85, 97],
        "MB_Channel_Amount": [301, 313]
    },
    "GENOME": {
        "Cluster_Encoded": [1, 6],
        "Lifestage_Encoded": [6, 13]
    },
    "RATIO": {
        "CREDIT_6": [19, 25],
        "MDAB_6": [7, 13],
        "DEBIT_6": [31, 37],
        "CASH_6": [43, 49]
    },
    "DEMOGRAPHIC": {
        "INB_Count": [29, 30],
        "NI_Count": [28, 29],
        "Total_Credits_Count": [32, 33],
        "Age": [20, 21],
        "BRN_Count": [26, 27],
        "No_Of_Live_Acc": [21, 22],
        "No_Of_Family": [22, 23],
        "ATM_Count": [24, 25],
        "MB_Count": [30, 31],
        "Segment": [1, 8],
        "AUTO_Count": [25, 26],
        "No_of_XH": [23, 24],
        "BNA_Count": [31, 32],
        "Total_Debits_Count": [33, 34],
        "Occupation": [8, 20],
        "POS_Count": [27, 28]
    },
    "DECILE": {
        "LOAN": [161, 171],
        "monthly_daily_average_balance": [61, 71],
        "CCPMT": [151, 161],
        "CHEQUE": [21, 31],
        "DEBIT": [181, 191],
        "DDPO": [91, 101],
        "FT": [31, 41],
        "ECS": [121, 131],
        "NEFT": [101, 111],
        "CREDIT": [171, 181],
        "SALARY": [51, 61],
        "TAXPMT": [81, 91],
        "RTGS": [11, 21],
        "INTEREST": [41, 51],
        "CHARGES": [1, 11],
        "LOCKER": [111, 121],
        "OFFLINE": [131, 141],
        "FD": [141, 151],
        "SI": [71, 81]
    }
}

probabilities = {
  "MODEL_CONFIG": {
    "CREDIT_DEBIT_RATIO": 1.0,
    "CREDIT_MDAB_RATIO": 1.0
  },
  "COLUMN_CONFIG": [
    {
      "FILE": "DECILE",
      "COLUMNS": {
        "RTGS": 0.5,
        "FD": 0.2,
        "ECS": 0.5,
        "LOCKER": 0.5,
        "OFFLINE": 0.5,
        "monthly_daily_average_balance": 1,
        "LOAN": 0.0,
        "CCPMT": 0.2,
        "TAXPMT": 0.2,
        "NEFT": 0.5,
        "CHEQUE": 0.5,
        "CHARGES": 0.5,
        "SALARY": 0.5,
        "DEBIT": 0.5,
        "DDPO": 0.5,
        "SI": 0.5,
        "FT": 0.5,
        "INTEREST": 0.5,
        "CREDIT": 0.5
      }
    },
    {
      "FILE": "GENOME",
      "COLUMNS": {
        "Lifestage_Encoded": 0.5,
        "Cluster_Encoded": 0.1
      }
    },
    {
      "FILE": "DEMOGRAPHIC",
      "COLUMNS": {
        "ATM_Count": 0.5,
        "No_Of_Family": 1.0,
        "Segment": 1.0,
        "POS_Count": 0.2,
        "Age": 1.0,
        "MB_Count": 0.0,
        "No_of_XH": 1.0,
        "BNA_Count": 0.2,
        "Total_Credits_Count": 0.5,
        "No_Of_Live_Acc": 0.5,
        "Total_Debits_Count": 0.5,
        "BRN_Count": 0.5,
        "INB_Count": 0.0,
        "AUTO_Count": 0.5,
        "Occupation": 1.0,
        "NI_Count": 0.0
      }
    },
    {
      "FILE": "TRANSACTIONS",
      "COLUMNS": {
        "AUTO_Channel_Amount": 0.5,
        "LOAN": 0.0,
        "MB_Channel_Count": 0.0,
        "FD": 0.2,
        "NI_Channel_Amount": 0.0,
        "LOCKER": 0.5,
        "monthly_daily_average_balance": 1,
        "MB_Channel_Amount": 0.0,
        "ECS": 0.5,
        "BNA_Channel_Count": 0.2,
        "NEFT": 0.5,
        "CHEQUE": 0.5,
        "CHARGES": 0.5,
        "SALARY": 0.5,
        "BNA_Channel_Amount": 0.2,
        "CCPMT": 0.2,
        "POS_Channel_Count": 0.2,
        "RTGS": 0.5,
        "BRN_Channel_Count": 0.5,
        "SI": 0.5,
        "INB_Channel_Count": 0.0,
        "ATM_Channel_Amount": 0.5,
        "NI_Channel_Count": 0.0,
        "FT": 0.5,
        "OFFLINE": 0.5,
        "AUTO_Channel_Count": 0.5,
        "CREDIT": 0.5,
        "TAXPMT": 0.2,
        "INTEREST": 0.5,
        "BRN_Channel_Amount": 0.5,
        "INB_Channel_Amount": 0.2,
        "DEBIT": 0.5,
        "DDPO": 0.5,
        "POS_Channel_Amount": 0.2,
        "ATM_Channel_Count": 0.5
      }
    },
    {
      "FILE": "TRANSACTION_COUNTS",
      "COLUMNS": {
        "RTGS": 0.5,
        "SI": 0.5,
        "FD": 0.2,
        "ECS": 0.5,
        "LOCKER": 0.2,
        "OFFLINE": 0.2,
        "DDPO": 0.5,
        "LOAN": 0.2,
        "CCPMT": 0.2,
        "TAXPMT": 0.2,
        "NEFT": 0.5,
        "CHEQUE": 0.5,
        "CHARGES": 0.5,
        "SALARY": 0.1,
        "DEBIT": 0.5,
        "FT": 0.2,
        "INTEREST": 0.5,
        "CREDIT": 0.5
      }
    },
    {
      "FILE": "RATIO",
      "COLUMNS": {
        "DEBIT_6": 1,
        "CASH_6": 0,
        "CREDIT_6": 1,
        "MDAB_6": 1
      }
    }
  ]
}

fs = FeatureSelector(columns=columns, probabilities=probabilities, number_of_models=2)

d = fs.get_columns()
exit()
