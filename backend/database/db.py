from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "postgresql://postgres:password@localhost:5432/Startup_Validator"

engine = create_engine(DATABASE_URL)

# create a database session
SessionLocal = sessionmaker(
    autocommit=False, # db.add(user) will not direclty commit to the database, you need to call db.commit() to save the changes
    autoflush=False,
    bind=engine       # attach the session with the engine
)
