# -*- coding: UTF-8_general_ci -*-
#讀取電腦上有的影片
# import cv2
#
# cap = cv2.VideoCapture('20160103_112553.mp4')
#
# while(cap.isOpened()):
#   ret, frame = cap.read()
#
#   cv2.imshow('frame',frame)
#   if cv2.waitKey(1) & 0xFF == ord('q'):
#     break
#
# cap.release()
# cv2.destroyAllWindows()

#儲存影片
import cv2
#選擇CAM
cap = cv2.VideoCapture(1)

# 設定擷取影像的尺寸大小
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

# 使用 XVID 編碼
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 建立 VideoWriter 物件，儲存影片至 output.avi
# FPS 值為 20.0，解析度為 640x360
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 360))

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    # 寫入影格
    out.write(frame)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break

# 釋放所有資源
cap.release()
out.release()
cv2.destroyAllWindows()