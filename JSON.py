import json, os
from pathlib import Path
from itertools import islice
import shutil

path =  'D:\\Desktop\\temp'
filepath = path + '\\jsonObjectFile.json'

s = str() # input key
txtcond = "0"
advm = False

routing = "route"
rlen = len(routing)

print("Type 1 or print help | man to get help.")
print("Introduce your arguments.")

while s != txtcond:
    print(routing + ">>>", end = ' ')
    s = str(input())
    if txtcond != s:
        
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
            print("\n\tProgram created by LoXewyX.\n")
            
        elif s == "2":
            
            if(advm == False):
                print("\n\tAdvanced mode enabled.\n")
                advm = True
            else:
                print("\n\tSimple mode enabled.\n")
                advm = False
        elif s == "t" and advm:
            
            print()
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
                    if "file.py" in line: print(" (running)", end = '')
                    print()
                if next(iterator, None):
                    print(f'... length_limit, {length_limit}, reached, counted:')
                print(f'\n\t{directories} directories' + (f', {files} files' if files else ''))
            
            if os.path.exists(path):
                tree(path)
            else:
                print("\tDirectory does not exist! Type 5 to restore all files.")
            print()
        
        elif s == "r" and advm:
            
            def create():
                if not os.path.exists(path):
                    os.mkdir('D:\\Desktop\\temp')

            data = {}

            with open(filepath, 'w') as values:
                json.dump(data, values)
                
            if not(os.path.exists(path)):
                create()
            
            def check(s = str()):
                if(os.path.exists(path)): 
                    print("\n\t" + s + "\n")
                else:
                    print("\n\tCould not create the file.\n")
            
            routing += "\\repair"
            if not(os.path.exists(path)):
                create()
                check("Created successfully!")
            else:
                print("\n\tFile exists. Would you like to repair it [Y/n]?\n")
                print(routing + ">>>", end = ' ')
                answer = input()
                while True:
                    if answer.lower() == "y":
                        create()
                        check("Repaired successfully!")
                        break
                    elif answer.lower() == "n":
                        break
                    else:
                        print("\n\tBad input! Would you like to repair it [Y/n]?\n")
                        print(routing + ">>>", end = ' ')
                        answer = input()
                
        elif s == "p" and advm:
            
            def remove():
                shutil.rmtree(path)
                if not os.path.exists(path): 
                    print("\n\tPurged successfully!\n")
                else:
                    print("\n\tCould not purge the file. Try manually.\n")
             
            routing += "\\remove"
            print("\n\tWould you like to remove all files [Y/n]?\n")
            print(routing + ">>>", end = ' ')
            answer = input()
            while True:
                if answer.lower() == "y":
                    remove()
                    break
                elif answer.lower() == "n":
                    break
                else:
                    print("\n\tBad input! Would you like to remove all files [Y/n]?\n")
                    print(routing + ">>>", end = ' ')
                    answer = input()
            
        elif s == "c" and advm:
            os.system('cls' if os.name == 'nt' else 'clear')
            
        elif s == "3":
            
            with open(filepath, 'r') as f:
                store = json.load(f)
                if(len(store) == 0):
                    print("\n\tJSON is empty!\n")
                else: print(json.dumps(store, indent = 3, sort_keys=True)[1:-1])
        
        elif s == "4":
            
            routing += "/addJSON"
            
            print("Introduce your chain name.")
            print(routing + ">>>", end = ' ')
            key = input()
            
            print("Introduce your value name.")
            print(routing + ">>>", end = ' ')
            value = input()
            
            try:
                value = float(value)
                if(value == int(value)):
                    value = int(value)
            except ValueError:
                pass
            
            if key != "" or value != "":
                with open(filepath, 'r') as f:
                    store = json.load(f)
                
                store.__setitem__(key, value)
                
                with open(filepath, 'w') as f:
                    json.dump(store, f)

        
        elif s == "5": 
            
            routing += "\\modifyJSON"
            
            with open(filepath, 'r') as f:
                store = json.load(f)

            print("Insert the key you want to modify.\nLeave it blank to exit.")
            
            error = bool(False)
            answer = str()
            
            while not answer in store:
                if error:
                    print("\n\tKey not found!\n")
                error = True
                
                print(routing + ">>>", end = ' ')
                answer = input()
                if(answer == ""): break
            if(answer != ""):
                print("\n\tInto? Default: ", store[answer], "\n")
                print(routing + ">>>", end = ' ')
                imp = input()
                try:
                    imp = float(imp)
                    if(imp == int(imp)):
                        imp = int(imp)
                except ValueError:
                    pass
                
                if(imp != ""):     
                    with open(filepath, 'r+') as f:
                        store[answer] = imp
                        f.seek(0)
                        json.dump(store, f, indent = 4)
                        f.truncate()
            
        elif s == "6":
            
            routing += "/removeJSON"
            
            print("Introduce your chain name.")
            print(routing + ">>>", end = ' ')
            key = input()
            
            with open(filepath, 'r') as f:
                store = json.load(f)
            
            if key in store.keys():
                del(store[key])
                with open(filepath, 'w') as f:
                    json.dump(store, f)
            elif(key == ""):
                pass
            else: print("\"" + key + "\" does not exist.")
            
        else: print("\n\tError on typing! Try 1 or help.\n")
        routing = routing[:rlen]

print("\n\tProgram EXIT with success!\n")