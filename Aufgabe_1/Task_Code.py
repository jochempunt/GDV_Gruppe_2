import cv2
import math
import numpy as np

#fps = 10
#size = (1270, 720)
#fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#video_Out = cv2.VideoWriter('Illusion.avi', fourcc, fps, size)
image_Width = 1280
image_Height = 720
blank_IMG = np.zeros((image_Height, image_Width, 1), np.uint8)

gray_Value = 0
for i in range(int(image_Width/5)):
    for j in range(5):
        blank_IMG[:, i*5+j] = [gray_Value]
    gray_Value += 1
copy_Array = blank_IMG[350:450, 600:700]
blank_IMG[100:200, 1150:1250] = copy_Array
blank_IMG[100:200, 30:130] = copy_Array
title = "Grayscale"
cv2.namedWindow(title, cv2.WINDOW_NORMAL)


def circle_path(t, scale, offset):
    result_Value = (int(scale*math.cos(t)+offset), 400)
    return result_Value


backup_Image = blank_IMG.copy()
graySquareColor = 127
timer = 1
while True:
    timer += 1
    backup_Image[int(400 + 30*math.cos(timer * 0.03)): int(500 + 30*math.cos(timer * 0.03)), timer:timer+100] = copy_Array
    animation_Image = backup_Image
    backup_Image = blank_IMG.copy()
    #video_Out.write(animation_Image)
    cv2.imshow(title, animation_Image)
   
    if cv2.waitKey(8) == ord('q'):
        cv2.destroyAllWindows()
        break
    if (timer >= 1179):
        break
if cv2.waitKey(0) == ord('q'):
    #video_Out.release()
    cv2.destroyAllWindows()