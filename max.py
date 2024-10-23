#!/usr/bin/env python3 
import os

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

current_directory = os.getcwd()

items_with_sizes = []

for item in os.listdir(current_directory):
    item_path = os.path.join(current_directory, item)
    
    if os.path.isfile(item_path):
        size = os.path.getsize(item_path)
        items_with_sizes.append((size, item))
    elif os.path.isdir(item_path):
        dir_size = get_directory_size(item_path)
        items_with_sizes.append((dir_size, item))
items_with_sizes.sort(key = lambda x: x[0], reverse=True)
for elem in items_with_sizes:
        print (int(elem[0]/1024),'Kb', elem[1])
