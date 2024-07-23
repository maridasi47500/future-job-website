from country import Country
from user import User
from ai import Ai
from stuff import Stuff
from post import Post
from job import Job
class Mydb():
  def __init__(self):
    print("hello")
    self.Country=Country()
    self.User=User()
    self.Ai=Ai()
    self.Stuff=Stuff()
    self.Post=Post()
    self.Job=Job()
