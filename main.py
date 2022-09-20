import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def video_reader():
    cam = cv2.VideoCapture(0) 
    detector = cv2.QRCodeDetector() 
    while True:
        _, img = cam.read()
        
        b,g,r,a = 255,0,0,0
        data, bbox, _ = detector.detectAndDecode(img)
        

        if data:
            
            

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.rectangle(img,(round(bbox[0][0][0]),round(bbox[0][0][1])), (round(bbox[0][2][0]), round(bbox[0][2][1])), (255,0,0), 2)
            
            font_path = 'C:/Windows/Fonts/arial.ttf'
            font = ImageFont.truetype(font_path, 15)
            img_pil = Image.fromarray(img)
            draw = ImageDraw.Draw(img_pil)
            draw.text((round(bbox[0][0][0]),round(bbox[0][0][1])),  data, font = font, fill = (b, g, r, a))
            img = np.array(img_pil)
            print("QR Code detected-->", data)
            

        miror_image = cv2.flip(img, 1)

        cv2.imshow("img", img)    
        if cv2.waitKey(1) == ord("Q"):
            break
    cam.release()
    cv2.destroyAllWindows()

video_reader()