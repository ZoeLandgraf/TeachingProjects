import matplotlib.pyplot as plt
import cv2
import torch

import utils
from network import Net

ckpt_file = "../data/pretrained_mnist_weights/model.pth"
path = "../data/digits"

# load network
network = Net()
network.load_state_dict(torch.load(ckpt_file))

digit_images = utils.load_digits(path)
network.eval()

for i,image in enumerate(digit_images):
  image_input = torch.from_numpy(image).unsqueeze(0).unsqueeze(0).float()
  output = network(image_input)
  pred = output.data.max(1, keepdim=True)[1]
  pred_str = str(output.data.max(1)[1].item())
  plt.subplot(3,4,i+1)
  plt.tight_layout()
  plt.imshow(image, cmap='gray', interpolation='none')
  plt.title("Prediction: {}".format(pred_str))
  plt.xticks([])
  plt.yticks([])


plt.show()