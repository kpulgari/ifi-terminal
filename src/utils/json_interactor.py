import json
from pathlib import Path


def write(file_path: Path, data):
    file_path.write_text(json.dumps(data))


def read(file_path: Path):
    return json.loads(file_path.read_text())


if __name__ == "__main__":
    print("Executing json_interactor.py")
    # write(Path("test.json"), {"test": "test"})
    # print(read(Path("test.json")))