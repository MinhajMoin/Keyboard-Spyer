name = str(input("Enter file name:"))
file=open(name, 'r')
def encrypt_number():
    sumnum = ""
    for line in file:
        ch=line
        ch=int(ch)
        if (ch == 30):
            rep = 'a'
        elif (ch == 48):
            rep = 'b'
        elif (ch == 46):
            rep = 'c'
        elif (ch ==32):
            rep = 'd'
        elif (ch == 18):
            rep = 'e'
        elif (ch == 33):
            rep = 'f'
        elif (ch == 34):
            rep = 'g'
        elif (ch == 35):
            rep = 'h'
        elif (ch == 23):
            rep = 'i'
        elif (ch == 36):
            rep = 'j'
        elif (ch == 37):
            rep = 'k'
        elif (ch == 38):
            rep = 'l'
        elif (ch == 50):
            rep = 'm'
        elif (ch == 49):
            rep = 'n'
        elif (ch == 24):
            rep = 'o'
        elif (ch == 25):
            rep = 'p'
        elif (ch == 16):
            rep = 'q'
        elif (ch == 19):
            rep = 'r'
        elif (ch == 31):
            rep = 's'
        elif (ch == 20):
            rep = 't'
        elif (ch == 22):
            rep = 'u'
        elif (ch == 47):
            rep = 'v'
        elif (ch == 17):
            rep = 'w'
        elif (ch == 45):
            rep = 'x'
        elif (ch == 21):
            rep = 'y'
        elif (ch == 44):
            rep = 'z'
        elif (ch == 57):
            rep = ' '
        elif (ch == 2):
            rep = '1'
        elif (ch == 3):
            rep = '2'
        elif (ch == 4):
            rep = '3'
        elif (ch == 5):
            rep = '4'
        elif (ch == 6):
            rep = '5'
        elif (ch == 7):
            rep = '6'
        elif (ch == 8):
            rep = '7'
        elif (ch == 9):
            rep = '8'
        elif (ch == 10):
            rep = '9'
        elif (ch == 11):
            rep = '0'
        elif (ch == 29):
            rep = '|CTRL|'
        elif (ch == 42):
            rep = '|SHIFT|'
        elif (ch == 54):
            rep = '|SHIFT|'
        elif (ch == 56):
            rep = '|ALTR|'
        elif (ch == 28):
            rep = '|ENTER| \n'
        elif (ch == 1):
            rep = '|ESC|'
        elif (ch == 15):
            rep = '|TAB|'
        elif (ch == 14):
            rep = '|BACKSPACE|'
        else:
            rep= 'UK'
        sumnum += rep
    print(sumnum)


print(encrypt_number())

input()


