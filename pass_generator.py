import random
password_len = int(input("enter the password lenth:"))
password_type = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*?"
password = "".join(random.sample(password_type, password_len))
print(password)
