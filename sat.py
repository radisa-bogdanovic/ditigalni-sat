

import tkinter as sat
import time

def azuriraj_sat():
    trenutno_vreme= time.strftime("%H:%M:%S")
    satt.config(text=trenutno_vreme)
    satt.after(1000, azuriraj_sat)

app=sat.Tk()
app.title("Digitalni sat")

satt= sat.Label(app, text="", font=("Helvetica"), height=6, width=16 )
satt.pack()


azuriraj_sat()
app.mainloop()


