import cv2
import face_recognition
import pickle
import os
import mysql.connector
from datetime import datetime

def load_encodings():
    encodings = []
    for filename in os.listdir("encodings"):
        if filename.endswith(".pkl"):
            with open(os.path.join("encodings", filename), "rb") as file:
                encodings.append(pickle.load(file))
    return encodings

def log_recognition(name):
    # Database connection
    connection = mysql.connector.connect(
        host="your_server_ip",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    cursor = connection.cursor()
    
    # Insert log into database
    query = "INSERT INTO face_logs (name) VALUES (%s)"
    cursor.execute(query, (name,))
    connection.commit()
    cursor.close()
    connection.close()

def recognize_face():
    known_faces = load_encodings()
    
    # Initialize camera
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        # Detect and encode faces in the frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(
                [enc["encoding"] for enc in known_faces], face_encoding
            )
            name = "Unknown"
            
            # If a match is found
            if True in matches:
                match_index = matches.index(True)
                name = known_faces[match_index]["name"]

                # Log recognition
                log_recognition(name)
                print(f"{datetime.now()}: Recognized {name}")

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

recognize_face()
