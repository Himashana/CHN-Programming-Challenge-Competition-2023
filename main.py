import json
import hashlib

try:
    f = open('users.json', 'r')
    users = json.load(f)
    f.close()
except:
    print("Error reading 'users.json' file.")


def hashKey(key):
    key = key.encode()
    hashObj = hashlib.sha1(key)
    hashValue = hashObj.hexdigest()
    return hashValue

def checkUser(name, access_key):
    for user in users:
        if name.lower() == user.lower():
            if users[user]['access-key'] == hashKey(access_key):
                return [True, user, "NO_ERROR"]
            else:
                return [True, user, "ACCESS-KEY-INVALID-ERROR"]
            
    return [False, "NONE", "NO_ERROR"]


while True:
    name = input("Enter your name : ").strip(" ")
    access_key = input("Enter your access key : ").strip(" ")

    results = checkUser(name, access_key)

    if results[0]:
        if results[2] == "ACCESS-KEY-INVALID-ERROR":
            print("Sorry " + results[1] + ". Your access key is invalid.")
        else:
            print("Welcome " + results[1])
            print("Your credentials are valid.")
            break
    else:
        print("ERROE: User not found!")
