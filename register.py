import cv2
import os

# Prompt user for name, use this as folder name for images
name = input("Enter Employee Name or ID: ")

# Define output directory based on the provided name/ID
output_dir = f"dataset/{name}/"
os.makedirs(output_dir, exist_ok=True)

# Initialize the USB camera
cap = cv2.VideoCapture(0)  # 0 is typically the default webcam

# Set up a named window with adjustable size
cv2.namedWindow("Press SPACE to take a photo, ESC to exit", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Press SPACE to take a photo, ESC to exit", 500, 300)

img_counter = 0  # Counter for image filenames

while True:
    # Capture frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Show the video feed with instructions
    cv2.imshow("Press SPACE to take a photo, ESC to exit", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC key pressed to exit
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE key pressed to capture photo
        img_name = f"{output_dir}/image_{img_counter}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} written!")
        img_counter += 1

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
