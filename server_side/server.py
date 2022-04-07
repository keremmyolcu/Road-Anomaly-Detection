import io
from pickle import FALSE
import socket
import struct
from PIL import Image
import cv2
import numpy as np
import tracker

# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
#DESKTOP-OMR5STA
#192.168.137.1

import socket
print(socket.gethostname())
server_socket = socket.socket()
print("Socket successfully created")
server_socket.bind(('192.168.137.1', 12345))
print("socket binded to ")
server_socket.listen(0) 

def get_centroid(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy

isFirst = 1
cnt=0
# Accept a single connection and make a file-like object out of it
conn, addr = server_socket.accept()
connection = conn.makefile('rb')
print("connected")
try:
    while True:
        #print(connection.fileno())
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        # Construct a stream to hold the image data and read the image
        # data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        # Rewind the stream, open it as an image with PIL and do some
        # processing on it
        image_stream.seek(0)
        file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        if isFirst == 1:
            firstFrame = img
            isFirst = 0

        else:
            frame_difference = cv2.absdiff(firstFrame, img)
            gray_image = cv2.cvtColor(frame_difference, cv2.COLOR_BGR2GRAY)
            blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0) 
            retrival_value, threshold = cv2.threshold(blur_image, 20, 255, cv2.THRESH_BINARY)
            dilated_image = cv2.dilate(threshold, None, iterations = 3)
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
            closing = cv2.morphologyEx(dilated_image, cv2.MORPH_OPEN, kernel=kernel, iterations=1)
            contours, hierarchy = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            cv2.line(firstFrame, (250, 0), (130, 480), (0,255,0), 1)
            cv2.line(firstFrame, (320, 0), (320, 480), (0,255,0), 1)
            cv2.line(firstFrame, (390, 0), (510, 480), (0,255,0), 1)
            
            for each_contor in contours :
        
                area = cv2.contourArea(each_contor)
                if area > 800:
                    (x, y, w, h) = cv2.boundingRect(each_contor)                
                    cv2.rectangle(firstFrame, (x, y), (x + w, y + h), (0, 255, 255), 2)                   
                    centroid = get_centroid(x, y, w, h)
                    cxx, cyy = get_centroid(x, y, w, h)
                    #print("KONUM *************:"+ str(cxx)+ ", "+str(cyy))
                    #print("SOLA UZAKLIK***********"+ str(tracker.distanceFromLeft(cxx, cyy)))
                    #print("SAGA UZAKLIK***********"+ str(tracker.distanceFromRight(cxx, cyy)))
                    #print("ORTAYA UZAKLIK***********"+ str(tracker.distanceFromMiddle(cxx, cyy)))
                    #print("----------------------------------------------------------------------")
                    if (tracker.distanceFromLeft(cxx, cyy) < 15 or 
                    tracker.distanceFromRight(cxx, cyy) < 15 or 
                    tracker.distanceFromMiddle(cxx, cyy) <15):
                        cnt=cnt+1
                        print("*********ANOMALI*******")
                        print(cnt)
                        print("------------------------------------------")
                        #lcdye gonder
                        sendWarn = "anomali"
                        conn.send(sendWarn.encode())
                        
                    
                    cv2.circle(firstFrame,centroid, 5, (0,255,0), -1)
            cv2.imshow("the captured Video", firstFrame)

            firstFrame = img

        cv2.waitKey(10)
        #print('Image is verified')

finally:
    connection.close()
    server_socket.close() 