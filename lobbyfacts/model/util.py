import re
from uuid import uuid4
from time import time
from datetime import datetime
from decimal import Decimal
import json
from sqlalchemy import sql
from sqlalchemy.orm.query import Query
from sqlalchemy.types import Text, TypeDecorator, UserDefinedType
from sqlalchemy.ext.mutable import Mutable

def make_id():
    return unicode(uuid4().hex)


def make_serial():
    return int(time() * 1000)


class TSVector(UserDefinedType):
    """Support for PostgreSQL full-text search."""

    def get_col_spec(self):
        from lobbyfacts.core import db
        if db.engine.dialect.name == 'postgresql':
            return 'tsvector'
        return 'text'

    @classmethod
    def make_text(cls, bind, text):
        if bind.engine.dialect.name == 'postgresql':
            return sql.select([sql.func.to_tsvector(text)], bind=bind).scalar()
        return text

class JSONEncoder(json.JSONEncoder):
    """ This encoder will serialize all entities that have a to_dict
    method by calling that method and serializing the result. """

    def __init__(self, shallow=False):
        self.shallow = shallow
        super(JSONEncoder, self).__init__()

    def encode(self, obj):
        return super(JSONEncoder, self).encode(obj)

    def default(self, obj):
        if self.shallow and hasattr(obj, 'as_shallow'):
            return obj.as_shallow()
        if hasattr(obj, 'as_dict'):
            return obj.as_dict()
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, Query):
            return list(obj)
        raise TypeError("%r is not JSON serializable" % obj)

class ReadJSONType(TypeDecorator):
    impl = Text

    def __init__(self):
        super(ReadJSONType, self).__init__()

    def process_bind_param(self, value, dialect):
        return value

    def process_result_value(self, value, dialiect):
        return MutableDict(json.loads(value))

    def copy_value(self, value):
        return value

class JSONType(ReadJSONType):

    def process_bind_param(self, value, dialect):
        return JSONEncoder().encode(value)

class MutableDict(Mutable, dict):
    @classmethod
    def coerce(cls, key, value):
        "Convert plain dictionaries to MutableDict."

        if not isinstance(value, MutableDict):
            if isinstance(value, dict):
                return MutableDict(value)

            # this call will raise ValueError
            return Mutable.coerce(key, value)
        else:
            return value

    def __setitem__(self, key, value):
        "Detect dictionary set events and emit change events."

        dict.__setitem__(self, key, value)
        self.changed()

    def __delitem__(self, key):
        "Detect dictionary del events and emit change events."

        dict.__delitem__(self, key)
        self.changed()
