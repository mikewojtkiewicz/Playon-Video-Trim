import os
from datetime import datetime
from moviepy.editor import VideoFileClip


def main():
    while True:
        start_time = datetime.now()
        folder_location = input("Enter Folder Location: ")
        output_location = input("Enter Output Location: ")
        folder = os.listdir(folder_location)
        print(f'{start_time}: Processing {len(folder)} files...')
        for file in folder:
            if file.endswith('.mp4'):
                file_name = f"{folder_location}\\{file}"
                video_file = VideoFileClip(file_name).cutout(0, 18)
                new_file_duration = float(video_file.duration) - 6.5
                video_file.duration = new_file_duration

                name_array = file.split('-')
                new_file_name = f"{name_array[0].strip()} - {name_array[1].strip()}.mp4"
                video_file.write_videofile(f"{output_location}\\{new_file_name}")
                video_file.close()
        end_time = datetime.now()
        print(f'Ended in {end_time - start_time} seconds')
        continue_input = input("Should I update another folder? (y or n): ")
        if continue_input.lower() == "n":
            return False


main()
