import requests
import os
import sys
from bs4 import BeautifulSoup

#'C:\\Users\\nEW u\\Desktop\\study\\4th sem\\Design &Analysis of Algorithms'
path = input('Enter the path where to create a new folder :')
originalpath = os.getcwd()
os.chdir(path)
path = path+'\\Answers-Introduction-to-Algorithms'
if os.path.exists(path):
    sys.exit()

os.makedirs('Answers-Introduction-to-Algorithms')
os.chdir(path)

web_page = 'https://ita.skanev.com'
r = requests.get(web_page)
htmlSoup = BeautifulSoup(r.text, "html.parser")
a = htmlSoup.find_all('a')

# First 3 links are intro,exercise,about

ref = []
for x in a:
    ref.append(str(x))

extension = ''
for line in range(len(ref)):
    fragment = ref[line].split('"')
    extension = fragment[1]
    name = fragment[2].split('\n')
    req = requests.get(r.url+extension)
    try :
        req.raise_for_status()
        filename = name[1].strip()+'.html'
        if not os.path.isfile(filename):
            file_object = open(filename, 'wb')
            for chunk in req.iter_content(100000):
                file_object.write(chunk)
            file_object.close()
        print("currently copying", extension)
    except Exception as exc:
        pass

os.chdir(originalpath)
file_object = open('path.txt','wb')
file_object.write(path)





