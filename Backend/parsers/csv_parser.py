import os
import glob
import csv


def csv_parser():
    csv_path = os.path.join("..", "upload", "*.csv")
    csv_files = glob.glob(csv_path)
    if not csv_files:
        print("No CSV files found in uploads folder")
        exit()
    data_path = os.path.join("..", "data", "data.txt")
    i = 1
    for csv_file in csv_files:
        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            with open(data_path, "a", encoding="utf-8") as data_file:
                for row in reader:
                    data_file.write(f'{i}. {row}\n')
                    i += 1
    print("CSV files parsed successfully and saved to data.txt")


csv_parser()



# def file_path_parser():
#     parsers = os.path.join("..", "upload", "*.csv")
#     csv_files = glob.glob(parsers)
#     if not csv_files:
#         print("No CSV files found in uploads folder")
#         exit()
#     return csv_files

# i = 0
# for file in file_path_parser():
#     with open(file, "r", encoding="utf-8") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             data.append((f'{i}. {row}\n'))
#             i += 1



# def file_path_data():
#     path_data = os.path.join("..", "data", "data.txt")
#     data_file = open(path_data, "w", encoding="utf-8")
#     data_file.write(''.join(data))
#     data_file.close()
#     print("Data saved to data.txt")

# file_path_data()