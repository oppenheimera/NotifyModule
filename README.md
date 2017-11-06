# Notify

This is a minimal module that supports simple task completion notifications in Python, without any dependencies beyond the standard library, or external API calls.

Setup is really straigtforward, and the program is simple enough that any modifications should be easy to implement.

## Usage
Once set up, notify is used as a decorator function.
```python
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
## Setup
To get this set up, clone the repository into whatever directory you'll be working out of, so that the directory structure looks like this:
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
Then edit `info.json` so that it contains information that is relevant to your accounts. 
And finally, make sure that the email account that you've linked allows access to outside applications. In Gmail, change your preferences so that you allow "less secure" apps.
