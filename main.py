import pandas as pd
from hierarhy import Controller
from config.main_config import x as config_x
data_file_name = "NP_Contracts.csv"
controller = Controller(data_file_name, config_x)
dir(controller)
