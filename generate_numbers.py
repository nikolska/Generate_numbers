from tkinter import *
from itertools import combinations


def generate_the_numbers():
    '''
    The main function that generates the numbers.
    '''
    quantity_ = entry_quantity.get()
    sum_n = entry_sum.get()
    quantity = int(quantity_)
    sum_ = int(sum_n)
    numbers = range(1, 10)
    res_num = [z for z in numbers if z < sum_]
    list_ = [y for y in combinations(res_num, quantity)]
    result = [x for x in list_ if sum(x) == sum_]
    if len(result) > 0:
        answer.insert(END, result)
    else:
        answer.insert(END, 'no possible combinations')


def clear_the_data():
    '''
    Clear the last answers.
    '''
    answer.delete('1.0', END)


window = Tk()
window.title("Generate the numbers")

text_sum = Label(text="Enter the sum of the numbers:", bg="LightBlue1", width=30, height=1)
text_sum.pack()

entry_sum = Entry(bg="white", width=30)
entry_sum.pack()

text_quantity = Label(text="Enter the quantity of the numbers:", bg="LightBlue1", width=30, height=1)
text_quantity.pack()

entry_quantity = Entry(bg="white", width=30)
entry_quantity.pack()

answer = Text(bg="white", width=28, height=6)
answer.pack()

clear = Button(text="Clear", bg="LightBlue1", width=15, height=1)
clear.pack()
clear.bind('<Button-1>', clear_the_data)

check = Button(text="Check", bg="LightBlue1", width=15, height=1)
check.pack()
check.bind('<Button-1>', generate_the_numbers)

window.mainloop()
