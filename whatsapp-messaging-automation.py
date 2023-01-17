import pywhatkit
import time

contacts = ["+22244444444","+22244444444"]
names = ["Aychouch", "Khalto"]

if time.strftime('%A'):  #if day is Sunday
    i = 0
    for contact, name in zip(contacts, names) : 
        i += 1 
        if i <len(contacts):
            pywhatkit.sendwhatmsg(contact, "{} ch7alek ye wenibik twa7achtek!".format(name), 12, i, 10)  # deliver message after 10s -> 12:01:10
        else: 
            pywhatkit.sendwhatmsg(contact, "{} ch7alek ye wenibik twa7achtek!".format(name), 12, i+1, 10, True, 5)  # True: close whatsapp browser after 5s
        
    
    

    
