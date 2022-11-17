import glob
import cv2
from pathlib import Path
import os


def createVideo(session):

    vidSavePath = str(session.sessionPath / f"{session.sessionID}_outVid.mp4")
    fps = 30
    shape = 1078, 647
    frame_array = []

    for filename in session.imOutPath.glob("*.png"):
        filename = str(filename)

        # reading each files
        img = cv2.imread(filename)
        # resized = cv2.resize(img,shape)
        # shape = img.shape[:2]
        resized = cv2.resize(img, shape)
        # inserting the frames into an image array
        frame_array.append(resized)
    out = cv2.VideoWriter(vidSavePath, cv2.VideoWriter_fourcc(*"DIVX"), fps, shape)
    for item in frame_array:
        # writing to a image array
        out.write(item)
    out.release()


def createBodyTrackingVideos(session):

    vidSavePath = str(session.sessionPath / f"{session.sessionID}_outVid.mp4")
    # frame_array = []

    if session.useOpenPose:

        fps = 30
        shape = 1078, 647
        for count,videoPath in enumerate(session.session_settings['openPose_imgPathList']):
            frame_array = []
            vidSavePath = str(session.openPoseDataPath / f"openPoseVideo_cam{count}.mp4")
            videoPath = Path(videoPath)
            for filename in videoPath.glob("*.png"):

                filename = str(filename)
                # reading each files
                img = cv2.imread(filename)
                # resized = cv2.resize(img,shape)
                # shape = img.shape[:2]
                resized = cv2.resize(img, shape)
                # inserting the frames into an image array
                frame_array.append(resized)
            out = cv2.VideoWriter(
                vidSavePath, cv2.VideoWriter_fourcc(*"DIVX"), fps, shape
            )
            for item in frame_array:
                # writing to a image array
                out.write(item)
            out.release()
