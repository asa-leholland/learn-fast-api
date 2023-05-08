# from sqlalchemy import create_engine, Column, Integer, String, Float, Enum
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()

# class ItemModel(Base):
#     __tablename__ = 'items'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     price = Column(Float)
#     count = Column(Integer)
#     category = Column(Enum(ItemCategory))

# engine = create_engine('postgresql://user:password@localhost/mydatabase')
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
