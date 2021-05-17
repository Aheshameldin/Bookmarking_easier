from tkinter import *
import pandas as pd
import webbrowser
import random # random typos


root = Tk()
root.title("Bookmark Search")
root.geometry("400x125")

greeting= Label(root, text="Hi, I am here to help you find Internal Links easily and more efficiently \n How can I help you today?" )
greeting.pack()

search=[]
unknown=[]
known=[]

e = Entry(root, width=50)
e.pack(padx=50)
mySubmit = Label(root)

def link_url():
    df = pd.read_excel('Links.xlsx')
    request=e.get()
    requested =request.lower()
    print(requested)
    for i in df.index:
        if requested in df['Name'][i]:
            print(df['Name'][i])
            link_url = df['Link'][i]
            known.append(requested)
            return link_url
    else:
        unknown.append(requested)
        unknown_request = "I will search and return back to you"
        return unknown_request


def myClick(event=None):
    global mySubmit
    global reply
    mySubmit["text"] = results()
    request=e.get()
    requested =request.lower()
    if e.get() != "":
        search.append(requested)
    # print(search)
    e.delete(0,"end")
    mySubmit.pack()
    print("unknown:", unknown)
    print("known:", known)
    print("search:",search)


def results():
    global result
    if len(e.get()) == 0:
        result = "Please Insert inquiry"
        return result
    elif link_url:
        # print("Success")
        result = link_url()
        return result


def open_url(event=None):
    if mySubmit["text"] != "I will search and return back to you":
        webbrowser.open_new(mySubmit["text"])


root.bind('<Return>', myClick)
mySubmit.bind("<Button-1>", open_url)
myButton= Button(root, text="Submit", command=myClick)
myButton.pack()






root.mainloop()


