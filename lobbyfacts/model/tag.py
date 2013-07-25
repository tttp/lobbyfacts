from datetime import datetime

from lobbyfacts.core import db
from lobbyfacts.model import util
from lobbyfacts.model.api import ApiEntityMixIn

class Tag(db.Model, ApiEntityMixIn):
    __tablename__ = 'tag'

    tag = db.Column(db.String(128), primary_key=True)

    def update_values(self, data):
        self.tag = data.get('tag')

    def as_shallow(self):
        d = {}
        d['tag'] = self.tag
        return d

    def as_dict(self):
        d = self.as_shallow()
        return d

    def __repr__(self):
        return "<Tag(%s)>" % (self.tag.encode('ascii', 'ignore'))
