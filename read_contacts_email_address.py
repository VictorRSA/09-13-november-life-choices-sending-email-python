def get_contacts(filename):
    names =[]  #we define a list of name sof individuals we going to send emails to
    emails=[] #a list of email addresses of the indivduals
    with  open(filename,mode='r',encoding='utf-8') as contacts_address_file:
        for a_contact_email_address in contacts_address_file:
            names.append(a_contact_email_address.split()[0])
            emails.append(a_contact_email_address.split()[1])
    return names ,emails


