import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-6f46c-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference('Students')

data = {
    "789456":
        {
            "name": "Chaitanya",
            "rollnumber": "20NR1A0529",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "studingyear": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "321654":
        {
            "name": "Sunitha",
            "rollnumber": "20NR1A0580",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "studyingyear": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Pavan Varma",
            "rollnumber": "20NR1A0582",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "studyingyear": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Dadi Keerthana",
            "rollnumber": "20NR1A0527",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "studyingyear": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)