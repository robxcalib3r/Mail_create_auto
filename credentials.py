def credentials(fileName, u_line, p_line):
    # with open(fileName, 'r') as file:
    #     _user = file.readline([1])
    #     print(_user)
    #     _pw = file.readline(14)
    #     print(_pw)

    fp = open(fileName)
    for i, line in enumerate(fp):
        if i==u_line:
            _user = line[:-1]
        elif i==p_line:
            _pw = line[:-1]
    fp.close()
    return _user, _pw

# print(credentials('credentials.txt', 5, 6))