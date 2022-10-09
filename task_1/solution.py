import csv

PATH_TO_FILE = "data.csv"


def group_by_country(file: str):
    with open(file, "r") as f:
        read_data = csv.reader(f)
        for s in read_data:
            print(s)
        
        


if __name__ == "__main__":
    data = group_by_country(file=PATH_TO_FILE)
    print(data)
