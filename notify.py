from smtplib import SMTP
from json import load

def get_info(jsonfile):
    """
    Returns a tuple containing logon, recipient, and SMTP info.
    """
    d = load(open("NotifyModule/" + jsonfile))
    ACCOUNT = d["ACCOUNT"]
    PASSWORD = d["PASSWORD"]
    GATEWAY = d["GATEWAY"]
    RECIPIENT = d["RECIPIENT"]
    SMTP_SERVER = d["SMTP_SERVER"]
    PORT = d["PORT"]
    return (ACCOUNT, PASSWORD, GATEWAY, RECIPIENT, SMTP_SERVER, PORT)

def notify(func):
    """
    A decorator function that sends a text message notification
    following a completed task. 
    """
    process = func.__name__
    def wrapper(*args):
        ans = func(*args)
        ACCOUNT, PASSWORD, GATEWAY, RECIPIENT, SMTP_SERVER, PORT = get_info('info.json')
        REC_ADDR = RECIPIENT + "@" + GATEWAY
        msgln1 = "Finished running '{}({})' on your machine\n".format(process, *args)
        msgln2 = "Found answer {}.".format(ans)
        server = SMTP(SMTP_SERVER, PORT)
        server.starttls()   
        server.login(ACCOUNT, PASSWORD)
        server.sendmail(ACCOUNT, REC_ADDR, msgln1 + msgln2)
        server.quit()
    return wrapper
