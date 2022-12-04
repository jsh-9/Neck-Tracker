# class VideoCamera():
#     def __init__(self):
#         self.mpPose = mp.solutions.pose
#         self.pose = self.mpPose.Pose()
#         self.cap = cv2.VideoCapture(0)
#         # self.mpDraw = mp.solutions.drawing_utils
#
#     def get_frame(self):
#
#         while True:
#             success, img = self.cap.read()  # read the camera frame
#             if not success:
#                 break
#             else:
#                 imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#                 results = self.pose.process(imgRGB)
#                 id = 0
#                 lm = results.pose_landmarks.landmark[id]
#                 h, w, c = img.shape
#                 cx_nose, cy_nose = int(lm.x * w), int(lm.y * h)
#                 cv2.circle(img, (cx_nose, cy_nose), 5, (255, 255, 255), cv2.FILLED)
#
#                 id = 7
#                 lm = results.pose_landmarks.landmark[id]
#                 h, w, c = img.shape
#                 cx_l_ear, cy_l_ear = int(lm.x * w), int(lm.y * h)
#                 cv2.circle(img, (cx_l_ear, cy_l_ear), 5, (255, 0, 0), cv2.FILLED)
#
#                 id = 8
#                 lm = results.pose_landmarks.landmark[id]
#                 h, w, c = img.shape
#                 cx_r_ear, cy_r_ear = int(lm.x * w), int(lm.y * h)
#                 cv2.circle(img, (cx_r_ear, cy_r_ear), 5, (255, 0, 0), cv2.FILLED)
#
#                 id = 11
#                 lm = results.pose_landmarks.landmark[id]
#                 h, w, c = img.shape
#                 cx_l_shoulder, cy_l_shoulder = int(lm.x * w), int(lm.y * h)
#                 cv2.circle(img, (cx_l_shoulder, cy_l_shoulder), 5, (255, 0, 0), cv2.FILLED)
#
#                 id = 12
#                 lm = results.pose_landmarks.landmark[id]
#                 h, w, c = img.shape
#                 cx_r_shoulder, cy_r_shoulder = int(lm.x * w), int(lm.y * h)
#                 cv2.circle(img, (cx_r_shoulder, cy_r_shoulder), 5, (255, 0, 0), cv2.FILLED)
#
#                 cx_middle_shoulder, cy_middle_shoulder = int(
#                     abs(cx_r_shoulder - cx_l_shoulder) / 2) + cx_r_shoulder, cy_r_shoulder
#                 cv2.circle(img, (cx_middle_shoulder, cy_middle_shoulder), 5, (255, 0, 0), cv2.FILLED)
#
#                 if flag:
#                     length_0 = [calculateDistance(cx_nose, cy_nose, cx_middle_shoulder, cy_middle_shoulder)]  # ,
#
#                     flag = False
#                     first_time = time.time()
#                 else:
#                     length = [calculateDistance(cx_nose, cy_nose, cx_middle_shoulder, cy_middle_shoulder)]  # ,
#
#                     ##############################################################################
#                     ##############################################################################
#                     duration = time.time() - first_time
#
#                     if duration > 20 and (length_0[0] - length[0]) > 20:
#                         cv2.putText(img, "Dangers ", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
#                                     (255, 0, 0), 3)
#                         flag_change_first_time = True
#                     # else:
#                     #     if flag_change_first_time:
#                     #         first_time = time.time()
#                     #         flag_change_first_time = False
#
#                     cv2.putText(img, " " + str(length_0[0] - length[0]), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0),
#                                 3)
#                     # cv2.putText(img,""+str(length_0[1])+"   "+ str(length[1]), (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
#                     # cv2.putText(img,"right ear to right shoulder  "+str(length_0[2] - length[2]), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
#                     ret, buffer = simplejpeg.encode_jpeg()('.jpg', img)
#                     frame = buffer.tobytes()
#                     return frame
#                     # yield (b'--frame\r\n'
#                     #        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame



# <!--      <div>-->
# <!--          <a    style="margin-top: 20px; top:65%; left:76%; position: absolute;"-->
# <!--                target="_blank"-->
# <!--                class="btn btn-info pull-right"-->
# <!--                href="{% url 'play_video'%}">-->
# <!--                Play Video-->
#
# <!--          </a>-->
# <!--      </div>-->