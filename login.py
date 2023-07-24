import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
import random
scale_factor = 1
window = tk.Tk()
window.title("Login form")
window.geometry('900x500')
window.configure(bg='#C8C8C8')
image = Image.open("ig2.png")
photo = ImageTk.PhotoImage(image)
new_width = image.width * scale_factor
new_height = image.height * scale_factor
image = image.resize((new_width, new_height), Image.ANTIALIAS)

# إنشاء عنصر العرض لعرض الصورة المكبرة
photo = ImageTk.PhotoImage(image)
label = tk.Label(window, image=photo)
label.pack()


def command():
     print








def change_text_color():
    color = "#032b57"  # قم بتغيير القيمة إلى لون النص المطلوب

    text_entry.configure(foreground=color)



def text():
     

       text = tk.Tk()
       text_entry = tk.Text(text, height=220, width=50)  # إنشاء عنصر Text
       text_entry.configure(bg='#032b57')
       text_entry.configure(font=("Arial", 25))  # تحديد حجم الخط

       text_entry.pack()
       text_entry.bind("<KeyRelease>", nice)  # ربط حدث "KeyRelease" بوظيفة "highlight_words"
       color_button = tk.Button(text, text="red", command=change_text_color)
       color_button.pack()
       text.configure(bg='#032b57')
       text.geometry('900x500')
     

def login():
    username = "slenr"
    password = "12345"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        
        root = tk.Tk()
        root.geometry('900x500')
        root.configure(bg='#262626')
        root.title('Welcome To App')
        test = tk.Label(root, text="مرحبا بك  هنا جميع الادوات", font='Tahoma 30 bold')
        test.pack()
        button = tk.Button(root, text="tool spammer",font=("Arial", 16), command=text, width=10)
        button.pack(side=tk.LEFT, padx=10, pady=10)  # ضبط الموقع والهوامش
        button1 = tk.Button(root, text="tool reports",font=("Arial", 16), command=text, width=10) 
        button1.pack(side=tk.LEFT, padx=10, pady=10)
       
    
        

        
        root.mainloop()
    

    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tk.Frame(bg='#333333')

# Creating widgets
login_label = tk.Label(
    frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tk.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
password_label = tk.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tk.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()















window.mainloop()
