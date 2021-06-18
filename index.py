import random

print("乱数生成機へようこそ")


def keisan():
    for i in range(30):
        print(random.randint(0,5))


def new_function():
    check_z = input("早速ですが実行しますか y/n >>>")
    if check_z == "y":
        print("キーを押したら実行します")
        input()
        keisan()
        input("なにかキーを押して終了>>>")
    
    elif check_z == "n":
        print("キャンセルします")
        input("なにかキーを押して終了>>>")
    
    else:
        print("「y」か「n」で答えてください")
        new_function()
new_function()
