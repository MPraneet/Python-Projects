#Use pip install pywhatkit in terminal.To automate messages to be sent on whatsapp.
import pywhatkit
a = int(input("Enter timing in Hours:"))
b = int(input("Enter timing in Minutes:"))
pywhatkit.sendwhatmsg("+919890261747","This is an Automated Whatsapp Message!",a,b)
