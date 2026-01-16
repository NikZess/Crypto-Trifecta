from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, BigInteger, Boolean

from .base import Base

class User(Base):
    
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    first_name: Mapped[str] = mapped_column(String(150), nullable=True)
    last_name: Mapped[str] = mapped_column(String(150), nullable=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)

    access_status: Mapped[bool] = mapped_column(Boolean, nullable=False)
    signal_permission: Mapped[bool] = mapped_column(Boolean, nullable=False)