import cv2
import numpy as np
import imageio

def calculate_motion(video_path):
    reader = imageio.get_reader(video_path)

    frame1 = reader.get_next_data()
    motion_list = []

    for i, frame2 in enumerate(reader):
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 900:
                continue
            motion_list.append(cv2.contourArea(contour))

        frame1 = frame2

    avg_motion = np.mean(motion_list)

    if avg_motion < 500:
        return "Slow video"
    elif avg_motion < 1500:
        return "Medium video"
    else:
        print(avg_motion)
        return "Fast video"

video_path = "Need 12 runs of 1 ball | TEAM WINS!!!!!!.mp4"
video_path_2 = "it's ok, you're ok.mp4"
print(calculate_motion(video_path))
# print(calculate_motion(video_path_2))