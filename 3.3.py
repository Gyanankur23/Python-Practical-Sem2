import re
file = open('3.3.html', 'r') 
content = file.read()
file.close()
print("Matches for 's':", re.findall(r's', content))  