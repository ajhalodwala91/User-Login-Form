from tkinter import *
from customtkinter import *
from PIL import Image
import pyttsx3

assist = pyttsx3.init()
def speak(audio):
    assist.say(audio)
    assist.runAndWait()

data = {'aliasgar': 'password1', 'insiyah': 'password2'}
button_mode = False
button_mode2 = False

def login_cmd():
    user_input = user_entry.get().lower()
    pass_input = pass_entry.get().lower()

    for user_data, pass_data in data.items():
        if user_data == user_input and pass_data == pass_input:
            access = True
            break
        else:
            access = False
        
    if access:
        speak('Login Successful')
        window.destroy()
    else:
        speak("Login Failed")

def register_cmd():
    user_input = str((user_entry2.get()).lower())
    pass_input = str((pass_entry.get()).lower())
    pass_input2 = str((pass2_entry.get()).lower())

    for user_data in data:
        if user_data == user_input:
            speak('User already exists')
            return

    if pass_input != pass_input2:
        speak('Passwords doesn\'t match')
        return
    
    if len(user_input)>1 and len(pass_input)>1:
        data[user_input] = pass_input
        speak('Account created successfully')
        window.destroy()
    else:
        speak('Please enter a username and password')

def new_user_cmd():
    main_frame.destroy()
    main_icon_lbl.destroy()
    login_btn.destroy()
    
    main_frame2 = CTkFrame(master = window)
    main_frame2.configure(fg_color = '#002453', height = 350, width = 500, corner_radius = 50)
    main_frame2.place(relx = 0.5, rely = 0.55, anchor = CENTER)

    sub_frame2 = CTkFrame(master = main_frame2)
    sub_frame2.configure(fg_color = '#002453', height = 170, width = 350)
    sub_frame2.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    user_frame2 = CTkFrame(master = sub_frame2)
    user_frame2.configure(fg_color = '#002453')
    user_frame2.pack(pady = 10)

    pass_frame2 = CTkFrame(master = sub_frame2)
    pass_frame2.configure(fg_color = '#002453')
    pass_frame2.pack(pady = 10)

    pass2_frame = CTkFrame(master = sub_frame2)
    pass2_frame.configure(fg_color = '#002453')
    pass2_frame.pack(pady = 10)
    
    try:
        main_icon2 = CTkImage(Image.open('main_icon.png'), size = (160, 190))
        main_icon_lbl2 = CTkLabel(master = window, text = '', image = main_icon2, width = 160, height = 190)
        main_icon_lbl2.place(relx = 0.5, rely = 0.18, anchor = CENTER)
    except Exception as e:
        print(f"No main icon found: {e}")

    global user_entry2
    user_lbl2 = CTkLabel(master = user_frame2, image = user_icon, text = '')
    user_lbl2.pack(side = LEFT)
    user_entry2 = CTkEntry(master = user_frame2, text_color = 'white', font = ('Arial', 18), placeholder_text = 'Enter Username', placeholder_text_color = '#9d9d9d', height = 50, width = 250, fg_color = '#324f77', corner_radius = 0, border_width = 0)
    user_entry2.pack(side=LEFT)

    global pass_entry
    global show_pass_btn
    pass_lbl2 = CTkLabel(master = pass_frame2, image = pass_icon, text = '')
    pass_lbl2.pack(side = LEFT)
    pass_entry = CTkEntry(master = pass_frame2, text_color = 'white', font = ('Arial', 16), placeholder_text = 'Enter Password', placeholder_text_color = '#9d9d9d', show = '*', height = 50, width = 250, fg_color = '#324f77', corner_radius = 0, border_width = 0, )
    pass_entry.pack(side=LEFT)
    show_pass_btn = CTkButton(master = pass_frame2, text = '', image = close_eye, fg_color = '#324f77', width = 50, border_width = 0, corner_radius = 0, hover_color = NONE, command = show_pass)
    show_pass_btn.place(relx = 1, rely = 0.5, anchor = E)

    global pass2_entry
    global show_pass_btn2
    pass2_lbl = CTkLabel(master = pass2_frame, image = pass_icon, text = '')
    pass2_lbl.pack(side = LEFT)
    pass2_entry = CTkEntry(master = pass2_frame, text_color = 'white', font = ('Arial', 16), placeholder_text = 'Re-enter Password', placeholder_text_color = '#9d9d9d', show = '*', height = 50, width = 250, fg_color = '#324f77', corner_radius = 0, border_width = 0, )
    pass2_entry.pack(side=LEFT)
    show_pass_btn2 = CTkButton(master = pass2_frame, text = '', image = close_eye, fg_color = '#324f77', width = 50, border_width = 0, corner_radius = 0, hover_color = NONE, command = show_pass2)
    show_pass_btn2.place(relx = 1, rely = 0.5, anchor = E)

    register_btn = CTkButton(master = window, text = 'Register', fg_color = '#002453', height = 55, corner_radius = 20, font = ('Arial', 20), command = register_cmd)
    register_btn.place(relx = 0.5, rely = 0.9, anchor = CENTER)

def show_pass():
    global button_mode
    if button_mode:
        show_pass_btn.configure(image = close_eye)
        pass_entry.configure(show = '*')
        button_mode = False
    else:
        show_pass_btn.configure(image = open_eye)
        pass_entry.configure(show = '')
        button_mode = True

def show_pass2():
    global button_mode2
    if button_mode2:
        show_pass_btn2.configure(image = close_eye)
        pass2_entry.configure(show = '*')
        button_mode2 = False
    else:
        show_pass_btn2.configure(image = open_eye)
        pass2_entry.configure(show = '')
        button_mode2 = True

window = CTk()
window.geometry('800x600')
window.title('Login Form')
window.configure(fg_color = 'lightblue')
window.resizable(False, False)

main_frame = CTkFrame(master = window)
main_frame.configure(fg_color = '#002453', height = 325, width = 500, corner_radius = 50)
main_frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)

sub_frame = CTkFrame(master = main_frame)
sub_frame.configure(fg_color = '#002453', height = 170, width = 350)
sub_frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

user_frame = CTkFrame(master = sub_frame)
user_frame.configure(fg_color = '#002453')
user_frame.pack(pady = 10)

pass_frame = CTkFrame(master = sub_frame)
pass_frame.configure(fg_color = '#002453')
pass_frame.pack(pady = 10)

try:
    main_icon = CTkImage(Image.open('main_icon.png'), size = (160, 190))
    main_icon_lbl = CTkLabel(master = window, text = '', image = main_icon, width = 160, height = 190)
    main_icon_lbl.place(relx = 0.5, rely = 0.22, anchor = CENTER)
except Exception as e:
    print(f"No image found to display: {e}")

user_icon = CTkImage(Image.open('login_icon.png'), size=(50, 50))
pass_icon = CTkImage(Image.open('pass_icon.png'), size=(50, 50))

open_eye = CTkImage(Image.open('openeye_icon.png'), size=(35, 35))
close_eye = CTkImage(Image.open('closedeye_icon.png'), size=(35, 35))

user_lbl = CTkLabel(master = user_frame, image = user_icon, text = '')
user_lbl.pack(side = LEFT)
user_entry = CTkEntry(master = user_frame, text_color = 'white', font = ('Arial', 18), placeholder_text = 'Enter Username', placeholder_text_color = '#9d9d9d', height = 50, width = 250, fg_color = '#324f77', corner_radius = 0, border_width = 0)
user_entry.pack(side=LEFT)

pass_lbl = CTkLabel(master = pass_frame, image = pass_icon, text = '')
pass_lbl.pack(side = LEFT)
pass_entry = CTkEntry(master = pass_frame, text_color = 'white', font = ('Arial', 16), placeholder_text = 'Enter Password', placeholder_text_color = '#9d9d9d', show = '*', height = 50, width = 250, fg_color = '#324f77', corner_radius = 0, border_width = 0, )
pass_entry.pack(side=LEFT)
show_pass_btn = CTkButton(master = pass_frame, text = '', image = close_eye, fg_color = '#324f77', width = 50, border_width = 0, corner_radius = 0, hover_color = NONE, command = show_pass)
show_pass_btn.place(relx = 1, rely = 0.5, anchor = E)

new_acc_lbl = CTkLabel(master = main_frame, text = 'Don\'t have an account?', font = ('Arial', 10), text_color = '#cdc8c8')
new_acc_lbl.place(rely = 0.8, relx = 0.45, anchor = CENTER)
new_acc_btn = CTkButton(master = main_frame, text='Register', font = ('Arial', 10), text_color = '#469dc6', width = 100, anchor = W, fg_color = '#002453', hover_color = NONE, command = new_user_cmd)
new_acc_btn.place(rely = 0.8, relx = 0.65, anchor = CENTER)

login_btn = CTkButton(master = window, text = 'Login', fg_color = '#002453', height = 55, corner_radius = 20, font = ('Arial', 20), command = login_cmd)
login_btn.place(relx = 0.5, rely = 0.9, anchor = CENTER)

window.mainloop()