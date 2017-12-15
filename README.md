# Notify

Notify is a lean utility providing task completion notifications in Python. It was designed to be be free of dependencies beyond the standard library, as well as interacting with expensive APIs.

Setup is straigtforward, and is outlined under *Setup*. Notify was intended to be simple and understandable enough that modifications could be easily implemented––although the batteries-included version should suit most needs.

## Usage
Once set up, notify is used as a decorator function.
```python
from NotifyModule.notify import notify

@notify
def inefficient_code(n=28433):
  big_num = n * efficient_exponenentiation(2, 7830457) + 1
  return str(big_num)[-10:]
```
After the code runs, a text message will be sent to you. In this case, the default message would read: 
```
Finished running 'inefficient_code(28433)' on your machine.
Found answer: 8739992577.
```
Notify works with an arbitrary number of arguments:
```python
>>> semantically_valid_orderings(["call", "me", "ishmael"])
``` 
## Setup
To set up Notify, clone this repository into the directory containing the project you wish to add it to. Ultimately, your directory should be structured as such:
```
project
|   README.md
|   yourcode.py 
|
|___NotifyModule
    | __init__.py
    | notify.py
    | info.json
    | README.md
```
After your directory has been made to resemble the one above, edit `info.json` so that it contains information that is relevant to your accounts. This includes adding your mobile number, some carrier information, and also some email information. WARNING: since this file contains information sensitive to your accounts, it is advised that you treat it very carefully!
Finally, make sure that the email account that you've linked allows access to outside applications. In Gmail, you must change your preferences to allow "less secure" applications to interact with your account.
