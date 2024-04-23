#!/usr/bin/python3

""" exporting to csv """
import csv
import requests 
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    userId = sys.argv[1]
    res = requests.get(url + "users/{}".format(userId)).json()
    todos_res = requests.get(url + "todos", params={'userId': userId})
    todos_res = todos_res.json()
    with open("{}.csv".format(userId), 'w', newline='') as file:
        writer = csv.writer(file)
        for todo in todos_res:
            writer.writerow([userId , res.get("name"), todo.get("completed"), todo.get("title")])

