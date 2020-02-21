import re

data = []
user = []
pswd = []

f = open("info.txt","r")

for line in f:
    data.append(line.strip())

for item in data:
    res = re.search(r"(.*)\.(.*)",str(item))
    user.append(res[1])
    pswd.append(res[2])

db = dict(zip(user,pswd))
u = input("Enter username : ")
p = input("Enter Password : ")

try:
    if db[u] == p:
        print("Password Verified - You are welcome")
    else:
        print("Wrong user id or password...")
except KeyError:
    print("Sorry! I am sure there is a problem in user id or password.")
    
