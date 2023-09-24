from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=200,height=200)

label_weight = Label(window, text="Enter Your Weight (kg):")
entry_weight = Entry(window,width=15)


label_height = Label(window, text="Enter Your Height (cm):")
entry_height = Entry(window,width=15)

result_label = Label(window, text="")
calculate_button = Button(window, text="Calculate")

label_weight.pack()
entry_weight.pack()

label_height.pack()
entry_height.pack()

calculate_button.pack()
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            result_label.config(text=f"{bmi} 'You Are Underweight.'")
        elif 18.5 <= bmi < 24.9:
            result_label.config(text=f"{bmi} 'You Are In Good Shape!' ")
        elif 24.9 <= bmi < 29.9:
            result_label.config(text=f"{bmi} 'You Are Overweight' ")
        else:
            result_label.config(text=":)")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        result_label.config(text="Invalid input Please enter valid numbers.")
calculate_button.config(command=calculate_bmi)

result_label.pack()
window.mainloop()
