import cv2
import face_recognition
import pickle
import os

def register_face():
    # Initialize camera
    cap = cv2.VideoCapture(0)

    print("Enter your name:")
    name = input("Name: ").strip()
    
    if not name:
        print("Name cannot be empty")
        return

    # Capture a frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        return

    # Detect and encode face
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    if len(face_encodings) == 0:
        print("No face detected. Try again.")
        return

    # Save the face encoding with name
    encoding_data = {"name": name, "encoding": face_encodings[0]}
    with open(f"encodings/{name}.pkl", "wb") as file:
        pickle.dump(encoding_data, file)

    print(f"Face registered for {name}.")

    cap.release()
    cv2.destroyAllWindows()

# Ensure encoding folder exists
if not os.path.exists("encodings"):
    os.makedirs("encodings")

register_face()
