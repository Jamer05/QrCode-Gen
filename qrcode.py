#if you are using google collab "!pip install pyqrcode" && "!pip install pypng"
#@author Hemerson G. Ramiro Jr.

import pyqrcode 
import png 
import cowsay
from pyqrcode import QRCode 
import os

back_is_true = True
def to_url():
    s = input("Enter URL: ")
    url = pyqrcode.create(s) 

	
    url.svg("myqr.svg", scale = 8) 
    url.png('myqr.png', scale = 4) 


def information(n,a,ad,cn,gen):

          return "Name: "+n+"\nAge: "+a+"\nAddress: "+ad+ "\nContact no.: "+cn+"\nGender.: "+gen

cowsay.cow("Wala kang qrcode? Pwes eto ang life hack para sa iyo By: JamerCute")
while (back_is_true):
    print ('''>>Press 1 to create qr urls
>>Press 2 to create qr information 
    ''')
    sel = int(input("Select mode: "))
    i=0
    i+=1  
    if sel == 1:
             to_url()
    elif sel == 2:
        n,a,ad,cn,gen = input("Enter name: "),input("Enter age: "), input("Enter Address: "), input("Enter contact number: "), input("Enter gender: ")
        myQR = pyqrcode.create(information(n,a,ad,cn,gen)) 
        myQR.png(n+str(i)+'.png', scale=8)
                
			
			
         