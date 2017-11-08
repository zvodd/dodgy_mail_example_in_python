import emails
import time
from pprint import pprint


def main():
    num = int(hash(time.gmtime()))
    message = emails.html(html="<p>Hi!<br>Here is your receipt... No. %r" % num,
                          subject="Your receipt No.%r" % num,
                          mail_from=('Example Sender', 'sender@example.com'))
    r = message.send(to='test@localhost', smtp={
                     'host': 'localhost', 'timeout': 5})
    pprint(r)


if __name__ == '__main__':
    main()
