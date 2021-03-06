from tkinter import *
import tkinter.messagebox
import winsound



tk = Tk()
tk.title('Tic Tac Toe')

icon = PhotoImage(file='tictactoe.png')
tk.tk.call('wm','iconphoto',tk._w,icon)


click = True

def checker(buttons):
    global click
    if buttons['text'] == " " and click == True:
        buttons['text'] = 'X'
        click = False
        winsound.PlaySound('button',winsound.SND_FILENAME)
        
    elif buttons['text'] == " " and click == False:
        buttons["text"] = 'O'
        click = True
        winsound.PlaySound('button',winsound.SND_FILENAME)
        

    elif(button1['text'] == "X" and button2["text"] == "X" and button3['text'] == 'X' or
        button4['text'] == "X" and button5["text"] == "X" and button6['text'] == 'X' or    
        button7['text'] == "X" and button8["text"] == "X" and button9['text'] == 'X' or
        button3['text'] == "X" and button5["text"] == "X" and button7['text'] == 'X' or
        button1['text'] == "X" and button5["text"] == "X" and button9['text'] == 'X' or
        button1['text'] == "X" and button4["text"] == "X" and button7['text'] == 'X' or
        button2['text'] == "X" and button5["text"] == "X" and button8['text'] == 'X' or
        button3['text'] == "X" and button6["text"] == "X" and button9['text'] == 'X'):
            tkinter.messagebox.showinfo('Winner X', 'You have just won a game!')
            winsound.PlaySound('congrats1',winsound.SND_FILENAME)


    elif(button1['text'] == "O" and button2["text"] == "O" and button3['text'] == 'O' or
        button4['text'] == "O" and button5["text"] == "O" and button6['text'] == 'O' or    
        button7['text'] == "O" and button8["text"] == "O" and button9['text'] == 'O' or
        button3['text'] == "O" and button5["text"] == "O" and button7['text'] == 'O' or
        button1['text'] == "O" and button5["text"] == "O" and button9['text'] == 'O' or
        button1['text'] == "O" and button4["text"] == "O" and button7['text'] == 'O' or
        button2['text'] == "O" and button5["text"] == "O" and button8['text'] == 'O' or
        button3['text'] == "O" and button6["text"] == "O" and button9['text'] == 'O'):
            tkinter.messagebox.showinfo('Winner O', 'You have just won a game!')
            winsound.PlaySound('congrats1',winsound.SND_FILENAME)
    else:
        tkinter.messagebox.showinfo('Draw', 'Nobody won!')
        
buttons = StringVar()

button1 = Button(tk,text=" ", font=('Arial',12,'bold'),height=4,width=8,fg = 'white',bg = 'grey',relief = RAISED,command=lambda:checker(button1))
button1.grid(row=1,column=0,sticky = 'snew')

button2 = Button(tk,text=" ", font=('Arial',12,'bold'),height=4,width=8,fg = 'white',bg = 'grey',relief = RAISED,command=lambda:checker(button2))
button2.grid(row=1,column=1,sticky = 'snew')

button3 = Button(tk,text=" ", font=('Arial',12,'bold'),height=4,width=8,fg = 'white',bg = 'grey',relief = RAISED,command=lambda:checker(button3))
button3.grid(row=1,column=2,sticky = 'snew')

button4 = Button(tk,text=" ", font=('Arial',12,'bold'),height=4,width=8,fg = 'white',bg = 'grey',relief = RAISED,command=lambda:checker(button4))
button4.grid(row=2,column=0,sticky = 'snew')

button5 = Button(tk,text=" ", font=('Arial',12,'bold'),height=4,width=8,fg = 'white',bg = 'grey',relief = RAISED,command=lambda:checker(button5))
button5.grid(row=2,column=1,sticky = 'snew')

button6 = Button(tk,text=" ", font=('Arial',12,'bold'),height=4,width=8,fg = 'white',bg = 'grey',relief = RAISED,command=lambda:checker(button6))
button6.grid(row=2,column=2,sticky = 'snew')

button7 = Button(tk,text=" ", font=('Arial',12,'bold'),height=4,width=8,fg = 'white',bg = 'grey',relief = RAISED,command=lambda:checker(button7))
button7.grid(row=3,column=0,sticky = 'snew')

button8 = Button(tk,text=" ", font=('Arial',12,'bold'),height=4,width=8,fg = 'white',bg = 'grey',relief = RAISED,command=lambda:checker(button8))
button8.grid(row=3,column=1,sticky = 'snew')

button9 = Button(tk,text=" ", font=('Arial',12,'bold'),height=4,width=8,fg = 'white',bg = 'grey',relief = RAISED,command=lambda:checker(button9))
button9.grid(row=3,column=2,sticky = 'snew')



tk.mainloop()





        
