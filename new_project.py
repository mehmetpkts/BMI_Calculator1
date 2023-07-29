import tkinter

# window
window = tkinter.Tk()
window.title("BMI PROJECT")
window.minsize(width=300,height=300)

# funaction

def funaction_button():
    input1 = entry.get()
    input2 = entry2.get()
    try:
        if input1 == "" or input2 == "":
            label3.config(text="Please enter both weight and height")
        else:
            new = float(input1)**2 / 10000
            sonuc = float(input2) / new
    except:
        label3.config(text="Please enter number")

    if float(input1) < 0 or float(input2) < 0:
        label3.config(text="please enter positive value")


    def arrangement():
        if sonuc < 18.5:
            label3.config(text=f"your BMI is : {round(sonuc,2)} = weak")
        elif sonuc >= 18.5 and sonuc < 24.9 :
            label3.config(text=f"your BMI is : {round(sonuc,2)} = ideal weight")
        elif sonuc >=24.9 and sonuc < 29.9:
            label3.config(text=f"your BMI is : {round(sonuc,2)} = overweight")
        else:
            label3.config(text=f"your BMI is : {round(sonuc,2)} = obesitys")
    arrangement()



# question one
label = tkinter.Label(text="Please enter your height(cm)")
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

# write

label3 = tkinter.Label(text="")
label3.pack()


#finish

window.mainloop()