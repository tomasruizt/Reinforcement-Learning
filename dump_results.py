import csv
import json
import os
import datetime


def dump_results(results, information, basedir, columns):
    date = datetime.datetime.today().strftime("%Y-%m-%d-%H:%M:%S")
    directory = os.path.join(basedir, date)
    os.makedirs(directory)

    for idx, run in enumerate(results):
        filename = os.path.join(directory, "run" + str(idx) + ".csv")
        with open(filename, "w") as file:
            writer = csv.writer(file)
            writer.writerow(columns)
            writer.writerows(run)

    directory_info = os.path.join(directory, "info")
    os.makedirs(directory_info)
    for idx, info in enumerate(information):
        filename = os.path.join(directory_info, "run" + str(idx) + ".json")
        info_json = {idx.__str__(): val for idx, val in info.items()}
        with open(filename, "w") as file:
            json.dump(info_json, file, sort_keys=True, indent=4)

    return directory
