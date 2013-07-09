#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv, sys, time
from collections import defaultdict
from operator import itemgetter

def UnicodeDictReader(utf8_data, **kwargs):
    csv_reader = csv.DictReader(utf8_data, **kwargs)
    for row in csv_reader:
        try:
            yield dict([(key, unicode(value or "", "utf8")) for key, value in row.iteritems()])
        except:
            print "csv read line error"
            print row.items()
            print row
            raise

# src: http://stackoverflow.com/questions/653157/a-better-similarity-ranking-algorithm-for-variable-length-strings
def get_bigrams(string):
    '''
    Takes a string and returns a list of bigrams
    '''
    s = string.lower()
    return [s[i:i+2] for i in xrange(len(s) - 1)]

# src: http://stackoverflow.com/questions/653157/a-better-similarity-ranking-algorithm-for-variable-length-strings
def similarity(str1, str2):
    '''
    Perform bigram comparison between two strings
    and return a percentage match in decimal form
    '''
    pairs1 = get_bigrams(str1)
    pairs2 = get_bigrams(str2)
    union  = len(pairs1) + len(pairs2)
    hit_count = 0
    for x in pairs1:
        for y in pairs2:
            if x == y:
                hit_count += 1
                break
    return (2.0 * hit_count) / union

#print similarity("European Federation of Homeopathic Patients’ Associations (EFHPA)", "European Federation of Homeopathic Patients’ Associations")
#print similarity("European Federation of Users Rights Associations", "European Federation of Homeopathic Patients’ Associations")
#sys.exit(0)

def hdate(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d:%02d' % (hours, mins, secs)

names=defaultdict(int)
with open(sys.argv[1],'r') as csvfile:
    headers = csv.reader(csvfile).next()
    reader = UnicodeDictReader(csvfile, fieldnames=headers)
    for line in reader:
        names[line['name']]+=1

names=sorted(names.items(), key=itemgetter(1), reverse=True)

start=time.time()
all=((len(names)**2)/2)
done=0
mapcnt=0
candidates=0
with open('mappings', 'a') as mappings:
    for name, cnt in names:
        #print "checking", name.encode('utf8'), cnt
        if not name.strip(): continue
        sims=[]
        for other, ocnt in names[names.index((name,cnt))+1:]:
            done+=1
            if (done % 100000) == 0:
                perc=(done*100.0)/all
                elapsed=(time.time() - start)
                rate=done/elapsed
                remaining=all-done
                eta=remaining/rate
                print >>sys.stderr, "checked... %s %f%%, %s maps / %s candidates - %0.0f op/s %s" % (done, perc, mapcnt, candidates, rate, hdate(eta))

            if not other.strip(): continue
            sim=similarity(name, other)
            if sim<0.8:
                continue
            if sim==1:
                print >>mappings, ("%s\t%s" % (name, other)).encode('utf8')
                mappings.flush()
                mapcnt+=1
            else:
                candidates+=1
                sims.append((other,sim))
        if len(sims)>0:
            print '[x]', name.encode('utf8')
            print '\n'.join(["[>] %s" % ( other.encode('utf8')) for other, sim in sorted(sims, key=itemgetter(1), reverse=True)])

