import json

def fun(name, password):
    s = {"username": name, "password": password}
    jsonString = json.dumps(s)
    file = open("users.json", "w")
    file.write(jsonString)
    file.close()

if __name__ == '__main__':
    u = input("Username : ")
    p = input("Password : ")
    yo_fun = fun(u, p)
