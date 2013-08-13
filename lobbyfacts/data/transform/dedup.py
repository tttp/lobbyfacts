import logging

from lobbyfacts.data import sl, etl_engine

log = logging.getLogger(__name__)

def dedup_fields(engine, field):
    table = sl.get_table(engine, 'representative')
    seen=set([])
    for n, rep in enumerate(sl.all(engine, table)):
        if n % 100 == 0:
            print n, 'done'
        if not rep[field] or not rep[field].strip() or rep[field] in seen: continue
        seen.update(rep[field])
        others = list(sl.find(engine, table, **{field: rep[field]}))
        if len(others) > 1:
            log.info("Duplicates for: %s", rep['name'])
            for i, re in enumerate(others):
                if re == rep: continue
                text = "(Duplicate %s)" % (i+1)
                sl.upsert(engine, table,
                    {'name_suffix': text,
                     'identification_code': re['identification_code']},
                    ['identification_code'])

def transform(engine):
    dedup_fields(engine, 'name')
    dedup_fields(engine, 'canonical_name')

if __name__ == '__main__':
    engine = etl_engine()
    transform(engine)
