import os
import sys
import cv2
import shutil
from tqdm import tqdm
import argparse

class video:

    def __init__(self, dir_name, dest_dir, stride, blanks):
        self.dir_name = dir_name
        self.dest_dir = dest_dir
        self.stride = stride
        self.blanks = blanks
        self.preprocessing()

    def preprocessing(self):
        if os.path.exists(self.dir_name):
            print(f"\nExtract directory : {os.getcwd()}/{self.dir_name}")
            print(f"Save directory : {os.getcwd()}/{self.dest_dir}\n")
        else:
            print("\n'" + self.dir_name+ "' is not exists.")
            print("Please check your sour_dir.\n")
            sys.exit()

        if os.path.exists(self.dest_dir):
            shutil.rmtree(self.dest_dir)

        os.mkdir(self.dest_dir)


    def run(self):
        file_list = os.listdir(self.dir_name)

        for file in file_list:
            if self.is_video_file(file):
                self.extract_frame(file)
            else:
                print(f"\<{file}\> is not video file")
                pass

        os.system(f"chmod 777 -R {self.dest_dir}")
        print("frame extract was done successfully.\n")


    def is_video_file(self, file_name):
        """Check video file format"""

        # If you want add video file format, then add format below line.
        video_file_format = ["mp4", "avi"]
        file_extension = file_name.split('.')[-1]

        if file_extension in video_file_format:
            return True
        else:
            return False


    def extract_frame(self, file_name):
        video_file = os.path.join(self.dir_name, file_name)
        capture = cv2.VideoCapture(video_file)
        stride = 1

        for index in tqdm(range(int(capture.get(cv2.CAP_PROP_FRAME_COUNT)))):
            if(index == int(capture.get(cv2.CAP_PROP_FRAME_COUNT))):
                break

            ret, frame = capture.read()

            if index % self.stride:
                continue

            if self.blanks is not None:
                for blank in self.blanks:
                    x1, y1, x2, y2 = blank
                    frame[y1:y2, x1:x2] = 0
                
            index = capture.get(cv2.CAP_PROP_POS_FRAMES)
            frame_name = \
                f"{file_name.split()[-1].split('.')[-2]}_{str(int(index))}.jpg"

            try:
                save_name = os.path.join(self.dest_dir, frame_name)
                cv2.imwrite(save_name, frame)
            except:
                pass


        capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sour_dir", default = "video_files", type=str,
                        help="directory name that have video files")

    parser.add_argument("--dest_dir", default = "frames", type=str,
                        help="destination directory name")

    parser.add_argument("--stride", default = 1, type=int,
                        help="how many frames to skip")

    parser.add_argument("--blanks", nargs='+', type=int, action='append',
                        help="format: left, top, right, bottom")

    args = parser.parse_args()
    video = video(dir_name = args.sour_dir, dest_dir = args.dest_dir, \
                stride = args.stride, blanks = args.blanks)
    
    video.run()
