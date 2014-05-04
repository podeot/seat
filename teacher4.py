import random
def random_color():
    color_const=['#']
    for k in range(6):
        temp=random.randint(1,15)
        color_const.append(str(hex(temp)).strip("0x"))
    color_const_num="".join(color_const)
    return color_const_num
def openhelp():
    import webbrowser
    webbrowser.open("http://seat.pode.es/help.html")
def opencopyright():
    import webbrowser
    webbrowser.open("http://seat.pode.es/license.html")
def secret_mode():
    pass
def run():
    txt1.delete(1.0,END)
    input_val1=ent1.get()
    for i in range(6):
        can.itemconfig(tab_name[i],fill=random_color())
    if input_val1=='':
        txt1.insert(INSERT,"값을 넣고 누르시오!")
        return clear()
    secret_code=['secret','bsis']
    if input_val1 in secret_code:
        return secret_mode()
    else:
        clear()
        if 0>=int(input_val1) or 25<=int(input_val1):
            txt1.insert(INSERT,'값은 1이상 24이하인 정수여야합니다.\n')
            return 
        else:algorithm()
def clear():
    for i in range(24):
        stu_name[i]['text']=''
def algorithm():
    txt1.insert(INSERT,'정상작동 시작\n')
    max_num=int(ent1.get())
    peo_list=[i+1 for i in range(max_num)]
    if ent2.get().strip(' ') != '':
        no_peo=ent2.get().split(',')
        for i in range(len(no_peo)):
            no_peo[i]=int(no_peo[i])
            if no_peo[i] in peo_list:
                peo_list.pop(peo_list.index(no_peo[i]))
    else:
        no_peo=[]
    random.shuffle(peo_list)
    txt1.insert(INSERT,'랜덤하게 섞기 완료.\n')
    for i in range(len(peo_list)):
        if i<=15 :
            stu_name[i]['text']=peo_list[i]
        elif i==16 or i==17:
            stu_name[i+2]['text']=peo_list[i]
        elif i==18 or i==19:
            stu_name[i+4]['text']=peo_list[i]
        elif i==20 or i==21:
            stu_name[i-4]['text']=peo_list[i]
        else:
            stu_name[i-2]['text']=peo_list[i]
        txt1.insert(INSERT,'자리배치 완료.\n')
tab_name=[]
for i in range(6):
    tab_name.append(str(i)+'tab')
from tkinter import *
stu_name=[]
for i in range(24):
    stu_name.append(str(i)+'seat')
#var
x1=60
x2=160
xstep=180
y1=150
y2=200
ystep=120
root=Tk()
root.title('자리배치 v2.1')
root.minsize(400,600)
root.maxsize(400,600)





menu=Menu(root)
helpmenu=Menu(menu)
helpmenu.add_command(label="Help", command=openhelp)
helpmenu.add_command(label="저작권", command=opencopyright)
menu.add_cascade(label="Help",menu=helpmenu)
bg_image=PhotoImage(file='logo.gif')
can=Canvas(root,width=400,height=550)
kyotak=can.create_polygon(50,80,50,110,350,110,350,80,fill='green',outline='black')
for i in [0,1,2]:
    for j in [0,1]:
        tab_name[2*i+j]=can.create_polygon(x1+xstep*j,y1+ystep*i,x1+xstep*j,y2+ystep*i,x2+xstep*j,y2+ystep*i,x2+xstep*j,y1+ystep*i,fill=random_color(),outline='black')
for i in range(6):
    for j in range(4):
        stu_name[4*i+j]=Label(text="",font=('바탕',18),fg='black')
        if j%2==0:
            x_val=x1+xstep*(j/2)-30
        else:
            x_val=x2+xstep*(j//2)+1
        if i%2==0:
            y_val=y1+ystep*(i/2)-10
        else:
            y_val=y2+ystep*(i//2)-15
            
        stu_name[4*i+j].place(x=x_val,y=y_val)

lab1=Label(root,text="칠판",bg='green',font=('바탕',12),fg='red')
lab2=Label(root,text="끝번호",font=('바탕',12),fg='blue')
lab3=Label(root,text="없는 번호(Comma로 분리)",font=('바탕',12),fg='blue')
ent1=Entry(root,width=5)
ent2=Entry(root,width=15)
txt1=Text(root,width=38,height=7)
but1=Button(root,image=bg_image,command=run,width=100,height=100)






can.place(x=0,y=0)
lab1.place(x=180,y=82)
lab2.place(x=10,y=00)
lab3.place(x=10,y=30)
ent1.place(x=220,y=00)
ent2.place(x=220,y=30)
txt1.place(x=10,y=500)
but1.place(x=290,y=490)





root.config(menu=menu)
root.mainloop()
