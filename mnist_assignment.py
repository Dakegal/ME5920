import torch
import torchvision
import random
from torch.utils.data import Subset
import matplotlib.pyplot as plt
from einops import rearrange
from mpl_toolkits.mplot3d import Axes3D

labels=[]
images=[]
##print("label", labels)

#Download 
mnist_data = torchvision.datasets.MNIST(
    root=r"c:\Users\kolan\Documents\2025_Spring\ME5920",  
    train=True,  
    download=True,
    transform=torchvision.transforms.ToTensor()  
)

#Create a subset with 1,000 random samples and collect labels
subset_indices = random.sample(range(len(mnist_data)), 1000) 
subset_1 = Subset(mnist_data, subset_indices)
for i in range(len(subset_1)):
    labels.append(subset_1[i][1])
    images.append(subset_1[i][0]) 

##print (len(images))
images= torch.stack(images)

##print(images.shape)

#plot hist
plt.figure(figsize=(8, 5))
plt.hist(labels, bins=range(11), edgecolor='black', align='left')
plt.xticks(range(10))
plt.xlabel("Class")
plt.ylabel("Frequency")
plt.title("Histogram of MNIST Subset Classes (1,000 Samples)")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()

#batching
batched_img = rearrange(images,"(b n) c h w -> b n c h w", n=25)
##print(batched_img.shape)

#Display the size of the subset
##print(f"Subset size: {len(subset_1)} samples")  

# Randomly select an MNIST image sample
random_img = random.randint(0, batched_img.shape[0] - 1)  
random_index = random.randint(0, 24)
image = batched_img[random_img,random_index]  

# Convert the image to a 2D numpy array for plotting
image_array = image.squeeze().numpy()  

# Get pixel coordinates (x, y) and corresponding intensities (z)
x, y = torch.meshgrid(torch.arange(28), torch.arange(28), indexing="ij")  # Create meshgrid for x, y
x = x.numpy().flatten()  # Flatten x coordinates
y = y.numpy().flatten()  # Flatten y coordinates
z = image_array.flatten()  # Flatten pixel intensities


##print("x shape:", x.shape)  # (784,)
##print("y shape:", y.shape)  # (784,)
##print("z shape:", z.shape)  # (784,)

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot with x, y, z coordinates
ax.scatter(x, y, z, c=z, cmap='gray', marker='o', s=10)

# Labels and title
ax.set_xlabel('X Pixel Location')
ax.set_ylabel('Y Pixel Location')
ax.set_zlabel('Pixel Intensity')
ax.set_title(f'3D Plot of MNIST Image (Label:)')

# Show the plot
plt.show()