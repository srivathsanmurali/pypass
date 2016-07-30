import entry
import passGen
import utils

class Database(object):
  """ Database - contains the various entries for pyPass
      manages the encrption and file access

  Attributes:
      entries: list of entries that store user data (better with dict)
      filepath: filepath for database
  """
  def __init__(self):
    print "Database"
    #self.filepath = filepath
    #self.entries = readDatabase(self.filepath);
    self.entries = {}

  def readDatabase(self, filepath):
    print "Reading database..."
    print "Read ", len(self.entries), " entries"

  def writeDatabase(self, filepath):
    print "Writing to database"

  def addEntry(self):
    print "New Entry..."
    name = raw_input("Entry name : ")
    if self.entries.has_key(name):
      print "An entry with the name ", name ," exists already"
      return False

    username = raw_input("Username : ")
    genPass = utils.choice("Genrate password? (Y/n)")
    if genPass == False:
      password = raw_input("Password : ")
    else:
      password = passGen.getRandomPass()
      print "Password : ", password
    URL = raw_input("URL : ")
    newEntry = entry.Entry(name, username, password, "internet", URL)
    self.entries[name]= newEntry
    copyToClipboard = utils.choice("Copy password to clipboard? (Y/n)")
    return True;

  def listEntries(self):
    print "Entries..."
    for entryName in self.entries:
      print " -> ", entryName

  def openEntry(self, name):
    if self.entries.has_key(name):
      self.entries[name].display()
    else:
      print "No entry with the name ", name

  def delEntry(self):
    print "Deleting Entry ", name ,"..."
    del self.entries[name]

def test():
  db = Database()
  db.addEntry()
  db.addEntry()
  db.listEntries()
  db.openEntry("fb")


if __name__ == "__main__":
  test()
