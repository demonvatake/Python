# 1. Напишите программу, которая принимает на вход цифру,
#    обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input())

if 5 < a < 8:
    print("выходной")
elif 0 < a < 6:
    print("рабочий день")
else:
    print("эта не день недели")