import cv2
data = cv2.QRCodeDetector()

val, points,straight_qrcode = data.detectAndDecode(cv2.imread("link.png"))
print(val)