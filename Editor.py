import tkinter,os,time
from colorama import Fore, init, Style
from tkinter import filedialog, messagebox
init(convert = True)
root = tkinter.Tk()
root.withdraw()
amount = 0
os.system("title https://github.com/kieronia // Combo Editor")
logo = f"""
{Fore.YELLOW} >  ██████╗ ██████╗ ███╗   ███╗██████╗  ██████╗ 
{Fore.YELLOW} > ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔═══██╗
{Fore.YELLOW} > ██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║
{Fore.YELLOW} > ██║     ██║   ██║██║╚██╔╝██║██╔══██╗██║   ██║
{Fore.YELLOW} > ╚██████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝╚██████╔╝
{Fore.YELLOW} >  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝  ╚═════╝ 
                                             
{Fore.YELLOW} > ███████╗██████╗ ██╗████████╗ ██████╗ ██████╗ 
{Fore.YELLOW} > ██╔════╝██╔══██╗██║╚══██╔══╝██╔═══██╗██╔══██╗
{Fore.YELLOW} > █████╗  ██║  ██║██║   ██║   ██║   ██║██████╔╝
{Fore.YELLOW} > ██╔══╝  ██║  ██║██║   ██║   ██║   ██║██╔══██╗
{Fore.YELLOW} > ███████╗██████╔╝██║   ██║   ╚██████╔╝██║  ██║
{Fore.YELLOW} > ╚══════╝╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
"""#i was gonna do something fancy but liked the yellow theme so just ignore xd
print(logo)

option = input(" > Assuming your list is username:password\n > How would you like it sorted?\n > (1) username\n > (2) password \n > (3) password:username\n >  ")

os.system("cls")
print(logo)
print(f" > Assuming your list is username:password\n > how would you like it sorted?\n > (1) username\n > (2) password \n > (3) password:username\n > ({option})\n")
#looks smooth xd
if "1" in option:
    print(" > Sorting to get usernames")
elif "2" in option:
    print(" > Sorting to get passwords!")
elif "3" in option:
    print(" > Sorting to make it password:username")
else:
    input(" > Invalid option, press enter to quit\n > ")
    os._exit(0)

time.sleep(0.5)
print(" > Select your combo file!")
time.sleep(0.8)

filepath = filedialog.askopenfile(parent=root, mode='rb', title='Select the file containing the combos!',
                            filetype=(("txt", "*.txt"), ("All files", "*.txt")))

nameoffinalfile = input(" > Name of file to store the results in?\n > ")

finalfileextension = nameoffinalfile[-4:]
if finalfileextension != ".txt": #detecting if the full file name has been inputted..
    nameoffinalfile = nameoffinalfile+".txt"

with open(filepath.name) as f:
    for i, l in enumerate(f):
        pass
totalamount = i + 1

print(" > Sorting Now!")
time.sleep(1)
with open(filepath.name, 'r') as f:
    for line in f.readlines():
        try:
            print(f" > {line.strip()}")
            emailandpass = line.strip().split(':') 
            email = emailandpass[0]
            password = emailandpass[1]
            f = open(nameoffinalfile, "a")
            if "1" in option:
                f.write(f"{email} \n")
            elif "2" in option:
                f.write(f"{password} \n")
            elif "3" in option:
                f.write(f"{password}:{email} \n")
            f.close()
        except:
            pass
        amount = amount + 1
        os.system(f"title Combo Editor // [{amount}] : [{totalamount}]")
        #pretty sure this slowed it down A LOT but it looks smoothe so :flushed:


print(" > Finished sorting")
os.system(nameoffinalfile)


