from tkinter import *
import PyPDF2
import pyttsx3



# window and labels
root = Tk()
root.geometry("300x300")
root.config(bg='white')
root.title("PDF To Speech")
Label(root, text='PDF To Speech', font='arial 20 bold', bg='white smoke').pack()
Label(root, text='Enter PDF File Path', font='arial 15 bold',
      bg='white smoke').place(x=20, y=60)

# PDF file path
path = StringVar()


#Entry Field
entry_field = Entry(root, textvariable=path, width='50')
entry_field.place(x=20, y=100)


# extract text from pdf function
def extract_text(file_path):
    pdf_File = open(file_path, 'rb')

    #Create PDF Reader Object
    pdf_Reader = PyPDF2.PdfFileReader(pdf_File)

    # number of pages in pdf
    pages = pdf_Reader.numPages

    # list to contain pdf file text
    textList = []

    #Extracting text data from each page
    for i in range(pages):
        try:
            page = pdf_Reader.getPage(i)
            textList.append(page.extractText())
        except:
            print("No text found")

    #Converting multiline text to single line text
    textString = " ".join(textList)
    return textString

# text to speech function
def Text_to_speech():
    file_path = entry_field.get()
    text = extract_text(file_path)
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
