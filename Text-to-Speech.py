from tkinter import *
import PyPDF2
import pyttsx3


# window and labels
root = Tk()
root.geometry("300x300")
root.config(bg='white')
root.title("Text To Speech")
Label(root, text='Text To Speech', font='arial 20 bold', bg='white smoke').pack()
Label(root, text='Enter your Text', font='arial 15 bold',
      bg='white smoke').place(x=20, y=60)

# PDF file path
msg = StringVar()


#Entry Field
entry_field = Entry(root, textvariable=msg, width='50')
entry_field.place(x=20, y=100)


# text to speech function

def Text_to_speech():
    text = entry_field.get()
    speak = pyttsx3.init()
    speak.save_to_file(text, 'speech.mp3')
    speak.say(text)
    speak.runAndWait()


# Exit app

def Exit():
    root.destroy()


#  Buttons for each function
Button(root, text="PLAY", font='arial 15 bold',
       command=Text_to_speech, width=4).place(x=25, y=140)
Button(root, text='EXIT', font='arial 15 bold',
       command=Exit).place(x=100, y=140)

# Infinite loop to run program
root.mainloop()
