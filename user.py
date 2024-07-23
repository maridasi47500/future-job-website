# coding=utf-8
import sqlite3
import sys
import os
import re
from fichier import Fichier
from model import Model
class User(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists user(
        id integer primary key autoincrement,
        email text,
        mypic text,
        country_id text,
        job_id text,
        description text,
        lat text,
        lon text,
        phone text,
        gender text,
            password text,
            nomcomplet text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from user")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from user where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyemailpwsecurity(self,email,pw):
        self.cur.execute("select * from user where email = ? and password = ? ",(email,pw,))
        myrow=dict(self.cur.fetchone())
        print(myrow["id"], "row id")
        row={}
        ai=Ai().findbyuserid(self.Program.get_session()["user_id"])
        try:
          row["notice"]="vous êtes connecté"
          row["name"]=myrow["nomcomplet"]
          row["user_id"]=myrow["id"]
          row["ai_id"]=ai["id"]
          row["email"]=myrow["email"]
        except Exception as e:
          row={"notice":"votre connexion n'a pas fonctionné","name":"","email":""}
        return row
    def getbyid(self,myid):
        self.cur.execute("select * from user where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        msg=""
        try:
          self.cur.execute("insert into user (lat,lon,description,job_id,email,country_id,phone,password,mypic,gender,nomcomplet) values (:lat,:lon,:description,:job_id,:email,:country_id,:phone,:password,:mypic,:gender,:nomcomplet)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)

          self.cur.execute("select user.*,job.name as jobname,country.unicode,country.phone as phonenum from user left join job on job.id = user.job_id left join country on country.id = user.country_id where user.id = ? ",(myid))

          anyuser=self.cur.fetchone()
          myjobname="../python_become_"+anuyser["jobname"]+anyuser["nomcomplet"].replace(" ","_")
          os.mkdir(myjobname)
          os.mkdir(myjobname+"/uploads")
          os.mkdir(myjobname+"/mypage")
          os.mkdir(myjobname+"/css")
          os.mkdir(myjobname+"/js")
          # In Unix/Linux
          os.popen('cp server** '+myjobname) 
          os.popen('cp chaine** '+myjobname) 
          os.popen('cp country** '+myjobname) 
          os.popen('cp addcountry** '+myjobname) 
          os.popen('cp addjob** '+myjobname) 
          os.popen('cp job** '+myjobname) 
          os.popen('cp css/ '+myjobname) 
          os.popen('cp fichier** '+myjobname) 
          os.popen('cp javascript** '+myjobname) 
          os.popen('cp ./uploads/'+anyuser["mypic"]+myjobname+"/uploads/") 
          os.popen('cp js/ '+myjobname) 
          os.popen('cp model** '+myjobname) 
          os.popen('cp mydb** '+myjobname) 
          os.popen('cp mypic** '+myjobname) 
          os.popen('cp mysite.sh** '+myjobname) 
          os.popen('cp render_** '+myjobname) 
          os.popen('cp nombre** '+myjobname) 
          os.popen('cp scaffold** '+myjobname) 
          os.popen('cp somehtml** '+myjobname) 
          os.popen('cp route1** '+myjobname+"/route.py") 

          os.popen('cp stylesheet** '+myjobname) 
          os.popen('cp user2** '+myjobname+"/user.py") 
          os.popen('cp user/ '+myjobname) 

          Fichier(myjobname+"/welcome","index.html").ecrire("<p>"+anyuser["unicode"]+" "+anyuser["nomcomplet"]+"</p><p>"+("femme" if anyuser["gender"] == "f" else "homme")+"</p><p>"+anyuser["phonenum"]+anyuser["phone"]+"</p/><p>"+anyuser["email"]+"</p><img src=\"/uploads/"+anyuser["mypic"]+"\" width=\"100\" height=\"100\" /><p>"+anyuser["description"]+"</p>"+"<div id=\"imap\"><div id=\"map\" onclick=\"onMapClick(event);\"></div></div>")
          Fichier(myjobname+"/css","App.css").ecrire("#map { width:100%;height:200px;}")
          Fichier(myjobname+"/","route.py").ecrire(Fichier("./","route1.py").lire().replace("name of this directory","become 1 "+anyuser["jobname"]))
          Fichier(myjobname+"/mypage","index.html").ecrire(Fichier("./mypage","index1.html").lire().replace("name of this directory","become 1 "+anyuser["jobname"]))
          Fichier(myjobname+"/js","mymap.js").ecrire(Fichier("./js","mymap.js").lire().replace("8.619543",anyuser["lat"]).replace("0.82",anyuser["lon"]))

          
        except Exception as e:
          print("my error"+str(e))
          msg+=str(e)
        azerty={}
        try:
          if myid and myid is not None:
            azerty["user_id"]=myid
            azerty["name"]=myhash["nomcomplet"]
            azerty["email"]=myhash["email"]
            azerty["notice"]="votre user a été ajouté"
          else:
            azerty["user_id"]=""
            azerty["name"]=""
            azerty["email"]=""
            azerty["notice"]="votre inscription n'a pas fonctionné"+msg
        except Exception as ee:
          azerty["user_id"]=""
          azerty["name"]=""
          azerty["email"]=""
          azerty["notice"]="votre inscription n'a pas fonctionné"+msg+str(ee)
        return azerty
