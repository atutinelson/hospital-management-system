import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import Mapped, MappedColumn, sessionmaker, DeclarativeBase
from datetime import datetime, time
import os


class Base(DeclarativeBase):
    pass


class Patient(Base):
    __tablename__ = 'patient'
    date_of_admission: Mapped[datetime] = MappedColumn("Date_Of_Admission")
    admission_number: Mapped[str] = MappedColumn("Admission_number", primary_key=True)
    fullname: Mapped[str] = MappedColumn("fullname")
    date_of_birth: Mapped[datetime] = MappedColumn("date_of_birth")
    age: Mapped[int] = MappedColumn("age")
    county: Mapped[str] = MappedColumn("county")
    sub_county: Mapped[str] = MappedColumn("sub_county")
    village: Mapped[str] = MappedColumn("village")
    marital_status: Mapped[str] = MappedColumn("marital_status")
    phone_number: Mapped[str] = MappedColumn("phone_number")
    parity: Mapped[str] = MappedColumn("parity")
    oviration: Mapped[str] = MappedColumn("oviration")
    no_of_anc_visits: Mapped[int] = MappedColumn("No_of_ANC_visits")
    date_of_last_menstrual_period: Mapped[datetime] = MappedColumn("date_of_last_menstrual_period")
    estimated_date_of_birth: Mapped[datetime] = MappedColumn("estimated_date_of_birth")
    diagnosis: Mapped[str] = MappedColumn("diagnosis")

    def __repr__(self):
        return f"Patient('patient_id:{self.admission_number}, patient_name:{self.fullname}')"


database_url = os.path.join(os.path.abspath(__file__), "database.db")
engine = sqlalchemy.create_engine('sqlite:///database.db', echo=True)
session = sessionmaker()(bind=engine)


# class Delivery(Base):
#     duration_of_delivery: Mapped[int] = MappedColumn("duration_of_delivery", nullable=True)
#     date_of_delivery: Mapped[datetime] = MappedColumn("date_of_delivery", nullable=True)
#     time_of_delivery: Mapped[time] = MappedColumn("time_of_delivery", nullable=True)
#     gestation_period: Mapped[int] = MappedColumn("gestation_period", nullable=True)
#     mode_of_delivery: Mapped[str] = MappedColumn("mode_of_delivery", nullable=True)
#     no_of_babies: Mapped[int] = MappedColumn("No_of_babies", nullable=True)
#     placenta_complete: Mapped[str] = MappedColumn("placenta_complete", nullable=True)
#     uterotonic_givern: Mapped[str] = MappedColumn("uterotonic_givern", nullable=True)
#     vigina_examination: Mapped[str] = MappedColumn("vigina_examination", nullable=True)
#     blood_loss: Mapped[int] = MappedColumn("blood_loss", nullable=True)
#     mother_status: Mapped[str] = MappedColumn("mother_status", nullable=True)
#     #patient_id: Mapped[int] =
#
#
# class Baby(Base):
#     baby_weight: Mapped[int] = MappedColumn("baby_weight", nullable=True)
#     sex: Mapped[str] = MappedColumn("sex", nullable=True)
#     initiated_on_bf: Mapped[str] = MappedColumn("initiated_on_bf", nullable=True)
#     kangaroo_mother_care: Mapped[str] = MappedColumn("Kangaroo_mother_care", nullable=True)
#     teo_givern_at_birth: Mapped[str] = MappedColumn("teo_givern_at_birth", nullable=True)
#     chlorhexidine: Mapped[str] = MappedColumn("chlorhexidine", nullable=True)
#     birth_with_deformity: Mapped[str] = MappedColumn("birth_with_deformity", nullable=True)
#     givern_vitamin_k: Mapped[str] = MappedColumn("givern_vitamin_k", nullable=True)
#     vdrl_result: Mapped[str] = MappedColumn("vdrl_result", nullable=True)




