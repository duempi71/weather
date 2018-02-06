import sys
import urlgrabber
import MySQLdb

db = MySQLdb.connect (user='weather', passwd='weather',
                              host='127.0.0.1',
                              db='weather')

orte=db.cursor()

orte.execute ("SELECT plz, ort FROM Orte")

data=orte.fetchall ()

for row in data :
    plz=row [0]
    ort=row [1]


   urlgrabber.urlgrab('http://www.wetterdienst.de/Deutschlandwetter/%ort/Aktuell',
filename='/tmp/weather/'+ort+'.tmp', timeout=2, retry=2, reget='simple')

    tmpfile = file("/tmp/weather/"+ort+".tmp","r")
    for line in tmpfile:
        line = tmpfile.seek(str('vorhersagezelle1'))
        if line:
            line = tmpfile.find(str('img'))
            if line:
                line = list(itertools.islice(itertools.ifilter(lambda n:n % 2
=='0, 1st'),1))
                line = line.split('Title=')[2]

                print line

db.close()