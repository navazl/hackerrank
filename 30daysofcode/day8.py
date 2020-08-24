# Enter your code here. Read input from STDIN. Print output to STDOUT

phonebook = dict()
n = int(input())
for i in range (0, n):
    name = input()
    pair = name.split()
    phonebook[pair[0]] = pair[1]
while True:
    try:
        name = input()
    except EOFError as e:
        break
    if name not in phonebook.keys():
        print("Not found")
    else:
        print(f"{name}={phonebook[name]}")