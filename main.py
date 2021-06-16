from StatHolder import StatMods
from MarketFetch import MarketFetch
import tkinter as tk
from tkinter import *


def marketBtnCallBack():
    MarketFetch()

stats = StatMods(1236, 3944, 2494, 380, 5605, 180)
print(stats.chd, stats.chr, stats.dhr, stats.detmod, stats.wd, stats.atk, stats.tnc)

print(stats.damage(400))



window = tk.Tk()
frame = tk.Frame(window, width=200, height=200)
frame.pack()
button = tk.Button(master=frame, text="Market Data", command=marketBtnCallBack)
button.pack()
window.mainloop()

