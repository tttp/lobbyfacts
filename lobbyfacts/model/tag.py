from datetime import datetime

from lobbyfacts.core import db
from lobbyfacts.model import util
from lobbyfacts.model.api import ApiEntityMixIn

class Tag(db.Model, ApiEntityMixIn):
    __tablename__ = 'tag'

    id = db.Column(db.BigInteger, primary_key=True)
    tag = db.Column(db.String(128), unique=True)

    def update_values(self, data):
        self.tag = data.get('tag')

    @classmethod
    def by_tag(cls, tag):
        q = db.session.query(cls)
        q = q.filter_by(tag=tag)
        return q.first()

    @classmethod
    def by_id(cls, id):
        q = db.session.query(cls)
        q = q.filter_by(id=id)
        return q.first()

    def as_shallow(self):
        d = {}
        d['tag'] = self.tag
        d['id'] = self.id
        return d

    def as_dict(self):
        d = self.as_shallow()
        return d

    def __repr__(self):
        return "<Tag(%s)>" % (self.tag.encode('ascii', 'ignore'))
