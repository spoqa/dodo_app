from datetime import datetime

from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.types import TIMESTAMP
from app.database import Base


class LMS(Base):
    __tablename__ = 'em_mmt_tran'
    mt_pr = Column(Integer, primary_key=True)
    subject = Column(VARCHAR(40))
    content = Column(VARCHAR(4000))
    callback = Column(VARCHAR(25))
    recipient_num = Column(VARCHAR(25))
    service_type = Column(VARCHAR(1), default='2', server_default='2')
    date_client_req = Column(TIMESTAMP(timezone=False))

    def __init__(self, subject, content, callback, recipient_num):
        self.subject = subject.encode('cp949', 'ignore')
        self.content = content.encode('cp949', 'ignore')
        self.callback = callback
        self.recipient_num = recipient_num
	self.date_client_req = datetime.utcnow()


class SMS(Base):
    __tablename__ = 'em_smt_tran'
    mt_pr = Column(Integer, primary_key=True)
    content = Column(VARCHAR(255))
    callback = Column(VARCHAR(25))
    recipient_num = Column(VARCHAR(25))
    service_type = Column(VARCHAR(1), default='0', server_default='0')
    date_client_req = Column(TIMESTAMP(timezone=False))

    def __init__(self, content, callback, recipient_num):
        self.content = content.encode('cp949', 'ignore')
        self.callback = callback
        self.recipient_num = recipient_num
	self.date_client_req = datetime.utcnow()
