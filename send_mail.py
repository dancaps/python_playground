import smtplib, socket, sys, getpass

def main():
    usr_smtp_server = 'smtp.gmail.com'
    #usr_smtp_port = 587
    usr_mail_user = 'danny.caperton@gmail.com'
    usr_mail_password = 'Xo2jq99Z'
    usr_to = 'danny.caperton@gmail.com'
    usr_from = 'danny.caperton@gmail.com'
    usr_msg = 'Test Message'
    usr_subject = 'Test Email from my Python code'

    #makes the connection
    try:
        mail = smtplib.SMTP(usr_smtp_server, 587)
        #mail.ehlo()
        mail.starttls()
        #mail.ehlo()
        print 'Connection to ' + usr_smtp_server + ' was sucessful.'
        #print 'Connected to ' + usr_smtp_server + ' on port ' + usr_smtp_port + '.\n'

        #logs in as the user
        try:
            mail.login(usr_mail_user, usr_mail_password)
        except smtplib.SMTPException:
            print 'Authentication failed \n'
            mail.close()
            raw_input('Press ENTER to continue...')
            sys.exit(1)

    except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
        print 'Connection to mail server failed.'
        print e
        raw_input('Press ENTER to continue...')
        sys.exit(1)

    header = 'To: ' + usr_to + '\n' + 'From: ' + usr_from + '\n' + 'Subject: ' + usr_subject + '\n'
    print header
    msg = header + '\n' + usr_msg + '\n'

    #send the email
    try:
        mail.sendmail(usr_from, usr_to, msg)
    except smtplib.SMTPException:
        print 'The email could not be sent.'
        raw_input('Press ENTER to continue...')
        mail.close()
        sys.exit(1)

    print 'The email was sent successfully! \n'
    mail.close()
    raw_input('Press ENTER to continue...')
    sys.exit(1)

main()