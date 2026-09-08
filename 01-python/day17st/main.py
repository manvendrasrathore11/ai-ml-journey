# class User :
#     pass        #  python interpreter accept to be something in function defintion in not  empty
#
# user_1 = User()
#
# user_1.id  = "001"
# user_1.username = "manvendra"
#
# print(user_1.username)
#
# user_2 = User
# user_2.id  = "002"
# user_2.username = "simmu"
#
# print(user_2.username)


#  now to simplify this problem we learn what is constructor
# also know as initialize an object
# in this case we set variable or counters to they're  starting values
#  to intitialize we use special function

# class User :
#     def __init__(self,seats):       #  this function is call everytime when we creat new object
#         self.seats = seats                    # self is object and seats is attributes

# example of constructor

class User:
    def __init__(self, user_id , name ):
        self.id = user_id
        self.name = name
        self.followers = 0 #  give default value to an attributes. no  need to pass in class callinhg
        self.following = 0

    def follow(self,user):
        user.followers +=1
        self.following +=1






user1 = User("001","manvendra")
user2 = User("002","simmu")

user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
