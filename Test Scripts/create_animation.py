import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

plt.axis(r'off')

FFMpegWriter = manimation.writers[r'ffmpeg']

metadata = dict(
    title = r'Gravity Test',
    artist = r'Isaac Newton',
    comment = r'Make a red apple fall from the sky.'
)

writer = FFMpegWriter(
    fps = 15,
    metadata = metadata
)

fig = plt.figure()

red_circle, = plt.plot([], [], r'ro', markersize = 10)

## n will be the number of frames in the video
n = 80
with writer.saving(fig, r'gravity_test.mp4', 100):
    for i in range(n):
        x0 = 0
        y0 = -1e-6 * 9.81 * (i)**2
        red_circle.set_data(x0, y0)
        writer.grab_frame()