from inbox import Inbox
from tinydb import TinyDB
import time

#
# Pretty sure this only runs in Python 2
#

db = TinyDB('./db.json')
inbox = Inbox()


@inbox.collate
def handle(to, sender, subject, body):
    # print("Handling")
    unique = hash(time.gmtime())
    db.insert(dict(id=unique, to=to, sender=sender, subject=subject, body=body))


# Bind directly.
inbox.serve(address='0.0.0.0', port=25)
