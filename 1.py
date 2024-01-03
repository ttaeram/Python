from math import *
from random import *
p = range(1, 21)
comment = list(p)
print(type(comment))
shuffle(comment)
win = sample(comment, 4)
print(win)
print("--당첨자--")
print("치킨 당첨자 :", win[0])
print("커피 당첨자 :", win[1:4])
print("치킨 당첨자 : {0}".format(win[0]))
print("커피 당첨자 : {0}".format(win[1:]))


input = ("http://daum.com")
input = input.replace("http://", "")
input = input[0:input.index(".")]
word = input[0:3] + str(len(input)) + str(input.count("e")) + "!"
print(word)

subject = ["a", "b", "c", "a"]
subject = set(subject)
subject = list(subject)
print(subject)