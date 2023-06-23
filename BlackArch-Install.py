import os
from os import system as cmd
from time import sleep as wait

cwd = os.getcwd()


def Start():
    print("Setting Up Repository...")
    wait(1)
    cmd("curl -O https://blackarch.org/strap.sh")

    wait(1)
    cmd("echo 5ea40d49ecd14c2e024deecf90605426db97ea0c strap.sh | sha1sum -c")

    wait(1)
    cmd("chmod +x strap.sh")

    wait(1)
    cmd("sudo ./strap.sh")

    wait(1)
    print("Updating pacman Repository...")

    wait(1)
    cmd("sudo pacman -Syu")


    tools_list = open(f"{cwd}/tools_list.txt", 'r')
    content = tools_list.readlines()

    for line in content:
        cmd(f"pacman -S --noconfirm {line}")

Start()
