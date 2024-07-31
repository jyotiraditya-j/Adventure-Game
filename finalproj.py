from tkinter import * 
#import tkinter as tk

from PIL import ImageTk,Image
root=Tk()
root.geometry("1000x500")
frame = Frame(root).pack() 
bottomframe = Frame(root).pack()
r = Tk()
r.geometry("500x500")
r.title('ADV GAME')
w = Label(r,text='ADVENTURE GAME',font="50").pack()
canvas = Canvas(r, width = 20, height = 30)
score=0
def inst(): #the instructions r mentioned
    t = Message(r , text= "HEY,READ THE STORY CAREFULLY AND ANSWER THE QUESTIONS TO MOVE TO NEXT LEVEL\n You've been deserted from your group during a forest expedition and have been roaming the forest for hours\nThe sun had already set a few hours ago.You look up the time in your watch and it's close to 11 pm\nThe ambience is errie and the forest is full of wild animals.Growls and screeches of carnivores, who're ready to pounce on you an devort you at any given time can be heard everywhere\n Fortunately, you stumble your way across and old mansion and decide to take shelter for the night\n The moment you stepped foot inside the mansion, the doors behind you shut tight.Doors and windows started rattling and afraid as you are, you start hyperventilating\nIt was at this moment a voice boomed in the air\n WELCOME TO THE WILSON MANSION, THIS PROPERTY IS HAUNTED BY THE SPIRIT OF THE DEAD MR. WILSON\n All you've gotta do - is play his game and you're good to go.Nope it ain't easy\n Follow my instructions,There are 3 levels in this mansion,Each level consists of 2 rooms\n Answer the question in each room to obtain keys to unlock the door to the next one").pack()

   



greet = Label(r, text="Welcome.").pack()

startButton = Button(r, text="Start" , command = r.destroy ).pack()
instr = Button(r, text="Instructions", command=inst).pack()
end = Button(r, text="Exit", command=r.destroy).pack()

load = Image.open("img1.png")
render = ImageTk.PhotoImage(load)
img = Label(bottomframe, image=render)
img.image = render
#img = img.resize((250, 250), Img.ANTIALIAS)
img.place(x=200, y=100)

def correct():
    Label(frame,text="Correct! Good job").pack()     
def incorrect():
    Label(frame,text="Incorrect, try again").pack()   
#def incorrect2():
    Label(frame,text="Incorrect, try again").pack()   
#def incorrect3():
    Label(frame,text="Incorrect, try again").pack()     
Question1 = Label(frame, text='Q.1.. You hear a creepy sultry voice coming from a room and investigate the source of the haunting voice. Can you locate the apparition in the room ? ')
Question1.pack() 

var = StringVar()
Q1A = Radiobutton(frame, text='[A] In the bed',command = incorrect )
Q1A.pack() 

#Q1B = Radiobutton(frame, text='[B] In the ???',command = incorrect2 )
#Q1B.pack() 

Q1B = Radiobutton(frame, text='[B] In the mirror', command = correct)
Q1B.pack() 

#Q1D = Radiobutton(frame, text='[D] In the ???', command = incorrect3)
#Q1D.pack() 

submit = Button(frame, text='Submit', command = root.destroy )
submit.pack() 
mainloop()
print("so are you ready to move to room 2?")
result=input("type the answer of room 1:")
if (result.upper() =='IN THE MIRROR'):
#L1R2
  root=Tk()
  root.geometry("1000x500")
  frame = Frame(root).pack() 
  bottomframe = Frame(root).pack()
  load = Image.open("img2.png")
  render = ImageTk.PhotoImage(load)
  img = Label(bottomframe, image=render)
  img.image = render
  #img = img.resize((250, 250), Img.ANTIALIAS)
  img.place(x=200, y=100)
  def correct():
    Label(frame,text="Correct! Good job").pack()     
  def incorrect():
    Label(frame,text="Incorrect, try again").pack()   
  def incorrect2():
    Label(frame,text="Incorrect, try again").pack()   
  def incorrect3():
    Label(frame,text="Incorrect, try again").pack()     
  Question1 = Label(frame, text='What pattern is carved on the wooden plank ? ')
  Question1.pack() 

  var = StringVar()
  Q1A = Radiobutton(frame, text='[A] triangular',command = incorrect )
  Q1A.pack() 

  Q1B = Radiobutton(frame, text='[B] hexagonal',command = incorrect2 )
  Q1B.pack() 

  Q1C = Radiobutton(frame, text='[C] floral', command = correct)
  Q1C.pack() 

  Q1D = Radiobutton(frame, text='[D] circular', command = incorrect3)
  Q1D.pack() 

  submit = Button(frame, text='Submit', command = root.destroy )
  submit.pack() 
else:
  exit()
mainloop()
#L2R1

root=Tk()
root.geometry("1000x500")
frame = Frame(root).pack() 
bottomframe = Frame(root).pack()
load10 = Image.open("img1.png")
render = ImageTk.PhotoImage(load10)
img = Label(bottomframe, image=render)
img.image = render


Question2 =  Message(frame, text = " You come across a friendly spirit who guides you to the next room .\n  You enter the room only to find a wall full of clocks displaying time from cities all around the globe. Here’s what she asks you –\nThis country lies close to the Land of the Rising Sun,\nAnswer it correctly ‘cause this ain’t fun\nFamous for it’s diversity and pop culture\nUnlike the North, it isn’t full of vultures?")
Question2.pack()
var = StringVar()
Q2A = Radiobutton(frame, text='[A] india',command = incorrect )
Q2A.pack()
Q2B = Radiobutton(frame, text='[B] Germany',command = incorrect )
Q2B.pack()
Q3B = Radiobutton(frame, text='[B] South Korea',command = correct )
Q3B.pack()
submit = Button(frame, text='Submit', command = root.destroy )
submit.pack() 
mainloop()
print("so are you ready to move to the next level?")
result=input("type the answer of room 2:")
if (result.upper() =='SOUTH KOREA'):
    root=Tk()
    root.geometry("1000x500")
    frame = Frame(root).pack() 
    bottomframe = Frame(root).pack()
#image addition thingy L2R1
    load2 = Image.open("img4.png")
    render = ImageTk.PhotoImage(load2)
    img = Label(bottomframe, image=render)
    img.image = render
    def correct():
        Label(frame,text="Correct! Good job").pack()
    def incorrect():
        Label(frame,text="Incorrect, try again").pack()
    def incorrect2():
        Label(frame,text="Incorrect, try again").pack()   
    def incorrect3():
        Label(frame,text="Incorrect, try again").pack()
    Question2 = Label(frame,text ='There’s a nauseating smell emanating from this room and you open it to find 2 beds with their mattresses stained with blood. What gas is giving off the Nauseating odour?')
    Question2.pack()
    var = StringVar()
    Q2A = Radiobutton(frame, text='[A]socks ',command = incorrect )
    Q2A.pack()
    Q2B = Radiobutton(frame, text='[B] ammonia',command = incorrect )
    Q2B.pack()
    Q2C = Radiobutton(frame, text='[B] hydrogen sulphide',command = correct )
    Q2C.pack()
    Q2D = Radiobutton(frame, text='[B] more socks',command = incorrect )
    Q2D.pack()
    submit = Button(frame, text='Submit', command = root.destroy )
    submit.pack() 
else:
  exit()
mainloop()

#Level2#Room1
root=Tk()
root.geometry("1000x500")
frame = Frame(root).pack() 
bottomframe = Frame(root).pack()
Question3 = Message(frame, text='You’ve reached the final level of the floor and you find 5 seats and a wheelchair in the lobby. 3/5 seats are defective and the wheel chair is unoperational thanks to the rust coating. Mr. Wilson’s spirit demands you to remove the rust from the wheelchair by using a chemical from a lab present in the same floor. What chemical do you use? (Hint – It’s an acid )  ')
Question3.pack()
var = StringVar()
Q3A = Radiobutton(frame, text='[A] phosphoric acid',command = correct )
Q3A.pack()
Q3B = Radiobutton(frame, text='[B] socks',command = incorrect )
Q3B.pack()
submit = Button(frame, text='Submit', command = root.destroy )
submit.pack() 
mainloop()
print("so are you ready to move to the next room?")
result=input("type the answer of room 1:")
if (result.upper() =='PHOSPHORIC ACID'):
    #image addition thingy
    root=Tk()
    root.geometry("1000x500")
    frame = Frame(root).pack() 
    bottomframe = Frame(root).pack()
    load1 = Image.open("img3.png")
    render = ImageTk.PhotoImage(load1)
    img = Label(bottomframe, image=render)
    img.image = render
    def correct():
        Label(frame,text="Correct! Good job").pack()
    def incorrect():
        Label(frame,text="Incorrect, try again").pack()
    def incorrect2():
        Label(frame,text="Incorrect, try again").pack()   
    def incorrect3():
        Label(frame,text="Incorrect, try again").pack()
   
    Question3 = Message(frame, text = ("You’re finally close to the exit and relishing your freedom. However, Mr Wilson has one final question left got you, He guides you to a the rooftop garden . You notice the apparition of another beautiful spirit hovering over the plants and this is what Mr Wilson says “She’s my son’s daughter’s grandfather’s neice’s son’s uncle’s mother’s husband’s wife How is she related to me?"))
    Question3.pack()
    var = StringVar()
    Q3A = Radiobutton(frame, text='[A] uncle ',command = incorrect )
    Q3A.pack()
    Q3B = Radiobutton(frame, text= "[B] step dad",command = incorrect )
    Q3B.pack()
    Q3C = Radiobutton(frame, text='[C] wife ',command = correct )
    Q3C.pack()
    Q3D = Radiobutton(frame, text="[D] vansh" ,command = incorrect )
    Q3D.pack()
    submit = Button(frame, text='Submit', command = root.destroy )
    submit.pack() 
else:
    print('Thank you for playing')
    exit()
mainloop()

 


