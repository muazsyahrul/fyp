import cv2
import os

# Get employee ID input
employee_id = input("Enter Employee ID: ")

# Create the directory if it doesn't exist
output_dir = f"dataset/{employee_id}/"
os.makedirs(output_dir, exist_ok=True)

# Initialize the webcam
cap = cv2.VideoCapture(0)  # Use 0 for USB camera

cv2.namedWindow("Press Enter to start capturing 50 images", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Press Enter to start capturing 50 images", 500, 300)

img_counter = 0

print("Press Enter to start capturing...")
input()  # Wait for Enter key press to start capturing

while img_counter < 50:
    # Capture frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Save the frame as an image
    img_name = f"{output_dir}/image_{img_counter}.jpg"
    cv2.imwrite(img_name, frame)
    print(f"{img_name} written!")
    img_counter += 1

    # Show the frame to the user
    cv2.imshow("Press Enter to start capturing 50 images", frame)
    cv2.waitKey(100)  # Capture every 100ms for a slight delay

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()
print("50 images captured successfully.")
