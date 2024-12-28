import os
from PIL import Image

def create_thumbnails_in_subfolders(base_dir, size=(1200, 900)):
    # Walk through each directory in the base directory
    for root, dirs, files in os.walk(base_dir):
        # Skip processing if the current directory is a 'thumbs' folder
        if os.path.basename(root) == 'thumbs':
            continue

        for file in files:
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                img_path = os.path.join(root, file)
                
                # Open the image
                img = Image.open(img_path)
                
                # Resize the image while maintaining aspect ratio
                img.thumbnail(size)

                # Check if the image has an alpha channel (RGBA) and convert it to RGB
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                
                # Create the 'thumbs' directory if it doesn't exist in the current subfolder
                thumbs_dir = os.path.join(root, 'thumbs')
                if not os.path.exists(thumbs_dir):
                    os.makedirs(thumbs_dir)
                
                # Save the resized image in the 'thumbs' directory with the same name
                print(f'Saving {file} to {thumbs_dir}')
                img.save(os.path.join(thumbs_dir, file))

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the base directory to 'images' relative to the script's location
base_directory = os.path.join(script_dir, 'images')

# Generate thumbnails for each image in subfolders
create_thumbnails_in_subfolders(base_directory)
