# TODO решите задачу
import json
def task() -> float:

    json_file_way = 'input.json'
    with open(json_file_way, 'r') as file:
        data = json.load(file)
    sum_ = 0.0
    for item in data:
        score = item.get("score", 0)
        weight = item.get("weight", 0)
        sum_ += score * weight
    return round(sum_, 3)

print(task())
