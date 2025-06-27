from sqlalchemy import Column, String, Date, TIMESTAMP, UUID
import uuid
from DATABASE.dbConnection import Base


class UserDB(Base):
    __tablename__ = "Users"

    UserId = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    Email = Column(String, nullable=False)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    DateOfBirth = Column(Date, nullable=False)
    TimeOfLastLogin = Column(TIMESTAMP(timezone=True), nullable=True)
