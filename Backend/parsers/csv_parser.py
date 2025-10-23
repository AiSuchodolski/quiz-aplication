import os
import glob
import csv

data = []


def file_path_parser():
    parsers = os.path.join("..", "upload", "*.csv")
    csv_files = glob.glob(parsers)
    if not csv_files:
        print("No CSV files found in uploads folder")
        exit()
    return csv_files

i = 0
for file in file_path_parser():
    with open(file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(f'{i}. {row}')
            i += 1



def file_path_data():
    data = os.path.join("..", "data", "data.txt")
    data_file = open(data, "w", encoding="utf-8")
    data_file.write(data)
    data_file.close()
    return data_file

print(file_path_data())