class Layer:
    def __init__(self, df, json):
        self.df = df
        links_list = json.get("links_list")
        self.columns_names = [value.get("column_name") for value in links_list]
        self.links = [value.get("links") for value in links_list]
        self.weights = []
        for value in links_list:
            weights = value.get("weights")
            if weights is 'auto':
                self.weights.append(self.set_weights())
            else:
                self.weights.append(weights)

    def set_weights(self):
        return 0

    def __repr__(self):
        l = []
        for i in range(len(self.columns_names)):
            s = f"column_name={self.columns_names[i]}\n" \
                f"links={self.links[i]}\n" \
                f"weights={self.weights[i]}\n\n"
            l.append(s)
        return ''.join(l)