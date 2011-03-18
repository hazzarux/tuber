import re, urllib
x = "youtube" # keyword for selecting links
mainURL = raw_input("Enter the URL you want to fetch: ") # ask for main URL
filename_without_txt = raw_input('Enter the desired filename: ')
filename = filename_without_txt + ".txt"
filename2 = filename_without_txt + "_edited.txt"
htmlSource = urllib.urlopen(mainURL).read(200000) # read up URL
linksList = re.findall('<a href=(.*?)>',htmlSource) # look up all links in source


for link in linksList:
    if x in link:
        savetotxt = str(link)
        f = open(filename, 'a')
        f.write(savetotxt + '\n' )
        pass
    pass

o = open(filename2, 'a') #open for append
for line in open(filename):
    line = line.replace('"/showyoutube.asp?id=', '')
    line = line.replace('&hl=nl&fs=1&" target="syncframe" onclick="document.getElementById(\'sync\').style.left=250;document.getElementById(\'sync\').style.top=tempY-80;document.getElementById(\'sync\').style.display=\'block\';"', '')
    line = line.replace('&hl=nl&fs=1&" target="syncframe" onclick="document.getElementById(\'sync\').style.left=250;document.getElementById(\'sync\').style.top=tempY+20;document.getElementById(\'sync\').style.display=\'block\';"', '')
    line = line.replace('&feature=av2n', '')
    line = line.replace('&ob=av2n', '')
    line = line.replace('v/', 'watch?v=')
    o.write(line)
    pass

o.close()

file1 = open(filename)
file2 = open(filename2)

lines1 = 0
for line in file1:
# line is ignored here, but it contains each line of the file,
# including the newline
    lines1 += 1
    pass
print "File1 has " + str(lines1) + " lines in it."

lines2 = 0
for line in file2:
    lines2 += 1
    pass
print "File2 has " + str(lines2) + " lines in it."

if lines2 == lines1:
    print "All set, captain!"
    pass

