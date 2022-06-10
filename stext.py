from random import shuffle
from rich import print
import os.path
import os

while True:
    print("[yellow]Example: 'file.txt'")
    print("[yellow]What's the file name (It must be in this folder)?:", end=" ")
    file_name = input("")
    is_file_exists = os.path.exists(file_name)

    if is_file_exists:
        break

    else:
        print(f"[bold red]'{file_name}' file does not exists!\n")

# shuffle strs
strings = [line.strip() for line in open('test.txt')]
shuffle(strings)

os.remove(f"{file_name}")

file = open(file_name, 'w')

for string in strings:
    file.write(string)
    file.write("\n")

file.close()

print("[bold green]Success!")
