import time
import smtplib


def create_email_content(payload):
    """
    Functrion creating email content
    """
    return f"""Hi {payload['name']},
               you have just created new account using,
               {payload['email']} email,
               and {payload['user_name']} username"""

def background_task(task):
    """ 
    Function sends an email and simulates delay
    """
    print("Task running")

    content = create_email_content(task['user'])
    with smtplib.SMTP("smtp.gmail.com", 587) as mail:
        mail.ehlo()
        mail.starttls()
        mail.login('perica.test22@gmail.com', 'Test_account1232')
        mail.sendmail('perica.test22@gmail.com', 'pprokic22@gmail.com', content)

    delay = 2
    print(f"Simulating a {delay} second delay")
    time.sleep(delay)

    print("Task complete")
