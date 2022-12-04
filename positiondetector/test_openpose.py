import cv2
import mediapipe as mp
import time
import numpy as np
from .utils import *
import simplejpeg
class pose_tracking:
    def __init__(self, vs):
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()
        self.cap =vs
        # self.mpDraw = mp.solutions.drawing_utils

    def get_frames(self):
        cap = cv2.VideoCapture(0)
        while True:
            success, img = cap.read()  # read the camera frame
            if not success:
                break
            else:
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                results = self.pose.process(imgRGB)
                id = 0
                lm = results.pose_landmarks.landmark[id]
                h, w, c = img.shape
                cx_nose, cy_nose = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx_nose, cy_nose), 5, (255, 255, 255), cv2.FILLED)

                id = 7
                lm = results.pose_landmarks.landmark[id]
                h, w, c = img.shape
                cx_l_ear, cy_l_ear = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx_l_ear, cy_l_ear), 5, (255, 0, 0), cv2.FILLED)

                id = 8
                lm = results.pose_landmarks.landmark[id]
                h, w, c = img.shape
                cx_r_ear, cy_r_ear = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx_r_ear, cy_r_ear), 5, (255, 0, 0), cv2.FILLED)

                id = 11
                lm = results.pose_landmarks.landmark[id]
                h, w, c = img.shape
                cx_l_shoulder, cy_l_shoulder = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx_l_shoulder, cy_l_shoulder), 5, (255, 0, 0), cv2.FILLED)

                id = 12
                lm = results.pose_landmarks.landmark[id]
                h, w, c = img.shape
                cx_r_shoulder, cy_r_shoulder = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx_r_shoulder, cy_r_shoulder), 5, (255, 0, 0), cv2.FILLED)

                cx_middle_shoulder, cy_middle_shoulder = int(
                    abs(cx_r_shoulder - cx_l_shoulder) / 2) + cx_r_shoulder, cy_r_shoulder
                cv2.circle(img, (cx_middle_shoulder, cy_middle_shoulder), 5, (255, 0, 0), cv2.FILLED)

                if flag:
                    length_0 = [calculateDistance(cx_nose, cy_nose, cx_middle_shoulder, cy_middle_shoulder)]  # ,

                    flag = False
                    first_time = time.time()
                else:
                    length = [calculateDistance(cx_nose, cy_nose, cx_middle_shoulder, cy_middle_shoulder)]  # ,

                    ##############################################################################
                    ##############################################################################
                    duration = time.time() - first_time

                    if duration > 20 and (length_0[0] - length[0]) > 20:
                        cv2.putText(img, "Dangers ", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (255, 0, 0), 3)
                        flag_change_first_time = True
                    else:
                        if flag_change_first_time:
                            first_time = time.time()
                            flag_change_first_time = False


                    cv2.putText(img, " " + str(length_0[0] - length[0]), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0),
                                3)
                    # cv2.putText(img,""+str(length_0[1])+"   "+ str(length[1]), (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                    # cv2.putText(img,"right ear to right shoulder  "+str(length_0[2] - length[2]), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                    ret, buffer = simplejpeg.encode_jpeg()('.jpg', img)
                    frame = buffer.tobytes()
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame



#
# #cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('/media/jsh/Data/archive/AIBridge/pose/action_trainer/video/2.mp4')
# pTime = 0
#
# flag = True
# flag_change_first_time = False
# while True:
#     cap = cv2.VideoCapture(0)
#     i = 0
#     while (cap.isOpened()):
#         ret, img = cap.read()
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         results = pose.process(imgRGB)
#         # print(results.pose_landmarks)
#         # if results.pose_landmarks:
#         #     mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
#         # for id, lm in enumerate(results.pose_landmarks.landmark):
#         id =0
#         lm = results.pose_landmarks.landmark[0]
#         h, w,c = img.shape
#         # print(id, lm)
#         cx_nose, cy_nose = int(lm.x*w), int(lm.y*h)
#         cv2.circle(img, (cx_nose, cy_nose), 5, (255,255,255), cv2.FILLED)
#         # cv2.putText(img, str(cx_nose)+" "+ str(cy_nose), (cx_nose+30, cy_nose+30), cv2.FONT_HERSHEY_SIMPLEX,
#         #             1, (255, 0, 0), 3)
#
#         # cTime = time.time()
#         # fps = 1/(cTime-pTime)
#         # pTime = cTime
#
#         # cv2.putText(img, str(int(fps)), (50,50), cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0), 3)
#         # cv2.imshow("Image", img)
#         # cv2.waitKey(1)
#
#         id = 7
#         lm = results.pose_landmarks.landmark[id]
#         h, w, c = img.shape
#         # print(id, lm)
#         cx_l_ear, cy_l_ear = int(lm.x * w), int(lm.y * h)
#         cv2.circle(img, (cx_l_ear, cy_l_ear), 5, (255, 0, 0), cv2.FILLED)
#
#         # cTime = time.time()
#         # fps = 1 / (cTime - pTime)
#         # pTime = cTime
#         #
#         # cv2.putText(img, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
#         # cv2.imshow("Image", img)
#         # cv2.waitKey(1)
#
#         id = 8
#         lm = results.pose_landmarks.landmark[id]
#         h, w, c = img.shape
#         # print(id, lm)
#         cx_r_ear, cy_r_ear = int(lm.x * w), int(lm.y * h)
#         cv2.circle(img, (cx_r_ear, cy_r_ear), 5, (255, 0, 0), cv2.FILLED)
#
#         id = 11
#         lm = results.pose_landmarks.landmark[id]
#         h, w, c = img.shape
#         # print(id, lm)
#         cx_l_shoulder, cy_l_shoulder = int(lm.x * w), int(lm.y * h)
#         cv2.circle(img, (cx_l_shoulder, cy_l_shoulder), 5, (255, 0, 0), cv2.FILLED)
#
#         id = 12
#         lm = results.pose_landmarks.landmark[id]
#         h, w, c = img.shape
#         # print(id, lm)
#         cx_r_shoulder, cy_r_shoulder = int(lm.x * w), int(lm.y * h)
#         cv2.circle(img, (cx_r_shoulder, cy_r_shoulder), 5, (255, 0, 0), cv2.FILLED)
#
#         cx_middle_shoulder, cy_middle_shoulder = int(abs(cx_r_shoulder - cx_l_shoulder) / 2) + cx_r_shoulder, cy_r_shoulder
#         cv2.circle(img, (cx_middle_shoulder, cy_middle_shoulder), 5, (255, 0, 0), cv2.FILLED)
#
#
#         if flag:
#             # coordination = [[cx_nose, cy_nose], [cx_l_ear, cy_l_ear],
#             #                 [cx_r_ear, cy_r_ear], [cx_l_shoulder, cy_l_shoulder],
#             #                 [cx_r_shoulder, cy_r_shoulder],[cx_middle_shoulder, cy_middle_shoulder] ]
#             length_0=[calculateDistance(cx_nose, cy_nose, cx_middle_shoulder, cy_middle_shoulder)]#,
#                       # calculateDistance(cx_l_ear, cy_l_ear, cx_l_shoulder, cy_l_shoulder),
#                       # calculateDistance(cx_r_ear, cy_r_ear, cx_r_shoulder,cy_r_shoulder)]
#
#             flag = False
#             first_time = time.time()
#         else:
#             # cv2.putText(img, str(coordination[0][0]) + " " + str(coordination[0][1]), (cx_nose, cy_nose), cv2.FONT_HERSHEY_SIMPLEX,
#             #             1, (255, 0, 0), 3)
#
#             # cx, cy = coordination[0][0], coordination[0][1]
#             # cv2.circle(img, (cx, cy), 5, (255,255, 0), cv2.FILLED)
#             #
#             # cx, cy = coordination[6][0], coordination[6][1]
#             # cv2.circle(img, (cx, cy), 5, (255, 255, 0), cv2.FILLED)
#             ##############################################################################
#             ##############################################################################
#             # lineESHL = [coordination[0], [cx3, cy3]]
#             # lineESHL = [coordination[0], [cx3, cy3]]
#             length = [calculateDistance(cx_nose, cy_nose, cx_middle_shoulder, cy_middle_shoulder)]#,
#                         # calculateDistance(cx_r_ear, cy_r_ear, cx_r_shoulder, cy_r_shoulder),
#                         # calculateDistance(cx_l_ear, cy_l_ear, cx_l_shoulder, cy_l_shoulder)]
#
#             # vector_2 = [cx3, cy3]
#             # unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
#             #
#             # unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
#             #
#             # dot_product = np.dot(unit_vector_1, unit_vector_2)
#             #
#             # angle = np.arccos(dot_product)
#             # print()
#             # print("###############", length0, length1, length0 - length1 )
#             ##############################################################################
#             ##############################################################################
#             duration = time.time() - first_time
#
#             if duration > 20 and (length_0[0] - length[0]) > 20:
#                 cv2.putText(img, "Dangers " , (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
#                             (255, 0, 0), 3)
#                 flag_change_first_time = True
#             else:
#                 if flag_change_first_time:
#                     first_time = time.time()
#                     flag_change_first_time =False
#
#             cTime = time.time()
#             fps = 1 / (cTime - pTime)
#             pTime = cTime
#
#             cv2.putText(img," "+str(length_0[0] - length[0]), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
#             # cv2.putText(img,""+str(length_0[1])+"   "+ str(length[1]), (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
#             # cv2.putText(img,"right ear to right shoulder  "+str(length_0[2] - length[2]), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
#
#             cv2.imshow("Image", img)
#             cv2.waitKey(1)
