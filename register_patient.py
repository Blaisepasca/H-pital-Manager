from tkinter import *
from database import insert_patient

def open_register_window():
    win = Toplevel()
    win.title("Enregistrer un patient")
    win.geometry("300x300")

    Label(win, text="Nom").pack()
    name = Entry(win)
    name.pack()

    Label(win, text="Âge").pack()
    age = Entry(win)
    age.pack()

    Label(win, text="Sexe").pack()
    gender = Entry(win)
    gender.pack()

    Label(win, text="Maladie").pack()
    disease = Entry(win)
    disease.pack()

    Label(win, text="Contact").pack()
    contact = Entry(win)
    contact.pack()

    def save_patient():
        insert_patient(name.get(), int(age.get()), gender.get(), disease.get(), contact.get())
        Label(win, text="Patient enregistré ✅").pack()

    Button(win, text="Enregistrer", command=save_patient).pack(pady=10)
