import os
# print help & command on screen
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
    
# for clear screen 
def clsfunc():
    os.system('cls')
    helpFunc()

# for show list of directory
def dirfunc():
    for items in os.listdir():
        print(items)

# for change directory        
def chdirfunc(path_):
    os.chdir(path_)

# for come back from directory    
def cdbackfunc():
    os.chdir('../')

# for make a new directory   
def mdirfunc(name_):
    os.mkdir(name_)

# main of program    
helpFunc()
while True:
    command_ = input(os.getcwd() + '>>')
    if command_ == 'cls':
        clsfunc()
    if command_ == 'dir':
        dirfunc()
    if command_ == 'cd':
        path_ = input ('Input you PATH:>>')
        chdirfunc(path_)
    if command_ == 'cd/':
        cdbackfunc()
    if command_ == 'mdir':
        name_ = input ('Input your Directory Name:>>')
        mdirfunc(name_)
    if command_ == 'quit':
        print('THANK YOU FOR CHOICE US')
        ans = input('Are you sure? (y/n)')
        if ans == str.lower('y'):
            os.system('cls')
            break
