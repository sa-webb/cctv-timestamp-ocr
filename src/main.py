import os
import cv2
import sys
from datetime import datetime

from src.extract_timestamp import extract_timestamp


def main(cap: cv2.VideoCapture):
    frame_count = 0
    while (cap.isOpened()):
        _, frame = cap.read()
        extracted_timestamp = extract_timestamp(frame, 14, 14)
        try:
            timestamp = datetime.strptime(extracted_timestamp, "%Y-%m-%d %H:%M:%S")

            print('Datetime object: ', timestamp)
            frame_count += 1

        except ValueError as e:
            print("value could not be converted to date: ", e, " at frame: ", frame_count)

        except Exception as e:
            print("unknown error: ", e, " at frame: ", frame_count)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    VIDEO_PATH = f"{sys.argv[1]}.mp4"
    cap = cv2.VideoCapture(VIDEO_PATH)
    main(cap)