import os
from PIL import Image
import imagehash

def calculate_image_hash(image_path):
    # Load the image and convert it to grayscale
    image = Image.open(image_path)
    hash_value = imagehash.average_hash(image)
    return hash_value

def find_duplicate_images(directory, input_image_path):
    input_hash = calculate_image_hash(input_image_path)
    image_hashes = {}
    duplicates = []

    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            file_path = os.path.join(directory, filename)
            hash_value = calculate_image_hash(file_path)

            # Check if the hash matches the input image hash
            if hash_value == input_hash:
                duplicates.append(file_path)

    return duplicates

if __name__ == "__main__":
    # Specify the base directory containing images
    base_directory = r"C:\Users\santhosh\Desktop\test\source"

    # Get the path to the user-provided input image
    input_image_path = input("Enter the path to the input image: ")

    # Find images matching the input image in the specified directory
    matching_images = find_duplicate_images(base_directory, input_image_path)

    # Print the results
    if matching_images:
        print("Your sample matches with the following images:")
        for matching_image in matching_images:
            print(matching_image)
    else:
        print("No matching images found for the provided sample.")
