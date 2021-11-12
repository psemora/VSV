import cv2
import pytesseract

def main():
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


    alpha = 2 # Contrast control (1.0-3.0)
    beta =  -20 # Brightness control (0-100)
    dim = (280,120) 
    img = cv2.imread('dataset/01.png')
    resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    resized_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
    #resized_img = cv2.convertScaleAbs(resized_img, alpha=alpha, beta=beta)

    """
    ## Detecting characters:
    hImg,wImg,_ = resized_img.shape
    boxes = pytesseract.image_to_boxes(resized_img, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    text = pytesseract.image_to_string(resized_img, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    print("Text found:", text)
    for b in boxes.splitlines():
        b = b.split(' ')
        x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(resized_img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
        cv2.putText(resized_img,b[0],(x,hImg-y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
    cv2.imshow("Result", resized_img)
    cv2.waitKey(0)
    """
    
    ##Detecting words:
    hImg,wImg,_ = resized_img.shape
    boxes = pytesseract.image_to_data(resized_img, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    text = pytesseract.image_to_string(resized_img, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    print("Text found:", text)
    for x,b in enumerate(boxes.splitlines()):
        if x!=0:
            b = b.split()
            if len(b) == 12:
                x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(resized_img,(x,y),(w+x,h+y),(0,0,255),3)
                cv2.putText(resized_img,b[11],(x,hImg-y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

    cv2.imshow("Result", resized_img)
    cv2.waitKey(0)
    
if __name__ == "__main__":
    main()
