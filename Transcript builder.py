from bs4 import BeautifulSoup
import urllib

transcriptaccess = 'http://video.google.com/timedtext?lang=en&v=' # base transcript url need to add video name to end
urls = open('Video Src.txt', 'r') #All the URLs for the videos
names = open('File names.txt', 'r') #Names of the files/ Headings
f = open("All Video Transcript.txt", 'w') # where to output to
for url in urls:

    r = urllib.urlopen(transcriptaccess+url) # path to transcript website
    soup = BeautifulSoup(r, "lxml") # assign the HTML tree to soup
    text = soup.find_all('text') # Find all lines text in them

    # Prints the chapter of the proceeding text
    print >> f,"------------------------------------------------------------"
    print >> f,names.readline()
    print >> f,"------------------------------------------------------------"
    for x in text: # go through each line
        cnv = str(x) # Convert to string format
        first = cnv.index
        cnv = cnv.replace('\n', ' ').replace('\r', '') #Remove new lines
        cnv = cnv.split('>') #get rid of HTML from left of text
        cnv = cnv[1].split('<') #get rid of HTML from right of text from second element in array
        print >> f,cnv[0] #print cleaned element from array


