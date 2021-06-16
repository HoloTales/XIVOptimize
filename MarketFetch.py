import requests
import json
import tkinter as tk
from tkinter import *

class MarketFetch:


    def __init__(self):
        window = tk.Tk()
        frame = tk.Frame(window, width=200, height=200)
        frame.pack(fill = tk.X)
        label1 = tk.Label(frame, text="Info on item:")
        label1.pack(side=tk.LEFT)
        self.entry1 = tk.Entry(frame)
        self.entry1.pack(side=tk.RIGHT, expand = True)
        framebot = tk.Frame(window, height=200)
        framebot.pack(fill=tk.X)
        button = tk.Button(master=framebot, text="Market Data", command=self.getInfo)
        button.pack(side=tk.BOTTOM)
        window.mainloop()

        r = requests.get('https://universalis.app/api/marketable/')
        #print(r.status_code)
        #print(r.headers)
        #print(r.text)
        j = json.loads(r.text)
        print(j)

        self.getInfo("33779")

        #p = r.text
        #p = p.replace("[", "").replace("]", "")
        #arr = p.split(",")
        #print(arr)
        #numarr = []
        #for numstr in arr:
        #    numarr.append(int(numstr))
        #print(numarr)

    def getInfo(self):
        str = self.entry1.get()
        q = requests.get('https://xivapi.com/item/'+str)
        j2 = json.loads(q.text)
        print(j2["Name_en"])