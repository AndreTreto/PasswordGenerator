from itertools import permutations

f = open("passwords.txt", "w")

f.truncate()

min_length = int(input("Minimum length of the passwords? :"))
amount = int(input("How many strings do you want per password? :"))
strings = input("Enter info with commas in between:")
stringlist = strings.split(',')

permutations = list(permutations(stringlist, amount))

f = open("passwords.txt", "a")

for i in permutations:
  if len(i) >= min_length:
    print(''.join(i))
    f.write(''.join(i) + '\n')
    
f.close()
