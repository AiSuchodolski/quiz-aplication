from pathlib import Path
import csv


def csv_parser(file_path):
    print("csv_parser wywołany")
    file_path = list(Path("Backend", "upload").glob("*.csv"))
    if not file_path:
        print("No CSV files found in uploads folder")
        return False
    data_path = Path("Backend", "data", "data.txt")
    data_path.parent.mkdir(exist_ok=True)
    with data_path.open("a", encoding="utf-8", errors="ignore") as open_data_file:
        for csv_file in file_path:
            with csv_file.open("r", encoding="utf-8", errors="ignore") as open_csv_file:
                reader = csv.reader(open_csv_file)
                for row in reader:
                    open_data_file.write(f'{row}\n')
    print(f"CSV files parsed successfully and saved to {data_path}")
    return True


if __name__ == "__main__":
    csv_parser()

