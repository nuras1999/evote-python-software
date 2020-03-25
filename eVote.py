from tkinter.ttk import *
from tkinter import *
from playsound import playsound
from PIL import Image, ImageTk
from time import sleep
import sys


def splashScreen():
    window=Tk()
    window.title(" ")
    window.geometry("600x400")
    window.resizable(0,0)
    window.configure(background = '#DAF1F1')

    width = 600
    height = 400
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def disable_event():
        pass 

    # def callback():
    #     print ("click!")


    print("Splashscreen STARTED")

    label_1=Label(window,text=" Vote", font=("Stencil",45),foreground="#232323",width="18",background="#DAF1F1")
    label_1.place(x=-29, y=220)

    label_2=Label(window,text="e", font=("Segoe Print",37),foreground="#343434",background="#DAF1F1")
    label_2.place(x=215, y=210)

    label_3=Label(window,text="Voting made simpler", font=("Segoe Print",25),foreground="#232323",background="#DAF1F1",width="18")
    label_3.place(x=120, y=290)
    
    

    load = Image.open("evote_icon.png")  
    load = load.resize((170, 170))
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render,border=FALSE)
    img.image = render
    img.place(x=220, y=30)
    #ttk.Button(window,text="Enter",command=callback).place(x=260, y=250)


    window.wm_attributes('-toolwindow',True)
    window.wm_attributes('-topmost',True)
    window.overrideredirect(True)
    window.protocol("WM_DELETE_WINDOW", disable_event) 
    

    windowWidth=600
    Style=ttk.Style()
    window.after(5000, window.destroy)
    #print("Splashscreen ended")
    window.mainloop()







def exitPage():
            
    window2=Tk()
    window2.title("Thankyou")
    window2.geometry("600x400")
    window2.resizable(0,0)
    window2.configure(background = '#DAF1F1')

    width = 600
    height = 400
    x = (window2.winfo_screenwidth() // 2) - (width // 2)
    y = (window2.winfo_screenheight() // 2) - (height // 2)
    window2.geometry('{}x{}+{}+{}'.format(width, height, x, y))


    def callMainloop():
        window2.destroy()
        print("Exit page closed")
        sleep(2)
        frontEnd()

    def exitApp():
        print("Closing the application")
        window2.destroy()
        sys.exit()
        
    def disable_event():
        pass  
    
    label_1=Label(window2,text="Thankyou for voting", font=("Segoe Print",40),foreground="#232323",width="18")
    label_1.place(x=0, y=140)


    # load2 = Image.open("exit_button.png")  
    # load2 = load2.resize((60, 30))
    # render2 = ImageTk.PhotoImage(load2)
    # img2 = Label(window2, image=render2)
    # img2.image = render2
    ttk.Button(window2,text="EXIT", command=callMainloop).place(x=280, y=320)


    # load3 = Image.open("smile.png")  
    # load3 = load3.resize((100, 100))
    # render3 = ImageTk.PhotoImage(load3)
    # img3 = Label(window2, image=render3)
    # img3.image = render3
    # img3.place(x=260, y=50)

    playsound('Thank_you.wav')


    b=Button(window2,command=exitApp)
    b.place(x=0,y=380)

    print("\nExit page started")

    window2.protocol("WM_DELETE_WINDOW", disable_event) 
    window2.wm_attributes('-topmost',True)
    windowWidth=600
    Style=ttk.Style()
    window2.mainloop()









def eVotePage():

    window1=Tk()
    window1.title("eVote")
    window1.geometry("600x400")
    window1.resizable(0,0)
    window1.configure(background = '#DAF1F1')

    width = 600
    height = 400
    x = (window1.winfo_screenwidth() // 2) - (width // 2)
    y = (window1.winfo_screenheight() // 2) - (height // 2)
    window1.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def disable_event():
        pass  

    def callExit():
        window1.destroy()
        sleep(2)
        print("\nSuccessfully voted")
        exitPage()

    def votename_display(selected):
        # load = Image.open("vote_button.png")  
        # load = load.resize((90, 50))
        # render = ImageTk.PhotoImage(load)
        # img = Label(window1, image=render)
        # img.image = render
        #ttk.Button(window1,text="VOTE" ,command=callExit).place(x=260, y=330)
        #print(radioclicked(selected))
        #name=radioclicked(selected)
        name2=selected.get()
        #print(selected.get())
        #name2="2"
        print(name2)
        vote_name=""
        if name2=="1":
            vote_name="Arun"
            # votename_display(vote_name)
        elif name2=="2":
            vote_name="Akash" 
            # votename_display(vote_name)
        elif name2=="3":
            vote_name= "Keshav"
            # votename_display(vote_name)
        elif name2=="4":
            vote_name= "Sanjay"
        print(vote_name)
        #print(name)
        #print(selected)
        callExit()
        


    label_1=Label(window1,text="VOTE", font=("Stencil",50),foreground="#232323",width="15")
    label_1.place(x=0, y=30)

    label_2=Label(window1,text="e", font=("Segoe Print",35),foreground="#343434")
    label_2.place(x=200, y=30)

    label_3=Label(window1,text="Whom do you vote?", font=("Segoe Print",20,"bold"),foreground="#343434", background="#DAF1F1")
    label_3.place(x=170, y=130)
    '''
    load = Image.open("vote_button.png")  
    load = load.resize((90, 50))
    render = ImageTk.PhotoImage(load)
    img = Label(window1, image=render)
    img.image = render
    b = Button(window1,image=render, command=lambda:votename_display(selected))
    b.place(x=260, y=330)
    '''
    ttk.Button(window1,text="VOTE", command=lambda:votename_display(selected)).place(x=260, y=330)


    selected=StringVar()

    rad1=Radiobutton(window1, text="Arun", font=("Segoe Print",15),background="#DAF1F1",value=1, variable=selected)
    rad2=Radiobutton(window1,text="Akash Sivadas Menon",font=("Segoe Print",15), background="#DAF1F1", value=2, variable=selected)
    rad3=Radiobutton(window1, text="Keshavamurthy",font=("Segoe Print",15), background="#DAF1F1", value=3, variable=selected)
    rad4=Radiobutton(window1,text="Sanjay kumar", font=("Segoe Print",15), background="#DAF1F1",value=4, variable=selected)
    rad1.place(x=90, y=200)
    rad2.place(x=320, y=200)
    rad3.place(x=90, y=270)
    rad4.place(x=320, y=270)

    window1.protocol("WM_DELETE_WINDOW", disable_event) 
    window1.wm_attributes('-topmost',True)
    windowWidth=600
    Style=ttk.Style()
    window1.mainloop()
    












def frontEnd():
    window=Tk()
    window.resizable(0,0)
    window.configure(background = '#DAF1F1')


    def welcomedestroy():
        window.after(2000, window.destroy)
        sleep(2)
        print("Successfully welcome page called and voting started")
        eVotePage()



    width = 600
    height = 400
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    label_1=Label(window,text="Welcome  to    Vote", font=("Stencil",40),foreground="#232323",width="18")
    label_1.place(x=0, y=140)

    label_2=Label(window,text="e", font=("Segoe Print",35),foreground="#343434")
    label_2.place(x=395, y=130)

    ttk.Button(window,text="VOTE", command=welcomedestroy).place(x=260, y=250)




    window.protocol("WM_DELETE_WINDOW", disable_event) 
    window.wm_attributes('-topmost',True)
    windowWidth=600
    Style=ttk.Style()
    window.mainloop()








def welcomePage():

    window=Tk()
    window.title("Welcome")
    window.geometry("600x400")
    window.resizable(0,0)
    window.configure(background = '#DAF1F1')

    width = 600
    height = 400
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def callback():
        print ("click!")

    def closewelcomepage():
        window.after(2000, window.destroy)
        sleep(2)
        print("Welcome page SUCCESS")
        frontEnd()


    label_1=Label(window,text="Welcome  to    Vote", font=("Stencil",40),foreground="#232323",width="18")
    label_1.place(x=0, y=140)

    label_2=Label(window,text="e", font=("Segoe Print",35),foreground="#343434")
    label_2.place(x=395, y=130)

    ttk.Button(window, text="START VOTING", command=closewelcomepage).place(x=250, y=250)

    windowWidth=600
    Style=ttk.Style()
    window.mainloop()













def detailsPage():
    username="a"
    password="a"

    username1=""
    password1=""
    person1=""
    person2=""
    person3=""
    person4=""

    window=Tk()
    window.title("Details registration")
    window.geometry("600x400")
    window.resizable(0,0)
    window.configure(background = '#DAF1F1')

    width = 600
    height = 400
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def closewindow():
        window.after(3000, window.destroy)
        sleep(2)
        print("Details page success")
        welcomePage()


    def printtext():
        username1 = entry_1.get() 
        password1 = entry_2.get()
        person1 = entry_3.get()
        person2 = entry_4.get()
        person3 = entry_5.get()
        person4 = entry_6.get()
        if username1==username and password1==password:
            print(username1) 
            print(password1+"\n") 
            print(person1) 
            print(person2) 
            print(person3) 
            print(person4) 
            print("\nSUCCESSFULLY LOGGED IN\n")
            #window.destroy
            closewindow()


        else:
            print("\nINVALID CREDENTIALS\n")



    label_1=Label(window,text="Username", font=("Segoe Print",15,"bold"),foreground="#343434", background="#DAF1F1")
    label_1.place(x=20, y=30)

    label_2=Label(window,text="Password", font=("Segoe Print",15,"bold"),foreground="#343434", background="#DAF1F1")
    label_2.place(x=340, y=30)

    entry_1 = ttk.Entry(window, textvariable = username1, justify = LEFT) 
    entry_1.place(x=130, y=41)
    entry_1.focus_force() 

    entry_2 = ttk.Entry(window, textvariable = password1, show="*",justify = LEFT) 
    # entry_2.config({"background": "yellow"})
    entry_2.place(x=450, y=41)


    label_3=Label(window,text="LIST OF NAMES", font=("Segoe Print",20,"bold"),foreground="#343434", background="#DAF1F1")
    label_3.place(x=200, y=70)

    label_4=Label(window,text="Person 1", font=("Segoe Print",13,"bold"),foreground="#343434", background="#DAF1F1")
    label_4.place(x=200, y=120)
    entry_3 = ttk.Entry(window, textvariable = person1, justify = LEFT) 
    entry_3.place(x=300, y=127)

    label_5=Label(window,text="Person 2", font=("Segoe Print",13,"bold"),foreground="#343434", background="#DAF1F1")
    label_5.place(x=200, y=170)
    entry_4 = ttk.Entry(window, textvariable = person2, justify = LEFT) 
    entry_4.place(x=300, y=177)

    label_6=Label(window,text="Person 3", font=("Segoe Print",13,"bold"),foreground="#343434", background="#DAF1F1")
    label_6.place(x=200, y=220)
    entry_5 = ttk.Entry(window, textvariable = person3, justify = LEFT) 
    entry_5.place(x=300, y=227)

    label_7=Label(window,text="Person 4", font=("Segoe Print",13,"bold"),foreground="#343434", background="#DAF1F1")
    label_7.place(x=200, y=270)
    entry_6 = ttk.Entry(window, textvariable = person4, justify = LEFT) 
    entry_6.place(x=300, y=277)

    ttk.Button(window, text="OK" ,command=printtext).place(x=280, y=340)

    windowWidth=600
    Style=ttk.Style()
    window.mainloop()










splashScreen()
print("\nSplashscreen ENDED")

detailsPage()

#welcomePage()

#exitPage()

#eVotePage()