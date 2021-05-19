import pathlib
from os import listdir
from os.path import isfile, join

test_file_name = "test_controller.py"

code_import = """import pytest
import pandas as pd
from hierarhy import Controller, MyException
"""
code_test = """def test_main():
    data_file_name = "..\\\\NP_Contracts.csv"
    with pytest.raises(expected_exception=MyException):
        Controller(data_file_name, config_name)\n\n    
"""

path_read = str(pathlib.Path(__file__).parent.parent.absolute()) + "\\test_data"
path_write = str(pathlib.Path(__file__).parent.parent.absolute()) + "\\tests"
onlyfiles = [f for f in listdir(path_read) if isfile(join(path_read, f))]

for i in onlyfiles:
    package_name = i.replace(".py", "")
    if package_name == "__init__":
        continue
    code_import += f"from test_data.{package_name} import x as {package_name.replace('config', 'data')}\n"
code_import += "\n\n"
print(code_import)
with open(path_write + "\\" + test_file_name, 'w+') as f:
    f.write(code_import)

for i in onlyfiles:
    package_name = i.replace(".py", "")
    if package_name == "__init__":
        continue
    #test_name = i.replace("config", "test").replace(".json", ".py")
    name = package_name.replace("config", "")
    data_name = "data"+name
    test_name = "test"+name
    with open(path_write + "\\" + test_file_name, 'a') as f:
        code = code_test
        f.write(code.replace("test_main", test_name).replace("config_name", data_name))
