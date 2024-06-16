from importlib import metadata
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Boolean
import os
import sys
dir2_path: str = os.path.normpath(os.path.join(os.path.dirname(__file__), '../res'))
sys.path.append(dir2_path)
import constants as res

metadata = MetaData()
engine=create_engine('sqlite:///'+res.sentences_path, echo=True)
table_sentences = Table('sentences', metadata,
              Column('index', Integer, primary_key=True),
              Column('sentence', String),
              Column('es', String),
              Column('fr', String),
              Column('de', String),
              Column('it', String),
              Column('pt', String),
              Column('ru', String),
              Column('ja', String),
              Column('ko', String),
              Column('pl', String),
              Column('hard', Boolean),
              )

def create_database():
    metadata.create_all(engine)

def drop_database():
    metadata.drop_all(engine)

def insert_sentence(index, sentence, es, fr, de, it, pt, ru, ja, ko, pl, hard):
    with engine.connect() as connection:
        connection.execute(table_sentences.insert().values(index=index, sentence=sentence, es=es, fr=fr, de=de, it=it, pt=pt, ru=ru, ja=ja, ko=ko, pl=pl, hard=hard))

def get_sentence(index):
    with engine.connect() as connection:
        result = connection.execute(table_sentences.select().where(table_sentences.columns.index == index))
        return result.fetchone()

def get_all_sentences():
    with engine.connect() as connection:
        result = connection.execute(table_sentences.select())
        return result.fetchall()

def get_last_index():
    with engine.connect() as connection:
        result = connection.execute(table_sentences.select().with_only_columns(table_sentences.columns.index).order_by(table_sentences.columns.index.desc()).limit(1))
        result = result.fetchone()
        if result is None:
            return 0
        return result[0]

if __name__=='__main__':
    create_database()


