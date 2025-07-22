from tkinter import *
from database import get_all_patients

def open_view_window():
    win = Toplevel()
    win.title("Liste des patients")
    win.geometry("500x400")

    rows = get_all_patients()
    for row in rows:
        Label(win, text=f"ID: {row[0]}, Nom: {row[1]}, Âge: {row[2]}, Sexe: {row[3]}, Maladie: {row[4]}, Contact: {row[5]}").pack()
