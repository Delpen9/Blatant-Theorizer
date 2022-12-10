import matplotlib.pyplot as plt
import imageio

filename = r'gravity_test.mp4'

vid = imageio.get_reader(filename, r'ffmpeg', r'I')

nums = range(0, 80, 5)[::-1]

for num in nums:
    image = vid.get_data(num)
    fig = plt.figure()
    plt.axis(r'off')
    plt.imshow(image)

plt.show()