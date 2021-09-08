import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

from kiosk_cau_sgt import *
from kiosk_cau_architecture import *
from kiosk_cau_chemical import *
from kiosk_cau_esg import *
from kiosk_cau_eng import *
from kiosk_cau_eee import *
#from kiosk_cau_mix import *



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Page_Select_Menu, Department, 
                    Which_Major_Engineering, Which_Major_Ict, Which_Major_Soft,
                    Which_Professor_Mechanical_1, Which_Professor_Mechanical_2,  
                    mechanical_kdg,
                    
                    lys,
                    Which_Professor_Sgt_1, Which_Professor_Sgt_2,
                    kkj,kjh,pkh,
                    Which_Professor_Archi_1, Which_Professor_Archi_2,
                    cyk,lcd,
                    Which_Professor_Chemical,
                    kcg,ksj,nih,yth,
                    Which_Professor_Esg,
                    #esg_kdu,esg_kdw,
                    esg_kmc, esg_kmg, esg_ysh, esg_kwh, esg_ogy, esg_mjh,

                    Which_Professor_EEE_1, Which_Professor_EEE_2, Which_Professor_EEE_3,
                    eee_space,
                    
                    eee_kh, eee_kjh, eee_kss, eee_khi, eee_kjp, eee_kjs, #eee_kci, eee_khs, 
                    eee_rjs, #eee_muc,
                    eee_psk, eee_psh, eee_phh, eee_pgh, #eee_pdh, 
                    eee_pcw, #eee_ssh, 
                    eee_soy, eee_sgb, eee_sds, eee_sy, #eee_ysy, eee_ysj,
                    eee_lmh, eee_space, eee_ljr, eee_ljw, eee_lhl, eee_lhg, eee_lsj, 
                    eee_jjg, eee_jtg, eee_jys, #eee_cgc, 
                    eee_cdh, eee_cyw, eee_cwj, eee_hch,

                    Which_Professor_Mix_1, Which_Professor_Mix_2,
                    mix_psk, 
                    Which_Professor_Sw_1, Which_Professor_Sw_2,
                    Which_Professor_Ai_1, Which_Professor_Ai_2,
                    Facilities, 
                    Which_Cafe, CafeDream303, CafeDream310, Appendix, Bluepot102, Bluepot301, Coffeeand, Tous_Les,
                    Which_Cafeteria, Cafeteria310, Cauburger, Cafeteria_Dorm, Cafeteria_Law,
                    Which_Library, Lawschool_Library, Central_Library, 
                    Smoking_Area, Enter, Page_Portal):

            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #background_main_img=tk.PhotoImage(file="C:/Users/breezze/Desktop/python_prac/title2.png")
        background_main_img=tk.PhotoImage(file=f"title2.png")
        background_main_img = background_main_img.zoom(10)
        background_main_img = background_main_img.subsample(17)

        background_main = tk.Label(self, image=background_main_img)
        background_main.image = background_main_img
        background_main.place(x = 0, y = 0)

        start_button_img=tk.PhotoImage(file=f"title_button.png")
        start_button_img = start_button_img.zoom(10)
        start_button_img = start_button_img.subsample(17)
        
        start_button = tk.Label(self, image=start_button_img)
        start_button.image = start_button_img

        button1 = tk.Button(self, image = start_button_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Page_Select_Menu"))
        button1.place(x = 215, y = 180)


class Page_Select_Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"start_menu.png")
        background_main_img = background_main_img.zoom(10)
        background_main_img = background_main_img.subsample(17)
        background_main = tk.Label(self, image=background_main_img)
        background_main.image = background_main_img
        background_main.place(x = 0, y = 0)
        #
        
        start_menu_prof_img=tk.PhotoImage(file=f"start_menu_prof.png")
        start_menu_prof_img = start_menu_prof_img.zoom(10)
        start_menu_prof_img = start_menu_prof_img.subsample(17)
        start_menu_prof = tk.Label(self, image=start_menu_prof_img)
        start_menu_prof.image = start_menu_prof_img
        button1 = tk.Button(self, image = start_menu_prof_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Department")) 

        start_menu_enter_img=tk.PhotoImage(file=f"start_menu_enter.png")
        start_menu_enter_img = start_menu_enter_img.zoom(10)
        start_menu_enter_img = start_menu_enter_img.subsample(17)
        start_menu_enter = tk.Label(self, image=start_menu_enter_img)
        start_menu_enter.image = start_menu_enter_img
        button2 = tk.Button(self, image = start_menu_enter_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Enter"))

        start_menu_conv_img=tk.PhotoImage(file=f"start_menu_conv.png")
        start_menu_conv_img = start_menu_conv_img.zoom(10)
        start_menu_conv_img = start_menu_conv_img.subsample(17)
        start_menu_conv = tk.Label(self, image=start_menu_conv_img)
        start_menu_conv.image = start_menu_conv_img
        button3 = tk.Button(self, image = start_menu_conv_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Facilities")) #####

        button1.place(x = 110, y = 185)
        button2.place(x = 335, y = 180)
        button3.place(x = 564, y = 168)
        


class Department(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"department.png")
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
                            command=lambda: controller.show_frame("Page_Select_Menu")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)
       
       
        dept_engineering_btn_img=tk.PhotoImage(file=f"dept_engineering_btn2.png")
        dept_engineering_btn_img = dept_engineering_btn_img.zoom(10)
        dept_engineering_btn_img = dept_engineering_btn_img.subsample(17)
        dept_engineering_btn = tk.Label(self, image=dept_engineering_btn_img)
        dept_engineering_btn.image = dept_engineering_btn_img
        button1 = tk.Button(self, image = dept_engineering_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Major_Engineering")) 

        dept_ict_engineering_btn_img=tk.PhotoImage(file=f"dept_ict_engineering_btn2.png")
        dept_ict_engineering_btn_img = dept_ict_engineering_btn_img.zoom(10)
        dept_ict_engineering_btn_img = dept_ict_engineering_btn_img.subsample(17)
        dept_ict_engineering_btn = tk.Label(self, image=dept_ict_engineering_btn_img)
        dept_ict_engineering_btn.image = dept_ict_engineering_btn_img
        button2 = tk.Button(self, image = dept_ict_engineering_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Major_Ict"))

        dept_soft_img_btn=tk.PhotoImage(file=f"dept_soft_btn2.png")
        dept_soft_img_btn = dept_soft_img_btn.zoom(10)
        dept_soft_img_btn = dept_soft_img_btn.subsample(17)
        dept_soft_btn = tk.Label(self, image=dept_soft_img_btn)
        dept_soft_btn.image = dept_soft_img_btn
        button3 = tk.Button(self, image = dept_soft_img_btn, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Major_Soft")) #####

        button1.place(x = 116, y = 280)
        button2.place(x = 346, y = 285)
        button3.place(x = 585, y = 290)



class Which_Major_Engineering(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"dept_engineering.png")
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
                            command=lambda: controller.show_frame("Department")) #####
        
        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)


        sgt_btn_img=tk.PhotoImage(file=f"sgt_btn.png")
        sgt_btn_img = sgt_btn_img.zoom(10)
        sgt_btn_img = sgt_btn_img.subsample(17)
        sgt_btn = tk.Label(self, image=sgt_btn_img)
        sgt_btn.image = sgt_btn_img
        button1 = tk.Button(self, image = sgt_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_Sgt_1")) 

        architect_btn_img=tk.PhotoImage(file=f"architect_btn.png")
        architect_btn_img = architect_btn_img.zoom(10)
        architect_btn_img = architect_btn_img.subsample(17)
        architect_btn = tk.Label(self, image=architect_btn_img)
        architect_btn.image = architect_btn_img
        button2 = tk.Button(self, image = architect_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Professor_Archi_1"))

        chemical_btn_img=tk.PhotoImage(file=f"chemical_btn.png")
        chemical_btn_img = chemical_btn_img.zoom(10)
        chemical_btn_img = chemical_btn_img.subsample(17)
        chemical_btn = tk.Label(self, image=chemical_btn_img)
        chemical_btn.image = chemical_btn_img
        button3 = tk.Button(self, image = chemical_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Professor_Chemical"))

        esg_btn_img=tk.PhotoImage(file=f"esg_btn.png")
        esg_btn_img = esg_btn_img.zoom(10)
        esg_btn_img = esg_btn_img.subsample(17)
        esg_btn = tk.Label(self, image=esg_btn_img)
        esg_btn.image = esg_btn_img
        button4 = tk.Button(self, image = esg_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Professor_Esg"))

        mechanical_btn_img=tk.PhotoImage(file=f"mechanical_btn.png")
        mechanical_btn_img = mechanical_btn_img.zoom(10)
        mechanical_btn_img = mechanical_btn_img.subsample(17)
        mechanical_btn = tk.Label(self, image=mechanical_btn_img)
        mechanical_btn.image = mechanical_btn_img
        button5 = tk.Button(self, image = mechanical_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Professor_Mechanical_1"))    

        button1.place(x = 130, y = 265)
        button2.place(x = 343, y = 255)
        button3.place(x = 550, y = 258)
        button4.place(x = 145, y = 386)
        button5.place(x = 345, y = 376)


class Which_Major_Ict(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"dept_ict.png")
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
                            command=lambda: controller.show_frame("Department")) #####
        
        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)


        eee_btn_img=tk.PhotoImage(file=f"eee_btn.png")
        eee_btn_img = eee_btn_img.zoom(10)
        eee_btn_img = eee_btn_img.subsample(17)
        eee_btn = tk.Label(self, image=eee_btn_img)
        eee_btn.image = eee_btn_img
        button1 = tk.Button(self, image = eee_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_EEE_1")) 

        mix_btn_img=tk.PhotoImage(file=f"mix_btn.png")
        mix_btn_img = mix_btn_img.zoom(10)
        mix_btn_img = mix_btn_img.subsample(17)
        mix_btn = tk.Label(self, image=mix_btn_img)
        mix_btn.image = mix_btn_img
        button2 = tk.Button(self, image = mix_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Professor_Mix_1"))


        button1.place(x = 205, y = 280)
        button2.place(x = 485, y = 285)

class Which_Major_Soft(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"dept_soft.png")
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
                            command=lambda: controller.show_frame("Department")) #####
        
        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)


        eee_btn_img=tk.PhotoImage(file=f"soft_btn.png")
        eee_btn_img = eee_btn_img.zoom(10)
        eee_btn_img = eee_btn_img.subsample(17)
        eee_btn = tk.Label(self, image=eee_btn_img)
        eee_btn.image = eee_btn_img
        button1 = tk.Button(self, image = eee_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_Sw_1")) 

        mix_btn_img=tk.PhotoImage(file=f"ai_btn.png")
        mix_btn_img = mix_btn_img.zoom(10)
        mix_btn_img = mix_btn_img.subsample(17)
        mix_btn = tk.Label(self, image=mix_btn_img)
        mix_btn.image = mix_btn_img
        button2 = tk.Button(self, image = mix_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Professor_Ai_1"))


        button1.place(x = 200, y = 280)
        button2.place(x = 485, y = 285)


class Which_Professor_Sw_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"which_prof_soft_1.png")
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
                            command=lambda: controller.show_frame("Which_Major_Soft")) #####
        
        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)


        tab_btn_img=tk.PhotoImage(file=f"which_prof_soft_1_tab.png")
        tab_btn_img = tab_btn_img.zoom(10)
        tab_btn_img = tab_btn_img.subsample(17)
        tab_btn = tk.Label(self, image=tab_btn_img)
        tab_btn.image = tab_btn_img
        tab_button1 = tk.Button(self, image = tab_btn_img, bg = "medium blue", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_Sw_2")) 

        """
        prof_btn1_img=tk.PhotoImage(file=f"which_prof_eng_1_kdg.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button1 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("mechanical_kdg")) 
        """

        tab_button1.place(x = 153, y = 89)
        #button1.place(x = 65, y = 173)

class Which_Professor_Sw_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"which_prof_soft_2.png")
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
                            command=lambda: controller.show_frame("Which_Major_Soft")) #####
        
        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)


        tab_btn_img=tk.PhotoImage(file=f"which_prof_soft_2_tab.png")
        tab_btn_img = tab_btn_img.zoom(10)
        tab_btn_img = tab_btn_img.subsample(17)
        tab_btn = tk.Label(self, image=tab_btn_img)
        tab_btn.image = tab_btn_img
        tab_button1 = tk.Button(self, image = tab_btn_img, bg = "medium blue", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_Sw_1")) 

        """
        prof_btn1_img=tk.PhotoImage(file=f"which_prof_eng_1_kdg.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button1 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("mechanical_kdg")) 
        """

        tab_button1.place(x = 67, y = 89)
        #button1.place(x = 65, y = 173)


class Which_Professor_Ai_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"which_prof_ai_1.png")
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
                            command=lambda: controller.show_frame("Which_Major_Soft")) #####
        
        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)


        tab_btn_img=tk.PhotoImage(file=f"which_prof_ai_1_tab.png")
        tab_btn_img = tab_btn_img.zoom(10)
        tab_btn_img = tab_btn_img.subsample(17)
        tab_btn = tk.Label(self, image=tab_btn_img)
        tab_btn.image = tab_btn_img
        tab_button1 = tk.Button(self, image = tab_btn_img, bg = "medium blue", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_Ai_2")) 

        """
        prof_btn1_img=tk.PhotoImage(file=f"which_prof_eng_1_kdg.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button1 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("mechanical_kdg")) 
        """

        tab_button1.place(x = 153, y = 88)
        #button1.place(x = 65, y = 173)

class Which_Professor_Ai_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"which_prof_ai_2.png")
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
                            command=lambda: controller.show_frame("Which_Major_Soft")) #####
        
        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)


        tab_btn_img=tk.PhotoImage(file=f"which_prof_ai_2_tab.png")
        tab_btn_img = tab_btn_img.zoom(10)
        tab_btn_img = tab_btn_img.subsample(17)
        tab_btn = tk.Label(self, image=tab_btn_img)
        tab_btn.image = tab_btn_img
        tab_button1 = tk.Button(self, image = tab_btn_img, bg = "medium blue", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_Ai_1")) 

        """
        prof_btn1_img=tk.PhotoImage(file=f"which_prof_eng_1_kdg.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button1 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("mechanical_kdg")) 
        """

        tab_button1.place(x = 73, y = 88)
        #button1.place(x = 65, y = 173)




        

class Which_Professor_Mix_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"which_prof_mix_1.png")
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
                            command=lambda: controller.show_frame("Which_Major_Ict")) #####
        
        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)


        tab_btn_img=tk.PhotoImage(file=f"which_prof_mix_1_tab.png")
        tab_btn_img = tab_btn_img.zoom(10)
        tab_btn_img = tab_btn_img.subsample(17)
        tab_btn = tk.Label(self, image=tab_btn_img)
        tab_btn.image = tab_btn_img
        tab_button = tk.Button(self, image = tab_btn_img, bg = "medium blue", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_Mix_2")) 


      
        prof_btn1_img=tk.PhotoImage(file=f"which_prof_mix_1_psk.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button1 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("mix_psk")) 
       

        tab_button.place(x = 210, y = 90)

        button1.place(x = 82, y = 175)
        
        
class Which_Professor_Mix_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"which_prof_mix_2.png")
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
                            command=lambda: controller.show_frame("Which_Major_Ict")) #####
        
        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)


        tab_btn_img=tk.PhotoImage(file=f"which_prof_mix_2_tab.png")
        tab_btn_img = tab_btn_img.zoom(10)
        tab_btn_img = tab_btn_img.subsample(17)
        tab_btn = tk.Label(self, image=tab_btn_img)
        tab_btn.image = tab_btn_img
        tab_button = tk.Button(self, image = tab_btn_img, bg = "medium blue", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_Mix_1")) 


      
        prof_btn1_img=tk.PhotoImage(file=f"which_prof_mix_2_ldh.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button1 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("mechanical_ldh")) 
        


        tab_button.place(x = 82, y = 90)
       
        button1.place(x = 80, y = 177)





#mix

class mix_psk(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"mix_psk_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_Mix_1"))
        button00.place(x = 22, y = 526)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 22, y = 477)





# Mechanical


class mechanical_kdg(tk.Frame):

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
                            command=lambda: controller.show_frame("Which_Professor_Mechanical_1"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)


class mechanical_ldh(tk.Frame):

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
                            command=lambda: controller.show_frame("Which_Professor_Mechanical_2"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)






class Facilities(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"conv_select.png")
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
                            command=lambda: controller.show_frame("Page_Select_Menu")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)
       
       
        dept_engineering_btn_img=tk.PhotoImage(file=f"conv_select_library.png")
        dept_engineering_btn_img = dept_engineering_btn_img.zoom(10)
        dept_engineering_btn_img = dept_engineering_btn_img.subsample(17)
        dept_engineering_btn = tk.Label(self, image=dept_engineering_btn_img)
        dept_engineering_btn.image = dept_engineering_btn_img
        button1 = tk.Button(self, image = dept_engineering_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Library")) 

        dept_ict_engineering_btn_img=tk.PhotoImage(file=f"conv_select_cafeteria.png")
        dept_ict_engineering_btn_img = dept_ict_engineering_btn_img.zoom(10)
        dept_ict_engineering_btn_img = dept_ict_engineering_btn_img.subsample(17)
        dept_ict_engineering_btn = tk.Label(self, image=dept_ict_engineering_btn_img)
        dept_ict_engineering_btn.image = dept_ict_engineering_btn_img
        button2 = tk.Button(self, image = dept_ict_engineering_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Cafeteria"))

        dept_soft_img_btn=tk.PhotoImage(file=f"conv_select_cafe.png")
        dept_soft_img_btn = dept_soft_img_btn.zoom(10)
        dept_soft_img_btn = dept_soft_img_btn.subsample(17)
        dept_soft_btn = tk.Label(self, image=dept_soft_img_btn)
        dept_soft_btn.image = dept_soft_img_btn
        button3 = tk.Button(self, image = dept_soft_img_btn, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Cafe")) #####

        conv_select_smoke_img=tk.PhotoImage(file=f"conv_select_smoke.png")
        conv_select_smoke_img = conv_select_smoke_img.zoom(10)
        conv_select_smoke_img = conv_select_smoke_img.subsample(17)
        conv_select_smoke = tk.Label(self, image=conv_select_smoke_img)
        conv_select_smoke.image = conv_select_smoke_img
        button4 = tk.Button(self, image = conv_select_smoke_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Smoking_Area"))

        button1.place(x = 102, y = 263)
        button2.place(x = 278, y = 263)
        button3.place(x = 447, y = 260)
        button4.place(x = 624, y = 266)
        

class Which_Cafe(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"which_cafe.png")
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
                            command=lambda: controller.show_frame("Facilities")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)
       
       
        dept_engineering_btn_img=tk.PhotoImage(file=f"which_cafe_bluepot102.png")
        dept_engineering_btn_img = dept_engineering_btn_img.zoom(10)
        dept_engineering_btn_img = dept_engineering_btn_img.subsample(17)
        dept_engineering_btn = tk.Label(self, image=dept_engineering_btn_img)
        dept_engineering_btn.image = dept_engineering_btn_img
        button1 = tk.Button(self, image = dept_engineering_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Bluepot102")) 

        dept_ict_engineering_btn_img=tk.PhotoImage(file=f"which_cafe_dream310.png")
        dept_ict_engineering_btn_img = dept_ict_engineering_btn_img.zoom(10)
        dept_ict_engineering_btn_img = dept_ict_engineering_btn_img.subsample(17)
        dept_ict_engineering_btn = tk.Label(self, image=dept_ict_engineering_btn_img)
        dept_ict_engineering_btn.image = dept_ict_engineering_btn_img
        button2 = tk.Button(self, image = dept_ict_engineering_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("CafeDream310"))

        dept_soft_img_btn=tk.PhotoImage(file=f"which_cafe_coffeeand.png")
        dept_soft_img_btn = dept_soft_img_btn.zoom(10)
        dept_soft_img_btn = dept_soft_img_btn.subsample(17)
        dept_soft_btn = tk.Label(self, image=dept_soft_img_btn)
        dept_soft_btn.image = dept_soft_img_btn
        button3 = tk.Button(self, image = dept_soft_img_btn, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Coffeeand")) #####

        conv_select_smoke_img=tk.PhotoImage(file=f"which_cafe_appendix.png")
        conv_select_smoke_img = conv_select_smoke_img.zoom(10)
        conv_select_smoke_img = conv_select_smoke_img.subsample(17)
        conv_select_smoke = tk.Label(self, image=conv_select_smoke_img)
        conv_select_smoke.image = conv_select_smoke_img
        button4 = tk.Button(self, image = conv_select_smoke_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Appendix"))
        
        which_cafe_bluepot301_img=tk.PhotoImage(file=f"which_cafe_bluepot301.png")
        which_cafe_bluepot301_img = which_cafe_bluepot301_img.zoom(10)
        which_cafe_bluepot301_img = which_cafe_bluepot301_img.subsample(17)
        which_cafe_bluepot301 = tk.Label(self, image=which_cafe_bluepot301_img)
        which_cafe_bluepot301.image = which_cafe_bluepot301_img
        button5 = tk.Button(self, image = which_cafe_bluepot301_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Bluepot301"))

        which_cafe_dream303_img=tk.PhotoImage(file=f"which_cafe_dream303.png")
        which_cafe_dream303_img = which_cafe_dream303_img.zoom(10)
        which_cafe_dream303_img = which_cafe_dream303_img.subsample(17)
        which_cafe_dream303 = tk.Label(self, image=which_cafe_dream303_img)
        which_cafe_dream303.image = which_cafe_dream303_img
        button6 = tk.Button(self, image = which_cafe_dream303_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("CafeDream303"))

        which_cafe_tous_img=tk.PhotoImage(file=f"which_cafe_tous.png")
        which_cafe_tous_img = which_cafe_tous_img.zoom(10)
        which_cafe_tous_img = which_cafe_tous_img.subsample(17)
        which_cafe_tous = tk.Label(self, image=which_cafe_tous_img)
        which_cafe_tous.image = which_cafe_tous_img
        button7 = tk.Button(self, image = which_cafe_tous_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Tous_Les"))

        button1.place(x = 70, y = 247)
        button2.place(x = 270, y = 255)
        button3.place(x = 452, y = 247)
        button4.place(x = 648, y = 248)
        button5.place(x = 72, y = 391)
        button6.place(x = 266, y = 388)
        button7.place(x = 648, y = 389)
        

class CafeDream310(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"bluepot102_qr.png")
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
                            command=lambda: controller.show_frame("Which_Cafe")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 23, y = 477)
       
       



class CafeDream303(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"bluepot102_qr.png")
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
                            command=lambda: controller.show_frame("Which_Cafe")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 23, y = 477)
       
       
        

class Appendix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"bluepot102_qr.png")
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
                            command=lambda: controller.show_frame("Which_Cafe")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 23, y = 477)
       
       


class Bluepot102(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"bluepot102_qr.png")
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
                            command=lambda: controller.show_frame("Which_Cafe")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 23, y = 477)
       
        

class Bluepot301(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"bluepot102_qr.png")
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
                            command=lambda: controller.show_frame("Which_Cafe")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 23, y = 477)


class Coffeeand(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"bluepot102_qr.png")
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
                            command=lambda: controller.show_frame("Which_Cafe")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 23, y = 477)


class Tous_Les(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"bluepot102_qr.png")
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
                            command=lambda: controller.show_frame("Which_Cafe")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 23, y = 477)

        

class Which_Cafeteria(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        background_main_img=tk.PhotoImage(file=f"which_cafeteria.png")
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
                            command=lambda: controller.show_frame("Facilities")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)
       
       
        dept_engineering_btn_img=tk.PhotoImage(file=f"which_cafeteria_310.png")
        dept_engineering_btn_img = dept_engineering_btn_img.zoom(10)
        dept_engineering_btn_img = dept_engineering_btn_img.subsample(17)
        dept_engineering_btn = tk.Label(self, image=dept_engineering_btn_img)
        dept_engineering_btn.image = dept_engineering_btn_img
        button1 = tk.Button(self, image = dept_engineering_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Cafeteria310")) 

        dept_ict_engineering_btn_img=tk.PhotoImage(file=f"which_cafeteria_cau.png")
        dept_ict_engineering_btn_img = dept_ict_engineering_btn_img.zoom(10)
        dept_ict_engineering_btn_img = dept_ict_engineering_btn_img.subsample(17)
        dept_ict_engineering_btn = tk.Label(self, image=dept_ict_engineering_btn_img)
        dept_ict_engineering_btn.image = dept_ict_engineering_btn_img
        button2 = tk.Button(self, image = dept_ict_engineering_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Cauburger"))

        dept_soft_img_btn=tk.PhotoImage(file=f"which_cafeteria_dorm.png")
        dept_soft_img_btn = dept_soft_img_btn.zoom(10)
        dept_soft_img_btn = dept_soft_img_btn.subsample(17)
        dept_soft_btn = tk.Label(self, image=dept_soft_img_btn)
        dept_soft_btn.image = dept_soft_img_btn
        button3 = tk.Button(self, image = dept_soft_img_btn, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Cafeteria_Dorm")) #####

        conv_select_smoke_img=tk.PhotoImage(file=f"which_cafeteria_law.png")
        conv_select_smoke_img = conv_select_smoke_img.zoom(10)
        conv_select_smoke_img = conv_select_smoke_img.subsample(17)
        conv_select_smoke = tk.Label(self, image=conv_select_smoke_img)
        conv_select_smoke.image = conv_select_smoke_img
        button4 = tk.Button(self, image = conv_select_smoke_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Cafeteria_Law"))

        button1.place(x = 110, y = 265)
        button2.place(x = 285, y = 269)
        button3.place(x = 448, y = 263)
        button4.place(x = 611, y = 269)


class Cafeteria310(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"310cafeteria_qr.png")
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
                            command=lambda: controller.show_frame("Which_Cafeteria")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 23, y = 477)
       

        

class Cauburger(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"cauburger_qr.png")
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
                            command=lambda: controller.show_frame("Which_Cafeteria")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 23, y = 477)
       
       

class Cafeteria_Dorm(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"dorm_cafeteria_qr.png")
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
                            command=lambda: controller.show_frame("Which_Cafeteria")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 23, y = 477)
       
class Cafeteria_Law(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"dorm_cafeteria_qr.png")
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
                            command=lambda: controller.show_frame("Which_Cafeteria")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 23, y = 477)
       


class Which_Library(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"which_library.png")
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
                            command=lambda: controller.show_frame("Facilities")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)
       
       
        dept_engineering_btn_img=tk.PhotoImage(file=f"which_library_central.png")
        dept_engineering_btn_img = dept_engineering_btn_img.zoom(10)
        dept_engineering_btn_img = dept_engineering_btn_img.subsample(17)
        dept_engineering_btn = tk.Label(self, image=dept_engineering_btn_img)
        dept_engineering_btn.image = dept_engineering_btn_img
        button1 = tk.Button(self, image = dept_engineering_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Central_Library")) 

        dept_ict_engineering_btn_img=tk.PhotoImage(file=f"which_library_law.png")
        dept_ict_engineering_btn_img = dept_ict_engineering_btn_img.zoom(10)
        dept_ict_engineering_btn_img = dept_ict_engineering_btn_img.subsample(17)
        dept_ict_engineering_btn = tk.Label(self, image=dept_ict_engineering_btn_img)
        dept_ict_engineering_btn.image = dept_ict_engineering_btn_img
        button2 = tk.Button(self, image = dept_ict_engineering_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Lawschool_Library")) #####


        button1.place(x = 205, y = 276)
        button2.place(x = 494, y = 276)
        

class Lawschool_Library(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"lawschool_library_qr.png")
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
                            command=lambda: controller.show_frame("Which_Library")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 23, y = 477)
       
       
        dept_engineering_btn_img=tk.PhotoImage(file=f"")
        dept_engineering_btn_img = dept_engineering_btn_img.zoom(10)
        dept_engineering_btn_img = dept_engineering_btn_img.subsample(17)
        dept_engineering_btn = tk.Label(self, image=dept_engineering_btn_img)
        dept_engineering_btn.image = dept_engineering_btn_img
        button1 = tk.Button(self, image = dept_engineering_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Major_Engineering")) 

        dept_ict_engineering_btn_img=tk.PhotoImage(file=f"")
        dept_ict_engineering_btn_img = dept_ict_engineering_btn_img.zoom(10)
        dept_ict_engineering_btn_img = dept_ict_engineering_btn_img.subsample(17)
        dept_ict_engineering_btn = tk.Label(self, image=dept_ict_engineering_btn_img)
        dept_ict_engineering_btn.image = dept_ict_engineering_btn_img
        button2 = tk.Button(self, image = dept_ict_engineering_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Major_Ict")) #####


        button1.place(x = 205, y = 276)
        button2.place(x = 494, y = 276)
        

class Central_Library(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"centeral_library_qr.png")
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
                            command=lambda: controller.show_frame("Which_Library")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 23, y = 477)
       
        




class Smoking_Area(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        background_main_img=tk.PhotoImage(file=f"smoking_qr.png")
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
                            command=lambda: controller.show_frame("Facilities")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 129, y = 529)
       
       






class Enter(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"enter_qr.png")
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
                            command=lambda: controller.show_frame("Page_Select_Menu")) #####

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) #####
        button00.place(x = 22, y = 526)
        button01.place(x = 23, y = 477)
       
       
        dept_engineering_btn_img=tk.PhotoImage(file=f"")
        dept_engineering_btn_img = dept_engineering_btn_img.zoom(10)
        dept_engineering_btn_img = dept_engineering_btn_img.subsample(17)
        dept_engineering_btn = tk.Label(self, image=dept_engineering_btn_img)
        dept_engineering_btn.image = dept_engineering_btn_img
        button1 = tk.Button(self, image = dept_engineering_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Major_Engineering")) 

        dept_ict_engineering_btn_img=tk.PhotoImage(file=f"")
        dept_ict_engineering_btn_img = dept_ict_engineering_btn_img.zoom(10)
        dept_ict_engineering_btn_img = dept_ict_engineering_btn_img.subsample(17)
        dept_ict_engineering_btn = tk.Label(self, image=dept_ict_engineering_btn_img)
        dept_ict_engineering_btn.image = dept_ict_engineering_btn_img
        button2 = tk.Button(self, image = dept_ict_engineering_btn_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("Which_Major_Ict")) #####


        button1.place(x = 205, y = 276)
        button2.place(x = 494, y = 276)
        


class Page_Portal(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        


if __name__== "__main__":
    app = SampleApp()
    app.title("[전전긍긍] 중앙대학교 교내 시설안내 키오스크")
    app.geometry("900x600")
    #app.attributes("-transparentcolor")
    app.mainloop()