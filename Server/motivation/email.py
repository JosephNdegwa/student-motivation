<<<<<<< HEAD
# Input emails information here
=======
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string




def send_welcome_email(name,receiver):
    # subject and sender
    subject = 'Welcome to the Stud Motive Family'
    sender = 'add your email here'

    #pass context vairables
    text_content = render_to_string('email/studentemail.txt',{"name": name})
    html_content = render_to_string('email/studentemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
>>>>>>> 70ebb605778868e17a54b7e109a990b615f3d6b4
