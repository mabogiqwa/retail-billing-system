from tkinter import *

def total():
    #Variables related to totaling the cosmetic products
    soapPrice=int(bathSoapEntry.get())*19
    cleanserPrice=int(cleanserEntry.get())*330
    colognePrice=int(cologneEntry.get())*900
    bodyLotionPrice=int(bodyLotionEntry.get())*100
    toothPastePrice=int(toothPasteEntry.get())*67

    totalCosmeticPrice= soapPrice+cleanserPrice+colognePrice+bodyLotionPrice+toothPastePrice
    cosmeticPriceEntry.insert(0,f'R{totalCosmeticPrice}')

    #Variables related to totaling the different meats
    freshMeatPrice=int(freshMeatEntry.get())*80
    processedMeatPrice=int(processedMeatEntry.get())*75
    freshSeaFoodPrice=int(freshSeaFoodEntry.get())*120
    frozenSeaFoodPrice=int(frozenSeaFoodEntry.get())*105
    specialityMeatPrice=int(specialityMeatsEntry.get())*115
    smokedMeatPrice=int(smokedMeatsEntry.get())*55

    totalMeatPrice= freshMeatPrice+processedMeatPrice+freshSeaFoodPrice+frozenSeaFoodPrice+specialityMeatPrice+smokedMeatPrice
    meatPriceEntry.insert(0,f'R{totalMeatPrice}')
