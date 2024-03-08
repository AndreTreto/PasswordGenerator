from itertools import product

f = open("passwords.txt", "w") #opens file for truncating

f.truncate() #deletes anything previously stored in file

#gather information from user
min_length = int(input("Minimum length of the passwords? :"))
amount = input("How many strings do you want per password? :")
strings = input("Enter info with commas in between:")
stringlist = strings.split(',')

#calculate cartesian product using information provided
product = list(product(stringlist, repeat=int(amount)))

f = open("passwords.txt", "a") #open file for appending

#iterate through product list and join the elemts together to form a string
for i in product: 
    password = str(''.join(i)) 
    if len(password) >= min_length: #check length of string
      print(password)
      f.write(password + '\n') #write to file

f.close()
