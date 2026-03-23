#API- application programming interface
#allows computers to share data  between devices Via internet

#functions that let us share data back and forth over the internet

import requests # modules--> is a object with methods and properties that were already written/pre-written

data = requests.get('https://en.wikipedia.org/wiki/Invincible_(TV_series)')

print(data)