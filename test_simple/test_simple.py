#!/usr/bin/env python3

import cv2
import time
from recordclass import RecordClass
from contexttimer import Timer


class HSV(RecordClass):
    hue: int
    sat: int
    val: int


gui = False
lowThresh = HSV(46, 47, 126)
highThresh = HSV(106, 255, 249)

wnd_main = 'test_simple_display'


def setLH(v):
    global lowThresh
    lowThresh.hue = v


def setLS(v):
    global lowThresh
    lowThresh.sat = v


def setLV(v):
    global lowThresh
    lowThresh.val = v


def setHH(v):
    global highThresh
    highThresh.hue = v


def setHS(v):
    global highThresh
    highThresh.sat = v


def setHV(v):
    global highThresh
    highThresh.val = v 


def create_hsv_trackbars():
    """
    Not currently used anymore, nor are the boring functions above that
    I wish I could stick in a lambda...
    Still handy if you want to re-threshold an image though.
    """
    global lowThresh, highThresh
    cv2.namedWindow(wnd_main)
    cv2.createTrackbar('Low Hue', wnd_main, lowThresh.hue, 255, setLH)
    cv2.createTrackbar('Low Saturation', wnd_main, lowThresh.sat, 255, setLS)
    cv2.createTrackbar('Low Value', wnd_main, lowThresh.val, 255, setLV)

    cv2.createTrackbar('High Hue', wnd_main, highThresh.hue, 255, setHH)
    cv2.createTrackbar('High Saturation', wnd_main, highThresh.sat, 255, setHS)
    cv2.createTrackbar('High Value', wnd_main, highThresh.val, 255, setHV)


def calculate_target_sim(img):
    """
    Run some calculations, basically simulate finding a target.
    """
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # print("filtering with low {} and high {}".format(low, high))
    # lowThresh = HSV(46, 47, 126)
    # highThresh = HSV(106, 255, 249)
    # low = (lowThresh.hue, lowThresh.sat, lowThresh.val)
    # high = (highThresh.hue, highThresh.sat, highThresh.val)
    # We'll skip the data reformatting and just use the raw values now
    # to keep the focus on making things fast
    thresh = cv2.inRange(hsv, (46, 47, 126), (106, 255, 249))
    # res = cv2.bitwise_and(img, img, mask=thresh)
    conts, hier = cv2.findContours(thresh, cv2.RETR_TREE,
                                   cv2.CHAIN_APPROX_SIMPLE)


def main():
    img = cv2.imread('target1.jpg')
    fc = 10_000
    with Timer(factor=1) as t:
        for x in range(fc):
            calculate_target_sim(img)
    print("Time in seconds: {} ({} loops)".format(t.elapsed, fc))
    if gui:
        print("Waiting for key...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
