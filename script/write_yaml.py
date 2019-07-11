import yaml

data = {"name": "张三", "age": 18}

with open("../data/write_data.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data=data, stream=f,allow_unicode=True)
