from pathlib import Path

def text_parser(file_path):
    print("text_parser wywołany")
    file_path = list(Path("Backend", "upload").glob("*.txt"))
    if not file_path:
        print("No TXT files found in upload folder")
        return False
    data_path = Path("Backend", "data", "data.txt")
    data_path.parent.mkdir(exist_ok=True)
    with data_path.open("a", encoding="utf-8", errors="ignore") as open_data_file:
        for text_file in file_path:
            with text_file.open("r", encoding="utf-8", errors="ignore") as open_text_file:
                for line in open_text_file:
                    open_data_file.write(line)
    print(f"Data saved to {data_path}")
    return True


if __name__ == "__main__":
    text_parser()   

