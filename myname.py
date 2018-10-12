import smtplib
import getpass
myemail="kartikswamy2000@gmail.com"
recemail="kartikswamy2000@gmail.com"
password=getpass.getpass()
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(myemail,password)
message="WHTAT'S GOING MAN ALL GOINNG WELL"
s.sendmail("kartikswamy2000@gmail.com","kartikswamy2000@gmail.com",message)
s.quit()
