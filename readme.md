#### 1. Run Program:
```
python main.py
```

#### 2. Run Test
```
python test.py
```

#### 3. The menu
```text
1. New user
2. Validate password
3. Login
4. Change password
5. Quit
```
* You must choose the mode number from 1 to 5

* Mode number 1: You have to enter a username and a password. This data will save to file 'password.txt' in json format. 
Example: {'username': 'your_username', 'password': 'your_password'}

* Mode number 2: You have to enter any passwords until you enter the right password that matched the rules(below)
* Mode number 3: You have to enter a password, it will encrypt and compare it with the password in the file 'password.txt'.
* Mode number 4: You enter a new password, it will encrypt and override data in the file.
* Mode number 5: Quit program.

#### 4. The rules

- The password must not contain whitespace
- The password must be at least 6 characters.
- The password must contain at least one uppercase and lowercase letter.
- The password must have at least one digit and symbol.