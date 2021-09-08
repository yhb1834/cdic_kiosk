import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3


class Which_Professor_EEE_1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"which_prof_eee_1.png")
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


        tab_btn_img=tk.PhotoImage(file=f"which_prof_eee_1_tab1.png")
        tab_btn_img = tab_btn_img.zoom(10)
        tab_btn_img = tab_btn_img.subsample(17)
        tab_btn = tk.Label(self, image=tab_btn_img)
        tab_btn.image = tab_btn_img
        tab_button1 = tk.Button(self, image = tab_btn_img, bg = "medium blue", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_EEE_2")) 

        tab2_btn_img=tk.PhotoImage(file=f"which_prof_eee_1_tab2.png")
        tab2_btn_img = tab2_btn_img.zoom(10)
        tab2_btn_img = tab2_btn_img.subsample(17)
        tab2_btn = tk.Label(self, image=tab2_btn_img)
        tab2_btn.image = tab2_btn_img
        tab_button2 = tk.Button(self, image = tab2_btn_img, bg = "medium blue", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_EEE_3")) 


        prof_btn1_img=tk.PhotoImage(file=f"which_prof_eee_1_kh.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button1 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_kh")) 

        prof_btn2_img=tk.PhotoImage(file=f"which_prof_eee_1_kjh.png")
        prof_btn2_img = prof_btn2_img.zoom(10)
        prof_btn2_img = prof_btn2_img.subsample(17)
        prof_btn2 = tk.Label(self, image=prof_btn2_img)
        prof_btn2.image = prof_btn2_img
        button2 = tk.Button(self, image = prof_btn2_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_kjh")) 

        prof_btn3_img=tk.PhotoImage(file=f"which_prof_eee_1_kss.png")
        prof_btn3_img = prof_btn3_img.zoom(10)
        prof_btn3_img = prof_btn3_img.subsample(17)
        prof_btn3 = tk.Label(self, image=prof_btn3_img)
        prof_btn3.image = prof_btn3_img
        button3 = tk.Button(self, image = prof_btn3_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_kss")) 

        prof_btn4_img=tk.PhotoImage(file=f"which_prof_eee_1_khi.png")
        prof_btn4_img = prof_btn4_img.zoom(10)
        prof_btn4_img = prof_btn4_img.subsample(17)
        prof_btn4 = tk.Label(self, image=prof_btn4_img)
        prof_btn4.image = prof_btn4_img
        button4 = tk.Button(self, image = prof_btn4_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_khi")) 

        prof_btn5_img=tk.PhotoImage(file=f"which_prof_eee_1_kjp.png")
        prof_btn5_img = prof_btn5_img.zoom(10)
        prof_btn5_img = prof_btn5_img.subsample(17)
        prof_btn5 = tk.Label(self, image=prof_btn5_img)
        prof_btn5.image = prof_btn5_img
        button5 = tk.Button(self, image = prof_btn5_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_kjp")) 

        prof_btn6_img=tk.PhotoImage(file=f"which_prof_eee_1_kjs.png")
        prof_btn6_img = prof_btn6_img.zoom(10)
        prof_btn6_img = prof_btn6_img.subsample(17)
        prof_btn6 = tk.Label(self, image=prof_btn6_img)
        prof_btn6.image = prof_btn6_img
        button6 = tk.Button(self, image = prof_btn6_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_kjs")) 


        prof_btn7_img=tk.PhotoImage(file=f"which_prof_eee_1_kci.png")
        prof_btn7_img = prof_btn7_img.zoom(10)
        prof_btn7_img = prof_btn7_img.subsample(17)
        prof_btn7 = tk.Label(self, image=prof_btn7_img)
        prof_btn7.image = prof_btn7_img
        button7 = tk.Button(self, image = prof_btn7_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_kci")) 



        prof_btn8_img=tk.PhotoImage(file=f"which_prof_eee_1_khs.png")
        prof_btn8_img = prof_btn8_img.zoom(10)
        prof_btn8_img = prof_btn8_img.subsample(17)
        prof_btn8 = tk.Label(self, image=prof_btn8_img)
        prof_btn8.image = prof_btn8_img
        button8 = tk.Button(self, image = prof_btn8_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_khs")) 

        
        prof_btn9_img=tk.PhotoImage(file=f"which_prof_eee_1_rjs.png")
        prof_btn9_img = prof_btn9_img.zoom(10)
        prof_btn9_img = prof_btn9_img.subsample(17)
        prof_btn9 = tk.Label(self, image=prof_btn9_img)
        prof_btn9.image = prof_btn9_img
        button9 = tk.Button(self, image = prof_btn9_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_rjs")) 

        prof_btn10_img=tk.PhotoImage(file=f"which_prof_eee_1_muc.png")
        prof_btn10_img = prof_btn10_img.zoom(10)
        prof_btn10_img = prof_btn10_img.subsample(17)
        prof_btn10 = tk.Label(self, image=prof_btn10_img)
        prof_btn10.image = prof_btn10_img
        button10 = tk.Button(self, image = prof_btn10_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_muc")) 

        prof_btn11_img=tk.PhotoImage(file=f"which_prof_eee_1_psg.png")
        prof_btn11_img = prof_btn11_img.zoom(10)
        prof_btn11_img = prof_btn11_img.subsample(17)
        prof_btn11 = tk.Label(self, image=prof_btn11_img)
        prof_btn11.image = prof_btn11_img
        button11 = tk.Button(self, image = prof_btn11_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_psk")) 

        prof_btn12_img=tk.PhotoImage(file=f"which_prof_eee_1_psh.png")
        prof_btn12_img = prof_btn12_img.zoom(10)
        prof_btn12_img = prof_btn12_img.subsample(17)
        prof_btn12 = tk.Label(self, image=prof_btn12_img)
        prof_btn12.image = prof_btn12_img
        button12 = tk.Button(self, image = prof_btn12_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_psh")) 

        prof_btn13_img=tk.PhotoImage(file=f"which_prof_eee_1_phh.png")
        prof_btn13_img = prof_btn13_img.zoom(10)
        prof_btn13_img = prof_btn13_img.subsample(17)
        prof_btn13 = tk.Label(self, image=prof_btn13_img)
        prof_btn13.image = prof_btn13_img
        button13 = tk.Button(self, image = prof_btn13_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_phh")) 

        prof_btn14_img=tk.PhotoImage(file=f"which_prof_eee_1_bgh.png")
        prof_btn14_img = prof_btn14_img.zoom(10)
        prof_btn14_img = prof_btn14_img.subsample(17)
        prof_btn14 = tk.Label(self, image=prof_btn14_img)
        prof_btn14.image = prof_btn14_img
        button14 = tk.Button(self, image = prof_btn14_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_pgh")) 


        prof_btn15_img=tk.PhotoImage(file=f"which_prof_eee_1_pdh.png")
        prof_btn15_img = prof_btn15_img.zoom(10)
        prof_btn15_img = prof_btn15_img.subsample(17)
        prof_btn15 = tk.Label(self, image=prof_btn15_img)
        prof_btn15.image = prof_btn15_img
        button15 = tk.Button(self, image = prof_btn15_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_pdh")) 

        prof_btn16_img=tk.PhotoImage(file=f"which_prof_eee_1_bcy.png")
        prof_btn16_img = prof_btn16_img.zoom(10)
        prof_btn16_img = prof_btn16_img.subsample(17)
        prof_btn16 = tk.Label(self, image=prof_btn16_img)
        prof_btn16.image = prof_btn16_img
        button16 = tk.Button(self, image = prof_btn16_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_pcw")) 

        tab_button1.place(x = 152, y = 90)
        tab_button2.place(x = 235, y = 90)
        button1.place(x = 60, y = 155)
        button2.place(x = 188, y = 151)
        button3.place(x = 315, y = 152)
        button4.place(x = 435, y = 152)
        button5.place(x = 568, y = 152)
        button6.place(x = 692, y = 152)
        
        button7.place(x = 60, y = 280)
        button8.place(x = 190, y = 280)
        button9.place(x = 315, y = 280)
        button10.place(x = 435, y = 278)
        button11.place(x = 565, y = 278)
        button12.place(x = 691, y = 279)

        button13.place(x = 60, y = 405)
        button14.place(x = 185, y = 405)
        button15.place(x = 315, y = 400)
        button16.place(x = 438, y = 405)
        


class Which_Professor_EEE_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"which_prof_eee_2.png")
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
        button00.place(x = 23, y = 526)
        button01.place(x = 130, y = 529)


        tab_btn_img=tk.PhotoImage(file=f"which_prof_eee_2_tab1.png")
        tab_btn_img = tab_btn_img.zoom(10)
        tab_btn_img = tab_btn_img.subsample(17)
        tab_btn = tk.Label(self, image=tab_btn_img)
        tab_btn.image = tab_btn_img
        tab_button1 = tk.Button(self, image = tab_btn_img, bg = "medium blue", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_EEE_1")) 

        tab2_btn_img=tk.PhotoImage(file=f"which_prof_eee_1_tab2.png")
        tab2_btn_img = tab2_btn_img.zoom(10)
        tab2_btn_img = tab2_btn_img.subsample(17)
        tab2_btn = tk.Label(self, image=tab2_btn_img)
        tab2_btn.image = tab2_btn_img
        tab_button2 = tk.Button(self, image = tab2_btn_img, bg = "medium blue", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_EEE_3")) 

        
        prof_btn1_img=tk.PhotoImage(file=f"which_prof_eee_2_ssh.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button1 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_ssh")) 
        
        prof_btn2_img=tk.PhotoImage(file=f"which_prof_eee_2_soy.png")
        prof_btn2_img = prof_btn2_img.zoom(10)
        prof_btn2_img = prof_btn2_img.subsample(17)
        prof_btn2 = tk.Label(self, image=prof_btn2_img)
        prof_btn2.image = prof_btn2_img
        button2 = tk.Button(self, image = prof_btn2_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_soy")) 

        prof_btn3_img=tk.PhotoImage(file=f"which_prof_eee_2_sgb.png")
        prof_btn3_img = prof_btn3_img.zoom(10)
        prof_btn3_img = prof_btn3_img.subsample(17)
        prof_btn3 = tk.Label(self, image=prof_btn3_img)
        prof_btn3.image = prof_btn3_img
        button3 = tk.Button(self, image = prof_btn3_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_sgb")) 

        prof_btn4_img=tk.PhotoImage(file=f"which_prof_eee_2_sds.png")
        prof_btn4_img = prof_btn4_img.zoom(10)
        prof_btn4_img = prof_btn4_img.subsample(17)
        prof_btn4 = tk.Label(self, image=prof_btn4_img)
        prof_btn4.image = prof_btn4_img
        button4 = tk.Button(self, image = prof_btn4_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_sds")) 

        prof_btn5_img=tk.PhotoImage(file=f"which_prof_eee_2_sy.png")
        prof_btn5_img = prof_btn5_img.zoom(10)
        prof_btn5_img = prof_btn5_img.subsample(17)
        prof_btn5 = tk.Label(self, image=prof_btn5_img)
        prof_btn5.image = prof_btn5_img
        button5 = tk.Button(self, image = prof_btn5_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_sy")) 

        prof_btn6_img=tk.PhotoImage(file=f"which_prof_eee_2_ysy.png")
        prof_btn6_img = prof_btn6_img.zoom(10)
        prof_btn6_img = prof_btn6_img.subsample(17)
        prof_btn6 = tk.Label(self, image=prof_btn6_img)
        prof_btn6.image = prof_btn6_img
        button6 = tk.Button(self, image = prof_btn6_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_ysy")) 


        prof_btn7_img=tk.PhotoImage(file=f"which_prof_eee_2_ysj.png")
        prof_btn7_img = prof_btn7_img.zoom(10)
        prof_btn7_img = prof_btn7_img.subsample(17)
        prof_btn7 = tk.Label(self, image=prof_btn7_img)
        prof_btn7.image = prof_btn7_img
        button7 = tk.Button(self, image = prof_btn7_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_ysj")) 

        prof_btn8_img=tk.PhotoImage(file=f"which_prof_eee_2_lmh.png")
        prof_btn8_img = prof_btn8_img.zoom(10)
        prof_btn8_img = prof_btn8_img.subsample(17)
        prof_btn8 = tk.Label(self, image=prof_btn8_img)
        prof_btn8.image = prof_btn8_img
        button8 = tk.Button(self, image = prof_btn8_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_lmh")) 

        prof_btn9_img=tk.PhotoImage(file=f"which_prof_eee_2_space.png")
        prof_btn9_img = prof_btn9_img.zoom(10)
        prof_btn9_img = prof_btn9_img.subsample(17)
        prof_btn9 = tk.Label(self, image=prof_btn9_img)
        prof_btn9.image = prof_btn9_img
        button9 = tk.Button(self, image = prof_btn9_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_space")) 

        prof_btn10_img=tk.PhotoImage(file=f"which_prof_eee_2_ljr.png")
        prof_btn10_img = prof_btn10_img.zoom(10)
        prof_btn10_img = prof_btn10_img.subsample(17)
        prof_btn10 = tk.Label(self, image=prof_btn10_img)
        prof_btn10.image = prof_btn10_img
        button10 = tk.Button(self, image = prof_btn10_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_ljr")) 

        prof_btn11_img=tk.PhotoImage(file=f"which_prof_eee_2_ljw.png")
        prof_btn11_img = prof_btn11_img.zoom(10)
        prof_btn11_img = prof_btn11_img.subsample(17)
        prof_btn11 = tk.Label(self, image=prof_btn11_img)
        prof_btn11.image = prof_btn11_img
        button11 = tk.Button(self, image = prof_btn11_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_ljw")) 

        prof_btn12_img=tk.PhotoImage(file=f"which_prof_eee_2_lhl.png")
        prof_btn12_img = prof_btn12_img.zoom(10)
        prof_btn12_img = prof_btn12_img.subsample(17)
        prof_btn12 = tk.Label(self, image=prof_btn12_img)
        prof_btn12.image = prof_btn12_img
        button12 = tk.Button(self, image = prof_btn12_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_lhl")) 

        prof_btn13_img=tk.PhotoImage(file=f"which_prof_eee_2_lhg.png")
        prof_btn13_img = prof_btn13_img.zoom(10)
        prof_btn13_img = prof_btn13_img.subsample(17)
        prof_btn13 = tk.Label(self, image=prof_btn13_img)
        prof_btn13.image = prof_btn13_img
        button13 = tk.Button(self, image = prof_btn13_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_lhg")) 

        prof_btn14_img=tk.PhotoImage(file=f"which_prof_eee_2_lsj.png")
        prof_btn14_img = prof_btn14_img.zoom(10)
        prof_btn14_img = prof_btn14_img.subsample(17)
        prof_btn14 = tk.Label(self, image=prof_btn14_img)
        prof_btn14.image = prof_btn14_img
        button14 = tk.Button(self, image = prof_btn14_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_lsj")) 

        tab_button1.place(x = 65, y = 90)
        tab_button2.place(x = 235, y = 90)
        
        button1.place(x = 65, y = 150)
        button2.place(x = 188, y = 151)
        button3.place(x = 315, y = 152)
        button4.place(x = 440, y = 152)
        button5.place(x = 568, y = 155)
        button6.place(x = 693, y = 155)
        button7.place(x = 60, y = 280)
        button8.place(x = 186, y = 280)
        button9.place(x = 316, y = 280)
        button10.place(x = 436, y = 278)
        button11.place(x = 565, y = 278)
        button12.place(x = 691, y = 279)
        button13.place(x = 60, y = 405)
        button14.place(x = 186, y = 405)
        


class Which_Professor_EEE_3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"which_prof_eee_3.png")
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

        tab_btn_img=tk.PhotoImage(file=f"which_prof_eee_2_tab1.png")
        tab_btn_img = tab_btn_img.zoom(10)
        tab_btn_img = tab_btn_img.subsample(17)
        tab_btn = tk.Label(self, image=tab_btn_img)
        tab_btn.image = tab_btn_img
        tab_button1 = tk.Button(self, image = tab_btn_img, bg = "medium blue", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_EEE_1")) 

        tab2_btn_img=tk.PhotoImage(file=f"which_prof_eee_1_tab1.png")
        tab2_btn_img = tab2_btn_img.zoom(10)
        tab2_btn_img = tab2_btn_img.subsample(17)
        tab2_btn = tk.Label(self, image=tab2_btn_img)
        tab2_btn.image = tab2_btn_img
        tab_button2 = tk.Button(self, image = tab2_btn_img, bg = "medium blue", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("Which_Professor_EEE_2")) 

        prof_btn1_img=tk.PhotoImage(file=f"which_prof_eee_3_jjg.png")
        prof_btn1_img = prof_btn1_img.zoom(10)
        prof_btn1_img = prof_btn1_img.subsample(17)
        prof_btn1 = tk.Label(self, image=prof_btn1_img)
        prof_btn1.image = prof_btn1_img
        button1 = tk.Button(self, image = prof_btn1_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_jjg")) 
        
        prof_btn2_img=tk.PhotoImage(file=f"which_prof_eee_3_jtg.png")
        prof_btn2_img = prof_btn2_img.zoom(10)
        prof_btn2_img = prof_btn2_img.subsample(17)
        prof_btn2 = tk.Label(self, image=prof_btn2_img)
        prof_btn2.image = prof_btn2_img
        button2 = tk.Button(self, image = prof_btn2_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_jtg")) 

        prof_btn3_img=tk.PhotoImage(file=f"which_prof_eee_3_jys.png")
        prof_btn3_img = prof_btn3_img.zoom(10)
        prof_btn3_img = prof_btn3_img.subsample(17)
        prof_btn3 = tk.Label(self, image=prof_btn3_img)
        prof_btn3.image = prof_btn3_img
        button3 = tk.Button(self, image = prof_btn3_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_jys")) 

        prof_btn4_img=tk.PhotoImage(file=f"which_prof_eee_3_cgc.png")
        prof_btn4_img = prof_btn4_img.zoom(10)
        prof_btn4_img = prof_btn4_img.subsample(17)
        prof_btn4 = tk.Label(self, image=prof_btn4_img)
        prof_btn4.image = prof_btn4_img
        button4 = tk.Button(self, image = prof_btn4_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_cgc")) 

        prof_btn5_img=tk.PhotoImage(file=f"which_prof_eee_3_cdh.png")
        prof_btn5_img = prof_btn5_img.zoom(10)
        prof_btn5_img = prof_btn5_img.subsample(17)
        prof_btn5 = tk.Label(self, image=prof_btn5_img)
        prof_btn5.image = prof_btn5_img
        button5 = tk.Button(self, image = prof_btn5_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_cdh")) 

        prof_btn6_img=tk.PhotoImage(file=f"which_prof_eee_3_cyw.png")
        prof_btn6_img = prof_btn6_img.zoom(10)
        prof_btn6_img = prof_btn6_img.subsample(17)
        prof_btn6 = tk.Label(self, image=prof_btn6_img)
        prof_btn6.image = prof_btn6_img
        button6 = tk.Button(self, image = prof_btn6_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_cyw")) 

        prof_btn7_img=tk.PhotoImage(file=f"which_prof_eee_3_cwj.png")
        prof_btn7_img = prof_btn7_img.zoom(10)
        prof_btn7_img = prof_btn7_img.subsample(17)
        prof_btn7 = tk.Label(self, image=prof_btn7_img)
        prof_btn7.image = prof_btn7_img
        button7 = tk.Button(self, image = prof_btn7_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_cwj")) 

        prof_btn8_img=tk.PhotoImage(file=f"which_prof_eee_3_hch.png")
        prof_btn8_img = prof_btn8_img.zoom(10)
        prof_btn8_img = prof_btn8_img.subsample(17)
        prof_btn8 = tk.Label(self, image=prof_btn8_img)
        prof_btn8.image = prof_btn8_img
        button8 = tk.Button(self, image = prof_btn8_img, bg = "white", overrelief="flat", relief="flat", borderwidth = 0, highlightthickness = 0,
                           command=lambda: controller.show_frame("eee_hch")) 

        tab_button1.place(x = 65, y = 90)
        tab_button2.place(x = 145, y = 88)

        button1.place(x = 60, y = 150)
        button2.place(x = 187, y = 156)
        button3.place(x = 314, y = 152)
        button4.place(x = 440, y = 152)
        button5.place(x = 571, y = 173)
        button6.place(x = 692, y = 154)
        button7.place(x = 58, y = 280)
        button8.place(x = 186, y = 280)





# EEE


class eee_kh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_kh_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_kjh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_kjh_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_kss(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_gss_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)


class eee_khi(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_khi_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_kjp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_kjp_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_kjs(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_kjs_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
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
class eee_kci(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_kci_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
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

"""
class eee_khs(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_khs_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_2"))
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

class eee_rjs(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_rjs_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
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
class eee_muc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_muc_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
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

class eee_psk(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_psk_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)


class eee_psh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_psh_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_phh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_bhh_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_pgh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_bgh_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
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
class eee_pdh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_pdh_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
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
class eee_pcw(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_bcw_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
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
class eee_ssh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_ssh_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_1"))
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
class eee_soy(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_soy_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_2"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_sgb(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_sgb_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_2"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_sds(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_sds_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_2"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_sy(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_sy_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_2"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_lmh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_lmh_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_2"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)




class eee_space(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_space_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_2"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_ljr(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_ljr_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_2"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_ljw(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_ljw_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_2"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_lhl(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_lhl_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_2"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_lhg(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_lhg_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_2"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_lsj(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_lsj_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_2"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_jjg(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_jjg_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_3"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_jtg(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_jtg_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_3"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_jys(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_jys_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_3"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_cdh(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_cdh_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_3"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_cyw(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_cyw_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_3"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_cwj(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_cwj_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_3"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)

class eee_hch(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        background_main_img=tk.PhotoImage(file=f"eee_hch_qr.png")
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
                            command=lambda: controller.show_frame("Which_Professor_EEE_3"))
        button00.place(x = 20, y = 524)

        goto_first_img=tk.PhotoImage(file=f"goto_first.png")
        goto_first_img = goto_first_img.zoom(10)
        goto_first_img = goto_first_img.subsample(17)
        goto_fisrt = tk.Label(self, image=goto_first_img)
        goto_fisrt.image = goto_first_img
        button01 = tk.Button(self, image = goto_first_img, bg = "white", overrelief="flat", relief="flat",borderwidth = 0, highlightthickness = 0,
                            command=lambda: controller.show_frame("StartPage")) 
        button01.place(x = 20, y = 475)