from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

img = cv2.imread(r'C:\Users\kusha\OneDrive\Desktop\cnn\OIP (5).jpg')

model(img, show= True)

cv2.waitKey(0)


# from ultralytics import YOLO
# import cv2

# # Load YOLO model
# model = YOLO("yolov8n.pt")

# # Read image (use forward slashes or raw string)
# img = cv2.imread(r"C:\Users\kusha\OneDrive\Desktop\cnn\OIP (5).jpg")

# # Safety check
# if img is None:
#     print("❌ Image not loaded. Check the path.")
#     exit()

# # Run inference
# results = model(img)

# # Draw detections
# annotated_img = results[0].plot()

# # Show window (this will NOT close automatically)
# cv2.imshow("YOLO Detection", annotated_img)

# print("Press ANY KEY on the image window to close...")
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#Taking the img frame by frame

# from ultralytics import YOLO
# import cv2

# model = YOLO('yolov8n.pt')


# cap = cv2.VideoCapture(0)


# while True: 
#     sucess, img = cap.read()
#     cv2.imshow("Webcam", img)
#     cv2.waitKey(1)


