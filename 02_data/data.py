import csv

def load_input(data):
    file = open('nba.csv')
    reader = csv.reader(file)
    data = list(reader)
    print(data)

if __name__ == "__main__":
    load_input('nba.csv')
