if __name__ == '__main__':
    l = []
    N = int(input())
    for i in range (0, N):
        command = input('').split()
        if command[0] == 'insert':
            l.insert(int(command[1]), int(command[2]))
        if command[0] == 'remove':
            l.remove(int(command[1]))
        if command[0] == 'append':
            l.append(int(command[1]))
        if command[0] == 'sort':
            l.sort()
        if command[0] == 'pop':
            l.pop()
        if command[0] == 'reverse':
            l.reverse()
        if command[0] == 'print':
            print(l)
