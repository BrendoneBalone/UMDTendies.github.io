from lxml import html
import requests
import fileinput

page = requests.get('http://dining.umd.edu/#specials')
tree = html.fromstring(page.content)
specials = tree.xpath('//*[@id="specials"]/div[1]/div[1]/div[3]/text()')
i = 2
done = False
day = ""
while not done: 
    oldSize = len(specials)
    specials += tree.xpath('//*[@id="specials"]/div[' + str(i) + ']/div[2]/div[3]/text()') 
    if "Chicken Tenders" in specials[len(specials)-1]:
       d = tree.xpath('//*[@id="specials"]/div[' + str(i) + ']/div[2]/div[2]/span/text()') 
       day = d[0]
    if len(specials) == oldSize:
        done = True
    i += 1

day = day[:day.find('-')-1]

message = ""

if day != "":
    message = "Tendie day is " + day + "\n"
else:
    message = "No tendies this week :("

f = open("index.html", "w")

f.write("<html><head><link href=\"tendies.png\" rel=\"shortcut icon\" type=\"image/png\"/><link href=\"https://fonts.googleapis.com/css?family=Rubik+Mono+One|Montserrat\" rel=\"stylesheet\"/><link href=\"styles.css\" rel=\"stylesheet\"/><title>When Is Tendie Day?</title></head><body><div class=\"content\">" + message + "</div><div class=\"footer\">By BJG and JMT @ UMD - College Park</div></body></html>")
f.close()
