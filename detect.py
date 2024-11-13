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
    host="192.168.137.1",
    user="root",
    password="",
    database="apsystem"
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

    # Convert the frame from BGR to RGB for face_recognition
    rgb_frame = frame[:, :, ::-1]

    # Detect faces in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_location, face_encoding in zip(face_locations, face_encodings):
        # Compare with registered faces
        matched_emp_id = None
        for emp_id, known_encoding in known_face_data.items():
            matches = face_recognition.compare_faces([known_encoding], face_encoding)
            if True in matches:
                matched_emp_id = emp_id
                break

        if matched_emp_id:
            # Draw a green rectangle around the detected face
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Display the employee ID
            cv2.putText(frame, f"ID: {matched_emp_id}", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Mark attendance in the database
            timestamp = datetime.now()
            sql = "INSERT INTO attendance (employee_id, date, time) VALUES (%s, %s, %s)"
            values = (matched_emp_id, timestamp.date(), timestamp.time())
            cursor.execute(sql, values)
            db_connection.commit()
            print(f"Attendance marked for Employee ID: {matched_emp_id}")

    # Display the video feed
    cv2.imshow("Face Recognition and Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_capture.release()
cv2.destroyAllWindows()
cursor.close()
db_connection.close()
