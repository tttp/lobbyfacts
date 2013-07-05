from datetime import datetime
from pprint import pprint
import logging, csv, hashlib

from lobbyfacts.data import sl, etl_engine

UNREGS='../unregistered-companies.csv'
log = logging.getLogger(__name__)

def dateconv(ds):
    return datetime.strptime(ds.split("+")[0], "%Y-%m-%dT%H:%M:%S.%f")

def load_rep(line, engine):
    # name, id, url, street, city + zip
    rep={}
    rep['original_name'] = line[0].strip()
    rep['name'] = line[0].strip()
    rep['identification_code'] = line[1] or hashlib.sha512(line[0].strip()).hexdigest()[:16]
    rep['web_site_url'] = line[2] or ''

    if line[3].strip():
        rep['contact_street'] = line[3]
    if line[4].strip():
        tmp=line[4].split()
        if tmp[0][0] == 'B':
            rep['contact_country'] = 'Belgium'
        elif tmp[0][0] == 'F':
            rep['contact_country'] = 'France'
        else:
            print 'bad zipcode country code', line[4]

        rep['contact_post_code'] = tmp[0][2:]
        rep['contact_town'] = ' '.join(tmp[1:])

    rep['network_extracted'] = False
    sl.upsert(engine, sl.get_table(engine, 'representative'), rep,
              ['etl_id'])

def extract_data(engine):
    log.info("Extracting unregistered interests data...")
    with open(UNREGS, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i, rep in enumerate(csvreader):
            load_rep(rep, engine)
            if i % 100 == 0:
                log.info("Extracted: %s...", i)

def extract(engine):
    #res = requests.get(URL)
    extract_data(engine) #, res.content.decode('utf-8'))

if __name__ == '__main__':
    engine = etl_engine()
    extract(engine)

