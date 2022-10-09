from csv import reader


PATH_TO_FILE = "data.csv"


def group_by_country(file: str):
    with open(file, "r") as f:
        read_data = reader(f)
        lst = tuple(reader(f))[1:]
        print(lst)
        
        


if __name__ == "__main__":
    data = group_by_country(file=PATH_TO_FILE)
    print(data)
