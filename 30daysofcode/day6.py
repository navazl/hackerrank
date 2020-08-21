# Enter your code here. Read input from STDIN. Print output to STDOUT

number = int(input(''))
s = []
for i in range(0, number):
    s.append(str(input('')))

for p in range(0, number):
    palavra = s[p]
    n = len(palavra) 

    string_par = []
    string_impar = []

    for i in range(0, n, 2):
        string_par.append(palavra[i])

    for i in range(1, n, 2):
        string_impar.append(palavra[i])

    print(''.join(string_par) + ' ' + ''.join(string_impar))