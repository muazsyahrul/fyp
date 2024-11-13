import cv2
import os

# Prompt user for the employee ID
employee_id = input("Enter Employee ID: ")

# Create a directory for the employee if it doesn't exist
output_dir = f"dataset/{employee_id}/"
os.makedirs(output_dir, exist_ok=True)

# Initialize the webcam
cap = cv2.VideoCapture(0)  # Adjust the camera index if needed
cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 1080, 1080)

img_counter = 0

while True:
    # Capture frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("press space to take a photo", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed, take a photo
        img_name = f"{output_dir}/image_{img_counter}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} written!")
        img_counter += 1

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()
