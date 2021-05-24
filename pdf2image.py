import os

from wand.image import Image, Color
from skimage import io, color, exposure,img_as_float
import matplotlib.pyplot as plt
import numpy as np


def pdf_to_jpg(pdf_path,  output_path = None, resolution = 200):
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    print(pdf_path)
    if not output_path:
        output_path = os.path.dirname(pdf_path)

    with Image(filename=pdf_path, resolution=resolution) as  pdf:
        for n, page in enumerate(pdf.sequence):
            with Image(page) as image:
                image.format = 'png'
                #image.background_color = Color('white')
                image.alpha_channel = 'remove'
                image_name = os.path.join(output_path, '{}.png'.format(pdf_name, n))
                image.save(filename = image_name)


pdf_to_jpg("144014.pdf")

img = io.imread("144014.png")
print(img.shape)
print(img.dtype)
datos=img[600:1450,75:2125]
plt.imshow(img[:,:,0])
plt.imshow(datos[:,:,1])
datos=datos[:,:,1]
print(datos.shape)
print(datos)

for c in np.arange(len(datos)):
    for x in np.arange(len(datos[0])):
        if(datos[c][x]>50):
            datos[c][x]=255

io.imsave("test.png",datos)
# Save 2D numpy array to csv file
np.savetxt('2darray.csv', datos, delimiter=',', fmt='%d')
print(img)

