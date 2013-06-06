from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, SmallInteger, DateTime, Text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'

	fingerprint = Column(String(32), primary_key = True)
	public_key = Column(Text)
	last_ip = Column(Integer)
	last_port = Column(SmallInteger)
	last_timestamp = Column(DateTime(timezone=True))

	def __init__(self, fingerprint, public_key=None, last_ip=None, last_port=None, last_timestamp=None):
		super(User, self).__init__()
		self.fingerprint = fingerprint
		if public_key: self.public_key = public_key
		if last_ip: self.last_ip = last_ip
		if last_port: self.last_port = last_port
		if last_timestamp: self.last_timestamp = last_timestamp

	def __repr__(self):
		return '<User(%s)>' % self.fingerprint


class Connection(object):
	def __init__(self):
		super(Connection, self).__init__()
		self.__engine = None
		self.__session = None

	def open(self, filename):
		if not self.__engine:
			self.__engine = create_engine('sqlite:///%s' % filename, echo=True)
			self.__session = sessionmaker(bind=self.__engine)
			Base.metadata.create_all(self.__engine)

	def close(self):
		if self.__engine:
			self.__engine.dispose()
			self.__engine = None

	def session(self):
		return self.__session() if self.__session else None



import string
import random
import datetime

def gen(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

c = Connection()
c.open('test.db')
s = c.session()
for i in range(1000):
	s.add(User(gen(32), gen(256), random.randint(0, 2**32-1), random.randint(0, 2**16-1), datetime.datetime.now()))
s.commit()
c.close()