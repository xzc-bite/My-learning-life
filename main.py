from src.basic_process import run_basic_demo
from src.camera_demo import run_camera
from src.image_transform import run_transform_demo

if __name__ == "__main__":
    print("===== OpenCV 通用视觉工具箱 =====")
    print("1. 基础图像处理演示")
    print("2. 摄像头实时预览")
    print("3. 图像变换演示")

    opt = input("请选择功能序号：")
    if opt == "1":
        run_basic_demo("assets/test.jpg")
    elif opt == "2":
        run_camera()
    elif opt == "3":
        run_transform_demo("assets/test.jpg")
    else:
        print("输入错误")