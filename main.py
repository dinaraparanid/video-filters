import cv2
import numpy as np
from filters.black_and_white_filter import black_and_white
from filters.erosion_filter import erosion
from filters.flip_horizontal_filter import flip_horizontal
from filters.inversion_filter import inversion

# Queue of filters
filters = [
    black_and_white,
    erosion,
    inversion,
    flip_horizontal
]

# Function for sequential application of filters
def apply_filters(frame, filters):
    for filter_function in filters:
        frame = filter_function(frame)
    return frame

# Loading the video file
video_capture = cv2.VideoCapture("path")

# Getting the original video's frame rate
original_fps = video_capture.get(cv2.CAP_PROP_FPS)
ideal_delay = int(1000 / original_fps)

# Video processing
while True:
    ret, frame = video_capture.read()
    if ret:
        processed_frame = apply_filters(frame, filters)

        # Displaying the processed frame
        cv2.imshow("Video", processed_frame)

        # Waiting for the ideal delay
        if cv2.waitKey(ideal_delay) & 0xFF == ord('q'):
            break
    else:
        break

# Freeing up resources
video_capture.release()
cv2.destroyAllWindows()
