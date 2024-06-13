
'''f = open('ExampleFile.txt','w')
f.write("bibek")
print(f.read())'''

#Reading data from file

'''with open('ExampleFile.txt','w') as file:
    file.write('hloo..how are you')
    file.write(' bibek')
    #print(file.read())
with open('ExampleFile.txt','r') as file:
    print(file.read())'''

import csv

with open('Example.csv','w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name','Age','City'])
    writer.writerow(['Alice','30','Newyork'])
    writer.writerow(['Bob','25','Los Angels'])