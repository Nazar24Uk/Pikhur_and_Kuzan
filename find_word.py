from tkinter import *
from tkinter import messagebox
from random import randint

repleced_letters = 0  # Кількість відгаданих букв
letters = []  # Зберігає слово у вигляді списку букв
letters_num = []  # Зберігає маски для букв (наприклад, '_')

# functions
def helpS():  
    print("Help section")

def word():
    global letters, letters_num, repleced_letters
    repleced_letters = 0  # Скидаємо лічильник відгаданих букв
    words = ['red', 'pop', 'fox', 'cat',
             'dog', 'mouse', 'fish', 'men',
             'horse', 'hair']
    index = randint(0, len(words)-1)
    word = words[index]
    letters = list(word)
    letters_num = ['_' for _ in letters]  # Генеруємо список масок
    word_label.config(text=' '.join(letters_num))
    button_word.config(state='disabled')  # Забороняємо натискати кнопку "Слово" під час гри
    inf_label.config(text='')  # Очищуємо інформаційне повідомлення

def play():
    global letters, letters_num, letter_geuss, repleced_letters
    guess = letter_geuss.get().strip()  # Отримуємо введену букву
    if not guess or len(guess) != 1:
        messagebox.showinfo("Увага", "Введіть одну букву")
        return
    
    if repleced_letters == len(letters_num):  # Перевіряємо, чи вже вгадане слово
        button_word.config(state='normal')
        inf_label.config(text='Згенеруйте нове слово')
        return
    
    if guess in letters:  # Якщо буква є у слові
        found = False
        for i in range(len(letters)):
            if letters[i] == guess:
                if letters_num[i] == '_':  # Перевіряємо, чи ця буква ще не відгадана
                    letters_num[i] = guess
                    repleced_letters += 1
                    found = True
        if found:
            inf_label.config(text=f"Буква '{guess}' є в слові!")
        else:
            inf_label.config(text=f"Буква '{guess}' вже відгадана.")
    else:
        inf_label.config(text=f"Букви '{guess}' немає.")
    
    word_label.config(text=' '.join(letters_num))  # Оновлюємо відображення слова
    
    if repleced_letters == len(letters):  # Перевіряємо, чи все слово відгадане
        inf_label.config(text="Ви відгадали слово! Натисніть 'Слово' для нової гри.")
        button_word.config(state='normal')  # Дозволяємо натискати кнопку "Слово"

# configure
win = Tk()
win.title(string='Вгадай слово')
win.geometry('400x300')
win.config(bg='#3021d9')

# menu
myMenu = Menu(win)
win.config(menu=myMenu)
myMenu.add_command(label='EXIT', command=quit)
myMenu.add_command(label='HELP', command=helpS)

label1 = Label(win, text='Вгадай англійське слово',
               bg='#3021d9',
               fg="#f8fc05",
               font='Arial 20')
label1.place(x=40, y=10)
label2 = Label(win, text='Введи англійську букву:',
               bg='#3021d9',
               fg="#fc0522",
               font='Arial 14')
label2.place(x=20, y=50)
letter_geuss = Entry(win, font=('Arial', 14, 'bold'))  # Поле вводу для літери
letter_geuss.place(x=250, y=50, width=30)
button_word = Button(win, font=('Arial', 16, 'bold'), text="Слово",
                     command=word)
button_word.place(x=20, y=100, width=150)
button_letter = Button(win, font=('Arial', 16, 'bold'), text="Ввести букву",
                       command=play)
button_letter.place(x=180, y=100, width=150)

word_label = Label(win, text='',
                   font=('Arial', 24, 'bold'),
                   fg="#FFFFFF",
                   bg="#4B0082")
word_label.place(anchor=CENTER, x=180, y=200)

inf_label = Label(win, text='',
                  font=('Arial', 14, 'bold'),
                  fg="#FFFFFF",
                  bg="#4B0082")
inf_label.place(anchor=CENTER, x=180, y=240)

win.mainloop()
