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
                            
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()
atul = User( name="atul",fullname="Atul Sharma", nickname="mantissaman")
session.add(atul)
session.commit()
atul_1 = session.query(User).filter_by(name='atul').first() 
print(atul_1)

atul_1.nickname="boss"

session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')
])

session.commit()

for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)

for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)

for row in session.query(User, User.name).all():
    print(row.User, row.name)

for row in session.query(User.name.label('name_label')).all():
    print(row.name_label)