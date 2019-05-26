import os

def helpFunc():
    os.system('cls')
    print('-_'*15 + 'Help' + '_-'*15)
    print('Wellcome to the CMD Project')
    print('Hello ' + os.getlogin())
    print('For clear Screen = cls')
    print('For List of Directory = dir')
    print('For goto a Directory = cd')
    print('For back to Root = cd/')
    print('For Make a Directory = mdir')
    print('For Exit the Program = quit')
    print('-_'*40)
    print()

def clsfunc():
    os.system('cls')
    helpFunc()

def dirfunc():
    for items in os.listdir():
        print(items)

def chdirfunc(path_):
    os.chdir(path_)
    #print(os.getcwd())

def cdbackfunc():
    os.chdir('../')

def mdirfunc(name_):
    os.mkdir(name_)

helpFunc()
while True:
    command_ = input(os.getcwd() + '>')
    if command_ == 'cls':
        clsfunc()
    if command_ == 'dir':
        dirfunc()
    if command_ == 'cd':
        path_ = input ('Input you PATH:>')
        chdirfunc(path_)
    if command_ == 'cd/':
        cdbackfunc()
    if command_ == 'mdir':
        name_ = input ('Input your Directory Name:>')
        mdirfunc(name_)
    if command_ == 'quit':
        print('THANK YOU FOR CHOICE US')
        ans = input('Are you sure? (y/n)')
        if ans == str.lower('y'):
            os.system('cls')
            break
