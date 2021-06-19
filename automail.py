import yagmail
import os

yag_smtp_connection = yagmail.SMTP( user="fathimaalmas53@gmail.com", password="applicationmail@53", host='smtp.gmail.com')
subject = 'Attendance'
filename = "Attendance"+os.sep+"Attendance_2020-02-09_00-20-30"  # attach the file
receiver_mail = ['navaz16kk@gmail.com']
yag_smtp_connection.send(receiver_mail, subject,filename)
print("mail sent successfully")