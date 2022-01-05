# Thank you to DJ Oamen (https://youtu.be/3PXfTTcLXqA) for his demonstration titled

# "How to Create a GUI Onscreen Keyboard in Python - Tutorial"

# Reference format: "lead" = 12c4

import random
import tkinter
from tkinter import*
window = Tk()
window.geometry('500x400')
inpu = Entry(window, width=10, bg='blue')
letterValue = ""

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


def dispButtons():
    def execute(character):
        print(character)
        # inpu.delete(0, "end")
        inpu.insert(0, character)
    r = 1
    for row in buttons:
        c = 1
        for character in row:
            # inpu.delete(0,"end")
            # if character == "/":
            # print(character)
            tkinter.Button(window, text=character, command=lambda: execute(
                character)).grid(row=r, column=c)
            # else:
            # inpu.insert(tkinter.END, column)
            c += 1
        r += 1


dispButtons()

# Reference format: "lead" = 13c4
# Reference format: "medicare" = 14d8

# Part One: Initial Letter
# Part Two: basis
# Part Three: length of word


def translateWordPartOne(randomWord):
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
    return letterValue


# Part Two: basis
# Reference format: "medicare" = 14d8
# Reference format: "moments" = 14d7
def translateWordPartTwo(randomWord):
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
    return basis


def translateWordPartThree(randomWord):
    length = len(randomWord)
    return length


def match():
    if inpu.get() == (str(translateWordPartOne(randomWord)) + translateWordPartTwo(randomWord) + str(translateWordPartThree(randomWord))):
        print("CORRECT!")
    else:
        print("Incorrect!!")


print(translateWordPartOne(randomWord))
print(translateWordPartTwo(randomWord))
print(translateWordPartThree(randomWord))
match()


window.mainloop()
