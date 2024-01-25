import os
from rembg import remove
from PIL import Image


def main():
    # Specify the input and output folder paths
    input_folder = "./in"
    output_folder = "./out"

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith((".jpg", ".png", ".jpeg"))]

    # Iterate over each image file
    for image_file in image_files:
        # Open the image file

        image_path = os.path.join(input_folder, image_file)
        print(image_path)
        input = Image.open(image_path)
        image = remove(input)
        
        output_path = os.path.join(output_folder, image_file)
        image.save(output_path, format='PNG')
        image.close()
    print("Images saved successfully!")


if __name__ == "__main__":
    main()
