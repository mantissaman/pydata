from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://alchemyuser:pa55word@localhost/alchemy', echo=True)



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                                self.name, self.fullname, self.nickname)
                            
#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()
atul = User( name="Atul",fullname="Atul Sharma", nickname="mantissaman")
session.add(atul)
session.commit()
atul_1 = session.query(User).filter_by(name='Atul').first() 
print(atul_1)