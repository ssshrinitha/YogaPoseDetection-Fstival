import cv2
# import PoseFstival
from app import video

class Video(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):

        ret,frame=self.video.read()
        # ret,frame=PoseFstival.detectPose(frame, video , display=False)
        
        # Perform Pose landmark detection.
        # pose_video = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=1)

        # frame, landmarks = PoseFstival.detectPose(frame, PoseFstival.pose_video, display=False)
    
    # Check if the landmarks are detected.
        # if landmarks:
        
        # Perform the Pose Classification.
            # frame, _ = PoseFstival.classifyPose(landmarks, frame, display=False)
        ret,jpg=cv2.imencode('.jpg',frame)
        return jpg.tobytes()

