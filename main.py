import os
from PIL import Image
import math


def merge_images(folder_path, output_file):
    images = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, filename)
            with Image.open(img_path) as img:
                images.append(img.copy())

    if not images:
        print(f"Изображения не найдены в папке {folder_path}.")
        return

    thumbnail_size = 200  # Размер миниатюр
    padding = 10  # Промежуток между миниатюрами

    num_images = len(images)
    num_cols = math.ceil(math.sqrt(num_images))
    num_rows = math.ceil(num_images / num_cols)

    canvas_width = num_cols * (thumbnail_size + padding) + padding
    canvas_height = num_rows * (thumbnail_size + padding) + padding

    background = Image.new('RGB', (canvas_width, canvas_height), (255, 255, 255))

    for index, img in enumerate(images):
        img.thumbnail((thumbnail_size, thumbnail_size))
        row = index // num_cols
        col = index % num_cols
        x = col * (thumbnail_size + padding) + padding
        y = row * (thumbnail_size + padding) + padding
        background.paste(img, (x, y), img if img.mode == 'RGBA' else None)

    background.save(output_file, 'TIFF')
    print(f"Файл {output_file} успешно создан.")


def process_all_folders(root_folder):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            output_file = os.path.join(folder_path, f"{folder_name}_Result.tif")
            merge_images(folder_path, output_file)


if __name__ == '__main__':
    root_folder = 'test'
    process_all_folders(root_folder)
