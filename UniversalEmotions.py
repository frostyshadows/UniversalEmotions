import argparse
import cv2
import numpy as np
from sklearn.cluster import KMeans


def create_images():
    """
    Create a .jpg frame per second of video.
    https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
    """
    for i in range(1, 5):
        count = 0
        vidcap = cv2.VideoCapture('DISFA_faces/LeftVideoSN00%d_comp.mp4'% i)
        success = True
        while success:
            vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))  # added this line
            success, image = vidcap.read()
            # print('Read a new frame: ', success)
            # save frame as JPEG file
            cv2.imwrite("DISFA_faces/LeftVideoSN00%(vid)d_comp_frame%(frame)d.jpg" % {"vid": i, "frame": count}, image)
            count += 1
    return

def preprocess_images():
    # TODO
    return


def train_model():
    # TODO
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--step', required=True,
                        choices=["images", "preprocess", "train", "visualize"])

    io_args = parser.parse_args()
    step = io_args.step

    if step == "images":
        create_images()
    elif step == "preprocess":
        preprocess_images()
    elif step == "train":
        train_model()
