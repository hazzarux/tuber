#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.



import re
import urllib
import time

x = 'youtube' # keyword for selecting links
mainURL = raw_input('Enter the URL you want to fetch: ') # ask for main URL
filename_without_txt = raw_input('Enter the desired filename: ')
start = time.time()
filename = filename_without_txt + '.txt'
filename2 = filename_without_txt + '_edited.txt'
htmlSource = urllib.urlopen(mainURL).read(200000) # read up URL
linksList = re.findall('<a href=(.*?)>',htmlSource) # look up all links in source


for link in linksList:
    if x in link:
        savetotxt = str(link)
        f = open(filename, 'a')
        f.write(savetotxt + '\n' )
        
    

o = open(filename2, 'a') #open for append
for line in open(filename):
    line = line.replace('"/showyoutube.asp?id=', '')
    line = line.replace('&hl=nl&fs=1&" target="syncframe" onclick="document.getElementById(\'sync\').style.left=250;document.getElementById(\'sync\').style.top=tempY-80;document.getElementById(\'sync\').style.display=\'block\';"', '')
    line = line.replace('&hl=nl&fs=1&" target="syncframe" onclick="document.getElementById(\'sync\').style.left=250;document.getElementById(\'sync\').style.top=tempY+20;document.getElementById(\'sync\').style.display=\'block\';"', '')
    line = line.replace('&feature=av2n', '')
    line = line.replace('&ob=av2n', '')
    line = line.replace('v/', 'watch?v=')
    line = line.replace('&tracker=False', '')
    o.write(line)
    

o.close()

file1 = open(filename)
file2 = open(filename2)

lines1 = 0
for line in file1:
# line is ignored here, but it contains each line of the file,
# including the new line
    lines1 += 1
    
print "File1 has ", lines1, " lines in it."

lines2 = 0
for line in file2:
    lines2 += 1
    
print "File2 has ", lines2, " lines in it."

if lines2 == lines1:
    print "All set, captain!"

print 'These files have been generated in %s seconds.' % (time.time() - start)

# end of yigtuber
