# import tkinter
# from tkinter import*
# from tkinter import ttk
#
# window = Tk()
# window.title("Data Entry")
# # Adding widget
# frame = Frame(window)
# frame.pack()
#
# user_info = LabelFrame(frame,text="User Information")
# user_info.grid(row=0,column=0)
#
#
# firstname = Label(user_info,text="Firstname")
# firstname.grid(row=0, column=0)
#
# firstname_entry = Entry(user_info)
# firstname_entry.grid(row= 1, column=0)
#
# lastname = Label(user_info,text= "Lastname")
# lastname.grid(row=0, column=1)
#
# lastname_entry = Entry(user_info)
# lastname_entry.grid(row=1,column=1)
#
# title = Label(user_info, text="Title")
# title_combobox = ttk.Combobox(user_info,value=["Mr","Mrs","Miss","Engr","Dr","Prof"])
# title.grid(row=0, column=2)
# title_combobox.grid(row=1, column=2)
#
# age_label = Label(user_info,text="Year")
# age_spinbox = Spinbox(user_info,from_=1998, to=2024)
# age_label.grid(row=2, column=0)
# age_spinbox.grid(row=3, column=0)
#
# nationality_label = Label(user_info, text = "Nationality")
# nationality_combobox = ttk.Combobox(user_info, value=["Nigerian", "Ghanian","Canadian","Turkish","German"])
# nationality_label.grid(row=2, column=1)
# nationality_combobox.grid(row=3, column=1)
#
# # Adding second frame
# course_frame = LabelFrame(frame, text="courses Information")
# course_frame.grid(row=1, column=0, sticky="news")
#
# reg_label = Label(course_frame, text = "Registration")
# reg_label.grid(row=0, column=0)
#
# register = StringVar(value="Not Registered")
# reg_check = Checkbutton(course_frame,text="Currently Registered",variable=register,onvalue="Registered",
#                         offvalue="Not Registered")
# reg_check.grid(row=1, column=0)
#
# numcourses_label = Label(course_frame,text="No, Completed")
# numcourses_spinbox = Spinbox(course_frame, from_=0,to="Infinity")
# numcourses_label.grid(row=0, column=1)
# numcourses_spinbox.grid(row=1, column=1)
#
# numsemester_label= Label(course_frame,text="# Semester")
# numsemester_spinbox = Spinbox(course_frame,from_=0, to="Infinity")
# numsemester_label.grid(row=0, column=2)
# numsemester_spinbox.grid(row=1, column=2)
#
# # terms
# terms_frame = LabelFrame(frame,text="Terms and Conditions")
# terms_frame.grid(row=2,column=0, sticky="news",padx=10,pady=5)
# terms_label = Label(frame,text="Registration")
# terms_label.grid(row=0, column=0)
#
# accept_var = tkinter.StringVar(value="Not Accepted")
# terms_check = tkinter.Checkbutton(terms_frame,text="I agree with terms and conditions")

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
window = Tk()
window.title("Data Entry")
# Adding widget
frame = Frame(window)
frame.pack()

def enter_data():
    accept = accept_var.get()
    if accept == "Accepted":
        fn = firstname_entry.get()
        ln = lastname_entry.get()


        if fn and ln:
            title= title_combobox.get()
            year= age_spinbox.get()
            nationality= nationality_combobox.get()


            print(fn+' '+ ln+ ''+ title+ ''+ year)

        else:
            messagebox.showwarning(title="Required",message="Firstname and Lastname are required")

    else:
        messagebox.showwarning(title="Error", message="Accept the Terms and Conditions")


user_info = LabelFrame(frame,text="User information")
user_info.grid(row=0, column=0)

firstname = Label(user_info, text="Firstname")
firstname.grid(row=0, column=0)
#
firstname_entry = Entry(user_info)
firstname_entry.grid(row = 1, column=0)
#
lastname = Label(user_info, text="Lastname")
lastname.grid(row=0, column=1)
#
lastname_entry = Entry(user_info)
lastname_entry.grid(row = 1, column=1)
#
title = Label(user_info, text="Title")
title_combobox = ttk.Combobox(user_info,value=["Mr", "Mrs", "Miss"])
title.grid(row =0, column=2)
title_combobox.grid(row= 1, column = 2)

#
age_label = Label(user_info, text = "year")
age_spinbox = Spinbox(user_info, from_=1998, to= 2023)
age_label.grid(row = 2, column=0)
age_spinbox.grid(row = 3, column= 0)
#
#
nationality_label = Label(user_info, text = "Nationality")
nationality_combobox = ttk.Combobox(user_info,
                                    value=["","Nigerian", "Ghanain", "Canadian"])
nationality_label.grid(row =2, column=1)
nationality_combobox.grid(row= 3, column = 1)
#
#
# # adding the second frame
course_frame = LabelFrame(frame,text="courses information")
course_frame.grid(row=1, column=0, sticky="news")
reg_label = Label(course_frame, text="Registration")
reg_label.grid(row = 0, column=0)
#
register = StringVar(value ="Not Registered")
reg_check = Checkbutton(course_frame,
                           text="Currently Registered",
                           variable = register,
                           onvalue="Registered",
                           offvalue="Not Registered")
reg_check.grid(row=1, column = 0)
#
numcourses_label = Label(course_frame,
                            text = "No. Completed courses")
numcourses_spinbox = Spinbox(course_frame, from_=0, to= "infinity")
numcourses_label.grid(row = 0, column=1)
numcourses_spinbox.grid(row = 1, column= 1)
#
#
numsemester_label = Label(course_frame,
                             text = "# Semester")
numsemester_spinbox = Spinbox(course_frame, from_=0, to= "infinity")
numsemester_label.grid(row = 0, column=2)
numsemester_spinbox.grid(row = 1, column= 2)
#

# # terms
terms_frame = LabelFrame(frame, text="Terms and condition")
terms_frame.grid(row =2, column =0,
                 sticky="news", padx=10, pady=5)

accept_var = StringVar(value="Not Accepted")
terms_check = Checkbutton(terms_frame,
                             text="I agree with the Terms and condition",
                          variable = accept_var,
                             onvalue="Accepted",
                             offvalue="Not Accepted")
terms_check.grid(row=0, column = 0)

button = Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news",
            padx=10, pady=5)

# applying padding
for widget in user_info.winfo_children():
    widget.grid_configure(padx = 10, pady= 5)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx = 10, pady= 5)

window.mainloop()