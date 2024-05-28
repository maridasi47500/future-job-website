# coding=utf-8
import sqlite3
import sys
import re
from model import Model
from chaine import Chaine
import requests
class ReverseQuickstart(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists reverse_quickstart(
        id integer primary key autoincrement,
        url text,
        filename text
        );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from reverse_quickstart")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from reverse_quickstart where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from reverse_quickstart where id = ?",(myid,))
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
        #
        fname = Chaine().fichier("page.html")
        myhash["filename"]=fname
        url = myhash["url"]
        r = requests.get(url)
        open("./uploads/"+fname , 'wb').write(r.content)
        try:
          self.cur.execute("insert into reverse_quickstart (url,filename) values (:url,:filename)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["reverse_quickstart_id"]=myid
        azerty["notice"]="votre reverse_quickstart a été ajouté"
        return azerty




