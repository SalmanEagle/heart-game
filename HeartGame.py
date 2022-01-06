# This is code written by github.com/winnerman212


import random
import tkinter as tk
from tkinter import *
window = Tk()
window.geometry('500x400')
inpu = Entry(window, width=10, bg='blue')
letterValue = ""
basis = ''
length = 1

with open("./wordlist.10000.txt") as word_file:
    words = word_file.read().split()


def generateWord():
    translate = random.choice(words)
    return translate


buttons = [['i', 'r', '|', '9'],
           ['h', 'q', 'z', '8'],
           ['g', 'p', 'y', '7'],
           ['f', 'o', 'x', '6'],
           ['e', 'n', 'w', '5'],
           ['d', 'm', 'v', '4'],
           ['c', 'l', 'u', '3'],
           ['b', 'k', 't', '2'],
           ['a', 'j', 's', '1'],
           ['0', '1', '2', '/']]

inpu.grid(row=0, column=0)

randomWord = generateWord()

Label(window, text=randomWord).grid(row=0, column=1)


def execute(ch):
    inpu.insert(END, ch)

# def dispButtons():
#     def execute(character):
#         print(character)
#         # inpu.delete(0, "end")
#         inpu.insert(0, character)
#     r = 1
#     for row in buttons:
#         c = 1
#         for character in row:
#             # inpu.delete(0,"end")
#             # if character == "/":
#             # print(character)
#             tk.Button(window, text=character, command=lambda: execute(
#                 character)).grid(row=r, column=c)
#             # else:
#             # inpu.insert(tk.END, column)
#             c += 1
#         r += 1


b1 = tk.Button(window, text="i", command=lambda: execute("i"))
b1.grid(row=1, column=1)

b2 = tk.Button(window, text="r", command=lambda: execute("r"))
b2.grid(row=1, column=2)

b3 = tk.Button(window, text="|", command=lambda: execute("|"))
b3.grid(row=1, column=3)

b4 = tk.Button(window, text="9", command=lambda: execute("9"))
b4.grid(row=1, column=4)

b5 = tk.Button(window, text="h", command=lambda: execute("h"))
b5.grid(row=2, column=1)

b6 = tk.Button(window, text="q", command=lambda: execute("q"))
b6.grid(row=2, column=2)

b7 = tk.Button(window, text="z", command=lambda: execute("z"))
b7.grid(row=2, column=3)

b8 = tk.Button(window, text="8", command=lambda: execute("8"))
b8.grid(row=2, column=4)

b9 = tk.Button(window, text="g", command=lambda: execute("g"))
b9.grid(row=3, column=1)

b10 = tk.Button(window, text="p", command=lambda: execute("p"))
b10.grid(row=3, column=2)

b11 = tk.Button(window, text="y", command=lambda: execute("y"))
b11.grid(row=3, column=3)

b12 = tk.Button(window, text="7", command=lambda: execute("7"))
b12.grid(row=3, column=4)

b13 = tk.Button(window, text="f", command=lambda: execute("f"))
b13.grid(row=4, column=1)

b14 = tk.Button(window, text="o", command=lambda: execute("o"))
b14.grid(row=4, column=2)

b15 = tk.Button(window, text="x", command=lambda: execute("x"))
b15.grid(row=4, column=3)

b16 = tk.Button(window, text="6", command=lambda: execute("6"))
b16.grid(row=4, column=4)

b17 = tk.Button(window, text="e", command=lambda: execute("e"))
b17.grid(row=5, column=1)

b18 = tk.Button(window, text="n", command=lambda: execute("n"))
b18.grid(row=5, column=2)

b19 = tk.Button(window, text="w", command=lambda: execute("w"))
b19.grid(row=5, column=3)

b20 = tk.Button(window, text="5", command=lambda: execute("5"))
b20.grid(row=5, column=4)

b21 = tk.Button(window, text="d", command=lambda: execute("d"))
b21.grid(row=6, column=1)

b22 = tk.Button(window, text="m", command=lambda: execute('m'))
b22.grid(row=6, column=2)

b23 = tk.Button(window, text="v", command=lambda: execute('v'))
b23.grid(row=6, column=3)

b24 = tk.Button(window, text="4", command=lambda: execute('4'))
b24.grid(row=6, column=4)

b25 = tk.Button(window, text="c", command=lambda: execute('c'))
b25.grid(row=7, column=1)

b26 = tk.Button(window, text="l", command=lambda: execute('l'))
b26.grid(row=7, column=2)

b27 = tk.Button(window, text="u", command=lambda: execute('u'))
b27.grid(row=7, column=3)

b28 = tk.Button(window, text="3", command=lambda: execute('3'))
b28.grid(row=7, column=4)

b29 = tk.Button(window, text="b", command=lambda: execute('b'))
b29.grid(row=8, column=1)

b30 = tk.Button(window, text="k", command=lambda: execute('k'))
b30.grid(row=8, column=2)

b31 = tk.Button(window, text="t", command=lambda: execute('t'))
b31.grid(row=8, column=3)

b32 = tk.Button(window, text="2", command=lambda: execute('2'))
b32.grid(row=8, column=4)

b33 = tk.Button(window, text="a", command=lambda: execute('a'))
b33.grid(row=9, column=1)

b34 = tk.Button(window, text="j", command=lambda: execute('j'))
b34.grid(row=9, column=2)

b35 = tk.Button(window, text="s", command=lambda: execute('s'))
b35.grid(row=9, column=3)

b36 = tk.Button(window, text="1", command=lambda: execute('1'))
b36.grid(row=9, column=4)

b37 = tk.Button(window, text="0", command=lambda: execute('0'))
b37.grid(row=10, column=1)

b38 = tk.Button(window, text="1", command=lambda: execute('1'))
b38.grid(row=10, column=2)

b39 = tk.Button(window, text="2", command=lambda: execute('2'))
b39.grid(row=10, column=3)

b40 = tk.Button(window, text="/", command=lambda: match())
b40.grid(row=10, column=4)

# dispButtons()

# Reference format: "lead" = 13c4
# Reference format: "medicare" = 14d8

# Part One: Initial Letter
# Part Two: basis
# Part Three: length of word


def translateWord(randomWord):
    # extract first letter
    # for i in range(0, 26):
    if randomWord[0] == 'a':
        letterValue = '01'
    elif randomWord[0] == 'b':
        letterValue = '02'
    elif randomWord[0] == 'c':
        letterValue = '03'
    elif randomWord[0] == 'd':
        letterValue = '04'
    elif randomWord[0] == 'e':
        letterValue = '05'
    elif randomWord[0] == 'f':
        letterValue = '06'
    elif randomWord[0] == 'g':
        letterValue = '07'
    elif randomWord[0] == 'h':
        letterValue = '08'
    elif randomWord[0] == 'i':
        letterValue = '09'
    elif randomWord[0] == 'j':
        letterValue = '11'
    elif randomWord[0] == 'k':
        letterValue = '12'
    elif randomWord[0] == 'l':
        letterValue = '13'
    elif randomWord[0] == 'm':
        letterValue = '14'
    elif randomWord[0] == 'n':
        letterValue = '15'
    elif randomWord[0] == 'o':
        letterValue = '16'
    elif randomWord[0] == 'p':
        letterValue = '17'
    elif randomWord[0] == 'q':
        letterValue = '18'
    elif randomWord[0] == 'r':
        letterValue = '19'
    elif randomWord[0] == 's':
        letterValue = '21'
    elif randomWord[0] == 't':
        letterValue = '22'
    elif randomWord[0] == 'u':
        letterValue = '23'
    elif randomWord[0] == 'v':
        letterValue = '24'
    elif randomWord[0] == 'w':
        letterValue = '25'
    elif randomWord[0] == 'x':
        letterValue = '26'
    elif randomWord[0] == 'y':
        letterValue = '27'
    elif randomWord[0] == 'z':
        letterValue = '28'
    else:
        letterValue = '29'
    print(letterValue)
# find the basic letter

    if randomWord[0] == 'a':
        basis = 'a'
    elif randomWord[0] == 'b':
        basis = 'b'
    elif randomWord[0] == 'c':
        basis = 'c'
    elif randomWord[0] == 'd':
        basis = 'd'
    elif randomWord[0] == 'e':
        basis = 'e'
    elif randomWord[0] == 'f':
        basis = 'f'
    elif randomWord[0] == 'g':
        basis = 'g'
    elif randomWord[0] == 'h':
        basis = 'h'
    elif randomWord[0] == 'i':
        basis = 'i'
    elif randomWord[0] == 'j':
        basis = 'a'
    elif randomWord[0] == 'k':
        basis = 'b'
    elif randomWord[0] == 'l':
        basis = 'c'
    elif randomWord[0] == 'm':
        basis = 'd'
    elif randomWord[0] == 'n':
        basis = 'e'
    elif randomWord[0] == 'o':
        basis = 'f'
    elif randomWord[0] == 'p':
        basis = 'g'
    elif randomWord[0] == 'q':
        basis = 'h'
    elif randomWord[0] == 'r':
        basis = 'i'
    elif randomWord[0] == 's':
        basis = 'a'
    elif randomWord[0] == 't':
        basis = 'b'
    elif randomWord[0] == 'u':
        basis = 'c'
    elif randomWord[0] == 'v':
        basis = 'd'
    elif randomWord[0] == 'w':
        basis = 'e'
    elif randomWord[0] == 'x':
        basis = 'f'
    elif randomWord[0] == 'y':
        basis = 'g'
    elif randomWord[0] == 'z':
        basis = 'h'
    else:
        basis = 'i'
    print(basis)
# find length of word
    length = len(randomWord)
    print(length)


def match():
    print(inpu.get())
    if inpu.get() == (str(letterValue) + basis + str(length)):
        print("CORRECT!")
    else:
        print("Incorrect!!")


translateWord(randomWord)


window.mainloop()
