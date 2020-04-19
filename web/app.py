from flask import Flask,jsonify,request
from flask_restful import Api,Resource
from pymongo import MongoClient
import brcypt
import numpy 
import tensorflow
from flask
import requests
import subprocess
import json


app=Flask(__name__)
api=Api(app)

client=MongoClient("mongodb://db:27017")
db=client.ImageRecognition
users = db["Users"]


def UserExist(username):

    if users.find({"Username":username}).count()==0:
        return False
    else:
        return True





class Register(Resource):

      def post(self):

          postedData=request.getJson()

          username=postedData["username"]
          password=postedData["password"]

          if UserExist(username):

              retJson={

                   "status":301,
                   "msg": "Invalid username"

               }
               return jsonify(retJson)

           hashed_pw=bcrypt.hashpw(password.encode('utf-8'),brcypt.gensalt())

           users.insert({


               "Username":username
               "Password":hashed_pw
               "Tokens":4

               })
           retJson={

                   "status":200
                   "msg":"msg": "You successfully signed up for the API"



                }
                return jsonify(retJson)




def verify_pw(username,password):

    if not UserExist(username):
        return False

    hashed_pw=users.find({"Username":username})[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False




def countTokens(username):

    users.find({

        "Username":username

        })[0]["Tokens"]

    return tokens









api.add_resource(Register,"/register")













if __name__="__main__":

    app.run(host='0.0.0.0')






          
