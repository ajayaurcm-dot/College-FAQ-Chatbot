from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from app.config import settings


class MySQLDatabase:
    def __init__(self):
        try:
            self.engine = create_engine(
                settings.MYSQL_URL,
                pool_size=10,
                max_overflow=20,
                pool_timeout=30,
                pool_recycle=1800,
                echo=False
            )

            self.SessionLocal = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine
            )

            print("✅ MySQL connected successfully")

        except SQLAlchemyError as e:
            print(f"[DB CONNECTION ERROR] {e}")
            self.engine = None

    # ---------------------------
    # Get DB session
    # ---------------------------
    def get_session(self):
        if not self.engine:
            raise Exception("Database not initialized")

        return self.SessionLocal()


# Singleton instance
db = MySQLDatabase()