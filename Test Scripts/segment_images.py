import matplotlib.pyplot as plt
import imageio
import cv2
import numpy as np

filename = r'gravity_test.mp4'

vid = imageio.get_reader(filename, r'ffmpeg', r'I')

nums = [0]

for num in nums:
    image = vid.get_data(num)
    image_output = image.copy()
    greyscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(
        greyscale_image,
        cv2.HOUGH_GRADIENT,
        dp = 1,
        param2 = 0.9,
        minDist = 100,
        minRadius = 1,
        maxRadius = 20
    )

    if circles is not None:
        circles = np.round(circles[0, :]).astype('int')

        for (x, y, r) in circles:
            circle_center = (x, y)
            cv2.circle(
                image_output,
                (x, y),
                r,
                (0, 255, 0),
                4
            )

        cv2.imshow('output', np.hstack([image, image_output]))
        cv2.waitKey(0)
