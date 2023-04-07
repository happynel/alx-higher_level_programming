#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Happiness", "Edeh")
say_my_name("Kenny", "Black")
say_my_name("Nelly")
try:
    say_my_name(41, "Ede")
except Exception as e:
    print(e)
