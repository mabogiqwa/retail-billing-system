from tkinter import messagebox
from tkinter import * #Imports all classes and methods within tkinter(GUI objects)
from PIL import Image, ImageTk

#An alternative function name such as 'bill' creates a logical error, not sure why
def get_the_bill():
    if nameEntry.get()=='':
        messagebox.showerror('Error','Name is missing!')
    elif phoneEntry.get()=='':
        messagebox.showerror('Error','Phone number is missing!')
    elif cosmeticPriceEntry.get()=='0.0' and meatPriceEntry.get()=='0.0':
        if beveragesPriceEntry.get()=='0.0':
            messagebox.showerror('Error','No product to bill!')
    elif cosmeticPriceEntry.get()=='R0.00' and meatPriceEntry.get()=='R0.00':
        if beveragesPriceEntry.get()=='R0.00':
            messagebox.showerror('Error','No product to bill!')
    else:
        textArea.delete(1.0, END)
        textArea.insert(END, '\tWelcome to Retail Billing System\n')
        textArea.insert(END, f'\nBill Number: {billEntry.get()}')
        textArea.insert(END, f'\nCustomer Name: {nameEntry.get()}')
        textArea.insert(END, f'\nPhone Number: {phoneEntry.get()}')
        textArea.insert(END, f'\n======================================')
        textArea.insert(END, '\nProduct\t\tQty\tPrice')
        textArea.insert(END, f'\n======================================')
        
        # Add product details if quantity > 0
        if float(bathSoapEntry.get()) > 0:
            textArea.insert(END, f'\nBath Soap\t\t{bathSoapEntry.get()}\tR{float(bathSoapEntry.get())*19}')
        if float(cleanserEntry.get()) > 0:
            textArea.insert(END, f'\nCleanser\t\t{cleanserEntry.get()}\tR{float(cleanserEntry.get())*330}')
        # Add similar entries for other products...
        
        total = int(cosmeticPriceEntry.get()) + int(cosmeticTaxEntry.get()) + int(meatPriceEntry.get()) + int(meatTaxEntry.get()) + int(beveragesPriceEntry.get()) + int(beveragesTaxEntry.get())
        
        textArea.insert(END, f'\n======================================')
        textArea.insert(END, f'\nCosmetics Price: \t\t{cosmeticPriceEntry.get()}')
        textArea.insert(END, f'\nCosmetics Tax: \t\t{cosmeticTaxEntry.get()}')
        textArea.insert(END, f'\nMeat Price: \t\t{meatPriceEntry.get()}')
        textArea.insert(END, f'\nMeat Tax: \t\t{meatTaxEntry.get()}')
        textArea.insert(END, f'\nBeverages Price: \t\t{beveragesPriceEntry.get()}')
        textArea.insert(END, f'\nBeverages Tax: \t\t{beveragesTaxEntry.get()}')
        textArea.insert(END, f'\n\nTotal: \t\t{total}')
        
def total():
    #Variables related to totaling the cosmetic products
    soapPrice=float(bathSoapEntry.get())*19
    cleanserPrice=float(cleanserEntry.get())*330
    colognePrice=float(cologneEntry.get())*900
    bodyLotionPrice=float(bodyLotionEntry.get())*100
    toothPastePrice=float(toothPasteEntry.get())*67

    totalCosmeticPrice = soapPrice+cleanserPrice+colognePrice+bodyLotionPrice+toothPastePrice
    cosmeticPriceEntry.delete(0, END)  # Clear existing value
    cosmeticPriceEntry.insert(0,f'R{totalCosmeticPrice:.2f}')

    cosmeticTax = totalCosmeticPrice * 0.05
    cosmeticTaxEntry.delete(0, END)
    cosmeticTaxEntry.insert(0,f'{cosmeticTax:.2f}')

    #Variables related to totaling the different meats
    freshMeatPrice=float(freshMeatEntry.get())*80
    processedMeatPrice=float(processedMeatEntry.get())*75
    freshSeaFoodPrice=float(freshSeaFoodEntry.get())*120
    frozenSeaFoodPrice=float(frozenSeaFoodEntry.get())*105
    specialityMeatPrice=float(specialityMeatsEntry.get())*115
    smokedMeatPrice=float(smokedMeatsEntry.get())*55

    totalMeatPrice = freshMeatPrice+processedMeatPrice+freshSeaFoodPrice+frozenSeaFoodPrice+specialityMeatPrice+smokedMeatPrice
    meatPriceEntry.delete(0, END)  # Clear existing value
    meatPriceEntry.insert(0,f'R{totalMeatPrice:.2f}')

    meatTax = totalMeatPrice * 0.04
    meatTaxEntry.delete(0, END)
    meatTaxEntry.insert(0,f'{meatTax:.2f}')

    #Variables related to totaling the different beverages
    waterPrice=float(waterEntry.get())*10
    softDrinksPrice=float(softDrinksEntry.get())*14
    dairyPrice=float(dairyEntry.get())*23
    alcoholicBevPrice=float(alcoholicBeveragesEntry.get())*56
    wellnessBevPrice=float(healthDrinksEntry.get())*45
    coffeeBevPrice=float(coffeeBeveragesEntry.get())*22

    totalBeveragePrice = waterPrice+softDrinksPrice+dairyPrice+alcoholicBevPrice+wellnessBevPrice+coffeeBevPrice
    beveragesPriceEntry.delete(0, END)  # Clear existing value
    beveragesPriceEntry.insert(0,f'R{totalBeveragePrice:.2f}')

    beveragesTax = totalBeveragePrice * 0.04
    beveragesTaxEntry.delete(0, END)
    beveragesTaxEntry.insert(0,f'{beveragesTax:.2f}')

screen=Tk()
screen.title('Retail Billing System')
screen.geometry('1320x730')

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

#Contact details
nameLabel=Label(customerDetailsFrame,
                text='Name:',
                font=('Helvetica',15,'bold'),
                bg='#36454F',
                fg='white'
               )
nameLabel.grid(row=0,column=0,padx=20,pady=2)

#Create an entry box for the name
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
                fg='white'
                )
billLabel.grid(row=0,column=4,padx=20,pady=2)

billEntry=Entry(customerDetailsFrame,
                font=('arial',15,'bold'),
                bd=7,
                width=18
                ) 
billEntry.grid(row=0,column=5,padx=8)

#Search button
searchButton=Button(customerDetailsFrame,
                    text='SEARCH',
                    font=('Helvetica',8,'bold'),
                    width=28,
                    height=2,
                    relief=GROOVE
                    )
searchButton.grid(row=0,column=6,padx=18)


#Frame for various product entries
productsFrame=Frame(screen)
productsFrame.pack(pady=7,anchor='nw')

#Cosmetics block of code
cosmeticsFrame=LabelFrame(productsFrame,
                          text='Cosmetics',
                          font=('Helvetica',15,'bold'),
                          bg='#36454F',
                          fg='#FFEB99',
                          bd=8,
                          relief=GROOVE
                          )
cosmeticsFrame.grid(row=0,column=0)

#Elements in frame

#Bath soap label and entry
bathSoapLabel=Label(cosmeticsFrame,text='Bath Soap:',
                    font=('Helvetica',15,'bold'),
                    bg='#36454F',
                    fg='white'
                   )
bathSoapLabel.grid(row=0,column=0,pady=9,padx=2)

bathSoapEntry=Entry(cosmeticsFrame,
                    font=('Helvetica',15,'bold'),
                    width=10,
                    bd=5)
bathSoapEntry.grid(row=0,column=1,pady=9,padx=2)
bathSoapEntry.insert(0,0)

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
cleanserEntry.insert(0,0)

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
cologneEntry.insert(0,0)

#Body lotion label and entry
bodyLotionLabel=Label(cosmeticsFrame,
                 text='Body lotion:',
                 font=('Helvetica',15,'bold'),
                 bg='#36454F',
                 fg='white'
                )
bodyLotionLabel.grid(row=3,column=0,pady=9,padx=2)

bodyLotionEntry=Entry(cosmeticsFrame,
                           font=('Helvetica',15,'bold'),
                           width=10,
                           bd=5
                           )
bodyLotionEntry.grid(row=3,column=1,pady=9,padx=10)
bodyLotionEntry.insert(0,0)

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
shampooLabelEntry.insert(0,0)

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
toothPasteEntry.insert(0,0)

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
freshMeatEntry.insert(0,0)

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
processedMeatEntry.insert(0,0)

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
freshSeaFoodEntry.insert(0,0)
                
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
frozenSeaFoodEntry.insert(0,0)

#Speciality meats
specialityMeatsLabel=Label(meatFrame,
                           font=('Helvetica',15,'bold'),
                           text='Speciality Meats:',
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
specialityMeatsEntry.insert(0,0)

#Smoked meats
smokedMeatsLabel=Label(meatFrame,
                       text='Smoked Meats:',
                       font=('Helvetica',15,'bold'),
                       bg='#36454F',
                       fg='white'
                       )
smokedMeatsLabel.grid(row=5,column=0,pady=9,padx=2)

smokedMeatsEntry=Entry(meatFrame,
                       font=('Helvetica',15,'bold'),
                       width=10,
                       bd=5
                       )
smokedMeatsEntry.grid(row=5,column=1,pady=9,padx=2)
smokedMeatsEntry.insert(0,0)

#Here
#Beverages block of code (Frame)
beveragesFrame=LabelFrame(productsFrame,
                           text='Beverages',
                           font=('Helvetica',15,'bold'),
                           bg='#36454F',
                           fg='#FFEB99',
                           bd=8,
                           relief=GROOVE
                           )
beveragesFrame.grid(row=0,column=3)

#Water entry
waterLabel=Label(beveragesFrame,
                 text='Water:',
                 font=('Helvetica',15,'bold'),
                 bg='#36454F',
                 fg='white',
                 )
waterLabel.grid(row=0,column=0,pady=9,padx=10)

waterEntry=Entry(beveragesFrame,
                 font=('Helvetica',15,'bold'),
                 width=10,
                 bd=5
                 )
waterEntry.grid(row=0,column=1,pady=9,padx=10)
waterEntry.insert(0,0)

#Soft drinks entry
softDrinksLabel=Label(beveragesFrame,
                      font=('Helvetica',15,'bold'),
                      text='Soft Drinks:',
                      bg='#36454F',
                      fg='white'
                      )
softDrinksLabel.grid(row=1,column=0,pady=9,padx=10)

softDrinksEntry=Entry(beveragesFrame,
                      font=('Helvetica',15,'bold'),
                      width=10,
                      bd=5
                      )
softDrinksEntry.grid(row=1,column=1,pady=9,padx=10)
softDrinksEntry.insert(0,0)

#Dairy beverages
dairyLabel=Label(beveragesFrame,
                 text='Dairy Drinks:',
                 font=('Helvetica',15,'bold'),
                 bg='#36454F',
                 fg='white'
                 )
dairyLabel.grid(row=2,column=0,pady=9,padx=10)

dairyEntry=Entry(beveragesFrame,
                 font=('Helvetica',15,'bold'),
                 width=10,
                 bd=5
                )
dairyEntry.grid(row=2,column=1,pady=9,padx=10)
dairyEntry.insert(0,0)

#Alcoholic beverages
alcoholicBeveragesLabel=Label(beveragesFrame,
                 text='Alcoholic Drinks:',
                 font=('Helvetica',15,'bold'),
                 bg='#36454F',
                 fg='white'
                 )
alcoholicBeveragesLabel.grid(row=3,column=0,pady=9,padx=10)

alcoholicBeveragesEntry=Entry(beveragesFrame,
                 font=('Helvetica',15,'bold'),
                 width=10,
                 bd=5
                )
alcoholicBeveragesEntry.grid(row=3,column=1,pady=9,padx=10)
alcoholicBeveragesEntry.insert(0,0)

#Health and Wellness Drinks
healthDrinksLabel=Label(beveragesFrame,
                        text='Wellness Drinks:',
                        font=('Helvetica',15,'bold'),
                        bg='#36454F',
                        fg='white'
                        )
healthDrinksLabel.grid(row=4,column=0,pady=9,padx=10)

healthDrinksEntry=Entry(beveragesFrame,
                        font=('Helvetica',15,'bold'),
                        width=10,
                        bd=5
                        )
healthDrinksEntry.grid(row=4,column=1,pady=9,padx=10)
healthDrinksEntry.insert(0,0)

#Coffee-based Drinks
coffeeBeveragesLabel=Label(beveragesFrame,
                           text='Coffee Drinks:',
                           font=('Helvetica',15,'bold'),
                           bg='#36454F',
                           fg='white'
                           )
coffeeBeveragesLabel.grid(row=5,column=0,pady=9,padx=10)

coffeeBeveragesEntry=Entry(beveragesFrame,
                           font=('Helvetica',15,'bold'),
                           width=10,
                           bd=5
                           )
coffeeBeveragesEntry.grid(row=5,column=1,pady=9,padx=10)
coffeeBeveragesEntry.insert(0,0)

billingFrame=Frame(productsFrame,bd=4,relief=GROOVE)
billingFrame.grid(row=0,column=4)

billingAreaLabel=Label(billingFrame,
                       text='Bill',
                       font=('Helvetica',15,'bold'),
                       relief=GROOVE
                       )
billingAreaLabel.pack(fill=X)

scrollBar=Scrollbar(billingFrame,orient=VERTICAL)
scrollBar.pack(side=RIGHT,fill=Y)

textArea=Text(billingFrame,height=20,width=38,yscrollcommand=scrollBar.set)
textArea.pack()
scrollBar.config(command=textArea.yview)

billMenuFrame=LabelFrame(screen,
                         text='Bill Menu',
                         font=('Helvetica',15,'bold'),
                         fg='gold',
                         bd=8,
                         relief=GROOVE,
                         bg='#36454F'
                         )
billMenuFrame.pack(anchor='nw')

cosmeticPriceLabel=Label(billMenuFrame,
                         text='Cosmetic Price:',
                         font=('Helvetica',15,'bold'),
                         bg='#36454F',
                         fg='white'
                   )
cosmeticPriceLabel.grid(row=5,column=0,pady=6,padx=10,sticky='w')

cosmeticPriceEntry=Entry(billMenuFrame,
                        font=('Helvetica',15,'bold'),
                        width=10,
                        bd=5
                        )
cosmeticPriceEntry.grid(row=5,column=1,pady=6,padx=10)
cosmeticPriceEntry.insert(0,0.0)


cosmeticTaxLabel=Label(billMenuFrame,
                       text='Cosmetic Tax:',
                       font=('Helvetica',15,'bold'),
                       bg='#36454F',
                       fg='white'
                       )
cosmeticTaxLabel.grid(row=5,column=2,pady=6,padx=10)

cosmeticTaxEntry=Entry(billMenuFrame,
                       font=('Helvetica',15,'bold'),
                       width=10,
                       bd=5
                       )
cosmeticTaxEntry.grid(row=5,column=3,pady=6,padx=10)
cosmeticTaxEntry.insert(0,0.0)

meatPriceLabel=Label(billMenuFrame,
                     text='Cosmetic Price:',
                     font=('Helvetica',15,'bold'),
                     bg='#36454F',
                     fg='white'
                     )
meatPriceLabel.grid(row=6,
                    column=0,
                    pady=6,
                    padx=10,
                    sticky='w')

meatPriceEntry=Entry(billMenuFrame,
                        font=('Helvetica',15,'bold'),
                        width=10,
                        bd=5
                        )
meatPriceEntry.insert(0,0.0)

meatPriceEntry.grid(row=6,
                    column=1,
                    pady=6,
                    padx=10
                    )

meatTaxLabel=Label(billMenuFrame,
                   font=('Helvetica',15,'bold'),
                   text='Meat Tax:',
                   bg='#36454F',
                   fg='white'
                   )
meatTaxLabel.grid(row=6,column=2,pady=6,padx=10)

meatTaxEntry=Entry(billMenuFrame,
                   font=('Helvetica',15,'bold'),
                   width=10,
                   bd=5
                   )
meatTaxEntry.grid(row=6,column=3,pady=6,padx=10)
meatTaxEntry.insert(0,0.0)
                   
beveragesPriceLabel=Label(billMenuFrame,
                         text='Meat Price:',
                         font=('Helvetica',15,'bold'),
                         bg='#36454F',
                         fg='white'
                         )
beveragesPriceLabel.grid(row=7,column=0,pady=6,padx=10,sticky='w')

beveragesPriceEntry=Entry(billMenuFrame,
                        font=('Helvetica',15,'bold'),
                        width=10,
                        bd=5
                        )
beveragesPriceEntry.grid(row=7,column=1,pady=6,padx=10)
beveragesPriceEntry.insert(0,0.0)

beveragesTaxLabel=Label(billMenuFrame,
                        text='Beverages Tax:',
                        font=('Helvetica',15,'bold'),
                        bg='#36454F',
                        fg='white'
                        )
beveragesTaxLabel.grid(row=7,column=2,pady=6,padx=10)

beveragesTaxEntry=Entry(billMenuFrame,
                        font=('Helvetica',15,'bold'),
                        width=10,
                        bd=5
                        )
beveragesTaxEntry.grid(row=7,column=3,pady=6,padx=10)
beveragesTaxEntry.insert(0,0.0)

#buttons
#Totality of bills
totalButton=Button(billMenuFrame,
                   text='Total',
                   font=('Helvetica',16,'bold'),
                   bg='gray20',
                   fg='white',
                   width=15,
                   relief=GROOVE,
                   command=total
                   )
totalButton.grid(row=5,column=4,pady=6,padx=10)

#display bill
billButton=Button(billMenuFrame,
                  text='Bill',
                  font=('Helvetica',16,'bold'),
                  bg='gray20',
                  fg='white',
                  width=15,
                  relief=GROOVE,
                  command=get_the_bill
                  )
billButton.grid(row=5,column=5,pady=6,padx=10)

emailButton=Button(billMenuFrame,
                   text='Email',
                   font=('Helvetica',16,'bold'),
                   bg='gray20',
                   fg='white',
                   width=15,
                   relief=GROOVE
                   )
emailButton.grid(row=5,column=6,pady=6,padx=10)

printButton=Button(billMenuFrame,
                   text='Print',
                   font=('Helvetica',16,'bold'),
                   bg='gray20',
                   fg='white',
                   width=15,
                   relief=GROOVE
                   )
printButton.grid(row=6,column=4,pady=6,padx=10)

clearButton=Button(billMenuFrame,
                   text='Clear',
                   font=('Helvetica',16,'bold'),
                   bg='gray20',
                   fg='white',
                   width=15,
                   relief=GROOVE
                   )
clearButton.grid(row=6,column=5,pady=6,padx=10)

screen.mainloop()

