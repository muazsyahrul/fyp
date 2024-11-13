import cv2
import os

# Prompt for employee ID
employee_id = input("Enter employee ID: ")

# Create the directory based on employee ID
output_dir = f"dataset/{employee_id}/"
os.makedirs(output_dir, exist_ok=True)

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 is typically the default webcam

cv2.namedWindow("Press SPACE to capture photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Press SPACE to capture photo", 500, 300)

img_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Press SPACE to capture photo", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        img_name = f"{output_dir}/image_{img_counter}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} written!")
        img_counter += 1

cap.release()
cv2.destroyAllWindows()
