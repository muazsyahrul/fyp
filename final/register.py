import cv2
import os

# Get Employee ID from user
employee_id = input("Enter Employee ID: ")

# Create a directory for the employee's dataset
output_dir = f"dataset/{employee_id}/"
os.makedirs(output_dir, exist_ok=True)

# Initialize the webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow("Face Registration", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Face Registration", 500, 300)

img_counter = 0
max_images = 50  # Number of images to capture

print("Press SPACEBAR to start capturing images...")

# Wait until SPACEBAR is pressed to start capturing
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Show preview
    cv2.putText(frame, "Press SPACEBAR to start capturing", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.imshow("Face Registration", frame)

    # Wait for SPACEBAR to start capturing images
    if cv2.waitKey(1) % 256 == 32:  # SPACEBAR key
        print("Starting image capture...")
        break

# Start capturing images
while img_counter < max_images:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    img_name = f"{output_dir}/image_{img_counter}.jpg"
    cv2.imwrite(img_name, frame)
    print(f"{img_name} written!")
    img_counter += 1

    # Display the current image count on the frame
    cv2.putText(frame, f"Capturing Image {img_counter}/{max_images}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.imshow("Face Registration", frame)
    cv2.waitKey(100)  # Small delay for better visibility of captured frame

print("Face registration complete.")

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()
