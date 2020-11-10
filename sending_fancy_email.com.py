
    def fancy_mime_card_email()
    """
    
    
    
    Sending Fancy Emails
    
    Python’s built-in email package allows you to structure more fancy emails, which can then be transferred with smtplib as you have done already.
    Below, you’ll learn how use the email package to send emails with HTML content and attachments.
    Including HTML Content
    
    If you want to format the text in your email (bold,
     italics, and so on), or if you want to add any images, hyperlinks, or responsive content, then HTML comes in very handy. Today’s most common type of email is the MIME (Multipurpose Internet Mail Extensions) Multipart email, combining HTML and plain-text.
     MIME messages are handled by Python’s email.mime module. For a detailed description, check the documentation.
    
    As not all email clients display HTML content by default, and some people choose only to receive plain-text emails for security reasons, it is important to include a plain-text alternative for HTML messages. As the email client will render the last multipart attachment first, make sure to add the HTML message after the plain-text version.
    
    In the example below, our MIMEText() objects will contain the HTML and plain-text versions of our message, and the MIMEMultipart("alternative") instance combines these into a single message with two alternative rendering optio
    """


    #link to MIMETEXT:https://docs.python.org/3/library/email.mime.html


    import  smtplib ,ssl,getpass
    from email.mime.text import MIMEText
    from email.mime.multipart import  MIMEMultipart
    sender_email = "victornkuna37@gmail.com"
    receriver_email = "victor.nkuna@yahoo.com"

    password = getpass("Type your password and press enter:")

    message = MIMEMultipart("alternative")

    message["Subject"] = "multipart test"

    message["From"] = sender_email
    message["To"] = receriver_email

    #create the plain text and HTML versionn of my message

    text = """\
    
    Hi,
    How are you?
    Real Python has many great tutorials
    
    www.realpython.com"""

    html = """\
    
    
    
    <html>
      <body>
        <p>Hi,<br>
           How are you?<br>
           <a href="http://www.realpython.com">Real Python</a>
           has many great tutorials.
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email,receriver_email, message.as_string()
        )
fancy_mime_card_email()


def emai_with_attachment():

    """


    n this example, you first define the plain-text and HTML message as string literals, and then store them as plain/html MIMEText objects. These can then be added in this order to the MIMEMultipart("alternative") message and sent through your secure connection with the email server. Remember to add the HTML message after the plain-text alternative, as email clients will try to render the last subpart first.
Adding Attachments Using the email Package

In order to send binary files to an email server that is designed to work with textual data, they need to be encoded before transport. This is most commonly done using base64, which encodes binary data into printable ASCII characters.

The code example below shows how to send an email with a PDF file as an attachment:
    :return:
    """
    import email, smtplib, ssl

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent from Python"
    sender_email = "my@gmail.com"
    receiver_email = "your@gmail.com"
    password = input("Type your password and press enter:")

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "document.pdf"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
emai_with_attachment()




def peronalizzed_email_service_of_vintech():

    """
    e MIMEultipart() message accepts parameters in the form of RFC5233-style key/value pairs, which are stored in a dictionary and passed to the .add_header method of the Message base class.

Check out the documentation for Python’s email.mime module to learn more about using MIME classes.
Remove ads
Sending Multiple Personalized Emails

Imagine you want to send emails to members of your organization, to remind them to pay their contribution fees. Or maybe you want to send students in your class personalized emails with the grades for their recent assignment. These tasks are a breeze in Python.
Make a CSV File With Relevant Personal Info

An easy starting point for sending multiple personalized emails is to create a CSV (comma-separated values) file that contains all the required personal information. (Make sure not to share other people’s private information without their consent.) A CSV file can be thought of as a simple table, where the first line often contains the column headers.

Below are the contents of the file contacts_file.csv, which I saved in the same folder as my Python code. It contains the names, addresses, and grades for a set of fictional people. I used my+modifier@gmail.com constructions to make sure all emails end up in my own inbox, which in this example is my@gmail.com:
    :return:
    """
    """
    In the example above, using with open(filename) as file:makes sure that your file closes at the end of the code block. csv.reader() makes it easy to read a CSV file line by line and extract its values. The next(reader) line skips the header row, so that the following line for name, email, grade in reader: splits subsequent rows at each comma, and stores the resulting values in the strings name, email and grade for the current contact.

If the values in your CSV file contain whitespaces on either or both sides, you can remove them using the .strip() method.
Personalized Content

You can put personalized content in a message by using str.format() to fill in curly-bracket placeholders. For example, "hi {name}, you {result} your assignment".format(name="John", result="passed") will give you "hi John, you passed your assignment".

As of Python 3.6, string formatting can be done more elegantly using f-strings, but these require the placeholders to be defined before the f-string itself. In order to define the email message at the beginning of the script, and fill in placeholders for each contact when looping over the CSV file, the older .format() method is used.

With this in mind, you can set up a general message body, with placeholders that can be tailored to individuals.
Code Example

The following code example lets you send personalized emails to multiple contacts. It loops over a CSV file with name,email,grade for each contact, as in the example above.

The general message is defined in the beginning of the script, and for each contact in the CSV file its {name} and {grade} placeholders are filled in, and a personalized email is sent out through a secure connection with the Gmail server, as you saw before:
    
    When creating a CSV file, make sure to separate your values by a comma, without any surrounding whitespaces.
Loop Over Rows to Send Multiple Emails

The code example below shows you how to open a CSV file and loop over its lines of content (skipping the header row). To make sure that the code works correctly before you send emails to all your contacts, I’ve printed Sending email to ... for each contact, which we can later replace with functionality that actually sends out emails:
    """

    import csv

    with open("contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            print(f"Sending email to {name}")
            # Send email here
            import csv, smtplib, ssl

            message = """Subject: Your grade

            Hi {name}, your grade is {grade}"""
            from_address = "my@gmail.com"
            password = input("Type your password and press enter: ")

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(from_address, password)
                with open("contacts_file.csv") as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip header row
                    for name, email, grade in reader:
                        server.sendmail(
                            from_address,
                            email,
                            message.format(name=name, grade=grade),
                        )
peronalizzed_email_service_of_vintech()



"""


Yagmail

There are multiple libraries designed to make sending emails easier, such as Envelopes, Flanker and Yagmail. Yagmail is designed to work specifically with Gmail, and it greatly simplifies the process of sending emails through a friendly API, as you can see in the code example below:
"""



def yagmail():
    import yagmail

    receiver = "victor.nkuna@yahoo.com"
    body = "Hello there from Yagmail"
    filename = "document.pdf"

    yag = yagmail.SMTP("victor.nkuna37@gmail.com")
    yag.send(
        to=receiver,
        subject="Yagmail test with attachment",
        contents=body,
        attachments=filename,
    )
yagmail()




"""ansactional Email Services

If you plan to send a large volume of emails, want to see email statistics, and want to ensure reliable delivery, it may be worth looking into transactional email services. Although all of the following services have paid plans for sending large volumes of emails, they also come with a free plan so you can try them out. Some of these free plans are valid indefinitely and may be sufficient for your email needs.

Below is an overview of the free plans for some of the major transactional email services. Clicking on the provider name will take you to the pricing section of their website.
Provider 	Free plan
Sendgrid 	40,000 emails for your first 30 days, then 100/day
Sendinblue 	300 emails/day
Mailgun 	First 10,000 emails free
Mailjet 	200 emails/day
Amazon SES 	62,000 emails/month

You can run a Google search to see which provider best fits your needs, or just try out a few of the free plans to see which API you like working with most.
Sendgrid Code Example

Here’s a code example for sending emails with Sendgrid to give you a flavor of how to use a transactional email service with Python:"""


def sendgrid():
    """




To run this code, you must first:

    Sign up for a (free) Sendgrid account
    Request an API key for user validation
    Add your API key by typing setx SENDGRID_API_KEY "YOUR_API_KEY" in Command Prompt (to store this API key permanently) or set SENDGRID_API_KEY YOUR_API_KEY to store it only for the current client session

More information on how to set up Sendgrid for Mac and Windows can be found in the repository’s README on Github.
Conclusion

You can now start a secure SMTP connection and send multiple personalized emails to the people in your contacts list!

You’ve learned how to send an HTML email with a plain-text alternative and attach files to your emails. The Yagmail package simplifies all these tasks when you’re using a Gmail account. If you plan to send large volumes of email, it is worth looking into transactional email services.

Enjoy sending emails with Python, and remember: no spam please!

    :return:
    """

import os
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail

sg = sendgrid.SendGridAPIClient(
    apikey=os.environ.get("SENDGRID_API_KEY")
)
from_email = Email("my@gmail.com")
to_email = Email("your@gmail.com")
subject = "A test email from Sendgrid"
content = Content(
    "text/plain", "Here's a test email sent through Python"
)
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())

# The statements below can be included for debugging purposes
print(response.status_code)
print(response.body)
print(response.headers)

sendgrid()