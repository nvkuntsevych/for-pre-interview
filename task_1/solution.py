from csv import reader
from itertools import groupby


PATH_TO_FILE = "data.csv"


def group_by_country(file: str):
    groupped_result = {}
    with open(file, "r") as f:
        read_data = reader(f)
        lst = sorted(tuple(reader(f))[1:], reverse=True)
        for country, groups in groupby(lst, lambda row: row[0]):
            names = [group[1] for group in groups]
            groupped_result[country] = {"people": names, "count": len(names)}
        return groupped_result

        
        


if __name__ == "__main__":
    data = group_by_country(file=PATH_TO_FILE)
    print(data)
