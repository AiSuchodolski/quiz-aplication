from pathlib import Path
import csv


def csv_parser():
    csv_path = list(Path("upload").glob("*.csv"))
    if not csv_path:
        print("No CSV files found in uploads folder")
        return False
    data_path = Path("data", "data.txt")
    data_path.parent.mkdir(exist_ok=True)
    with data_path.open("a", encoding="utf-8", errors="ignore") as open_data_file:
        for csv_file in csv_path:
            with csv_file.open("r", encoding="utf-8", errors="ignore") as open_csv_file:
                reader = csv.reader(open_csv_file)
                for row in reader:
                    open_data_file.write(f'{row}\n')
    print(f"CSV files parsed successfully and saved to {data_path}")
    return True


if __name__ == "__main__":
    csv_parser()

