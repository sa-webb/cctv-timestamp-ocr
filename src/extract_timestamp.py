import cv2
import sys
import numpy as np
import pytesseract

# Path to Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def extract_timestamp(frame: np.ndarray, kernel1: int, kernel2: int):
    # Static bounding box for camera configuration.
    timestamp_frame = frame[0:29, 0:253]
    ts = exec_ocr(timestamp_frame, kernel1, kernel2)
    return ts

def exec_ocr(timestamp_frame: np.ndarray, kernel1: int, kernel2: int):
	# Convert the image to gray scale
	gray = cv2.cvtColor(timestamp_frame, cv2.COLOR_BGR2GRAY)

	_, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
	
	rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel1, kernel2))

	dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

	contours, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
													cv2.CHAIN_APPROX_NONE)

	im2 = timestamp_frame.copy()

	for cnt in contours:
		x, y, w, h = cv2.boundingRect(cnt)
		cropped = im2[y:y + h, x:x + w]
		timestamp = pytesseract.image_to_string(cropped)
		return timestamp.strip()
