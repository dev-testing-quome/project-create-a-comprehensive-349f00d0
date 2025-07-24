from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class HTTPError(BaseModel):
    detail: str

class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr
    first_name: str
    last_name: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    is_staff: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    date_time: datetime
    description: str

class AppointmentResponse(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date_time: datetime
    description: str
    created_at: datetime
    updated_at: datetime

class PrescriptionCreate(BaseModel):
    patient_id: int
    medication: str
    dosage: str
    instructions: str
    refills_remaining: int

class PrescriptionResponse(BaseModel):
    id: int
    patient_id: int
    medication: str
    dosage: str
    instructions: str
    refills_remaining: int
    created_at: datetime
    updated_at: datetime

class MessageCreate(BaseModel):
    sender_id: int
    recipient_id: int
    content: str

class MessageResponse(BaseModel):
    id: int
    sender_id: int
    recipient_id: int
    content: str
    created_at: datetime
    updated_at: datetime
