import json, os
from pathlib import Path
from itertools import islice
import shutil

### cannot do the array store

from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()

path =  filedialog.askdirectory()
if not path.split('/')[-1] == "temp":
    path += '/temp'
currentfile = str("jsonObjectFile.json")
filepath = str(path + '/' + currentfile)

s = str()
advm = bool(False)
advs = ">"

finalroute = "route"
routing = finalroute

rlen = len(routing)

def create():
    if not os.path.exists(path):
        os.mkdir(path)

    data = {}

    with open(filepath, 'w') as values:
        json.dump(data, values)
        
def check(s = str()):
    if(os.path.exists(path)): 
        print("\n\t" + s + "\n")
    else:
        print("\n\tCould not create the file.\n")
        
def remove():
    if os.path.exists(path):
        
        shutil.rmtree(path)
        if not os.path.exists(path): 
            print("\n\tPurged successfully!\n")
        else:
            print("\n\tCould not purge the file. Try manually.\n")
            
    else: print("\n\tThe current directory does not exist.\n")

print("\n\tType 1 or print help | man to get help.")
print("\tIntroduce your arguments.\n")

while s != "0" and s != "exit":
    
    filebrks = bool(True)
    
    try:
        with open(filepath, 'r') as f:
            store = json.load(f)
            filebrks = bool(False)
    except: pass
    
    if not os.path.exists(path):
        routing = "📂❌ " + finalroute
        warntype = 0
    
    elif filebrks:
        routing = "📃❌ " + finalroute
        warntype = 1
    
    elif len(store) == 0: 
            routing = "📭❌ " + finalroute
            warntype = 2
            
    else:
        routing = "✅ " + finalroute
        rlen = len(routing)
        warntype = -1
    
    print(routing + advs, end = ' ')  
    s = str(input())
        
    if s == "":
        
        print(end = '')
        
    elif s == "1" or s == "help" or s == "man":
        
        print("0 - exit.")
        print("1 - help.")
        if not advm:
            print("2 - advanced mode.")
        else:
            print("2 - simple mode.")
        print("3 - read JSON keys.")
        print("4 - add JSON key.")
        print("5 - overwrite JSON key.")
        print("6 - remove JSON key.")
        if advm:
            print("t - tree.")
            print("r - restore file health.")
            print("p - purge all files.")
            print("c - clear teminal")
        if advm or warntype != -1:
            print("e - shows possible errors")
        print("\n\tProgram created by LoXewyX.\n")
        
    elif s == "2" or s == "en" or s == "enabl" or s == "enable":
        
        if(advm == False):
            advs = ">>>"
            advm = True
        else:
            advs = ">"
            advm = False
            
    elif (s == "t" or s == "tree") and advm:
        
        space =  '    '
        branch = '│   '
        tee =    '├── '
        last =   '└── '
        
        def tree(dir_path: Path, level: int=-1, limit_to_directories: bool=False,
            length_limit: int=1000):
            dir_path = Path(dir_path)
            files = 0
            directories = 0
        
            def inner(dir_path: Path, prefix: str='', level=-1):
                nonlocal files, directories
                if not level: 
                    return
                if limit_to_directories:
                    contents = [d for d in dir_path.iterdir() if d.is_dir()]
                else: 
                    contents = list(dir_path.iterdir())
                pointers = [tee] * (len(contents) - 1) + [last]
                for pointer, path in zip(pointers, contents):
                    if path.is_dir():
                        yield prefix + pointer + path.name
                        directories += 1
                        extension = branch if pointer == tee else space 
                        yield from inner(path, prefix=prefix+extension, level=level-1)
                    elif not limit_to_directories:
                        yield prefix + pointer + path.name
                        files += 1
            print(dir_path.name)
            iterator = inner(dir_path, level=level)
            for line in islice(iterator, length_limit):
                print(line, end = '')
                if currentfile in line: print(" (in use)", end = '')
                print()
            if next(iterator, None):
                print(f'... length_limit, {length_limit}, reached, counted:')
            print(f'\n\t{directories} directories' + (f', {files} files' if files else ''))
        
        print()    
        
        if os.path.exists(path):
            tree(path)
        else:
            print("\tDirectory does not exist! Type r to restore all files.")
        print()
    
    elif (s == "r" or s == "repair") and advm:
        
        routing += "\\repair"
        
        if os.path.exists(path) and Path(filepath).is_file():
            print("\n\tWould you like to restore your document. It will be empty [Y/n]?\n")
            print(routing + advs, end = ' ')
            answer = input()
            while True:
                if answer.lower() == "y":
                    create()
                    check("\tRestored successfully!")
                    break
                elif answer.lower() == "n":
                    break
                else:
                    print("\n\tBad input! Would you like to create it [Y/n]?\n")
                    print(routing + advs, end = ' ')
                    answer = input()
        else:
            if not Path(filepath).is_file() and os.path.exists(path):
                print("\n\tWould you like to create an empty document? It will be empty [Y/n]?\n")
                created = True
            else:
                print("\n\tWould you like to create the file structure? Your document will be empty [Y/n]?\n")
            print(routing + advs, end = ' ')
            answer = input()
            while True:
                if answer.lower() == "y":
                    create()
                    check("\tCreated successfully!")
                    break
                elif answer.lower() == "n":
                    break
                else:
                    print("\n\tBad input! Would you like to repair it [Y/n]?\n")
                    print(routing + advs, end = ' ')
                    answer = input()
            
            
    elif (s == "p" or s == "purge" ) and advm:
            
        routing += "\\remove"
        print("\n\tWould you like to remove all files [Y/n]? 🗑️ ❗\n")
        print(routing + advs, end = ' ')
        answer = input()
        while True:
            if answer.lower() == "y":
                remove()
                break
            elif answer.lower() == "n":
                break
            else:
                print("\n\tBad input! Would you like to remove all files [Y/n]?\n")
                print(routing + advs, end = ' ')
                answer = input()
        
    elif (s == "c" or s == "clear" or s == "cls") and advm:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif (s == "e" or s == "error" or s == "err") and advm:
        
        if warntype == 0:
            print("\n\tStatus 0: Directory \"" + path + "\" does not exist!\n\tTry r to create the files.\n")
        elif warntype == 1:
            print("\n\tStatus 1: File \"" + currentfile + "\" does not exist!\n\tTry r to c restore the files.\n")
        elif warntype == 2:
            print("\n\tStatus 2: JSON is empty!\n\tTry 4 and fill the file.\n")
        else:
            print("\n\tStatus -1: Everything works fine!\n")
        
    elif s == "3" or s == "show":
        
        try:
            with open(filepath, 'r') as f:
                store = json.load(f)
                filebrks = bool(False)
        except: pass
        
        exists = bool(os.path.exists(path))
        
        if exists and not filebrks:
            
            with open(filepath, 'r') as f:
                if(len(store) == 0):
                    print("\n\tJSON is empty!\n")
                else: print(json.dumps(store, indent = 3, sort_keys=True)[1:-1])
                
        elif exists: print("\n\tDirectory does not exist! Type r to restore all files. ❗\n")
        else: print("\n\tFile does not exist! ❗\n")
    
    elif s == "4" or s == "add" or s == "create":
        
        try:
            with open(filepath, 'r') as f:
                store = json.load(f)
                filebrks = bool(False)
        except: pass
        
        exists = bool(os.path.exists(path))
        
        if exists and not filebrks:
            
            routing += "/addJSON"
            
            print("\n\tIntroduce your chain name.\n\tWrite [\"\"] to set a blank string.\n\tLeave it blank to exit.\n")
            print(routing + advs, end = ' ')
            key = input()
            if key != "":
                if key == "\"\"": key = ""
                print("\n\tNow, introduce your value name. 📩\n")
                print(routing + advs, end = ' ')
                value = input()
                if value == "\"\"": value = ""
                try:
                    value = float(value)
                    if(value == int(value)):
                        value = int(value)
                except ValueError:
                    pass
                
                if value != "":
                    with open(filepath, 'r') as f:
                        store = json.load(f)
                    
                    store.__setitem__(key, value)
                    
                    with open(filepath, 'w') as f:
                        json.dump(store, f)
                    
                    print("\n\tKey \"" + str(key) + "\": ", end = "")
                    if type(value) == str:
                        print("\"" + str(store[key]) + "\"", end = "")
                    else:
                        print("" + str(store[key]) + "", end = "")
                    print(" was added! 🥳\n")
                        
        elif exists: print("\n\tDirectory does not exist! Type r to restore all files. ❗\n")
        else: print("\n\tFile does not exist! ❗\n")
    
    elif s == "5" or s == "mod" or s == "modify": 
        
        empty = bool(False)
        
        with open(filepath, 'r') as f:
            store = json.load(f)
            if(len(store) == 0):
                empty = bool(True)
        
        if os.path.exists(path) and not empty and not filebrks:
        
            routing += "\\modifyJSON"
            
            with open(filepath, 'r') as f:
                store = json.load(f)
                
            print("\n\tIntroduce the key you want to modify.\n\tWrite [\"\"] to set a blank string.\n\tLeave it blank to exit.\n")
            error = bool(False)
            key = str("\"\"")
            
            while not key in store:
                if error:
                    print("\n\tKey " + key + " was not found. ❕\n")
                error = True
                
                print(routing + advs, end = ' ')
                key = input()
                if(key == ""): break
                
            if(key != ""):
                if key == "\"\"": key = ""
                print("\n\tInto? Default: ", store[key], " 📩\n")
                print(routing + advs, end = ' ')
                imp = input()
                try:
                    imp = float(imp)
                    if(imp == int(imp)):
                        imp = int(imp)
                except ValueError:
                    pass
                
                if(imp != ""):
                    if imp == "\"\"": imp = ""  
                    with open(filepath, 'r+') as f:
                        store[key] = imp
                        f.seek(0)
                        json.dump(store, f, indent = 4)
                        f.truncate()
                        print("\n\tKey \"" + key + "\" was updated with the value ", end = "")
                        if type(imp) == str:
                            print("\"" + str(imp) + "\"", end = "")
                        else:
                            print("" + str(imp) + "", end = "")
                        print("! 🥳\n")
                        
        elif not os.path.exists(path): print("\n\tDirectory does not exist! Type r to restore all files. ❗\n")
        else: print("\n\tJSON is empty! \n")         
        
        
    elif s == "6" or s == "rm" or s == "remov" or s == "remove":
        
        empty = bool(False)
        
        with open(filepath, 'r') as f:
            store = json.load(f)
            if(len(store) == 0):
                empty = bool(True)
        
        if os.path.exists(path) and not empty and not filebrks:
        
            routing += "/removeJSON"
            
            print("\n\tIntroduce your key name. ✍️\n")
            print(routing + advs, end = ' ')
            key = input()
            
            with open(filepath, 'r') as f:
                store = json.load(f)
            
            if key in store.keys():
                
                print("\n\tAre you sure you want to remove " + key + " [Y/n]? 🗑️\n")
                print(routing + advs, end = ' ')
                answer = input()
                while True:
                    if answer.lower() == "y":
                        del(store[key])
                        with open(filepath, 'w') as f:
                            json.dump(store, f)
                        if not key in store.keys(): print("\n\tRemoved successfully! 🥳\n")
                        else: print("\n\tError on removing! Try it via manually. ❗\n")
                        break
                    elif answer.lower() == "n":
                        break
                    else:
                        print("\n\tBad input! Would you like to repair it [Y/n]? ⚒️\n")
                        print(routing + advs, end = ' ')
                        answer = input()
                    
            elif(key == ""): pass
            else: print("\n\tKey \"" + key + "\" does not exist. ❕\n")
        
        elif not os.path.exists(path): print("\n\tDirectory does not exist! Type r to restore all files. 🔁\n")
        else: print("\n\tJSON is empty! \n")   
        
    elif(s != "0" and s != "exit"): print("\n\tError on typing! Try 1 or help. 📖\n")
    routing = routing[:rlen]

print("\n\tProgram EXIT with success. Have a nice day!\n")
