import numpy as np
import numbers


class MyException(Exception):
    pass


class Checker:
    def __init__(self, df):
        self.df = df
        self.columns_names_set = set(self.df.columns)
        self.features = set()
        # like {"column_name":  "Контракт", "links": [1,2,3]}

    def check(self, condition, message=""):
        if not condition:
            raise MyException(message)

    def deep_all(self, iterable):
        return all(np.array(iterable).flatten())

    def __check_list_type(self, values, type_):
        # self.check(isinstance(values, list))
        values_ = np.array(values).flatten()
        self.check(self.deep_all(list(map(lambda x: isinstance(x, type_), values_))))

    def check_columns(self, json_: dict):
        columns_name = json_.get("column_name")
        self.check(isinstance(columns_name, str))
        self.check(columns_name in self.df)

    def check_links(self, json_: dict):
        links = json_.get("links")
        self.__check_list_type(links, str)

        links_set = set(links)
        self.check((len(links_set) == len(links)))
        self.check(links_set.issubset(self.columns_names_set))

        column = json_.get("column_name")
        self.check(column not in links)
        self.check(column not in self.features)
        self.check((len(self.features.intersection(links_set)) == 0))
        self.features.add(column)

    def check_matrix(self, matrix):
        np_weights = np.array(matrix)
        self.check(len(np_weights.shape) == 2)
        self.check(np_weights.shape[0] == np_weights.shape[1])
        self.__check_list_type(matrix, numbers.Number)
        self.check((self.deep_all(9 >= np_weights) and self.deep_all(np_weights >= 0)))

    def check_weights(self, json_: dict):
        weights = json_.get("weights")
        links = json_.get("links")
        self.check((isinstance(weights, list) or weights is "auto"))
        if weights is not "auto":
            self.check_matrix(weights)
            self.check((len(weights) == len(links)))


