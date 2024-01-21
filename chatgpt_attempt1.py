from skimage import io, feature, color
import matplotlib.pyplot as plt

# Load the image
image_path = '/mnt/data/tile_1_1.png' # REMEBER TO REPLACE THE IMAGE PATH
image = io.imread(image_path)

# Convert to grayscale
gray_image = color.rgb2gray(image)

# Apply Canny edge detector
edges = feature.canny(gray_image)

# Display the results
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
ax = axes.ravel()

ax[0].imshow(image)
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(edges, cmap=plt.cm.gray)
ax[1].set_title('Canny Edge Detection')
ax[1].axis('off')

plt.tight_layout()
plt.show()
