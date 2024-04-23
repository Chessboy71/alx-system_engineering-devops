#!/usr/bin/python3

"""
Write a Python script that, using this REST API, for a given
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

"""
import sys
import requests


if __name__ == "__main__":
    """"""
    url = "https://jsonplaceholder.typicode.com/"

userId = sys.argv[1]
res = requests.get(url + "users/{}".format(userId)).json()
todos_res = requests.get(url + "todos", params={'userId': "{}".format(userId)})
todos_res = todos_res.json()
finiTodo = []
for todo in todos_res:
    if todo.get("completed") is True:
        finiTodo.append(todo.get("title"))

print(
        "Employee {} is done with tasks({}/{}):"
        .format(res.get("name"), len(finiTodo), len(todos_res)))

for todo in finiTodo:
    print("\t {}".format(todo))
