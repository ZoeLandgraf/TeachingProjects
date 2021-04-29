import matplotlib.pyplot as plt
import cv2
import os

def visualize_image(image, target):
    fig = plt.figure()
    plt.tight_layout()
    plt.imshow(image[0][0], cmap='gray', interpolation='none')
    plt.title("Ground Truth: {}".format(target[0]))
    plt.xticks([])
    plt.yticks([])
    fig.show()


def load_and_scale(file):
    image = cv2.imread(file, 2)
    scaled_image = cv2.resize(image, (28, 28), interpolation=cv2.INTER_AREA)
    return scaled_image


def load_digits(path):
    digit_images = []
    for i in range(10):
        file_n = os.path.join(path, ("handwritten_" + str(i) + ".png"))
        digit_images.append(load_and_scale(file_n))
    return digit_images