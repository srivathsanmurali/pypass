"""
    password entry and database controls
"""

from datetime import datetime

class Entry(object):
    """Entry - class that contains the data pass word entry
    Attributes
        name: A name for the entry that is easy to remember the entry
        username: username for the website
        password: password for the website
        URL: the address of the website
        doc: date of change - used to remind users of need to change password
    """
    def __init__(self, name, username, password, URL):
        self.name = name
        self.username = username
        self.password = password
        self.URL = URL
        self.doc = datetime.now()

    def display (self, showPassword = False):
        print self.name
        print "Username = ", self.username
        if showPassword:
            print "Password = ", self.password
        else:
            print "Password = ", "*" * len(self.password)
        print "URL = ", self.URL
        print "Date of change = ", self.doc
        print "\n"

    def edit(self, change):
        self.username = change.username
        self.password = change.password
        self.URL = change.URL
        self.doc = datetime.now()


def test():
    pass1 = Entry("facebook", "srivathsan", "asjhdkajhds", "www.facebook.com")
    pass1.display()

    pass1.display(True)
    change = Entry("facebook", "sri", "akdshkajd", "sfd")
    pass1.edit(change)
    pass1.display(True)

if __name__ == "__main__":
    test()
