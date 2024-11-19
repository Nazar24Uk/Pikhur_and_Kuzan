from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import math

nv_c=0
#Функції
def info_box():
    info_wik=Toplevel(wik2)
    info_wik.title('Інформація')
    info_wik.geometry('650x250')
    txt=Label(info_wik,
              font=('Arial',15,"bold"),
              text='Для заповнення полів потрібно підняти сівалку домкратом, \nа в насіннєвий ящик на 1/3 засипати насіння. \nПідставте під сошник брезент. Включіть передачу \nі зробіть 2 – 3 оберти колеса для заповнення \nнасінням коробок насівних апаратів. Висіяне насіння зберіть \nі знову засипте в насіннєвий ящик сівалки. \nПісля цього ручку регулятора норми висіву встановіть \nу відповідне положення і рівномірно прокрутіть ходове колесо'
              )
    txt.place(x=0,y=0)

def nv_k():
     ch_n=0
     sh_n=0
     global pp_c
     pp_c=0
     global nv_c
     nv_c=0
     global m_c
     m_c=0
     #Провірка синтаксису схожості насіння
     if sh.get()=='':
          messagebox.showinfo('Увага!','Ви не обрали схожість насіння!')
     elif sh.get().isdigit()==False:
          messagebox.showinfo('Увага!','Ви ввели невірну схожість насіння!')
     elif float(sh.get())>100:
          messagebox.showinfo('Увага!','Ви ввели завелику cхожість насіння!')
     else:
          sh_n=round(int(sh.get()))


     #Провірка синтаксису чистоти насіння      
          if ch.get()=='':
               messagebox.showinfo('Увага!','Ви не обрали чистоту насіння!')
          elif ch.get().isdigit()==False:
               messagebox.showinfo('Увага!','Ви ввели невірну чистоту насіння!')
          elif float(ch.get())>100:
               messagebox.showinfo('Увага!','Ви ввели завелику чистоту насіння!')
          else:
               ch_n=round(int(ch.get()))
               pp_c=round(ch_n*sh_n/100)
               pp.config(text='Посівна придатність: '+str(pp_c)+'%')

               if m.get()=='':
                    messagebox.showinfo('Увага!','Ви не обрали масу 1000 насінин!')
               elif m.get().isdigit()==False:
                    messagebox.showinfo('Увага!','Ви ввели невірну масу 1000 насінин!')
               else:
                    m_c=round(float(m.get()))

               if k.get()=='':
                    messagebox.showinfo('Увага!','Ви не обрали к-сть рослин на 1 га!')
               elif k.get().isdigit()==False:
                    messagebox.showinfo('Увага!','Ви ввели невірну к-сть рослин на 1 га!')
               else:
                    k_c=float(k.get())
                    nv_c=round((k_c*m_c)/(pp_c*10000))
                    nv.config(text='Норма висіву: '+str(nv_c)+' кг/га')



def c_c():
    pi_val=math.pi
    if nv_c==0 or nv_c=='':
        messagebox.showinfo('Увага!','Ви не розрахували норму висіву!')
    else:
        if d.get()=='':
            messagebox.showinfo('Увага!','Ви не ввели діаметр колеса!')
        elif float(d.get())==0:
            messagebox.showinfo('Увага!','Ви не ввели діаметр колеса!')
        else:
            d_c=float(d.get())
            if ns.get()=='':
                messagebox.showinfo('Увага!','Ви не ввели число обертів колеса сівалки!')
            elif float(ns.get())==0:
                messagebox.showinfo('Увага!','Ви не ввели число обертів колеса сівалки!')
            else:
                ns_c=float(ns.get())
                if w.get()=='':
                    messagebox.showinfo('Увага!','Ви не ввели ширину захвату сівалки!') 
                elif w.get()==0:
                    messagebox.showinfo('Увага!','Ви ввели невірну ширину захвату сівалки!')
                else:
                    w_c=float(w.get())
                    #Розрахунок
                    if wid_r.get()=='':
                        sosh1=((nv_c*pp_c*10000)/m_c)/66000
                        sosh.config(text='К-сть насінин з одного \nсошника на 1 п.м: '+str(round(sosh1)))
                    else:
                        sosh1=((nv_c*pp_c*10000)/m_c)/(10000/(float((wid_r.get()))/100))
                        sosh.config(text='К-сть насінин з одного \nсошника на 1 п.м: '+str(round(sosh1)))
                    c_k=round((nv_c*pi_val*d_c*w_c*ns_c)/10000*2)
                    nv_n.config(text='Норма висіву насіння за \nвизначене число обертів: '+str(c_k))

#Вікно          
wik=Tk()
wik.geometry('1100x730')
wik.title('Калькулятор норми висіву з поправкою на посівну придатність')
wik.config(bg='#5F9EA0')

#Вікно 2
wik2=Tk()
wik2.geometry('900x400')
wik2.title('Установка сівалки під норму висіву')
wik2.config(bg='#5F9EA0')

#Заголовок
zag1=Label(wik,
	     fg='black',
	     font=('Arial',25,"bold"),
          bg='#5F9EA0',
	     text='Калькулятор норми висіву')
zag1.place(x=310,y=0)

zag2=Label(wik,
          font=('Arial',15,"bold"),
          text='Таблиця орієнтовних значень',
          fg='DarkGreen',
          bg='#5F9EA0'
          )
zag2.place(x=80,y=35)

#Поле вводу для пп
#Поле вводу схожості насіння
shT=Label(wik,
	fg='black',
	font=('Arial',15,"bold"),
	bg='#5F9EA0',
	text='Схожість насіння, %'
     )
shT.place(x=700,y=140)

sh=Entry(wik,
    font=('Arial',15,"bold")
	)
sh.place(x=930,y=140,width=100)

#Поле вводу чистоти насіння
chT=Label(wik,
     fg='black',
	font=('Arial',15,"bold"),
	text='Чистота насіння, %',
     bg='#5F9EA0'
     )
chT.place(x=700,y=185)

ch=Entry(wik,
     fg='black',
	font=('Arial',15,"bold")
	)
ch.place(x=930,y=185,width=100)

#Вивід посівної придатності
pp=Label(wik,
         font=('Arial',20,"bold"),
         text='Посівна придатність: 0%',
         fg='black',
         bg='#5F9EA0'
        )
pp.place(x=50,y=590)

#Вивід норми висіву
nv=Label(wik,
         font=('Arial',20,"bold"),
         text='Норма висіву: 0 кг/га',
         fg='black',
         bg='#5F9EA0')
nv.place(x=50,y=550)


#Поле вводу для нв
#Поле вводу масси 1000 насінин
mT=Label(wik,
         font=('Arial',15,"bold"),
         text='Маса 1000 насінин, г',
         fg='black',
         bg='#5F9EA0')
mT.place(x=700,y=230)

m=Entry(wik,
        fg='black',
        font=('Arial',15,"bold")
        )
m.place(x=930,y=230,width=100)

#Поле вводу рослин на 1 га
kT=Label(wik,
         font=('Arial',15,"bold"),
         text='К-сть рослин на 1 га',
         fg='black',
         bg='#5F9EA0'
         )
kT.place(x=700,y=275)

k=Entry(wik,
        fg='black',
	   font=('Arial',15,"bold")
        )
k.place(x=930,y=275,width=100)


#Таблиця орієнтовної норми висіву і маси 1000 насінин
img1=PhotoImage(file='tab2.png')
tab=Canvas(wik,width='457',height='440',bg='white')
tab.create_image(230,223,image=img1)
tab.place(x=20,y=65)

#Кнопка розрахунку норми висіву
kn_nv=Button(wik,
          font=('Arial',20,"bold"),
          text='Розрахувати норму висіву',
          command=lambda:nv_k()
          )
kn_nv.place(x=100,y=650,height=50,width=900)




#Друге вікно
#Заголовок1
zag_1=Label(wik2,
            text='Установка сівалки під норму висіву',
            font=('Arial',25,"bold"),
            bg='#5F9EA0',
            fg='black'
            )
zag_1.place(x=150,y=20)

#Виведення підказки
button_info=Button(wik2,
                   font=('Arial',20,"bold"),
                   text='\u24d8',
                   command=lambda:info_box()
                   )
button_info.place(x=840,y=20,width=40,height=40)

#Поле вводу діаметру колеса
dT=Label(wik2,
        text='Діаметр колеса, м',
        font=('Arial',15,"bold"),
        bg='#5F9EA0',
        fg='black'
        )
dT.place(x=20,y=85)
d=Entry(wik2,
        font=('Arial',15,"bold"),
        fg='black'
        )
d.place(x=390,y=85,width=100)

#Число обертів колеса сівалки
nsT=Label(wik2,
          text='Число обертвів колеса сівалки',
          font=('Arial',15,"bold"),
          bg='#5F9EA0',
          fg='black'
          )
nsT.place(x=20,y=120)

ns=Entry(wik2,
         font=('Arial',15,"bold"),
         fg='black'
        )
ns.place(x=390,y=120,width=100)

#Поле вводу ширини захвати сівалки
wT=Label(wik2,
         text='Ширина захвату сівалки, м',
         font=('Arial',15,"bold"),
         bg='#5F9EA0',
         fg='black'
         )
wT.place(x=20,y=155)

w=Entry(wik2,
       font=('Arial',15,"bold"),
       fg='black'
        )
w.place(x=390,y=155,width=100)

#Ввід ширини міжрядь при широкорядному посіві
wid_rT=Label(wik2,
            text='При сівбі широкорядним способом\n введіть ширину міжрядь, см',
            font=('Arial',15,"bold"),
            bg='#5F9EA0',
            fg='black',
            )
wid_rT.place(x=20,y=190)
wid_r=Entry(wik2,
            font=('Arial',15,"bold"),
            fg='black'
            )
wid_r.place(x=390,y=190,width=100)

#К-сть насінин з одного сошника на п.м
sosh=Label(wik2,
           text='К-сть насінин з одного \nсошника на 1 п.м: 0',
           bg='#5F9EA0',
           fg='black',
           font=('Arial',15,"bold")
           )
sosh.place(x=500,y=85)

#Норма висіву насіння за визначене число обертів
nv_n=Label(wik2,
           text='Норма висіву насіння за \nвизначене число обертів: 0',
           bg='#5F9EA0',
           fg='black',
           font=('Arial',15,"bold")
           )
nv_n.place(x=500,y=150)

#Кнопка
roz=Button(wik2,
           font=('Arial',20,"bold"),
           text='Розрахувати',
           command=lambda:c_c()
           )
roz.place(x=20,y=300,width=860)

wik.mainloop()
wik2.mainloop()