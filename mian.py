import webbrowser
import phonenumbers
from phonenumbers import geocoder
from tkinter import *


def main():
    number = phonenumbers.parse(display.get())
    # Location
    number_location = geocoder.description_for_number(number, "en")
    countryLab.config(text="Location: "+number_location)

    # Service Provider
    from phonenumbers import carrier
    service_provider = carrier.name_for_number(number, "en")
    ServiceLab.config(text="Service Provider: "+service_provider)

    # Location open
    webbrowser.open("https://www.google.co.in/maps/place/"+number_location)


# Frontend##################################
window = Tk()
window.title('File Explorer')
window.geometry("455x350+1000+100")
window.config(bg="white")

head = Label(window, text="Enter Phone Number", justify="center", width=26, font=("areal", 20), bg="white")
head.grid(row=0)

display = Entry(window, justify="right", text="253", bd=29, bg="white", width=26, font=("areal", 20))
display.grid(row=1)

find = Button(window, bd=10, text="find", width=26, height=2, command=main)
find.grid(column=0, row=3, pady="30")

countryLab = Label(window, justify="center", width=26, font=("areal", 20), bg="white")
countryLab.grid(row=4)

ServiceLab = Label(window, justify="center", width=26, font=("areal", 20), bg="white")
ServiceLab.grid(row=5)

window.mainloop()
