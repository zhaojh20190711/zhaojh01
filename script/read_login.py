import yaml


def read_login_data():
    with open("../data/login.yaml", "r", encoding="utf-8")as f:
        data = yaml.load(f)
        list = []
        for item in data.values():
            list.append(tuple(item.values()))
    return list


print(read_login_data())
