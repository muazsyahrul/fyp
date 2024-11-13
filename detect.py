import cv2
import face_recognition
import pickle
import mysql.connector
from datetime import datetime

# Load registered faces
with open("employee_faces.pkl", "rb") as f:
    known_face_data = pickle.load(f)

# Connect to MySQL database on your server
db_connection = mysql.connector.connect(
    host="YOUR_SERVER_IP",
    user="YOUR_DB_USER",
    password="YOUR_DB_PASSWORD",
    database="YOUR_DATABASE_NAME"
)
cursor = db_connection.cursor()

# Initialize USB camera
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to capture image.")
        break

    # Detect faces in frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        # Compare with registered faces
        for emp_id, known_encoding in known_face_data.items():
            matches = face_recognition.compare_faces([known_encoding], face_encoding)
            if True in matches:
                # Mark attendance
                timestamp = datetime.now()
                sql = "INSERT INTO attendance (employee_id, date, time) VALUES (%s, %s, %s)"
                values = (emp_id, timestamp.date(), timestamp.time())
                cursor.execute(sql, values)
                db_connection.commit()
                print(f"Attendance marked for Employee ID: {emp_id}")
                break

    # Display the video
    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_capture.release()
cv2.destroyAllWindows()
cursor.close()
db_connection.close()
