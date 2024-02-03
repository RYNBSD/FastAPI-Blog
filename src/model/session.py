from . import Base, SessionLocal, engine

Base.metadata.create_all(bind=engine)

def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()