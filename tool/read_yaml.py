import yaml


def read_yaml():
    with open("./data/login.yaml","r",encoding="utf-8") as f:
        return yaml.load(f)

# 问题：预期格式：[(),()],实际格式为字典？
# 解决：将数据取出来，进行组装
if __name__ == '__main__':
    print(read_yaml())
    print("--" * 30)
    # 第一种方式：
    arrs = []
    for data in read_yaml().values():
        arrs.append((data.get("username"),data.get("pwd")))
    print(arrs)
    # 第二中方式
    # for data in read_yaml().values():
    #     arrs.append(tuple(data.values()))
    # print(arrs)