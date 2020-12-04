import matplotlib.pyplot as plt 
import numpy as np 
from PIL import Image

img = Image.open('img_data/img_0000.jpg')

img_plot = plt.imshow(img)

for i in range(1,79):
       
    img = Image.open('img_data/img_{:04d}.jpg'.format(i))
    img_plot.set_data(img)
    plt.pause(0.01)
    
plt.show()