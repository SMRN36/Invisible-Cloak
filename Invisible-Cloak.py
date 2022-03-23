import cv2
import numpy



def fun(x):
    print("")

capture = cv2.VideoCapture(0)
bars = cv2.namedWindow("bars")

cv2.createTrackbar("upper_hue", "bars", 110, 180, fun)
cv2.createTrackbar("upper_saturation", "bars", 255, 255, fun)
cv2.createTrackbar("upper_value", "bars", 255, 255, fun)
cv2.createTrackbar("lower_hue", "bars", 68, 180, fun)
cv2.createTrackbar("lower_saturation", "bars", 55, 255, fun)
cv2.createTrackbar("lower_value", "bars", 54, 255, fun)

while (True):
    cv2.waitKey(1000)
    ret_frame, init_frame = capture.read()
    # check if the frame is returned then brake
    if (ret_frame):
        break

while (True):
    ret_frame, frame = capture.read()
    inspect = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    upper_hue = cv2.getTrackbarPos("upper_hue", "bars")
    upper_saturation = cv2.getTrackbarPos("upper_saturation", "bars")
    upper_value = cv2.getTrackbarPos("upper_value", "bars")
    lower_value = cv2.getTrackbarPos("lower_value", "bars")
    lower_hue = cv2.getTrackbarPos("lower_hue", "bars")
    lower_saturation = cv2.getTrackbarPos("lower_saturation", "bars")

    kernel = numpy.ones((3, 3), numpy.uint8)
    upper_hsv = numpy.array([upper_hue, upper_saturation, upper_value])
    lower_hsv = numpy.array([lower_hue, lower_saturation, lower_value])

    mask = cv2.inRange(inspect, lower_hsv, upper_hsv)
    mask = cv2.medianBlur(mask, 3)
    mask_inverse = 255 - mask
    mask = cv2.dilate(mask, kernel, 5)

    B = frame[:, :, 0]
    G = frame[:, :, 1]
    R = frame[:, :, 2]
    B = cv2.bitwise_and(mask_inverse, B)
    G = cv2.bitwise_and(mask_inverse, G)
    R = cv2.bitwise_and(mask_inverse, R)
    frame_inv = cv2.merge((B, G, R))

    B = init_frame[:, :, 0]
    G = init_frame[:, :, 1]
    R = init_frame[:, :, 2]
    B = cv2.bitwise_and(B, mask)
    G = cv2.bitwise_and(G, mask)
    R = cv2.bitwise_and(R, mask)
    blanket_area = cv2.merge((B, G, R))

    final = cv2.bitwise_or(frame_inv, blanket_area)

    cv2.imshow("Harry's Cloak", final)

    if (cv2.waitKey(3) == ord('q')):
        break;

cv2.destroyAllWindows()
capture.release()