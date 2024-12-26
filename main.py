from tkinter import * #Imports all classes and methods within tkinter(GUI objects)
from PIL import Image, ImageTk

screen=Tk()
screen.title('Retail Billing System')
screen.geometry('1270x685')

#Adds that small image at the top of the window
billing=Image.open("images/billing icon.jpg")
resizedBilling=billing.resize((30,20))
billingIcon=ImageTk.PhotoImage(resizedBilling)
screen.iconphoto(False,billingIcon)

#Adds a label heading at the top of the window
headingLabel=Label(
                   screen,
                   text='Retail Billing System',
                   font=('Helvetica',30,'bold'),
                   bg='#36454F',
                   fg='#FFEB99',
                   bd=12, #border width
                   relief=GROOVE, #Creates a sunken grooved appearance
                   )
headingLabel.pack(fill=X, pady=10) #centers 'Retail Billing System' a
                          #nd fills it with background color

customerDetailsFrame=LabelFrame(screen,
                                text='Customer Details',
                                font=('Helvetica',15,'bold'),
                                bg='#36454F',
                                fg='#FFEB99',
                                bd=8,
                                relief=GROOVE) #Organizes elements into a frame
                                                                #called 'Customer Details'
customerDetailsFrame.pack(fill=X)

nameLabel=Label(customerDetailsFrame,
                text='Name:',
                font=('Helvetica',15,'bold'),
                bg='#36454F',
                fg='white'
               )
nameLabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(customerDetailsFrame,font=('Helvetica',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customerDetailsFrame,
                 text='Phone:',
                 font=('Helvetica',15,'bold'),
                 bg='#36454F',
                 fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customerDetailsFrame,
                 font=('arial',15,'bold'),
                 bd=7,
                 width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billLabel=Label(customerDetailsFrame,
                text='Bill Number:',
                font=('Helvetica',15,'bold'),
                bg='#36454F',
                fg='white')
billLabel.grid(row=0,column=4,padx=20,pady=2)

billEntry=Entry(customerDetailsFrame,
                font=('arial',15,'bold'),
                bd=7,
                width=18
                )
billEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customerDetailsFrame,
                    text='SEARCH',
                    font=('Helvetica',8,'bold'),
                    width=20,
                    height=2,
                    relief=GROOVE
                    )
searchButton.grid(row=0,column=6,padx=10)

productsFrame=Frame(screen)
productsFrame.pack()


screen.mainloop()
