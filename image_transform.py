import cv2

def run_transform_demo(img_path):
    img = cv2.imread(img_path)
    if img is None:
        return

    resize_img = cv2.resize(img, (400, 300))
    rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    cv2.imshow("Resize", resize_img) # 重新定义大小
    cv2.imshow("Rotated", rotated_img) # 翻转
    cv2.waitKey(0)
    cv2.destroyAllWindows()