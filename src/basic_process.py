import cv2

def run_basic_demo(img_path):
    img = cv2.imread(img_path)
    if img is None:
        print("图片读取失败")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 这行代码是将彩色图转化为灰度图
    blur = cv2.GaussianBlur(gray, (5, 5), 0) # 高斯滤波
    edge = cv2.Canny(blur, 50, 150)  # 边缘检测

    cv2.imshow("Original", img)
    cv2.imshow("Gray", gray)
    cv2.imshow("Edge", edge)

    cv2.waitKey(0)
    cv2.destroyAllWindows()