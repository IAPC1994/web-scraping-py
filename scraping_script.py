import re
from colorama import Fore
import requests

website = "https://www.vulnhub.com"
result = requests.get(website)
content = result.text

pattern = r"/entry/[\w-]*"
repeated_machines = re.findall(pattern, str(content))

without_duplicate = list(set(repeated_machines))

final_machines = []

for x in without_duplicate:
    name_machine = x.replace("/entry/", "")
    final_machines.append(name_machine)
    print(name_machine)

# Validate if is a new machine on the website
    
machine_noob = "noob-1"
noob_exist = False

for y in final_machines:
    if y == machine_noob:
        noob_exist = True
        break

green_color = Fore.GREEN
yellow_color = Fore.YELLOW

if noob_exist == True:
    print("\n" + green_color + "There is not a new machine")
else:
    print("\n" +yellow_color + "New machine detected")