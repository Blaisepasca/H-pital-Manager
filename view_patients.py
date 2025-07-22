from tkinter import *
from database import get_all_patients

def open_view_window():
    win = Toplevel()
    win.title("Liste des patients")
    win.geometry("500x400")

    