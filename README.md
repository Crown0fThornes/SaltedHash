# PasswordManager
PasswordManager works to manage the storage and validation of a set of username/password pairs.

PM uses a salted hash with a low probabilty of collision in order to avoid keeping a user's password in its memory. It only stores each user's name, randomly generated salt, and the resultant hash. It also does not permit duplicate usernames, raising a KeyError.

(Proof of concept only, not recommended for use with sensitive information)

See test.py to see how this PM can be used.

.add(username: str, password: str) adds a username and their respective password to the PM.
.validate(username: str, password: str) returns true if the username password pair exists in the PM, false otherwise. 

e.g.
passwords = PasswordManager()
passwords.add("user1", "pw1")
passwords.add("user2", "pw2")

username = input("Please enter your username: ")
password = input("Please enter your password: ")

passwords.validate(username, password)