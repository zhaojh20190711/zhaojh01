import yaml


def read_data():
    with open("../data/data.yaml", "r", encoding="utf-8") as f:
        data = yaml.load(f)
        # print(data)
    return data


if __name__ == '__main__':
    # print(__name__)
    # print("if __name__ == '__main__':")
    print(read_data())
