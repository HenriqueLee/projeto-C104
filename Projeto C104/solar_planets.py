import cv2
img= cv2.imread("solar-system.jpg")
cv2.putText(img,"Sol", (100,80), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"Mercurio", (100,200), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Venus", (185,180), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Terra", (280,180), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Marte", (380,180), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Jupiter", (480,180), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Saturno", (780,180), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Urano", (980,180), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))
cv2.putText(img,"Netuno", (1080,180), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255))









cv2.imshow("Sistema solar", img )
cv2.waitKey(0)
