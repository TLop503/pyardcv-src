import cv2
import pyautogui
import time

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

def swap_window():
    pyautogui.moveTo(2780, 1660)
    pyautogui.click()

def export_text(text):
    #reconfigure as needed
    pyautogui.typewrite(text)
    pyautogui.press('enter')


last = "cent"

swap_window()

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        h = 3 * h
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        if ((x > 400) and last != "right"): #right of cam
            export_text("right")
            last = "right"
        elif ((x < 200)and last != "left"): #left of cam
            export_text("left")
            last = "left"
        else:
            export_text("cent")
            last = "cent"
            

    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    
# Release the VideoCapture object
cap.release()