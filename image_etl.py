import cv2
import os

# Folder paths
input_folder = "raw_images"
output_folder = "processed_images"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, file))
    resized_img = cv2.resize(img, (224, 224))
    normalized_img = resized_img / 255.0
    cv2.imwrite(os.path.join(output_folder, file), resized_img)