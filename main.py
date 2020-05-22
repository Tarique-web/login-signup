import json

def greed():
    print('\n \t \t welcome yo my Terminal    !!')



def asking():
    print('\t 1.SIGNIN \n  \t 2.Login  ')
    userask = input(' Signup or login \n \n \t ')
    return userask

# def write_data(data):
#     with open("userdetails.json",'w') as f: 
#         json.dump(data, f) 


def signup():
    details = {}
    print("welcme to signup Page")
    username = input("\n \n  Enter your username  \t \t  " )
    email = input("\n \n \t Enter your email \t \t")
    password = input("\n \n  Enter your password  \t \t  " )
    password2 = input("\n \n  Confirm  your password  \t \t  " )
    profile = input("\n \n \t Enter your bio \t \t")
    if password == password2:
        if '@' in  password or '#' in password  :
            details['username'] = username
            details['password'] = password
            details['profile'] = profile
            details['email'] = email
            with open('/home/bhaskar/Documents/Question/userdetails.json','r') as json_file: 
                data = json.load(json_file)
                temp = data['users']
                for ex in temp:
                    if ex['email'] == email:
                        print("user allready exists please login")
                        return False
                temp.append(details)
            with open("/home/bhaskar/Documents/Question/userdetails.json",'w') as f: 
                json.dump(data, f)
            print("\n \t  You are succesfully signup ")
        else:
            print("password must contain '@' or '#' ")
            signup()
    else:
        print("Error!! \n password does't match " )
        signup()
    


def login():
    username = input("\n \n \t Enter your username  ")
    password = input("\n \n \t Enter your password  ")
    with open("/home/bhaskar/Documents/Question/userdetails.json",'r') as fd:
        users_data = json.load(fd)
        all_data = users_data["users"]
    for dics in all_data:
        if username == dics['username'] and password == dics['password']:
            print("\n \n \t \t \t  succesfully logged IN")
            print(dics)
            return dics
    return "User Not found"

def main():
    greed()
    deci = asking()
    if  deci == "signup":
        signup()
        login()
    elif  deci == "login":
        login()
    else:
        print("unvalid operation")

if __name__ == "__main__":
    main()
