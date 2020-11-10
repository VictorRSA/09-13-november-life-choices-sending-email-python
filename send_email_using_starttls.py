"""
nstead of using .SMTP_SSL() to create a connection that is secure from the outset,
 we can create an unsecured SMTP connection and encrypt it using .starttls().

To do this, create an instance of smtplib.SMTP,
which encapsulates an SMTP connection and allows you access to its methods. I
 recommend defining your SMTP server and port at the beginning of your script to configure them easily.

The code snippet below uses the construction server = SMTP(),
rather than the format with SMTP() as server: which we used in the previous example.
To make sure that your code doesn’t crash when something goes wrong,
 put your main code in a try block, and let an except block print any error messages to stdout:
"""


import  smtplib ,ssl,getpass
sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

# Send email here

smtp_server = "smtp.gmail.com"

port = 587 #for starttls

sender_email = "victornkuna37@gmail.com"

password = getpass(prompt ="Type your password and press enter: ")

#Create a secure ssl_context

context = ssl.create_default_context()

#try  to login  to a server(i.e. connect to it) and send email(the server is uses STMP
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() #can be ommited
    server.starttls(context=context) #secure the connection
    server.login(sender_email,password)
    #TODO: SEND an email here
except Exception as e:
    print(e)
    print("the error messages to standard output stdout")


finally:
    server.quit()

server_email = "victor.nkuna37@gmail.com"
receiver_email = "victor.nkuna@yahoo.com"
message = """\
Subject: Hi there

This message is sent from Python using the Python Interpretor


"""
"""
To identify yourself to the server, .helo() (SMTP) or .ehlo() (ESMTP) should be called after creating an .SMTP() object, 
and again after .starttls(). 
This function is implicitly called by .starttls() and .sendmail() if needed, s
o unless you want to check the SMTP service extensions of the server, 
it is not necessary to use .helo() or .ehlo() explicitly.

<br />

Sending Your Plain-text Email

After you initiated a secure SMTP connection using either of the above methods, 
you can send your email using .sendmail(),
 which pretty much does what it says on the tin:
"""

server.sendmail(sender_email,receiver_email,message)

#Send email here

"""
#The message string starts with Subject: Hi  tthere"followed by two newlines(\n).
#This ensures that Hi there shows up as the subject of the email,and the text following
#the newlines will be treated as the message body
"""

#The following exapmle code below send a plain-text email using SMTP_SSL()

def email_function():
    # import smtplib ,ssl
    port  = 465
    smpt_server = "smtp.gmail.com"
    sender_email = "victornkuna37@gmail.com"
    receiver_email = "victor.nkuna@yahoo.com"
    password = getpass("Type your password and press enter: ")
    message = """\
    Subject: Hi there
    
    This message is send using python
    """

    port = 465#for SSL
    smpt_server = "smtp.gmail.com"
    sender_email = "victor.nkuna@gmail.com" # Enter the cender's email adrss
    receiver_email = "victor.nkuna@yahoo.com" #enter the receiver addrsas
    context  =ssl.create_default_context()
    with smtplib.SMTP_SSL(smpt_server,port,context=context) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,message)

    email_function()



















def send_email():

    import smtplib ,ssl
    port = 587 # for starttls

    smtp_server = "smtp.gmail.com"
    sender_email = "victornkuna37@gmail.com"
    receiver_email = "victor.nkuna@yahooo.com"

    password = getpass("TYpe your password and press <enter>:")

    message = """\
    Subject: Hi there
    
    This message is send from python.
    
    """
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server,port) as server:
    server.ehlo() # it can be ommited
    server.starttls(context=context)
    server.ehlo() #it can be ommited
    server.login(sender_email,password,message)






