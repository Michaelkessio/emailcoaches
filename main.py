import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import secrets
import time
import random

def read_template(filename):

    # Returns a Template object comprising the contents of the 
    # file specified by filename.

    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main(filename='contacts.txt'):
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(secrets.MY_ADDRESS, secrets.PASSWORD)

    # open contacts file
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        # read single lines in the contactd file
        for line in contacts_file.readlines():
            # split the line into two
            line=line.split()
            emails=line[-1]
            # now remove email so that you are left with names only
            line=line[:-1]
            names=[]
            for name in line:
                names.append(name)
            random_number= random.randrange(1,3)
            # generate a random name between the two posted
            random_name=names[random_number-1]
            # remove trailing whitespaces
            personal_names=random_name.strip().capitalize()
            # also for every line send an email
            print(r'Sending email to:{} with address:{}'.format(personal_names,emails))
        
            send_mail(s,personal_names,emails,secrets.MY_NAME,secrets.SUBJECT)
            time.sleep(3)
        s.quit()
        contacts_file.close()
                

def send_mail(s,name,email,personalname,subject):

    msg = MIMEMultipart()       
    # create a message
    message_template = read_template('message.txt')
    # add the name of the person to be sent the email
    message = message_template.substitute(Name_of_coach=name,My_Name= secrets.MY_NAME)
    

    # Prints out the message body for our sake

    # setup the parameters of the message
    msg['From']= secrets.MY_NAME
    msg['To']=email
    msg['Subject']=subject
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # Attach the pdf to the msg going by e-mail
    path_to_pdf='scorereport.pdf'
    with open(path_to_pdf, "rb") as f:
        #attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
        attach = MIMEApplication(f.read(),_subtype="pdf")
    attach.add_header('Content-Disposition','attachment',filename=str(path_to_pdf))
    msg.attach(attach)
    # send the message via the server set up earlier.
    try:
        s.send_message(msg)
        if True:
            print('email sent successfully ✓✓')       
    except:
        print(r'Failed sending email to:{} with address:{}'.format(name,email))
    del msg

if __name__=='__main__':
    main()


