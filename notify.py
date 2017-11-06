from smtplib import SMTP
from json import load

def get_info(jsonfile):
    """
    Returns a tuple containing logon, recipient, and SMTP info. 
    Obviously depends on the existence of the appropriate json file
    at the appropriate location. Don't make this function angry.
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
    following the completion of a task.

    One might use it like this:
    @notify
    def inefficient_code(n=28433):
      big_num = n * efficient_exponenentiation(2, 7830457) + 1
      return str(big_num)[-10:]
    In which case, a text message might appear, notifying you something like: 
    "Finished running inefficient_code(28433) on your machine.
    Found answer: 8739992577."
    Yay.
    """
    process = func.__name__
    def wrapper(*args):
        ans = func(*args)
        ACCOUNT, PASSWORD, GATEWAY, RECIPIENT, SMTP_SERVER, PORT = get_info('info.json')
        REC_ADDR = RECIPIENT + "@" + GATEWAY
        msgln1 = "Finished running '{}({})' on your machine.\n".format(process, *args)
        msgln2 = "Found answer: {}.".format(ans)
        server = SMTP(SMTP_SERVER, PORT)
        server.starttls()   
        server.login(ACCOUNT, PASSWORD)
        server.sendmail(ACCOUNT, REC_ADDR, msgln1 + msgln2)
        server.quit()
    return wrapper
