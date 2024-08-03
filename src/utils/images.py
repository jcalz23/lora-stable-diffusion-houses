import matplotlib.pyplot as plt
from PIL import Image

def view_image(image_path, title=None, figsize=(6, 4)):
    img = Image.open(image_path)
    plt.figure(figsize=figsize)
    plt.imshow(img)
    plt.axis('off')
    if title:
        plt.title(title)
    plt.show()