import smtplib

Name = "email"

def send_email(user, pwd, recipient, subject, body):
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        return 'successfully sent the mail'
    except:
        return "failed to send mail"

async def process(client, msg, args, extra):
    if len(args) == 0:
        client.edit_message(msg, "No email to send")
    else:
        config = extra["config"]["email"]
        resp = send_email(config["fEmail"], config["fPwd"], args[0], "Sent from a selfbot", " ".join(args[1:]))
        await client.edit_message(msg, "Response: {}".format(resp))