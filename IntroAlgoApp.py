import requests
import os
from bs4 import BeautifulSoup

web_page = 'https://ita.skanev.com'
r = requests.get(web_page)
htmlSoup = BeautifulSoup(r.text,"html.parser")
a = htmlSoup.find_all('a')

# First 3 links are intro,exercise,about

ref = []
for x in a:
    ref.append(str(x))

# print(ref[3])

# inputex=input()
path = 'C:\\Users\\nEW u\\Desktop\\study\\4th sem\\Design &Analysis of Algorithms'
os.chdir(path)
os.makedirs('Answers-Introduction-to-Algorithms')
# path=path+'\\Answers-Introduction-to-Algorithms'
extension = ''
for line in range(len(ref)):
    fragment = ref[line].split('"')
    extension = fragment[1]
    name = fragment[2].split('\n')
    req = requests.get(r.url+extension)
    try :
        req.raise_for_status()

        filename = name[1].strip()+'.html'
        file_object = open(filename,'wb')
        for chunk in req.iter_content(100000):
            file_object.write(chunk)
        file_object.close()
        print(extension)
    except Exception as exc:
        pass

    '''for index in range(9,22,1):
		extension=extension+ref[line][index]
	print(extension)
    extension=''
    '''

#extensions for problems differ normal

#C:\Users\nEW u\Desktop\study\4th sem\Design &Analysis of Algorithms




