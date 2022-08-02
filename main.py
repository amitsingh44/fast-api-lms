from fastapi import FastAPI
from api import users, sections, courses

app = FastAPI(
    title="FastAPI LMS",
    description="LMS for managing students and courses"
)


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)