from tkinter import *

class Calculater(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x500")
        self.title("Calculator")
        self.wm_iconbitmap("29_icon.ico")
        self.minsize(300, 400)
        self.maxsize(300, 400) 
        self.srcVar = StringVar()
        self.srcVar.set("") 
        self.srcn = Label(self, textvar=self.srcVar, relief=SUNKEN, font="Lucida 50 bold", anchor=W)
        self.srcn.pack(fill=BOTH)
    
    def click(self, event):
        value = event.widget.cget("text")
        print(value)
        if value == "=":
            if self.srcVar.get().isdigit():
                value = int(self.srcVar.get())
            else:
                try:
                    value = eval(self.srcVar.get())
                except Exception as e:
                    value="Error"
            self.srcVar.set(value)
            self.srcn.update() 

        elif value == "CLS":
            self.srcVar.set("")
            self.srcn.update()           
        else:
            self.srcVar.set(self.srcVar.get() + str(value))
            self.srcn.update()

    def buttons(self):
        count = 0
        j = 0
        for i in range(9,-1,-1):
            if i == 0:
                self.f = Frame(self)
                b1 = Button(self.f, text=".", padx=31, pady=20,)
                b1.pack(side="left", anchor="nw")
                b1.bind("<Button-1>", self.click)  
                b2 = Button(self.f, text=i, padx=30, pady=20)
                b2.pack(side="left", anchor="nw") 
                b2.bind("<Button-1>", self.click)
                b3 = Button(self.f, text="%", padx=29, pady=20)
                b3.pack(side="left", anchor="nw")
                b3.bind("<Button-1>", self.click)
                b4 = Button(self.f, text="/", padx=31, pady=20)
                b4.pack(side="left", anchor="nw")
                b4.bind("<Button-1>", self.click)
                self.f.pack(fill=BOTH)

                self.f = Frame(self)
                b5 = Button(self.f, text="CLS", padx=60, pady=20)
                b5.pack(side="left", anchor="nw")
                b5.bind("<Button-1>", self.click)
                b6 = Button(self.f, text="=", padx=67, pady=20)
                b6.pack(side="left", anchor="nw") 
                b6.bind("<Button-1>", self.click)
                self.f.pack(fill=BOTH)

                break

            count += 1
            l = ["+" , "-", "*"]
            if count%3 == 0 and count!= 0:
                b7 = Button(self.f, text=l[j], padx=29, pady=20)
                b7.pack(side=RIGHT)
                b7.bind("<Button-1>", self.click) 
                j += 1

            if i%3 == 0 and i != 0:
                self.f = Frame(self)
                self.f.pack(fill=BOTH)   

            b = Button(self.f, text=i, padx=30, pady=20)
            b.pack(side="left")
            b.bind("<Button-1>", self.click)
   

if __name__ == '__main__':
    window = Calculater()
    window.buttons()
    window.mainloop()