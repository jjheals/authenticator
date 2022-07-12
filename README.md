# authenticator
This is a script that authenticates a user based on username and password credentials. Passwords are encrypted and stored in 'creds.txt'. 

I wanted a little more practice on hashing and encryption, and I wanted to do another small project, so I did some research on the hashlib python library and cryptography in python and wrote this script. The user has two options: create a new user or authenticate an existing user. Best practices were used where the on-screen error if the username OR password is incorrect is the same in both cases, there is a login attempt limit (3 attempts) and the passwords are hashed before being stored.

