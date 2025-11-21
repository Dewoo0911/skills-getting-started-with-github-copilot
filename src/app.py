"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },

    # Sports activities
    "Soccer Team": {
        "description": "Outdoor team soccer practice and matches",
        "schedule": "Mon/Wed/Fri, 4:00 PM - 6:00 PM",
        "max_participants": 22,
        "participants": ["alex@mergington.edu", "lisa@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Pickup games, drills, and interschool competitions",
        "schedule": "Tuesdays and Thursdays, 5:00 PM - 7:00 PM",
        "max_participants": 15,
        "participants": ["tyler@mergington.edu", "maria@mergington.edu"]
    },

    # Artistic activities
    "Art Studio": {
        "description": "Drawing, painting, and portfolio development",
        "schedule": "Wednesdays, 3:30 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["nina@mergington.edu", "omar@mergington.edu"]
    },
    "Drama Club": {
        "description": "Acting workshops, stagecraft, and school productions",
        "schedule": "Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 25,
        "participants": ["hannah@mergington.edu", "leo@mergington.edu"]
    },

    # Intellectual activities
    "Math Olympiad": {
        "description": "Problem solving and competition preparation for math contests",
        "schedule": "Mondays, 3:30 PM - 4:30 PM",
        "max_participants": 16,
        "participants": ["sanjay@mergington.edu", "emily@mergington.edu"]
    },
    "Science Club": {
        "description": "Hands-on experiments, research projects, and science fairs",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["kevin@mergington.edu", "zoe@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

# validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
