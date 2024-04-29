#coding=utf-8
ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
shot = "б1"  # квадрат обстрела

if shot.lower() in ship.lower():
    print("ГООЛ!")
else:
    print("анрег(")
