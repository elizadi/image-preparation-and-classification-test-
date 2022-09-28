import cv2
import os

video_file = "C:/Users/ASUS/Documents/GitHub/image_preparation/Camera_3_20220526_003249.mp4"
video_capture = cv2.VideoCapture(video_file)
filename, _ = os.path.splitext(video_file)
filename += "-moviepy"
video_capture.set(cv2.CAP_PROP_FPS, 1)

saved_frame_name = 0
count = 0

while video_capture.isOpened():
    frame_is_read, frame = video_capture.read()

    if frame_is_read and count % 15 == 0:
        frame = frame[210:445, 115:350]
        frame = cv2.resize(frame, (116, 116))
        cv2.imwrite(f"frame{str(saved_frame_name)}.jpg", frame)
        saved_frame_name += 1

    else:
        print("Could not read the frame.")
    
    count += 1