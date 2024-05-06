#coding=utf-8
weekdays = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
weekdays_dict = {day: index + 1 for index, day in enumerate(weekdays)}
print(weekdays_dict)
