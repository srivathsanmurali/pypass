import entry
import passGen
import utils
import security

import yaml
import errno

class Database(object):
  """ Database - contains the various entries for pyPass
      manages the encrption and file access

  Attributes:
      entries: list of entries that store user data (better with dict)
      filepath: filepath for database
      password: database master password
  """
  def __init__(self):
    print "Database"
    #self.filepath = filepath
    #self.entries = readDatabase(self.filepath);
    self.entries = {}
    self.dbChanged = False

  def newDB(self):
    print "New Database"
    self.password = raw_input("Enter master password : ")
    self.filepath = raw_input("Enter file path : ")
    self.entries = {}
    self.dbChanged = False
    self.writeDatabase()

  def readDatabase(self, filepath):
    print "Reading database..."
    passwd = raw_input("Enter master password : ")
    with open(filepath, 'r') as f:
      data = f.read()
      yamlStr = security.decrypt(data, passwd)
      try:
        self = yaml.load(yamlStr)
      except:
        print 'incorrect password'
        return False
    print "Read {} entries.".format(len(self.entries))
    return True

  def writeDatabase(self):
    print "Writing to database"
    passwd = raw_input("Enter master password : ")
    if not passwd == self.password:
      print "Password doesnt match"

    yamlStr = yaml.dump(self)
    encryptStr = security.encrypt(yamlStr, self.password)
    with open(self.filepath, 'w') as f:
        f.write(encryptStr)
        print "Database written to disk"


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
  #db.newDB()
  #db.addEntry()
  #db.writeDatabase()

  db.readDatabase('./db.bin')

if __name__ == "__main__":
  test()
