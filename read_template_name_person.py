from string import Template
"""
To send an email,Victor I need to make use of SMTP Simple Mail Transer Protocol.
just like an HTTP Protocol it send bytes of digital electrical signal that turns into a an encoded messagge
there communication can be acheived like talkin glanguage,to share  ideas,reports ,technologgy even throughout
 
 history civilization strives -attempt to interachange along-economical,social,cultural,political muatuality-in interconnected world.
 
"""

import  smtplib ,ssl ,getpass #it system starndard library

#create a secure SSL context
port = 565 #for Secure Sockets  Transport layer
context = ssl.create_default_context()

#Set up the SMTP Server

s= smtplib.SMTP(host='victor.nkuna@yahoo.com',port =465 )
inpt_pswd = getpass("Please enter your server-SMTP_password")
with smtplib.SMTP_SSL("smtp.gmail.com",port=465,context=context) as server:
    server.login("victornkuna37@gmail.com",inpt_pswd)
    #TODO: Send email here
"""
Using with smtplib.SMTP_SSL() as server: makes sure that the connection is automatically closed at the end of the indented code block. 
If port is zero, or not specified, .SMTP_SSL() will use the standard port for SMTP over SSL (port 465).

It’s not safe practice to store your email password in your code, especially if you intend to share it with others. 
Instead, use input() to let the user type in their password when running the script, as in the example above. 
If you don’t want your password to show on your screen when you type it, 
you can import the getpass module and use .getpass() instead for blind input of your password
"""


