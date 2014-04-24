import sys, time

class Online():
    users = []
    def add(user):
        flag = False
        for i in range(0,len(Online.users)):
            if Online.users[i][0] == user:
                ts = time.time()
                Online.users[i][1] = ts
                flag = True
        if flag == False:
            ts = time.time()
            Online.users.append([user,ts])

        print(Online.users)

    def remove():
        ts = time.time()
        ts = ts-3
        removed = []
        for i in range(0,len(Online.users)):
            if Online.users[i][1] < ts:
                removed.append(i) 
        for i in range(0,len(removed)):
               Online.users.pop(i)
