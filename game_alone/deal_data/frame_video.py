import cv2
import os


def video_to_frames(video_path, output_folder, frame_interval=1):
    """
    将视频拆分为图片
    :param video_path: 视频文件路径
    :param output_folder: 输出图片的文件夹路径
    :param frame_interval: 保存的帧间隔，默认1表示保存每一帧
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("无法打开视频文件:", video_path)
        return

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"总帧数: {frame_count}")

    current_frame = 0
    saved_frames = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 每隔 frame_interval 保存一帧
        if current_frame % frame_interval == 0:
            output_file = os.path.join(output_folder, f"frame_{current_frame:05d}.jpg")
            cv2.imwrite(output_file, frame)
            saved_frames += 1

        current_frame += 1

    cap.release()
    print(f"保存的帧数: {saved_frames}, 输出目录: {output_folder}")


# 示例用法
video_path = r"C:\Users\12700\PycharmProjects\yolov5\cf_monster\穿越火线 怪物.mp4"  # 替换为你的视频文件路径
output_folder = r"C:\Users\12700\PycharmProjects\yolov5\cf_monster\穿越火线怪物"  # 替换为你的输出目录路径
frame_interval = 20

video_to_frames(video_path, output_folder, frame_interval)
