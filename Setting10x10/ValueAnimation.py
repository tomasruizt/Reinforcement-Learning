import numpy as np

import pandas as pd
import os
import json


def load_matrices(directory, z_function):
    directory_info = os.path.join(directory, "info")
    runs = [file for file in os.listdir(directory_info) if file.endswith(".json")]
    values = []
    for run in sorted(runs, key=_numeric):
        filename = os.path.join(directory_info, run)
        with open(filename, "r") as file:
            values.append(json.load(file))

    X, Y = np.meshgrid(np.arange(10), np.arange(10))
    Zs = [z_function(X, Y, value) for value in values]

    return X, Y, Zs


def _numeric(s: str):
    return int(s.replace("run", "").replace(".json", ""))


def load_results(directory):
    dfs = []
    runs = [file for file in os.listdir(directory) if file.endswith(".csv")]
    for run in runs:
        filename = os.path.join(directory, run)
        df = pd.read_csv(filename)
        df["STATE"] = df["STATE"].apply(_parse_tuple)
        dfs.append(df)
    return dfs


def _parse_tuple(string):
    return int(string[1]), int(string[4])