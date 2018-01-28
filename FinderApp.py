import os
import webbrowser

file_object = open('path.txt', 'r')
# Set ANY path of your choice instead
path = file_object.read()+'\\Answers-Introduction-to-Algorithms'

org_path = os.getcwd()
os.chdir(path)

key = input('Type y*x.x.x where y=e for exercises and p for problems\n')

# typ : type (exercise/problems)
# numb : Question numb
[typ, numb] = key.split("*")
print(numb,typ)
if typ is 'p':
    #
    frag = numb.split('.')
    print(frag)
    numb = frag[0] + "." + frag[1]

#
path ='file:///C:/Users/nEW%20u/Desktop/study/4th%20sem/Design%20&Analysis%20of%20Algorithms/Answers-Introduction-to-Algorithms/'
webbrowser.open(path+numb+'.html')
