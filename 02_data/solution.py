import csv

def population_center(data):
    with open(data, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        x, y, counter = 0, 0, 0
        for row in reader:
            x += float(row[0])
            y += float(row[1])
            counter += 1
        longitude = x / counter
        latitude = y / counter
        print(f"The mean center of the squirrel population is at {longitude}, {latitude}")

if __name__ == "__main__":
    population_center('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
