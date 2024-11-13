import cv2
import face_recognition
import pickle

# Initialize USB camera
video_capture = cv2.VideoCapture(0)

# Dictionary to store face encodings with Employee IDs
face_data = {}

while True:
    emp_id = input("Enter Employee ID: ")

    # Capture frame
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to capture image.")
        break

    # Detect face and encode
    face_locations = face_recognition.face_locations(frame)
    if face_locations:
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Save the encoding with the Employee ID
        face_data[emp_id] = face_encodings[0]
        print(f"Registered face for Employee ID: {emp_id}")

        # Save to a file
        with open("employee_faces.pkl", "wb") as f:
            pickle.dump(face_data, f)
        print("Face data saved.")
    else:
        print("No face detected. Try again.")

    # Exit after registration
    break

video_capture.release()
cv2.destroyAllWindows()
