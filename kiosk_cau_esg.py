import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3

class Which_Professor_Esg(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"which_prof_esg.png")   #사회기반시스템공학부 2
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


        prof_btn1_img=tk.PhotoImage(file=f"which_prof_esg_kmc.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button6 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("esg_kmc"))

        prof_btn1_img=tk.PhotoImage(file=f"which_prof_esg_kmg.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button7 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("esg_kmg"))  


        prof_btn1_img=tk.PhotoImage(file=f"which_prof_esg_ysh.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button8 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("esg_ysh"))  

        prof_btn1_img=tk.PhotoImage(file=f"which_prof_esg_kwh.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button9 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("esg_kwh"))  

        prof_btn1_img=tk.PhotoImage(file=f"which_prof_esg_kdu.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button10 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("esg_kdu"))
        
        prof_btn1_img=tk.PhotoImage(file=f"which_prof_esg_ogy.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button12 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("esg_ogy"))        

        prof_btn1_img=tk.PhotoImage(file=f"which_prof_esg_kdw.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button13 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("esg_kdw"))  


        prof_btn1_img=tk.PhotoImage(file=f"which_prof_esg_mjh.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button14 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("esg_mjh"))        
                        
        
        button6.place(x = 82, y = 276)
        button7.place(x = 226, y = 272)
        button8.place(x = 373, y = 276)
        button9.place(x = 520, y = 270)
        button10.place(x = 663, y = 276)
        button12.place(x = 225, y = 392)
        button13.place(x = 370, y = 396)
        button14.place(x = 517, y = 388)


class esg_kmc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"esg_kmc_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_Esg"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)


class esg_kmg(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"esg_kmg_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_Esg"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class esg_ysh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"esg_ysh_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_Esg"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class esg_kwh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"esg_kwh_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_Esg"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

"""
class esg_kdu(tk.Frame):

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
                            command=lambda: controller.show_frame("Which_Professor_Esg"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class esg_kdw(tk.Frame):

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
                            command=lambda: controller.show_frame("Which_Professor_Esg"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)
"""

class esg_ogy(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"esg_ogy_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_Esg"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class esg_mjh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"esg_mjh_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_Esg"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)