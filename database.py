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
    self.dbChanged = False

  def readDatabase(self, filepath):
    print "Reading database..."
    print "Read ", len(self.entries), " entries"

  def writeDatabase(self, filepath):
    print "Writing to database"

  def addEntry(self):
    print "New Entry..."
    name = raw_input("Entry name : ")
    if not name:
      print "name cant be blank"
      return
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
    self.dbChanged = True

    copyToClipboard = utils.choice("Copy password to clipboard? (Y/n)")
    print "\n"

    return True;

  def editEntry(self, name):
    if not self.entries.has_key(name):
      print 'No entry with name ', name
      return

    print "Edit Entry ", name
    print "Press enter to no edit field"

    username = raw_input('Username : ')
    if username == "":
      username = self.entries[name].username

    password = raw_input('Password : ')
    if password == "":
        genPass = utils.choice("Genrate password? (Y/n)")
        if genPass == False:
          password = self.entries[name].password
        else:
          password = passGen.getRandomPass()
          print "Password : ", password

    URL = raw_input('URL : ')
    if URL == "":
      URL = self.entries[name].URL

    tag = "internet"
    change = entry.Entry(name, username, password,tag, URL)

    change.display(True)
    modify = utils.choice("complete edit ? (Y/n)")
    if modify:
      self.entries[name].edit(change)
      print "Editted entry ", name
      self.dbChanged = True;


  def listEntries(self):
    print "Entries..."
    for entryName in self.entries.keys():
      print " -> ", entryName
    print "\n"

  def openEntry(self, name):
    if self.entries.has_key(name):
      self.entries[name].display()
    else:
      print "No entry with the name ", name

  def delEntry(self, name):
    if self.entries.has_key(name):
      print "Deleting Entry ", name ,"..."
      del self.entries[name]
      seld.dbChanged = True;
    else:
      print "Cant find entry ", name , "!!"

def test():
  db = Database()
  db.addEntry()
  db.editEntry("fb")
  db.delEntry("fb")


if __name__ == "__main__":
  test()
