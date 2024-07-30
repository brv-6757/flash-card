from tkinter import *
from data import *
import random
import time

class FlashcardWindow():
    def __init__(self):
        self.curr_word = ""
        self.curr_lang = "French"
        self.window = Tk()
        self.window.config(padx=30,pady=30,bg=BACKGROUND_COLOR)
        self.card_front = PhotoImage(file = images_loc + "card_front.png")
        self.card_back = PhotoImage(file = images_loc + "card_back.png")
        self.unknown = list_of_words
        random.shuffle(self.unknown)
        self.idx = 0
        self.known = []
    
    def count_down(self,count):
        #print(count)
        if(count==0):
            self.canvas.itemconfig(self.card,image = self.card_back)
            self.curr_lang = "English"
            self.canvas.itemconfig(self.lang,text=self.curr_lang)
            self.canvas.itemconfig(self.word,text=self.curr_word[self.curr_lang])
            return
        self.window.after(1000,self.count_down,count-1)
    
    def right(self):
        self.known.append(self.curr_word)
        self.curr_lang = "French"
        self.start()
        
    def wrong(self):
        self.curr_lang = "French"
        self.start()
    
    def start(self):
        self.canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
        self.card = self.canvas.create_image(400,263,image=self.card_front)
        self.lang = self.canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
        self.word = self.canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
        self.canvas.grid(row=0,column=0,columnspan=2)
        tick_photo = PhotoImage(file = images_loc + "right.png")
        self.tick = Button(image=tick_photo,bg=BACKGROUND_COLOR,highlightthickness=0,command=self.right)
        self.tick.grid(row=1,column=0)
        cross_photo = PhotoImage(file = images_loc + "wrong.png")
        self.cross = Button(image=cross_photo,bg=BACKGROUND_COLOR,highlightthickness=0,command=self.wrong)
        self.cross.grid(row=1,column=1)
        self.curr_word = self.unknown[self.idx]
        self.idx+=1
        self.canvas.itemconfig(self.word,text=self.curr_word[self.curr_lang])
        self.canvas.itemconfig(self.lang,text=self.curr_lang)
        self.count_down(3)
        
        self.window.mainloop()
        
        
        
