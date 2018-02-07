# coding: utf-8
import sys
import urlgrabber
import MySQLdb

#db = MySQLdb.connect (user='weather', passwd='weather',
#                              host='127.0.0.1',
#                              db='weather')

db = MySQLdb.connect (user='duempi_weather', passwd='GQjgvfdbeNbNpRMWNGr4',
                              host='www.db4free.net',
                              db='duempi_weather')



line.split('>')[3]

orte.execute ("SELECT plz, ort FROM Orte")

data=orte.fetchall ()

for row in data :
    plz=row [0]
    ort=row [1]


    urlgrabber.urlgrab('http://www.wetterdienst.de/Deutschlandwetter/%ort/Aktuell',
    filename='/tmp/weather/'+ort+'.tmp', timeout=2, retry=2, reget='simple')

    tmpfile = file("/tmp/weather/"+ort+".tmp","r")

    for line in tmpfile:
# Temperatur
        line = tmpfile.seek(str('temp_2'))
        if line:
            line = line.head(line, 1)
            line = line.split('=')[6]
            line = line.split('>')[2]
            temp = line.split('°')[1]
            print temp

# aktuelles wetter
        line = tmpfile.seek(str('vorhersagezelle1'))
        if line:
            line = list(itertools.islice(itertools.ifilter(lambda n:n % 2 == '0, 1st'),1))
            aktuell = line.split('Title=')[2]
            print aktuell

# Niederschlag
        line = tmpfile.seek(str('vorhersagezelle1'))
        if line:
            line = list(itertools.islice(itertools.ifilter(lambda n: n % 2 == '0, 1st'), 1))
            line = line.seek('nieders_content_1')
            line = line.split('default')[2]
            line = line.split('>')[2]
            line = line.split('<')[1]
            niederschlag = line.split(' ')[1]
            print niederschlag

# Art#
        line = tmpfile.seek(str('vorhersagezelle1'))
        if line:
            line = list(itertools.islice(itertools.ifilter(lambda n: n % 2 == '0, 1st'), 1))
            line = line.seek('weather_symbol')
            line = line.split('default')[10]
            line = line.split(' \' ')[10]
            art = line.split(' \" ')[2]
            print art

# Druck
        line = tmpfile.seek(str('vorhersagezelle1'))
        if line:
            line = list(itertools.islice(itertools.ifilter(lambda n: n % 2 == '0, 1st'), 1))
            line = line.seek('hPa')
            line = line.split('>')[3]
            druck = line.split('hPa')[1]
            print druck

# Wind
        line = tmpfile.seek(str('vorhersagezelle1'))
        if line:
            line = list(itertools.islice(itertools.ifilter(lambda n: n % 2 == '0, 1st'), 1))
            line = line.seek('km/h')
            line = line.split(' \' ')[3]
            wind = line.split('>')[1]
            print wind

# Boeen
        line = tmpfile.seek(str('vorhersagezelle1'))
        if line:
            line = list(itertools.islice(itertools.ifilter(lambda n: n % 2 == '0, 1st'), 1))
            line = line.seek('km/h')
            line = line.split(' \' ')[7]
            boeen = line.split(' \' ')[2]
            print boeen

# Richtung
        line = tmpfile.seek(str('vorhersagezelle1'))
        if line:
            line = list(itertools.islice(itertools.ifilter(lambda n: n % 2 == '0, 1st'), 1))
            line = line.seek('km/h')
            line = line.split(' \' ')[3]
            line = line.split('>')[3]
            richtung = line.split('>')[1]
            print richtung

# Werte in DB schreiben

    wetter_data = {
            plz: plz,
            timestamp: time.time(),
            temp: temp,
            aktuell: aktuell,
            niederschlag: niederschlag;
            art: art,
            wind: wind,
            boeen: booen,
            richtung: richtung
    }

        wetter_sql= ("insert plz, timstamp, temp, aktuell, niederschlag, art, wind, boeen, richtung into wetter;")
        db.execute(wetter_sql, wetter_data)

        next(line)
    next(row)

db.close()


