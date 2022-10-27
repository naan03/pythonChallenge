from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


Base = declarative_base()
#Map the table structure of a relational database to objects
class DataFile(Base):

    #Define table name and columns
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(Text, nullable=False)
    file_data = Column(Text)

    @classmethod
    def get_by_filename(cls, db: Session, filename):
        data = db.query(cls).filter_by(file_name=filename).first()
        return data

    def __repr__(self):
        return 'File(id={}, file_name={}, file_data={},)'.format(self.id, self.file_name, self.file_data)

    def __str__(self):
        return self.__repr__()