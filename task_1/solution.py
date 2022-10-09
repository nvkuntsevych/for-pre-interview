from csv import reader
from itertools import groupby


PATH_TO_FILE = "data.csv"


def group_by_country(file: str):
    with open(file, "r") as f:
        read_data = reader(f)
        lst = sorted(tuple(reader(f))[1:], reverse=True)
        for country, groups in groupby(lst, lambda row: row[0]):
            print(country, groups)

        
        


if __name__ == "__main__":
    data = group_by_country(file=PATH_TO_FILE)
    print(data)
