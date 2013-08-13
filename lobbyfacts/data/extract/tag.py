from datetime import datetime
import logging, csv

import requests, sys
from lobbyfacts.data import sl, etl_engine

log = logging.getLogger(__name__)

URL = 'https://github.com/stef/lobbyfacts/raw/master/lobbyfacts/resources/tags.csv'

def parse_tag(tag_el):
    dat = {}
    dat['id'] = tag_el.get('id')
    dat['name'] = tag_el.get('name').decode('utf8')
    dat['tags'] = [x.strip().decode('utf8') for x in tag_el.get('tags','').split(',')]
    return dat

def load_tag(rec, engine):
    tags=[]
    for tag in rec['tags']:
        sl.upsert(engine, sl.get_table(engine, 'tag'), {'tag': tag} , ['tag'])
        tags.append(sl.find_one(engine,sl.get_table(engine, 'tag'),tag=tag))
    if rec['id']:
        rep=sl.find_one(engine,sl.get_table(engine, 'representative'), identification_code=rec['id'])
    else:
        rep=sl.find_one(engine,sl.get_table(engine, 'representative'), original_name=rec['name'])
    if not rep:
        print >>sys.stderr, "couldn't find", rec['id'] or rec['name'].encode('utf8')
        return
    for tag in tags:
        sl.upsert(engine, sl.get_table(engine, 'tags'),
                  {'representative_id': rep['id'],
                   'tag_id': tag['id']},
                  ['representative_id', 'tag_id'])
    return

def parse(data):
    reader = csv.DictReader(data.split('\n'), delimiter=',', quotechar='"')
    for tag_el in reader:
        yield parse_tag(tag_el)

def extract_data(engine, data):
    log.info("Extracting tags ...")
    for i, tag in enumerate(parse(data)):
        load_tag(tag, engine)
        if i % 100 == 0:
            log.info("Extracted: %s...", i)

def extract(engine):
    res = requests.get(URL)
    extract_data(engine, res.content)

if __name__ == '__main__':
    engine = etl_engine()
    if len(sys.argv)<2:
        # extract current
        extract(engine)
    else:
        # extract from file
        with open(sys.argv[1],'r') as fd:
            extract_data(engine, fd.read().decode('utf-8'))
