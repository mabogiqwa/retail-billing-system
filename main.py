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
productsFrame.pack(pady=10)

cosmeticsFrame=LabelFrame(productsFrame,
                          text='Cosmetics',
                          font=('Helvetica',15,'bold'),
                          bg='#36454F',
                          fg='#FFEB99',
                          bd=8,
                          relief=GROOVE
                          )
cosmeticsFrame.grid(row=0, column=0)

#Elements in frame

#Bath soap label and entry
bathSoapLabel=Label(cosmeticsFrame,text='Bath Soap:',font=('Helvetica',15,'bold'),
                    bg='#36454F',
                    fg='white'
                   )
bathSoapLabel.grid(row=0,column=0,pady=9,padx=2)

bathSoapEntry=Entry(cosmeticsFrame,
                    font=('Helvetica',15,'bold'),
                    width=10,
                    bd=5)
bathSoapEntry.grid(row=0,column=1,pady=9,padx=2)

#Cleanser soap label and entry
cleanserLabel=Label(cosmeticsFrame,
                    text='Cleanser:',
                    font=('Helvetica',15,'bold'),
                    bg='#36454F',
                    fg='white'
                   )
cleanserLabel.grid(row=1,column=0,pady=9,padx=2)

cleanserEntry=Entry(cosmeticsFrame,
                    font=('Helvetica',15,'bold'),
                    width=10,
                    bd=5
                   )
cleanserEntry.grid(row=1,column=1,pady=9,padx=2)

#Cologne label and entry
cologneLabel=Label(cosmeticsFrame,
                   text="Cologne:",
                   font=('Helvetica',15,'bold'),
                   bg='#36454F',
                   fg='white'
                  )
cologneLabel.grid(row=2,column=0,pady=9,padx=2)

cologneEntry=Entry(cosmeticsFrame,
                   font=('Helvetica',15,'bold'),
                   width=10,
                   bd=5
                  )
cologneEntry.grid(row=2,column=1,pady=9,padx=2)

#Body lotion label and entry
bodyLotionLabel=Label(cosmeticsFrame,
                 text='Body lotion:',
                 font=('Helvetica',15,'bold'),
                 bg='#36454F',
                 fg='white'
                )
bodyLotionLabel.grid(row=3,column=0,pady=9,padx=2)

bodyLotionLabelEntry=Entry(cosmeticsFrame,
                           font=('Helvetica',15,'bold'),
                           width=10,
                           bd=5
                           )
bodyLotionLabelEntry.grid(row=3,column=1,pady=9,padx=10)

#Shampoo label and entry
shampooLabel=Label(cosmeticsFrame,
                   text='Shampoo:',
                   font=('Helvetica',15,'bold'),
                   bg='#36454F',
                   fg='white'
                   )
shampooLabel.grid(row=4,column=0,pady=9,padx=2)

shampooLabelEntry=Entry(cosmeticsFrame,
                        font=('Helvetica',15,'bold'),
                        width=10,
                        bd=5
                        )
shampooLabelEntry.grid(row=4,column=1,pady=9,padx=2)

#Toothpaste
toothPasteLabel=Label(cosmeticsFrame,
                      text='Toothpaste:',
                      font=('Helvetica',15,'bold'),
                      bg='#36454F',
                      fg='white'
                      )
toothPasteLabel.grid(row=5,column=0,pady=9,padx=2)

toothPasteEntry=Entry(cosmeticsFrame,
                      font=('Helvetica',15,'bold'),
                      width=10,
                      bd=5
                      )
toothPasteEntry.grid(row=5,column=1,pady=9,padx=2)

#Meat and Sea-food block of code
meatFrame=LabelFrame(productsFrame,
                          text='Meat and Seafood',
                          font=('Helvetica',15,'bold'),
                          bg='#36454F',
                          fg='#FFEB99',
                          bd=8,
                          relief=GROOVE
                          )
meatFrame.grid(row=0,column=1)

#Fresh meat
freshMeatLabel=Label(meatFrame,
                     text='Fresh Meat:',
                     font=('Helvetica',15,'bold'),
                     bg='#36454F',
                     fg='white',
                     )
freshMeatLabel.grid(row=0,column=0,pady=9,padx=2)

freshMeatEntry=Entry(meatFrame,
                     font=('Helvetica',15,'bold'),
                     width=10,
                     bd=5
                     )
freshMeatEntry.grid(row=0,column=1,pady=9,padx=10)

#Processed meat
processedMeatLabel=Label(meatFrame,
                         font=('Helvetica',15,'bold'),
                         text='Processed Meat:',
                         bg='#36454F',
                         fg='white'
                         )
processedMeatLabel.grid(row=1,column=0,pady=9,padx=2)

processedMeatEntry=Entry(meatFrame,
                              font=('Helvetica',15,'bold'),
                              width=10,
                              bd=5
                              )
processedMeatEntry.grid(row=1,column=1,pady=9,padx=2)

#Fresh seafood
freshSeaFoodLabel=Label(meatFrame,
                        font=('Helvetica',15,'bold'),
                        text='Fresh Sea Food:',
                        bg='#36454F',
                        fg='white'
                        )
freshSeaFoodLabel.grid(row=2,column=0,pady=9,padx=10)

freshSeaFoodEntry=Entry(meatFrame,
                        font=('Helvetica',15,'bold'),
                        width=10,
                        bd=5
                        )
freshSeaFoodEntry.grid(row=2,column=1,pady=9,padx=2)
                
#Frozen seafood
frozenSeaFoodLabel=Label(meatFrame,
                         font=('Helvetica',15,'bold'),
                         text='Frozen Sea Food:',
                         bg='#36454F',
                         fg='white'
                         )
frozenSeaFoodLabel.grid(row=3,column=0,pady=9,padx=2)

frozenSeaFoodEntry=Entry(meatFrame,
                         font=('Helvetica',15,'bold'),
                         width=10,
                         bd=5
                         )
frozenSeaFoodEntry.grid(row=3,column=1,pady=9,padx=2)

#Speciality meats
specialityMeatsLabel=Label(meatFrame,
                           font=('Helvetica',15,'bold'),
                           text='Offal & Speciality Meats:',
                           bg='#36454F',
                           fg='white'
                          )
specialityMeatsLabel.grid(row=4,column=0,pady=9,padx=2)

specialityMeatsEntry=Entry(meatFrame,
                           font=('Helvetica',15,'bold'),
                           width=10,
                           bd=5
                           )
specialityMeatsEntry.grid(row=4,column=1,pady=9,padx=2)

#Smoked meats
smokedMeatsLabel=Label(meatFrame,
                       text='Smoked meats:',
                       font=('Helvetica',15,'bold'),
                       bg='#36454F',
                       fg='white'
                       )
smokedMeatsLabel.grid(row=5,column=0,pady=9,padx=2)

smokedMeatsLabel=Entry(meatFrame,
                       font=('Helvetica',15,'bold'),
                       width=10,
                       bd=5
                       )
smokedMeatsLabel.grid(row=5,column=1,pady=9,padx=2)

#Beverages block of code (Frame)
beveragesFrame=LabelFrame(productsFrame,
                           text='Beverages',
                           font=('Helvetica',15,'bold'),
                           bg='#36454F',
                           fg='#FFEB99',
                           bd=8,
                           relief=GROOVE
                           )
beveragesFrame.grid(row=0,column=2)

#Water entry
waterLabel=Label(beveragesFrame,
                 text='Water:',
                 font=('Helvetica',15,'bold'),
                 bg='#36454F',
                 fg='white',
                 )
waterLabel.grid(row=0,column=0,pady=9,padx=2)

waterEntry=Entry(beveragesFrame,
                 font=('Helvetica',15,'bold'),
                 width=10,
                 bd=5
                 )
waterEntry.grid(row=0,column=1,pady=9,padx=2)

#Soft drinks entry
softDrinksLabel=Label(beveragesFrame,
                      font=('Helvetica',15,'bold'),
                      text='Soft Drinks:',
                      bg='#36454F',
                      fg='white'
                      )
softDrinksLabel.grid(row=1,column=0,pady=9,padx=2)

softDrinksEntry=Entry(beveragesFrame,
                      font=('Helvetica',15,'bold'),
                      width=10,
                      bd=5
                      )
softDrinksEntry.grid(row=1,column=1,pady=9,padx=2)

#Dairy beverages
dairyLabel=Label(beveragesFrame,
                 text='Dairy Beverages:',
                 font=('Helvetica',15,'bold'),
                 bg='#36454F',
                 fg='white'
                 )
dairyLabel.grid(row=2,column=0,pady=9,padx=2)

screen.mainloop()
