import smtplib
from pwinput import pwinput
import random  

otp=''.join([str(random.randint(0,9)) for i in range(6)])

senderemail=input("\nEnter the sender's email\n")
senderemailpassword=pwinput("\nEnter the sender's email password\n",'*')
recieveremail=input("Enter the reciever's email\n")
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(senderemail,senderemailpassword)
server.sendmail(senderemail,recieveremail,"Hello your otp is " + otp)
server.quit()
print("mail sent")

for i in range(3):
    otpverify=int(input("enter the otp"))
    if otpverify==int(otp):
        print("otp verified successfully")
        break
    else:
        print("otp verification denied")
 