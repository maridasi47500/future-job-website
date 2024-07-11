# coding=utf-8
import sqlite3
import sys
import re
from model import Model
from aistuff import Aistuff
class Ai(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists ai(
        id integer primary key autoincrement,
        username text,
            user_id text,
            mypic text,
            name text,
            description text,
            gender text
    ,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );""")
        self.con.commit()
        self.Aistuff=Aistuff()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from ai")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from ai where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def findbyuserid(self,myid):
        self.cur.execute("select * from ai where user_id = ?",(myid,))
        azer=self.cur.fetchone()
        row ={"name":"","mypic":"","gender":"","username":""}
        if azer is not None:
          row=dict(azer)
          print(row["id"], "row id")
        return row
    def getbyid(self,myid):
        self.cur.execute("select * from ai where id = ?",(myid,))
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
        try:
          self.cur.execute("insert into ai (username,user_id,mypic,name,description,gender) values (:username,:user_id,:mypic,:name,:description,:gender)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["ai_id"]=myid
        azerty["notice"]="votre ai a été ajouté"
        return azerty
    def update(self,params):
        print("ok")
        myhash={}
        mystuff_ids=params["description"].split(",")
        user_id=params["user_id"]
        allstuffs=self.Aistuff.getbyuserid(user_id)
        for z in allstuffs:
            if z["stuff_id"] not in mystuff_ids:
                self.Aistuff.deletebyid(z["id"])
        for mystuff_id in mystuff_ids:
            if mystuff_id not in allstuffs:
                self.Aistuff.create({"user_id":user_id,"stuff_id":mystuff_id})
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
        myai=None
        userid=None
        myname=None
        try:
          self.cur.execute("update ai set username = :username,mypic = :mypic,name = :name,description = :description,gender = :gender where user_id = :user_id",myhash)
          self.con.commit()
          self.cur.execute("select * from ai where user_id = :user_id",(myhash["user_id"],))
          myai=self.cur.fetchone()
          myid=myai["id"]
          userid=myai["user_id"]
          myname=myai["name"]
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["ai_id"]=myid
        azerty["user_id"]=userid
        azerty["name"]=myname
        azerty["notice"]="votre ai a été modifié(e)"
        return azerty



