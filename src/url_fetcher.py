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


####################################### IMPORTS
import re
import urllib
import time
####################################### IMPORTS

####################################### VARIABLES
x = 'youtube' # keyword for selecting links
####################################### VARIABLES


main_url = raw_input('Enter the URL you want to fetch: ') # ask for main URL
filename_without_txt = raw_input('Enter the desired filename: ')
start = time.time()
original_file = filename_without_txt + '.txt'
edited_file = filename_without_txt + '_edited.txt'
html_source = urllib.urlopen(main_url).read(200000) # read up URL
linkslist = re.findall('<a href=(.*?)>',html_source) # look up all links in source


for link in linkslist:
    if x in link:
        savetotxt = str(link)
        f = open(original_file, 'a')
        f.write(savetotxt + '\n' )
        
    

o = open(edited_file, 'a') #open for append
for line in open(original_file):
    line = line.replace('"/showyoutube.asp?id=', '')
    line = line.replace('&hl=nl&fs=1&" target="syncframe" onclick="document.getElementById(\'sync\').style.left=250;document.getElementById(\'sync\').style.top=tempY-80;document.getElementById(\'sync\').style.display=\'block\';"', '')
    line = line.replace('&hl=nl&fs=1&" target="syncframe" onclick="document.getElementById(\'sync\').style.left=250;document.getElementById(\'sync\').style.top=tempY+20;document.getElementById(\'sync\').style.display=\'block\';"', '')
    line = line.replace('&feature=av2n', '')
    line = line.replace('&ob=av2n', '')
    line = line.replace('v/', 'watch?v=')
    line = line.replace('&tracker=False', '')
    o.write(line)
    

o.close()

o_file = open(original_file)
e_file = open(edited_file)

o_lines = 0
for line in o_file:
# line is ignored here, but it contains each line of the file,
# including the new line
    o_lines += 1
    
print "File1 has", o_lines, "lines in it."

e_lines = 0
for line in e_file:
    e_lines += 1
    
print "File2 has", e_lines, "lines in it."

if e_lines == o_lines:
    print "All set, captain!"

print 'These files have been generated in %s seconds.' % (time.time() - start)

# end of yigtuber
