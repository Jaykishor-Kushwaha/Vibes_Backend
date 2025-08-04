import tkinter as tk
from tkinter import messagebox

students=[]

student_id_count=1

def cal_grade(p):
    if p>=(90):
        return "A+"
    elif p>=(80):
        return "A"
    elif p>=(70):
        return "B"
    elif p>=(60):
        return "C"
    elif p>=(50):
        return "D"
    else:
        return "Fail"
    
def add_students():
    global student_id_count
    name=entry_name.get()
    try:
        marks1=entry_m1.get()
        marks2=entry_m2.get()
        marks3=entry_m3.get()
    
    except ValueError:
        messagebox.showerror("invaild Input","Please Enter Interger")
        return 
    
    total=marks1+marks2+marks3
    per=total/3
    grade=cal_grade(per)

    student={
        "id":student_id_count,
        "name":name,
        "marks":[marks1,marks2,marks3],
        "per":round(per,2),
        "grade":grade

    }
    students.append(student)
    student_id_count+=1
    messagebox.showinfo("success",f"Student `{name}` added ")
    clear_inputs()


def clear_inputs():
    entry_name.delete(0,tk.END)
    entry_m1.delete(0,tk.END)
    entry_m2.delete(0,tk.END)
    entry_m3.delete(0,tk.END)




root=tk.Tk()
root.title("Student Grade System")
root.geometry("300x450")


tk.Label(root,text="Student Name").pack()
entry_name=tk.Entry(root)
entry_name.pack()






    