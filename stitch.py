from panorama import Stitcher
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
                help="path to the first image")
ap.add_argument("-s", "--second", required=True,
                help="path to the second image")
args = vars(ap.parse_args())


imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])

# imageA = cv2.imread("first.jpg")
# imageB = cv2.imread("second.jpg")
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

Stitcher = Stitcher()
(result, vis) = Stitcher.stitch([imageA, imageB], showMatches=True)

cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)
'''
imageA = cv2.imread("E:\\1.png")
imageB = cv2.imread("E:\\2.png")
'''
