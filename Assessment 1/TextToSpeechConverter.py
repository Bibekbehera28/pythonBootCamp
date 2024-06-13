'''
to install pyttsx3
run command : pip install pyttsx3

'''


import pyttsx3

obj = pyttsx3.init()
while True :
    text = input('Enter text you want to convert into speech : ')
    obj.say(text)
    obj.runAndWait()
    text = input('Do you continue (y/n) : ')
    if text == 'n' :
        break
print('Thank you !')

# import pyttsx3
# obj =  pyttsx3.init()
# text= input()
# obj.say(text)
# obj.runAndWait()