import cv2
import os

# Prompt for employee ID
employee_id = input("Enter Employee ID: ")

# Create a directory for the employee if it doesn't exist
output_dir = f"dataset/{employee_id}/"
os.makedirs(output_dir, exist_ok=True)

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 is typically the default webcam
img_counter = 0

print("Press Enter to start capturing images...")
input()  # Wait for Enter key

# Capture 50 images
while img_counter < 50:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Capturing Face", frame)
    img_name = f"{output_dir}/image_{img_counter}.jpg"
    cv2.imwrite(img_name, frame)
    print(f"{img_name} written!")
    img_counter += 1

    # Display for a short time to avoid too-fast capture
    cv2.waitKey(100)

print("Face registration complete.")
cap.release()
cv2.destroyAllWindows()
