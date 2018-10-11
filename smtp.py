import smtplib
server=smtplib.SMTP('smtp.gmail.com')
server.starttls()
server.login("melumaria2000@gmail.com","melumaria")
msg = "Hello!"
server.sendmail("melumaria2000@gmail.com","lekhana016@gmail.com",msg)
print('msg sent')
server.quit()