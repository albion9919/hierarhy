import pytest
import pandas as pd
from hierarhy import Controller, MyException
from test_data.config_cyclic_links import x as data_cyclic_links
from test_data.config_cyclic_links2 import x as data_cyclic_links2
from test_data.config_incorrect_columns_name_type import x as data_incorrect_columns_name_type
from test_data.config_incorrect_columns_name_values import x as data_incorrect_columns_name_values
from test_data.config_incorrect_level_weights_len import x as data_incorrect_level_weights_len
from test_data.config_incorrect_level_weights_type import x as data_incorrect_level_weights_type
from test_data.config_incorrect_level_weights_type2 import x as data_incorrect_level_weights_type2
from test_data.config_incorrect_level_weights_values import x as data_incorrect_level_weights_values
from test_data.config_incorrect_links_type import x as data_incorrect_links_type
from test_data.config_incorrect_links_values import x as data_incorrect_links_values
from test_data.config_incorrect_weights_len import x as data_incorrect_weights_len
from test_data.config_incorrect_weights_type import x as data_incorrect_weights_type
from test_data.config_incorrect_weights_values import x as data_incorrect_weights_values


def test_cyclic_links():
    data_file_name = "..\\NP_Contracts.csv"
    with pytest.raises(expected_exception=MyException):
        Controller(data_file_name, data_cyclic_links)

    
def test_cyclic_links2():
    data_file_name = "..\\NP_Contracts.csv"
    with pytest.raises(expected_exception=MyException):
        Controller(data_file_name, data_cyclic_links2)

    
def test_incorrect_columns_name_type():
    data_file_name = "..\\NP_Contracts.csv"
    with pytest.raises(expected_exception=MyException):
        Controller(data_file_name, data_incorrect_columns_name_type)

    
def test_incorrect_columns_name_values():
    data_file_name = "..\\NP_Contracts.csv"
    with pytest.raises(expected_exception=MyException):
        Controller(data_file_name, data_incorrect_columns_name_values)

    
def test_incorrect_level_weights_len():
    data_file_name = "..\\NP_Contracts.csv"
    with pytest.raises(expected_exception=MyException):
        Controller(data_file_name, data_incorrect_level_weights_len)

    
def test_incorrect_level_weights_type():
    data_file_name = "..\\NP_Contracts.csv"
    with pytest.raises(expected_exception=MyException):
        Controller(data_file_name, data_incorrect_level_weights_type)

    
def test_incorrect_level_weights_type2():
    data_file_name = "..\\NP_Contracts.csv"
    with pytest.raises(expected_exception=MyException):
        Controller(data_file_name, data_incorrect_level_weights_type2)

    
def test_incorrect_level_weights_values():
    data_file_name = "..\\NP_Contracts.csv"
    with pytest.raises(expected_exception=MyException):
        Controller(data_file_name, data_incorrect_level_weights_values)

    
def test_incorrect_links_type():
    data_file_name = "..\\NP_Contracts.csv"
    with pytest.raises(expected_exception=MyException):
        Controller(data_file_name, data_incorrect_links_type)

    
def test_incorrect_links_values():
    data_file_name = "..\\NP_Contracts.csv"
    with pytest.raises(expected_exception=MyException):
        Controller(data_file_name, data_incorrect_links_values)

    
def test_incorrect_weights_len():
    data_file_name = "..\\NP_Contracts.csv"
    with pytest.raises(expected_exception=MyException):
        Controller(data_file_name, data_incorrect_weights_len)

    
def test_incorrect_weights_type():
    data_file_name = "..\\NP_Contracts.csv"
    with pytest.raises(expected_exception=MyException):
        Controller(data_file_name, data_incorrect_weights_type)

    
def test_incorrect_weights_values():
    data_file_name = "..\\NP_Contracts.csv"
    with pytest.raises(expected_exception=MyException):
        Controller(data_file_name, data_incorrect_weights_values)

    
