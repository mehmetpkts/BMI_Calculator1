import tkinter

# window
window = tkinter.Tk()
window.title("BMI PROJECT")
window.minsize(width=300,height=300)

# funaction

def funaction_button():
    input1 = float(entry.get())
    input2 = float(entry2.get())
    new = input1**2 / 10000
    sonuc = input2 / new
    print(sonuc)
    def siralama():
        if sonuc < 18.5:
            print("weak")
        elif sonuc >= 18.5 and sonuc < 24.9 :
            print("ideal weight")
        elif sonuc >=24.9 and sonuc < 29.9:
            print("overweight")
        else:
            print("obesity")
    siralama()
    

# question one
label = tkinter.Label(text="Please enter your length(cm)")
label.config(bg="black",fg="white")
label.pack()

# entry one

entry = tkinter.Entry()
entry.pack()

# questione two

label2 = tkinter.Label(text="Please enter your weight(kg)")
label2.config(bg="blue",fg="white")
label2.pack()

# entry two
entry2 = tkinter.Entry()
entry2.pack()

# button 

button = tkinter.Button(text="Click",command=funaction_button)
button.pack()

#finish

window.mainloop()