from password_manager import PasswordManager

#Testing

#Create Accounts
pws = PasswordManager("");
pws.add("lnclndsll@gmail.com", "GoBucks!");
pws.add("email@email.email", "MyPassword@123");

pws.add("MyName", "HelloThere");
pws.add("myname", "hellothere");

print(pws);

#Test username and password combos
#Should be true
print(pws.validate("lnclndsll@gmail.com", "GoBucks!"));
print(pws.validate("email@email.email", "MyPassword@123"));

#Should be false
print(pws.validate("lnclndsll@gmail.com", "MyPassword@123"));
print(pws.validate("email@email.email", "GoBucks!"));
print(pws.validate("lnclndsll", "MyPassword@123"));
print(pws.validate("email", "GoBucks!"));

try:
    pws.add("lnclndsll@gmail.com", "ClassOf2026")
    print("Duplicate username incorrectly accepted")
except KeyError:
    print("Duplicate username correctly rejected")

while True:
    username = input("Enter username: ");
    password = input("Enter password: ");

    if pws.validate(username, password):
        print("Congrats! You're in.")
    else:
        print("Wrong! Try again.")