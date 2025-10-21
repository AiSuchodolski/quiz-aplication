import os


def get_prompt(prompt_name):
    prompt_path  = os.path.join(os.path.dirname(__file__), f"{prompt_name}.txt")
    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()