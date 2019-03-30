import cv2
import pytesseract

# tesseract commmad 불러오기
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# 결과 텍스트 값 클립보드 저장
#def setClipboard(text):
#    win32clipboard.OpenClipboard()
#    win32clipboard.EmptyClipboard()
#    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, text)
#    win32clipboard.CloseClipboard()

def ocrClip():
    #im_gray = cv2.imread('./test_file/test_3.png', cv2.IMREAD_GRAYSCALE)
    im_color = cv2.imread('./test_file/CurrentImage.jpg', cv2.IMREAD_COLOR)


    (thresh, im_bw) = cv2.threshold(im_color, 127, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)
    cv2.imwrite('./result/result.jpg', im_bw)
#     cv2.imwrite('bw_image.png', im_bw)
    text = pytesseract.image_to_string(im_bw, lang='eng', config="--psm 8 --oem 3")
#    setClipboard(text)
    print(text)

ocrClip()