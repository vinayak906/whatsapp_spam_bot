from pyautogui import press,sleep,hotkey,confirm,prompt,typewrite
FAILSAFE = False
sleep(1)

con=confirm(text='Please make sure whatsapp is installed in your system and login your whatsapp account ',title="Confirmation promt",buttons=['Continue','Quit'])
if con=='Continue':
    press("win")
    sleep(.2)
    typewrite("whatsapp",interval=0.2)
    press("enter")
    sleep(4)
    hotkey('win','up')
    contact=prompt(text='Please make sure whatsapp account is login and wondow is loaded\nEnter the contect name for spam',title='Enter the contect name for spam :- ')
    sleep(2)
    if contact!=None:
        press("tab")
        typewrite(contact)
        press("enter")
        sleep(2)
        message=prompt(text="What massage you want to spam", title="Spam Massage input box")
        if message!=None:
            n=prompt(text="how many messages you want to spam", title="Spam count input box",default=100)
            for i in range (0,int(n)):
                typewrite(message,interval=0.02)
                press('Enter')
        else:
            hotkey('alt','f4')
            quit
    else:
        hotkey('alt','f4')
        quit
else:
    quit