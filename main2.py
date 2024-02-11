import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import matplotlib.pyplot as plt


# Function to generate a stylish image
def generate_stylish_image(size=(500, 500)):
    # Create a blank canvas
    img = Image.new('RGB', size, color='white')
    draw = ImageDraw.Draw(img)

    # Draw stylish patterns or shapes
    for _ in range(10):
        x1, y1 = np.random.randint(0, size[0]), np.random.randint(0, size[1])
        x2, y2 = np.random.randint(0, size[0]), np.random.randint(0, size[1])
        color = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
        draw.line([x1, y1, x2, y2], fill=color, width=np.random.randint(1, 5))

    # Apply some filters for a stylish effect
    img = img.filter(ImageFilter.SMOOTH)
    img = img.filter(ImageFilter.SMOOTH_MORE)

    return img


# Generate and display the stylish image
stylish_image = generate_stylish_image()
plt.imshow(stylish_image)
plt.axis('off')
plt.show()