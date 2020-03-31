Getting Started
---------------
```
$ git clone https://github.com/lyjourney/video2frame.git
$ cd video2frame
$ python3 extract_frame.py [--sour_dir <name>] [--dest_dir <name>] [--stride <num>] [--blanks <left, top, right, bottom>]
```
Usage example
-------------
```
$ python3 extract_frame.py \
  --sour_dir video_files \
  --dest_dir frames \
  --stride 3 \
  --blanks 1000 130 1600 400 \
  --blanks ...
```

Directory
---------
```
video2frame/
└─ video_files/
    ├─ video1.mp4
    ├─ video2.avi
    ├─ video3.mp4
    └─ ...
```
Python package list
-------------------
* cv2
* shutil
* tqdm
