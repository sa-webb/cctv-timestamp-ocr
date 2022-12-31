# CCTV Timestamp OCR with Pytesseract

Extracting timestamps from the overlay on CCTV's requires an Optical Character Recognition or OCR library. This project uses [Pytesseract](https://pypi.org/project/pytesseract/) to extract the timestamp from static CCTV footage (mp4 file).

In order to do this, you need to simply draw a tight bounding box around the timestamp and then pass it to the OCR library. The bounding box is drawn using [OpenCV](https://pypi.org/project/opencv-python/).

