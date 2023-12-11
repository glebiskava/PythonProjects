import os
from datetime import datetime
import shutil
import exifread

def get_image_date(image_path):
    try:
        with open(image_path, 'rb') as file:
            tags = exifread.process_file(file, details=False)
            date_str = tags.get('EXIF DateTimeOriginal')
            if date_str:
                return datetime.strptime(str(date_str), '%Y:%m:%d %H:%M:%S')
    except Exception as e:
        print(f"Error reading EXIF data for {image_path}: {e}")
    return None

def sort_images_by_date(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    files = os.listdir(source_dir)
    files.sort(key=lambda x: get_image_date(os.path.join(source_dir, x)), reverse=True)

    for filename in files:
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            source_path = os.path.join(source_dir, filename)
            date_taken = get_image_date(source_path)

            if date_taken:
                date_folder = date_taken.strftime('%Y-%m-%d')
                destination_path = os.path.join(destination_dir, date_folder)

                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)

                shutil.copy(source_path, destination_path)
                print(f"Moved {filename} to {destination_path}")

if __name__ == "__main__":
    source_directory = "\\E:\\Photobuch"
    destination_directory = "\\E:\\PhotobuchSorted"

    sort_images_by_date(source_directory, destination_directory)
