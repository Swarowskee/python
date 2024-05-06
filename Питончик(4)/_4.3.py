#coding=utf-8﻿
def write_text_to_file(text, file_name):
    with open(file_name, mode='a+') as file:
        file.write(text + '\n')
    with open(file_name, mode='r') as file:
        lines = file.readlines()
        for i in range(1, len(lines), 2):
            print(lines[i].strip())
write_text_to_file("Старт", "text.txt")
write_text_to_file("1", "text.txt")
write_text_to_file("2", "text.txt")
S