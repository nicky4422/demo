import tkinter as tk
from tkinter import ttk
def submit_from():
#retrive values from the form
first_name=entry_first_name.get()
last_name=entry_last_name.get()
email=entry-email.get()
contact_number=entry_contact_number.get()
passeord=entry_password.get()
gender=gender_var.get()
#display the submitted information in blue color
result_lable.config(text=f"registrationfrom successfully created!\n"
f"First Name:{first_name}\n"
f"Last Name:{last_name}\n"
f"Email:{email}\n"
f"Contact Number:{contact_number}\n"
f"Password:{password}\n"
f"Gender:{gender}",foreground="blue")
root=tk.Tk()
root.tittle("Flood-Registration Form")
root.geometry("400*400")
root.configure(bg="lightgreen")
label_first_name=ttk.Label(root,text="first Name:",Foreground="purple")
label_last_name=ttk.Label(root,text="last Name:",Foreground="purple")
label_email=ttk.Label(root,text="Email:",forground="purple")
label_contact_number=ttk.Label(root,text="Contact Number:",foreground="purole")
lable_password=ttk.Lable(root,text="Password:",foreground="purple")
lable_gender=ttk.Lable(root,text="Gender:",foreground="purple")
#create entry eidgets
entry_first_name=ttk.Entry(root)
entery_last_name=ttk.Entry(root)
entry_email=ttk.Entry(root)
entry_contact_number=ttk.Entry(root)
entry_password=ttk.Entry(root,show"*")
#create acombobox for gender
gender_var=tk.stringVar()
gender_combobox=tkk.cobobox(root,textvariable=gender_var,values=["Male","Femal"],state="readonly")
gender_combobox.set("Male")#Default value
#create submit button
submit_button=tt.kButton(root,text="submit",command=submit_form,style="TButton")
#create lable for displaying the result
result_lable=ttk.Lable(root,text="",foreground="blue")
lable_first_name.grid(row=0,column=0,padx=10,pady=5,sticky="w")
lable_last_name.grid(row=1,column=0,padx=10,pady=5,sticky="w")
lable_email.grid(row=3,column=0,padx=10,pady=5,sticky="w")
lable_contact_number.grid(row=3,column=0,padx=10,pady=5,sticky="w")
lable_password.grid(row=4,column=0,padx=10,pady=5,sticky="w")
lable_password.grid(row=4,column=0,padx=10,pady=5,sticky="w")
gender_combobox.grid(row=5,column=0,padx=10,pady=5,sticky="w")
submit_button.grid(row=6,column=0,columnspan=2,pady=10)
result_lable.grid(row=7,column=0,columnspan=2,pady=10)
#configure style for the submit button
style=ttk.style()
style.configure("Tbutton",foreground="red")
#Run the Tkinter main loop
root.mainloop()

