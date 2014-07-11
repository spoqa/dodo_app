from sqlalchemy import Column, Integer, String, VARCHAR
from apptest.database import Base


class LMS(Base):
    __tablename__ = 'em_mmt_tran'
    mt_pr = Column(Integer, primary_key=True)
    subject = Column(VARCHAR(40))
    content = Column(VARCHAR(4000))
    callback = Column(VARCHAR(25))
    recipent_num = Column(VARCHAR(25))

    def __init__(self, subject, content, callback, recipent_num):
        self.subject = subject
        self.content = content
        self.callback = callback
        self.recipent_num = recipent_num


class SMS(Base):
    __tablename__ = 'em_smt_trans'
    mt_pr = Column(Integer, primary_key=True)
    content = Column(VARCHAR(255))
    callback = Column(VARCHAR(25))
    recipent_num = Column(VARCHAR(25))

    def __init__(self, content, callback, recipent_num):
        self.content = content
        self.callback = callback
        self.recipent_num = recipent_num
