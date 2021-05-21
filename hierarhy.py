import pandas as pd
from checker import Checker, MyException
from layer import Layer


class Controller:
    def __init__(self,
                 dafa_file_name,
                 config,
                 ):
        self.dafa_file_name = dafa_file_name
        self.df = pd.read_csv(self.dafa_file_name, nrows=1000)
        self.layers = []
        self.checker = Checker(df=self.df)
        self.json_ = config
        self.__configure()

    def __configure(self):
        for _, layer in self.json_.items():

            links_list = layer.get("links_list")

            if links_list is None:
                raise MyException

            for links_list_element in links_list:
                self.checker.check_columns(links_list_element)
                self.checker.check_links(links_list_element)
                self.checker.check_weights(links_list_element)

            self.layers.append(Layer(self.df, layer))

        for l in self.layers:
            print(l)
        print("OK")
