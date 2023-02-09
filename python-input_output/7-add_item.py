#!/usr/bin/python3
"""Module that adds all arguments in a Python list"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


with open("add_item.json", 'a') as f:
    args_list = []
    args_list = list(sys.argv[1:])
    save_to_json_file(args_list, "add_item.json")
    load_from_json_file("add_item.json")
