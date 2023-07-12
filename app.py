from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
import pyrebase
import pyttsx3
import threading
from datetime import date
import requests
from datetime import datetime
from random import randint
import json

config = {
    "apiKey": "AIzaSyB_vMbdEOmrMH_Eo4IuNkuObyY_ACLI5-k",
    "authDomain": "ampplex-75da7.firebaseapp.com",
    "databaseURL": "https://ampplex-75da7-default-rtdb.firebaseio.com",
    "projectId": "ampplex-75da7",
    "databaseURL": "https://ampplex-75da7-default-rtdb.firebaseio.com/",
    "storageBucket": "ampplex-75da7.appspot.com",
    "messagingSenderId": "730587965700",
    "appId": "1:730587965700:web:7c71f40fd541c7b91bc851",
    "measurementId": "G-BSPPZFVTMS"
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()
storage = firebase.storage()

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'team.amplex@gmail.com'
app.config['MAIL_PASSWORD'] = 'iyfmqibihwffqvjn'
mail = Mail(app)


def Server_Assistant(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def Cryptography_Encrypt(text):
    alpha = {'a': 2073, 'b': 2076, 'c': 2079, 'd': 2082, 'e': 2085, 'f': 2088,
             'g': 2091, 'h': 2094, 'i': 2097, 'j': 2100, 'k': 2103, 'l': 2106, 'm': 2109, 'n': 2112, 'o': 2115, 'p': 2118, 'q': 2121, 'r': 2124, 's': 2127, 't': 2130, 'u': 2133, 'v': 2136, 'w': 2139, 'x': 2142, 'y': 2145, 'z': 2148, ' ': 2151,
             '1': 234, '2': 89, '3': 45, '4': 1095,
             '5': 77, '6': 12, '7': 61, '8': 55, '9': 23, '0': 22,
             '`': 1288, '~`': 226096, '!': 33, '@': 44, '#': 59, '$': 66, '%': 7754, '^': 88, '&': 99, '*': 401, '(': 402, ')': 403, '-': 404, '_': '405', '=': 406, '+': 407, '[': 408, ']': 409, '{': 410, '}': 411, '\\': 412, '|': 413, ';': 414, ':': 415, "'": 416, '"': 417, ',': 418, '.': 419, '/': 420, '?': 422, 'A': 630, 'B': 632, 'C': 634, 'D': 636, 'E': '638', 'F': 640, 'G': 642, 'H': 644, 'I': 646, 'J': 648, 'K': 650, 'L': 652, 'M': 654, 'N': 656, 'O': 658, 'P': 660, 'Q': 662, 'R': 664, 'S': 666, 'T': 668, 'U': 670, 'V': 672, 'W': 674, 'X': 676, 'Y': 678, 'Z': 680}

    encryptedTxt = ""

    for i in text:
        encryptedTxt += ' '
        encryptedTxt += str(alpha[i])

    return encryptedTxt


def Cryptography_Decrypt(encryptedTxt):

    alpha_num = {'2073': 'a', '2076': 'b', '2079': 'c',
                 '2082': 'd', '2085': 'e', '2088': 'f', '2091': 'g', '2094': 'h', '2097': 'i', '2100': 'j', '2103': 'k', '2106': 'l', '2109': 'm', '2112': 'n', '2115': 'o', '2118': 'p', '2121': 'q', '2124': 'r', '2127': 's', '2130': 't', '2133': 'u', '2136': 'v', '2139': 'w', '2142': 'x', '2145': 'y', '2148': 'z', '2151': ' ', '234': '1', '89': '2', '45': '3',
                 '1095': '4', '77': '5', '12': '6', '61': '7', '55': '8', '23': '9', '22': '0', '1288': '`', '226096': '~', '33': '!', '44': '@', '59': '#', '66': '$', '7754': '%', '88': '^', '99': '&', '401': '*', '402': '(', '403': ')', '404': '-', '405': '_', '406': '=', '407': '+', '408': '[', '409': ']', '410': '{', '411': '}', '412': '\\', '413': '|', '414': ';', '415': ':', '416': "'", '417': '"', '418': ',', '419': '.', '420': '/', '422': '?', '630': 'A', '632': 'B', '634': 'C', '636': 'D', '638': 'E', '640': 'F', '642': 'G', '644': 'H', '646': 'I', '648': 'J', '650': 'K', '652': 'L', '654': 'M', '656': 'N', '658': 'O', '660': 'P', '662': 'Q', '664': 'R', '666': 'S', '668': 'T', '670': 'U', '672': 'V', '674': 'W', '676': 'X', '678': 'Y', '680': 'Z'}

    decryptedTxt = ""

    encryptedLst = encryptedTxt.split()

    for i in encryptedLst:
        decryptedTxt += alpha_num[i]

    return decryptedTxt


@app.route('/home')
@app.route('/')
def Home():
    if request.url == "http://ampplex-backened.herokuapp.com/":
        return redirect('https://ampplex-backened.herokuapp.com/')
    return render_template('index.html')


@app.route('/Login/<string:email>/<string:password>', methods=['GET'])
def Login(email, password):

    if request.url == f"http://ampplex-backened.herokuapp.com/Login/<string:email>/<string:password>":
        return redirect("https://ampplex-backened.herokuapp.com/Login/<string:email>/<string:password>")

    try:

        db_val = database.child("User").get().val()

        password = Cryptography_Decrypt(password)

        for i in db_val:
            if db_val[i]["Email"] == email and Cryptography_Decrypt(db_val[i]["password"]) == password:
                # If user's email and password is correct then returning the status success and user id
                response = {
                    "status": "success",
                    "user_id": i,
                    "UserName": db_val[i]["UserName"]
                }
                return json.dumps(response)
    except:
        # If user's email or password is incorrect then returning the response error
        response = {
            "status": "error",
        }
    return json.dumps(response)


@app.route('/SignUp/<string:username>/<string:email>/<string:password>', methods=['GET'])
def SignUp(username, email, password):
    if request.url == "http://ampplex-backened.herokuapp.com/SignUp/<string:username>/<string:email>/<string:password>":
        return redirect('https://ampplex-backened.herokuapp.com/SignUp/<string:username>/<string:email>/<string:password>')

    password_len = password.split(' ')

    if len(password_len) >= 8:

        data = {"UserName": username, "Email": email,
                "password": password, "Follower": 0, "Bio": ""}
        database.child("User").push(data)

        msg = Message("Congratulations! you have successfully became a part of Ampplex family",
                      sender="team.amplex@gmail.com", recipients=[email])
        msg.body = f"Hi, {username} Thanks for downloading our app. We would love to hear your feedback! \n https://play.google.com/store/apps/details?id=com.ankeshkumar.Ampplex"
        mail.send(msg)

        return "success"

    else:
        return "error"


@app.route('/Category/<string:categories>/<string:userID>', methods=['GET'])
def Category(categories, userID):

    if request.url == f"http://ampplex-backened.herokuapp.com/Category/<string:categories>/<string:userID>":
        return redirect("https://ampplex-backened.herokuapp.com/Category/<string:categories>/<string:userID>")

    data = {"Category": categories}

    try:
        database.child("User").child(userID).child('Category').update(data)
        response = {
            "status": "success"
        }
        return json.dumps(response)
    except:
        response = {
            "status": "error"
        }
        return json.dumps(response)


def getPostJson():

    if request.url == "http://ampplex-backened.herokuapp.com/GetPostJson/":
        return redirect("https://ampplex-backened.herokuapp.com/GetPostJson/")

    response = []
    fetchPostFromDb = database.child("User").get().val()
    # Path for retrieving user name

    for i in fetchPostFromDb:

        fetchPostFromDb = database.child(
            "User").child(i).child("Post").get().val()

        UserName = database.child("User").child(i).get().val().get("UserName")

        if fetchPostFromDb != None:
            for j in fetchPostFromDb:

                ImgPath = fetchPostFromDb[j].get("imgPath")

                Caption = ""
                try:
                    Caption = fetchPostFromDb[j]["caption"]
                except:
                    print("Caption is None")

                try:
                    Timestamp = fetchPostFromDb[j].get("timestamp")
                    if Timestamp == None:
                        continue
                except Exception as e:
                    print(e)

                print("Timestamp is ", Timestamp)

                Type = ""
                try:
                    Type = fetchPostFromDb[j]['type']
                except Exception as e:
                    print("Type is None")

                UserID = i

                try:
                    profilePicPath = database.child("User").child(i).child(
                        "ProfilePicture").get().val()["profilePicPath"]
                except:
                    profilePicPath = "null"

                response.append({"UserName": UserName, "ImgPath": ImgPath,
                                 "Caption": Caption, "Timestamp": Timestamp, "UserID": UserID, "profilePicPath": profilePicPath, "Type": Type, "Post_ID": j})

    return response


@app.route("/GetShortVideos/", methods=['GET'])
def getShortVideos():

    if request.url == "http://ampplex-backened.herokuapp.com/GetShortVideos/":
        return redirect("https://ampplex-backened.herokuapp.com/GetShortVideos/")

    response = []
    fetchPostFromDb = database.child("User").get().val()
    # Path for retrieving user name

    for i in fetchPostFromDb:

        fetchPostFromDb = database.child(
            "User").child(i).child("Post").get().val()

        UserName = database.child("User").child(i).get().val().get("UserName")

        if fetchPostFromDb != None:
            for j in fetchPostFromDb:

                VideoPath = fetchPostFromDb[j].get("imgPath")

                Caption = ""
                try:
                    Caption = fetchPostFromDb[j]["caption"]
                except:
                    print("Caption is None")

                Timestamp = fetchPostFromDb[j].get("timestamp")

                Type = ""

                try:
                    Type = fetchPostFromDb[j]['type']
                except Exception as e:
                    print("Type is None")
                    assert Type != None, "Type cannot be none"

                UserID = i

                try:
                    profilePicPath = database.child("User").child(i).child(
                        "ProfilePicture").get().val()["profilePicPath"]
                except:
                    profilePicPath = "null"
                if Type == "Video":
                    response.append({"UserName": UserName, "VideoPath": VideoPath,
                                     "Caption": Caption, "Timestamp": Timestamp, "UserID": UserID, "profilePicPath": profilePicPath, "Type": Type, "Post_ID": j})

    return json.dumps(response)


@app.route("/UploadPost/<path:imgPath>/<string:caption>/<string:timestamp>/<string:userID>", methods=['GET'])
def UploadPost(imgPath, caption, timestamp, userID):

    if request.url == f"http://ampplex-backened.herokuapp.com/UploadPost/<path:imgPath>/<string:caption>/<string:timestamp>/<string:userID>":
        return redirect("https://ampplex-backened.herokuapp.com/UploadPost/<path:imgPath>/<string:caption>/<string:timestamp>/<string:userID>")

    data = {"Image_Path": imgPath, "Caption": caption,
            "Timestamp": timestamp}
    try:
        database.child("User").child(userID).child("Post").push(data)

        response = {
            "status": "success",
        }

        return json.dumps(response)

    except:
        response = {
            "status": "error"
        }
        return json.dumps(response)


@app.route("/Count_Posts/<string:userID>/", methods=['GET'])
def Count_Posts(userID):

    if request.url == f"http://ampplex-backened.herokuapp.com/Count_Posts/<string:userID>/":
        return redirect("https://ampplex-backened.herokuapp.com/Count_Posts/<string:userID>/")

    db_val = database.child("User").child(userID).child("Post").get().val()

    try:
        response = {
            "status": "success",
            "Posts": len(db_val.keys())
        }
        return json.dumps(response)

    except:
        response = {
            "status": "success",
            "Posts": 0
        }
        return json.dumps(response)


@app.route("/getMyPosts/<string:userID>/", methods=['GET'])
def getMyPosts(userID):

    if request.url == f"http://ampplex-backened.herokuapp.com/getMyPosts/<string:userID>/":
        return redirect("https://ampplex-backened.herokuapp.com/getMyPosts/<string:userID>/")

    response = []

    fetchPostFromDb = database.child(
        "User").child(userID).child("Post").get().val()

    if fetchPostFromDb != None:
        for j in fetchPostFromDb:

            ImgPath = fetchPostFromDb[j].get("imgPath")

            Caption = ""
            try:
                Caption = fetchPostFromDb[j].get("caption")
            except:
                print("Caption is None")

            Timestamp = fetchPostFromDb[j].get("timestamp")
            if Timestamp is None:
                continue

            try:
                Type = fetchPostFromDb[j].get("type")
            except:
                print("Type is None")

            print(Timestamp)
            response.append({"ImgPath": ImgPath,
                             "Caption": Caption, "Timestamp": Timestamp, "Type": Type, "Post_ID": j})

    return json.dumps(response)


@app.route('/getUsers')
def getUsers():

    if request.url == "http://ampplex-backened.herokuapp.com/getUsers/":
        return redirect("https://ampplex-backened.herokuapp.com/getUsers/")

    response = []
    db = database.child("User").get().val()
    for i in db:
        response.append(db[i]["UserName"])
    return json.dumps(response)


@app.route('/getProfilePicture/<string:userID>/', methods=['GET'])
def getProfilePicture(userID):

    if request.url == f"http://ampplex-backened.herokuapp.com/getProfilePicture/<string:userID>/":
        return redirect("https://ampplex-backened.herokuapp.com/getProfilePicture/<string:userID>/")

    try:
        profilePic = database.child("User").child(
            userID).child("ProfilePicture").get().val()["profilePicPath"]
        print(profilePic)
        response = {
            "status": "success",
            "profilePic": profilePic
        }
    except:
        profilePic = None
        response = {
            "status": "success",
            "profilePic": profilePic
        }

    return json.dumps(response)


@app.route('/Unfollow/<string:userID>/MyID/<string:myID>', methods=['GET'])
def Unfollow(userID, myID):

    if request.url == f"http://ampplex-backened.herokuapp.com/Unfollow/<string:userID>/MyID/<string:myID>":
        return redirect("https://ampplex-backened.herokuapp.com/Unfollow/<string:userID>/MyID/<string:myID>")

    response = {}

    try:
        Followers = database.child("User").child(
            userID).child("Follower").get().val()

        FollowingID = database.child("User").child(
            myID).child("Following").get().val()

        FollowersID = database.child("User").child(
            userID).child("Followers").get().val()

        for i in FollowingID:
            if userID == FollowingID[i]["userID"]:

                # Removing the user from the following list
                database.child("User").child(myID).child(
                    "Following").child(i).child("userID").remove()

                # Decreamenting followers
                database.child("User").child(userID).update(
                    {"Follower": Followers - 1})

                response = {
                    "status": "success"
                }

        for i in FollowersID:
            if myID == FollowersID[i]["userID"]:
                # Removing the user from the followers list
                database.child("User").child(userID).child(
                    "Followers").child(i).child("userID").remove()

    except Exception as e:
        response = {
            "status": "error"
        }
        print(e)

    return json.dumps(response)


@app.route('/Increament_Followers/<string:userID>/MyID/<string:myID>', methods=['GET'])
def Increament_Followers(userID, myID):

    if request.url == f"http://ampplex-backened.herokuapp.com/Increament_Followers/<string:userID>/MyID/<string:myID>":
        return redirect("https://ampplex-backened.herokuapp.com/Increament_Followers/<string:userID>/MyID/<string:myID>")

    try:
        userID_Found = False
        userID_Found2 = False

        Followers = database.child("User").child(
            userID).child("Follower").get().val()

        try:
            FollowingID = database.child("User").child(
                myID).child("Following").get().val()
            for i in FollowingID:
                if userID == FollowingID[i]["userID"]:
                    userID_Found = True

                print(FollowingID[i]["userID"])

        except:
            userID_Found = False

        try:
            FollowerID = database.child("User").child(
                userID).child("Followers").get().val()
            for i in FollowerID:
                if myID == FollowerID[i]["userID"]:
                    userID_Found2 = True

                print(FollowerID[i]["userID"])

        except:
            userID_Found2 = False

        if userID_Found == False:
            database.child("User").child(myID).child(
                "Following").push({"userID": userID})

            database.child("User").child(userID).update(
                {"Follower": Followers + 1})

            response = {
                "status": "success",
                "Already_Followed": "false",
            }

        if userID_Found2 == False:
            database.child("User").child(userID).child(
                "Followers").push({"userID": myID})

        else:
            response = {
                "status": "success",
                "Already_Followed": "true",
            }

    except Exception as e:
        response = {
            "status": "error"
        }
        print(e)

    return json.dumps(response)


# myUserID is logined user's user-ID
@app.route("/UpdateLikes/<string:myUserID>/<string:pressedPostID>/<string:pressedUserID>/<string:LikeOrDislike>", methods=['GET'])
def UpdateLikes(myUserID, pressedPostID, pressedUserID, LikeOrDislike):

    if request.url == f"http://ampplex-backened.herokuapp.com/UpdateLikes/<string:myUserID>/<string:pressedPostID>/<string:pressedUserID>/<string:LikeOrDislike>":
        return redirect("https://ampplex-backened.herokuapp.com/UpdateLikes/<string:myUserID>/<string:pressedPostID>/<string:pressedUserID>/<string:LikeOrDislike>")

    try:
        getLikes = database.child("User").child(pressedUserID).child(
            "Post").child(pressedPostID).get().val()["Likes"]  # Retrieving likes

        if LikeOrDislike == "Like":
            database.child("User").child(pressedUserID).child(
                "Post").child(pressedPostID).update({"Likes": getLikes + 1})  # Increamenting likes when user presses like button
            database.child("User").child(myUserID).child(
                "LikedPost").push({"LikedPostID": pressedPostID})  # Pushing liked postID in loged  user

        elif LikeOrDislike == "Dislike":
            if getLikes > 0:
                database.child("User").child(pressedUserID).child(
                    "Post").child(pressedPostID).update({"Likes": getLikes - 1})  # Decreamenting likes when user presses dislike button
                liked_PostID = database.child("User").child(myUserID).child(
                    "LikedPost").get().val()

                for i in liked_PostID:
                    if liked_PostID[i]["LikedPostID"] == pressedPostID:
                        database.child("User").child(
                            myUserID).child("LikedPost").child(i).child("LikedPostID").remove()

        response = {
            "status": "success"
        }

    except Exception as e:
        response = {
            "status": "error"
        }
        print(e)

    return json.dumps(response)


@app.route('/GetLikes/<string:pressedUserID>/<string:pressedPostID>', methods=['GET'])
def GetLikes(pressedUserID, pressedPostID):

    if request.url == f"http://ampplex-backened.herokuapp.com/GetLikes/<string:pressedUserID>/<string:pressedPostID>":
        return redirect("https://ampplex-backened.herokuapp.com/GetLikes/<string:pressedUserID>/<string:pressedPostID>")

    getLikes = database.child("User").child(pressedUserID).child(
        "Post").child(pressedPostID).get().val()["Likes"]  # Retrieving likes

    response = {
        "status": "success",
        "Likes": getLikes,
    }

    return json.dumps(response)


@app.route("/isLiked/<string:myUserID>/<string:postID>", methods=['GET'])
def isLiked(myUserID, postID):

    if request.url == f"http://ampplex-backened.herokuapp.com/isLiked/<string:myUserID>/<string:postID>":
        return redirect("https://ampplex-backened.herokuapp.com/isLiked/<string:myUserID>/<string:postID>")

    try:
        likedPosts = database.child("User").child(
            myUserID).child("LikedPost").get().val()

        isLiked = False

        for i in likedPosts:
            print(likedPosts[i]["LikedPostID"], postID)
            if likedPosts[i]["LikedPostID"] == postID:
                isLiked = True

        response = {
            "status": "success",
            "likedPosts": isLiked
        }

    except Exception as e:
        likedPosts = None
        response = {
            "status": "success",
            "likedPosts": likedPosts
        }
        print(e)
    return json.dumps(response)


@app.route('/GetFollower/<string:userID>/', methods=['GET'])
def GetFollower(userID):

    if request.url == f"http://ampplex-backened.herokuapp.com/GetFollower/<string:userID>/":
        return redirect("https://ampplex-backened.herokuapp.com/GetFollower/<string:userID>/")

    Followers = database.child("User").child(
        userID).child("Follower").get().val()

    response = {
        "status": "success",
        "Followers": Followers
    }

    return json.dumps(response)


@app.route("/Check_Followed/<string:userID>/MyID/<string:myID>", methods=['GET'])
def Check_Followed(userID, myID):

    if request.url == f"http://ampplex-backened.herokuapp.com/Check_Followed/<string:userID>/MyID/<string:myID>":
        return redirect("https://ampplex-backened.herokuapp.com/Check_Followed/<string:userID>/MyID/<string:myID>")

    try:
        FollowingID = database.child("User").child(
            myID).child("Following").get().val()

        userID_Found = False

        for i in FollowingID:
            if userID == FollowingID[i]["userID"]:
                userID_Found = True

            print(FollowingID[i]["userID"])

        if userID_Found == False:

            response = {
                "status": "success",
                "Already_Followed": "false",
            }

        else:
            response = {
                "status": "success",
                "Already_Followed": "true",
            }

    except Exception as e:
        if userID_Found == False:

            response = {
                "status": "success",
                "Already_Followed": "false",
            }

        print(e)

    return json.dumps(response)


@app.route('/GetUserNames/<string:userName>', methods=['GET'])
def GetUserNames(userName):

    if request.url == f"http://ampplex-backened.herokuapp.com/GetUserNames/{userName}":
        return redirect(f"https://ampplex-backened.herokuapp.com/GetUserNames/{userName}")

    UserNames = database.child("User").get().val()
    response = []

    for i in UserNames:

        try:
            profilePicPath = database.child("User").child(i).child(
                "ProfilePicture").get().val()["profilePicPath"]
        except:
            print("ProfilePicture is None")
            profilePicPath = None

        Retreived_userName = database.child(
            "User").child(i).get().val().get("UserName")

        if Retreived_userName != None and userName.lower() == Retreived_userName.lower()[: len(userName)]:
            print(userName.lower(), Retreived_userName.lower())
            response.append({"UserName": Retreived_userName, "userID": i,
                             "ProfilePicPath": profilePicPath})

    return json.dumps(response)


@ app.route('/Comment/<string:myUserID>/<string:clickedUserID>/<string:postID>/<string:Comment>/', methods=['GET'])
def Comment(myUserID, clickedUserID, postID, Comment):

    if request.url == f"http://ampplex-backened.herokuapp.com/Comment/<string:myUserID>/<string:clickedUserID>/<string:postID>/<string:Comment>/":
        return redirect("https://ampplex-backened.herokuapp.com/Comment/<string:myUserID>/<string:clickedUserID>/<string:postID>/<string:Comment>/")

    try:
        ImgPath = json.loads(getProfilePicture(myUserID))["profilePic"]
        UserName = database.child("User").child(
            myUserID).get().val()["UserName"]

        data = {"myUserID": myUserID, "UserName": UserName,
                "ImgPath": ImgPath, "Comment": Comment}
        database.child("User").child(clickedUserID).child(
            "Post").child(postID).child("Comments").push(data)
        response = {
            "status": "success",
        }
    except Exception as e:
        response = {
            "status": "error",
        }

    return json.dumps(response)


@ app.route('/getComments/<string:pressedUserID>/<string:postID>', methods=['GET'])
def getComments(pressedUserID, postID):

    if request.url == f"http://ampplex-backened.herokuapp.com/getComments/<string:pressedUserID>/<string:postID>":
        return redirect("https://ampplex-backened.herokuapp.com/getComments/<string:pressedUserID>/<string:postID>")

    try:
        response_Data = []

        Comment_Data = database.child("User").child(
            pressedUserID).child("Post").child(postID).child("Comments").get().val()

        for i in Comment_Data:
            print(i)
            Comment_Data[i]["Comment_ID"] = i
            response_Data.append(Comment_Data[i])

        return json.dumps(response_Data)

    except Exception as e:
        print(e)
        return "error"


@ app.route("/getUserData/<string:userID>/", methods=["GET"])
def getUserData(userID):  # For edit profile

    if request.url == f"http://ampplex-backened.herokuapp.com/getUserData/<string:userID>/":
        return redirect("https://ampplex-backened.herokuapp.com/getUserData/<string:userID>/")

    UserData = database.child("User").child(userID).get().val()
    UserName = UserData["UserName"].split()
    FirstName = UserName[0]
    LastName = " ".join(UserName[1:])
    Bio = UserData["Bio"]

    response = {
        "FirstName": FirstName,
        "LastName": LastName,
        "Bio": Bio,
    }

    return json.dumps(response)


@ app.route("/EditProfile/<string:userID>/<string:FirstName>/<string:LastName>/<string:Bio>/", methods=["GET"])
def EditProfile(userID, FirstName, LastName, Bio):

    if request.url == f"http://ampplex-backened.herokuapp.com/EditProfile/<string:userID>/<string:FirstName>/<string:LastName>/<string:Bio>/":
        return redirect("https://ampplex-backened.herokuapp.com/EditProfile/<string:userID>/<string:FirstName>/<string:LastName>/<string:Bio>/")

    try:
        if LastName != "null":
            UserName = FirstName + " " + LastName
        else:
            UserName = FirstName

        database.child("User").child(userID).update(
            {"UserName": UserName, "Bio": Bio})

        return "success"
    except Exception as e:
        print(e)
        return "error"


@ app.route("/getUserNameFromUserID/<string:userID>/", methods=["GET"])
def getUserNameFromUserID(userID):

    if request.url == f"http://ampplex-backened.herokuapp.com/getUserNameFromUserID/<string:userID>/":
        return redirect("https://ampplex-backened.herokuapp.com/getUserNameFromUserID/<string:userID>/")

    try:
        UserName = database.child("User").child(userID).get().val()["UserName"]
        response = {
            "status": "success",
            "UserName": UserName
        }
    except Exception as e:
        print(e)
        response = {
            "status": "error",
        }

    return json.dumps(response)


@app.route("/SendOTP/<string:email>/<string:message>/", methods=["GET"])
def SendOTP(email, message):

    if request.url == f"http://ampplex-backened.herokuapp.com/SendOTP/<string:email>/<string:message>/":
        return redirect("https://ampplex-backened.herokuapp.com/SendOTP/<string:email>/<string:message>/")

    try:
        msg = Message("Ampplex OTP verification",
                      sender="team.amplex@gmail.com", recipients=[email])
        msg.body = message
        mail.send(msg)
        return "success"
    except Exception as e:
        print(e)
        return "error"


@app.route("/Reset_password", methods=['GET'])
def Reset_password():
    if request.url == f"http://ampplex-backened.herokuapp.com/Reset_password":
        return redirect("https://ampplex-backened.herokuapp.com/Reset_password")

    return render_template("reset_password.html")


@app.route("/EnterOTP/<string:otp>/<string:email>", methods=['GET'])
def EnterOTP(otp, email):

    if request.url == f"http://ampplex-backened.herokuapp.com/EnterOTP/<string:otp>/<string:email>":
        return redirect("https://ampplex-backened.herokuapp.com/EnterOTP/<string:otp>/<string:email>")

    return render_template("InputOTP.html", otp=otp, email=email)


@app.route('/CreateNewPassword/<string:email>/<string:new_password>/<string:secret_key>', methods=['GET'])
def CreateNewPassword(email, new_password, secret_key):

    if request.url == f"http://ampplex-backened.herokuapp.com/CreateNewPassword/<string:email>/<string:new_password>/<string:secret_key>":
        return redirect("https://ampplex-backened.herokuapp.com/CreateNewPassword/<string:email>/<string:new_password>/<string:secret_key>")

    if secret_key == ";';][][3543{]';[sidjg868567**-+~&=32057dfjgiodfgoidfo;ji><<><>][[+-":

        try:
            UserData = database.child("User").get().val()

            for i in UserData:
                if UserData[i]["Email"] == email:
                    database.child("User").child(i).update(
                        {"password": new_password})

            return "success"
        except Exception as e:
            print(e)
            return "error"


@app.route('/DeletePost/<string:userID>/<string:postID>', methods=['GET'])
def DeletePost(userID, postID):

    if request.url == f"http://ampplex-backened.herokuapp.com/DeletePost/<string:userID>/<string:postID>":
        return redirect("https://ampplex-backened.herokuapp.com/DeletePost/<string:userID>/<string:postID>")

    try:
        database.child("User").child(userID).child(
            "Post").child(postID).remove()
        return "success"
    except Exception as e:
        print(e)
        return "error"


@app.route('/DeleteComment/<string:userID>/<string:postID>/<string:commentID>', methods=['GET'])
def DeleteComment(userID, postID, commentID):

    if request.url == f"http://ampplex-backened.herokuapp.com/DeleteComment/<string:userID>/<string:postID>/<string:commentID>":
        return redirect("https://ampplex-backened.herokuapp.com/DeleteComment/<string:userID>/<string:postID>/<string:commentID>")

    try:
        database.child("User").child(userID).child(
            "Post").child(postID).child("Comments").child(commentID).remove()
        return "success"
    except Exception as e:
        print(e)
        return "error"


@app.route('/BlockUser/<string:userID>/<string:myUserID>')
def BlockUser(userID, myUserID):

    if request.url == f"http://ampplex-backened.herokuapp.com/BlockUser/<string:userID>/<string:myUserID>":
        return redirect("https://ampplex-backened.herokuapp.com/BlockUser/<string:userID>/<string:myUserID>")

    try:
        database.child("User").child(myUserID).child(
            "Blocked").child(userID).set(True)
        return "success"
    except Exception as e:
        print(e)
        return "error"


@app.route('/IncreaseViewCount/<string:postID>/<string:userID>')
def IncreaseViewCount(postID, userID):

    # Increamenting the view count of the post
    if request.url == f"http://ampplex-backened.herokuapp.com/IncreaseViewCount/<string:postID>/<string:userID>":
        return redirect("https://ampplex-backened.herokuapp.com/IncreaseViewCount/<string:postID>/<string:userID>")

    try:
        try:
            ViewCount = database.child("User").child(userID).child(
                "Post").child(postID).get().val()["ViewCount"]
        except Exception as e:
            print(e)
            ViewCount = 0

        database.child("User").child(userID).child(
            "Post").child(postID).update({"ViewCount": ViewCount + 1})
        return "success"
    except Exception as e:
        print(e)
        return "error"


@app.route('/GetViewCount/<string:postID>/<string:userID>')
def GetViewCount(postID, userID):

    if request.url == f"http://ampplex-backened.herokuapp.com/GetViewCount/<string:postID>/<string:userID>":
        return redirect("https://ampplex-backened.herokuapp.com/GetViewCount/<string:postID>/<string:userID>")

    try:
        # Retreiving the view count of the post by checking the userID
        ViewCount = database.child("User").child(userID).child(
            "Post").child(postID).get().val()["ViewCount"]

        response = {
            "ViewCount": ViewCount
        }

    except Exception as e:
        print(e)
        response = {
            "ViewCount": 0
        }

    return json.dumps(response)


@app.route('/ReportComment/<string:commentID>/<string:userID>/<string:myUserID>/<string:reason>')
def ReportComment(commentID, userID, myUserID, reason):

    # Getting commentID, userID, myUserID and reason. Sending the report to the admin through email

    if request.url == f"http://ampplex-backened.herokuapp.com/ReportPost/<string:postID>/<string:userID>/<string:myUserID>/<string:reason>":
        return redirect("https://ampplex-backened.herokuapp.com/ReportPost/<string:postID>/<string:userID>/<string:myUserID>/<string:reason>")

    messageBody = f"{myUserID} reported the commentID: {commentID} , his/her userID : {userID} for reason: {reason}"

    try:
        msg = Message("Ampplex : Report",
                      sender="team.amplex@gmail.com", recipients=['ankesh3905222@gmail.com'])
        msg.body = messageBody
        mail.send(msg)

        response = {
            "message": "success"
        }

    except Exception as e:
        print(e)
        response = {
            "message": "error"
        }

    return json.dumps(response)


@app.route('/ReportPost/<string:postID>/<string:userID>/<string:myUserID>/<string:reason>')
def ReportPost(postID, userID, myUserID, reason):

    if request.url == f"http://ampplex-backened.herokuapp.com/ReportPost/<string:postID>/<string:userID>/<string:myUserID>/<string:reason>":
        return redirect("https://ampplex-backened.herokuapp.com/ReportPost/<string:postID>/<string:userID>/<string:myUserID>/<string:reason>")

    messageBody = f"{myUserID} reported the postID: {postID} , his/her userID : {userID} for reason: {reason}"

    try:
        msg = Message("Ampplex : Report",
                      sender="team.amplex@gmail.com", recipients=['ankesh3905222@gmail.com'])
        msg.body = messageBody
        mail.send(msg)

        response = {
            "message": "success"
        }

    except Exception as e:
        print(e)
        response = {
            "message": "error"
        }

    return json.dumps(response)


@app.route('/UploadAssignment/<string:myUserID>/<string:postID>/<string:subject>/<string:question>/<string:option1>/<string:option2>/<string:option3>/<string:option4>/<string:Correctoption>/<string:question_mark_isThere>')
def UploadAssignment(myUserID, postID, subject, question, option1, option2, option3, option4, Correctoption, question_mark_isThere):

    # Uploading the assignment to the database

    response = {}

    if request.url == f"http://ampplex-backened.herokuapp.com/UploadAssignment/<string:myUserID>/<string:postID>/<string:subject>/<string:question>/<string:option1>/<string:option2>/<string:option3>/<string:option4>/<string:Correctoption>/<string:question_mark_isThere>":
        return redirect("https://ampplex-backened.herokuapp.com/UploadAssignment/<string:myUserID>/<string:postID>/<string:subject>/<string:question>/<string:option1>/<string:option2>/<string:option3>/<string:option4>/<string:Correctoption>/<string:question_mark_isThere>")

    try:
        database.child("User").child(myUserID).child(
            "Post").child(postID).child("Assignment").child(subject).child(question).set(
            {"option1": option1, "option2": option2, "option3": option3, "option4": option4, "Correctoption": Correctoption, "question_mark_isThere": question_mark_isThere})
        response = {
            "status": "success"
        }
    except Exception as e:
        print(e)

        response = {
            "status": "error"
        }

    return json.dumps(response)


@app.route("/Send_Push_notification/<string:myUserID>/<string:postID>/<string:caption>/<string:PostTime>")
def Send_Push_notification(myUserID, postID, caption, PostTime):

    if request.url == f"http://ampplex-backened.herokuapp.com/Send_Push_notification/<string:myUserID>/<string:postID>/<string:caption>/<string:PostTime>":
        return redirect("https://ampplex-backened.herokuapp.com/Send_Push_notification/<string:myUserID>/<string:postID>/<string:caption>/<string:PostTime>")

    # Sending the push notification to the followers of the user
    """
    This function returns the following responses:
    1. UserName: The name of the user who posted the post
    2. Caption: The caption of the post
    3. PostID: The postID of the post
    4. ProfilePic: The profile pic of the user who posted the post
    5. PostPic: The post pic of the post/Image path
    6. PostType: The type of the post
    7. PostTime: The time of the post
    """

    try:
        # Searching for the followers of the user
        Followers = database.child("User").child(
            myUserID).child("Followers").get().val()

        # Searching for the userName who posted the post
        UserName = database.child("User").child(
            myUserID).get().val()["UserName"]

        # Searching for the profile picture of the user who posted the post
        ProfilePic = database.child("User").child(myUserID).child(
            "ProfilePicture").get().val()["profilePicPath"]

        # Retrieving PostPic from the database
        Posts = database.child("User").child(myUserID).child(
            "Post").get().val()

        # Searching for the post pic of the post
        for post in Posts:

            post_ID_2 = database.child("User").child(myUserID).child(
                "Post").child(post).get().val().get("postID")

            if str(post_ID_2) == str(postID):
                postID = post

        PostPic = database.child("User").child(myUserID).child(
            "Post").child(postID).get().val()["imgPath"]

        # Retrieving PostType from the database
        PostType = database.child("User").child(myUserID).child(
            "Post").child(postID).child("type").get().val()

        # Sending the push notification to the followers of the user
        for user in Followers:
            data = {"UserName": UserName, "Caption": caption, "PostID": postID,
                    "ProfilePic": ProfilePic, "PostPic": PostPic, "PostType": PostType, "PostTime": PostTime, "read": False}
            Follower_UserID = database.child("User").child(myUserID).child(
                "Followers").child(user).get().val()["userID"]

            database.child("User").child(Follower_UserID).child(
                "Notification").push(data)

        response = {
            "status": "success",
            "UserName": UserName,
            "Caption": caption,
            "PostID": postID,
            "ProfilePic": ProfilePic,
            "PostPic": PostPic,
            "PostType": PostType,
            "PostTime": PostTime,
        }

    except Exception as e:
        print(e)
        response = {
            "status": "error"
        }

    return json.dumps(response)


@app.route("/Retrieve_Notification/<string:myUserID>/<string:Day>")
def Retrieve_Notification(myUserID, Day):

    if request.url == f"http://ampplex-backened.herokuapp.com/Retrieve_Notification/<string:myUserID>/<string:Day>":
        return redirect("https://ampplex-backened.herokuapp.com/Retrieve_Notification/<string:myUserID>/<string:Day>")

    response = []

    month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'Mar': 5, 'Jun': 6,
             'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

    # Retrieving the notification of the user
    try:
        Notifications = database.child("User").child(
            myUserID).child("Notification").get().val()

        for notification in Notifications:
            Notification_Data = database.child("User").child(myUserID).child(
                "Notification").child(notification).get().val()

            try:
                Caption = Notification_Data["Caption"]
            except:
                # In case of no caption
                Caption = ""

            PostID = Notification_Data["PostID"]
            PostPic = Notification_Data["PostPic"]
            PostTime = Notification_Data["PostTime"]
            ProfilePic = Notification_Data["ProfilePic"]
            UserName = Notification_Data["UserName"]
            read = Notification_Data["read"]

            Month = int(month[PostTime.split(" ")[3]])
            Date = int(PostTime.split(" ")[4])
            Year = int(PostTime.split(" ")[5])

            Current_Month = int(str(date.today()).split("-")[1])
            Current_Date = int(str(date.today()).split("-")[2])
            Current_Year = int(str(date.today()).split("-")[0])

            if Current_Year == Year and Current_Month == Month and Current_Date == Date and Day == "Today":
                response.append(
                    {"Caption": Caption, "PostID": PostID, "PostPic": PostPic, "PostTime": PostTime, "ProfilePic": ProfilePic, "UserName": UserName, "read": read})

            elif Day != "Today":
                data = {
                    "Caption": Caption,
                    "PostID": PostID,
                    "PostPic": PostPic,
                    "PostTime": PostTime,
                    "ProfilePic": ProfilePic,
                    "UserName": UserName,
                    "read": read
                }

                response.append(data)

        if len(response) > 0:
            print(response)
            response = {
                "status": "success",
                "Notification": response
            }
        else:
            return "no_notifications_found"

    except Exception as e:
        print("Exception: ", e)
        return "no_notifications_found"

    return json.dumps(response)


@app.route('/Check_For_Notifications/<string:myUserID>', methods=['GET'])
def check_for_notifications(myUserID):
    if request.url == f"http://ampplex-backened.herokuapp.com/Check_For_Notifications/<string:myUserID>":
        return redirect("https://ampplex-backened.herokuapp.com/Check_For_Notifications/<string:myUserID>")

    try:
        Notifications = database.child("User").child(
            myUserID).child("Notification").get().val()

        if Notifications != None:
            for notification_ID in Notifications:
                Notification_Data = database.child("User").child(myUserID).child(
                    "Notification").child(notification_ID).get().val()

                read = Notification_Data["read"]

                # Checking if any notification is unread

                if read == False:
                    response = {
                        "status": "success",
                        "ShowNotification_Badge": True
                    }
                    return json.dumps(response)

        # If all notifications are read by the user or no notifications are found
        response = {
            "status": "success",
            "ShowNotification_Badge": False
        }

        return json.dumps(response)

    except Exception as e:
        print(e)
        response = {
            "status": "error"
        }

        return json.dumps(response)


@app.route('/Update_Notification_Status/<string:myUserID>/<string:postID>', methods=['GET'])
def update_notification_status(myUserID, postID):
    if request.url == f"http://ampplex-backened.herokuapp.com/Update_Notification_Status/<string:myUserID>/<string:postID>":
        return redirect("https://ampplex-backened.herokuapp.com/Update_Notification_Status/<string:myUserID>/<string:postID>")

    try:
        Notifications = database.child("User").child(
            myUserID).child("Notification").get().val()

        if Notifications != None:
            for notification_ID in Notifications:
                Notification_Data = database.child("User").child(myUserID).child(
                    "Notification").child(notification_ID).get().val()

                PostID = Notification_Data["PostID"]

                if PostID == postID:
                    database.child("User").child(myUserID).child(
                        "Notification").child(notification_ID).update({"read": True})

        response = {
            "status": "success"
        }

        return json.dumps(response)

    except Exception as e:
        print(e)
        response = {
            "status": "error"
        }

        return json.dumps(response)


@app.route('/getAssignments/<string:userID>/<string:postID>/<int:asssignment_Num>', methods=['GET'])
def getAssignments(userID, postID, asssignment_Num):

    # asssignment_Num - assignment number to be retrieved

    if request.url == f"http://ampplex-backened.herokuapp.com/getAssignments/<string:userID>/<string:postID>/<int:asssignment_Num>":
        return redirect("https://ampplex-backened.herokuapp.com/getAssignments/<string:userID>/<string:postID>/<int:asssignment_Num>")

    Assignment = database.child("User").child(userID).child(
        "Post").child(postID).child("Assignment").get().val()

    if Assignment == None:
        return "no_assignments_found"

    Subject = ""
    Questions = []
    response = []
    counter = 0

    # Retreiving Subject from the database. TimeComplexity: Both worst and best case is O(1)
    for key, value in Assignment.items():
        Subject = key

    # Retreiving Subject from the database. TimeComplexity: worst case is O(n) and best case is O(1)
    for key, value in Assignment[Subject].items():
        if counter == asssignment_Num:
            Questions.append(key)
            break
        counter += 1
        print(counter)

    counter = 0

    for question in Questions:
        if counter == asssignment_Num:
            Correctoption = Assignment[Subject][question]["Correctoption"]
            option1 = Assignment[Subject][question]["option1"]
            option2 = Assignment[Subject][question]["option2"]
            option3 = Assignment[Subject][question]["option3"]
            option4 = Assignment[Subject][question]["option4"]
            question_mark_isThere = Assignment[Subject][question]["question_mark_isThere"]

            data = {"CorrectOption": Correctoption, "option1": option1, "option2": option2,
                    "option3": option3, "option4": option4, "question_mark_isThere": question_mark_isThere, "question": question}

            response.append(data)
            break
        print(counter)

        counter += 1

    response = {"Subject": Subject, "Questions": response}

    return json.dumps(response)


def getResponse(url):

    response = []

    resp = requests.get(url).json()

    # Retreiving news articles from the API

    print("INTEGRATION : ",resp)
    for i in range(len(resp['articles'])):
        Caption = str(resp['articles'][i]["title"]) + '\n' + \
            str(resp['articles'][i]["description"])
        ImgPath = resp['articles'][i]["urlToImage"]
        Type = "News"
        if ImgPath != None:
            response.append(
                {"Caption": Caption, "ImgPath": ImgPath, "Type": Type})

    return response


@app.route('/GetNewsFeed/<string:DATA_LENGTH>', methods=['GET'])
def getNewsFeed(DATA_LENGTH):
    # if request.url == f"http://ampplex-backened.herokuapp.com/GetNewsFeed/<string:DATA_LENGTH>":
    #     return redirect("https://ampplex-backened.herokuapp.com/GetNewsFeed/<string:DATA_LENGTH>")

    response = []  # List to store all the news

    DATA_LENGTH = int(DATA_LENGTH)

    # CategoryList for students
    CategoryList = ["technology", "science", "education",
                    "elon musk", "health", "sports", "business", "entrepreneurship", "Software Development", "Google", "Twitter"]

    UserPosts = getPostJson()  # Getting user posts
    response += UserPosts  # Appending user posts to the response list

    for i in range(len(CategoryList)):

        # Fetching news articles from the News API
        try:
            url = f"https://newsapi.org/v2/everything?q={CategoryList[i]}&sortBy=publishedAt&apiKey=49490b8a2fed496ebfc5a63a7ca3a96f"
            # Retreiving news articles from the API
            # Appending the news articles to the response list
            if getResponse(url) != None:
                response = response + getResponse(url)

        except:
            print("Url 1 is not working")
            try:
                # If the Above url is not working, then the below url is used
                url = f"https://newsapi.org/v2/everything?q={CategoryList[i]}&sortBy=publishedAt&apiKey=039ca0b02106448b8b0f9b31cd569302"

                # Retreiving news articles from the API
                # Appending the news articles to the response list
                if getResponse(url) != None:
                    response = response + getResponse(url)
            except:
                print("Url 2 is not working")
                # If the Above url is not working, then the below url is used
                url = f"https://newsapi.org/v2/everything?q={CategoryList[i]}&sortBy=publishedAt&apiKey=63eb5520a6674e8c999ecdceab7d6bc8"

                # Retreiving news articles from the API
                # Appending the news articles to the response list
                if getResponse(url) != None:
                    response = response + getResponse(url)

    # Returning UserPosts and news articles as a response in the form of json object
    return json.dumps(response[DATA_LENGTH - 20: DATA_LENGTH])


if __name__ == '__main__':
    # Server_Assistant("STARTING AMPPLEX SERVER")
    app.run(debug=True, host='0.0.0.0', port=4567)
