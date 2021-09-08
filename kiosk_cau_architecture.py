import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3


class Which_Professor_Archi_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"which_prof_archi_1.png")   #사회기반시스템공학부 2
        background_main_img = background_main_img.zoom(10)
        background_main_img = background_main_img.subsample(17)
        background_main = tk.Label(self, image=background_main_img)
        background_main.image = background_main_img
        background_main.place(x = 0, y = 0)
       
        goto_back_img=tk.PhotoImage(file=f"goto_back.png")
        goto_back_img = goto_back_img.zoom(10)
        goto_back_img = goto_back_img.subsample(17)
        goto_back = tk.Label(self, image=goto_back_img)
        goto_back.image = goto_back_img
        button00 = tk.Button(self, image = goto_back_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Major_Engineering")) #####
        
        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)


        tab_btn_img=tk.PhotoImage(file=f"which_prof_archi_1_tab.png")
        tab_btn_img = tab_btn_img.zoom(10)
        tab_btn_img = tab_btn_img.subsample(17)
        tab_btn = tk.Label(self, image=tab_btn_img)
        tab_btn.image = tab_btn_img
        tab_button1 = tk.Button(self, image = tab_btn_img, bg = "medium blue", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
        #tab_button1 = tk.Button(self, image = tab_btn_img, bg = "blue2", overrelief="flat", relief="flat",
                           command=lambda: controller.show_frame("Which_Professor_Archi_2")) 


        prof_btn1_img=tk.PhotoImage(file=f"which_prof_archi_1_cyk.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button1 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("cyk"))
        
        tab_button1.place(x = 155, y = 88)
        button1.place(x = 82, y = 162)

class Which_Professor_Archi_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"which_prof_archi_2.png")   #사회기반시스템공학부 2
        background_main_img = background_main_img.zoom(10)
        background_main_img = background_main_img.subsample(17)
        background_main = tk.Label(self, image=background_main_img)
        background_main.image = background_main_img
        background_main.place(x = 0, y = 0)
       
        goto_back_img=tk.PhotoImage(file=f"goto_back.png")
        goto_back_img = goto_back_img.zoom(10)
        goto_back_img = goto_back_img.subsample(17)
        goto_back = tk.Label(self, image=goto_back_img)
        goto_back.image = goto_back_img
        button00 = tk.Button(self, image = goto_back_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Major_Engineering")) #####
        
        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)


        tab_btn_img=tk.PhotoImage(file=f"which_prof_archi_2_tab.png")
        tab_btn_img = tab_btn_img.zoom(10)
        tab_btn_img = tab_btn_img.subsample(17)
        tab_btn = tk.Label(self, image=tab_btn_img)
        tab_btn.image = tab_btn_img
        tab_button1 = tk.Button(self, image = tab_btn_img, bg = "medium blue", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
        #tab_button1 = tk.Button(self, image = tab_btn_img, bg = "blue2", overrelief="flat", relief="flat",
                           command=lambda: controller.show_frame("Which_Professor_Archi_1")) 


        prof_btn1_img=tk.PhotoImage(file=f"which_prof_archi_2_lcd.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button1 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("lcd")) 


        tab_button1.place(x = 60, y = 90)
        button1.place(x = 77, y = 236)


class cyk(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"mechanical_prof_kdg.png")
        background_main_img = background_main_img.zoom(10)
        background_main_img = background_main_img.subsample(17)
        background_main = tk.Label(self, image=background_main_img)
        background_main.image = background_main_img
        background_main.place(x = 0, y = 0)
       
        goto_back_img=tk.PhotoImage(file=f"goto_back.png")
        goto_back_img = goto_back_img.zoom(10)
        goto_back_img = goto_back_img.subsample(17)
        goto_back = tk.Label(self, image=goto_back_img)
        goto_back.image = goto_back_img
        button00 = tk.Button(self, image = goto_back_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Professor_Archi_1"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)


class lcd(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"mechanical_prof_kdg.png")
        background_main_img = background_main_img.zoom(10)
        background_main_img = background_main_img.subsample(17)
        background_main = tk.Label(self, image=background_main_img)
        background_main.image = background_main_img
        background_main.place(x = 0, y = 0)
       
        goto_back_img=tk.PhotoImage(file=f"goto_back.png")
        goto_back_img = goto_back_img.zoom(10)
        goto_back_img = goto_back_img.subsample(17)
        goto_back = tk.Label(self, image=goto_back_img)
        goto_back.image = goto_back_img
        button00 = tk.Button(self, image = goto_back_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Professor_Archi_2"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)
