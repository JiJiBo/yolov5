import os
import shutil
import random

def split_data(images_dir, labels_dir, output_dir, train_ratio=0.8, val_ratio=0.1):
    """
    将图片和标注文件按比例划分为训练集、验证集和测试集。
    :param images_dir: 图片目录
    :param labels_dir: 标注目录
    :param output_dir: 输出目录
    :param train_ratio: 训练集比例
    :param val_ratio: 验证集比例
    """
    # 获取所有图片文件
    image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png'))]
    random.shuffle(image_files)

    # 计算数据集划分数量
    total_images = len(image_files)
    train_count = int(total_images * train_ratio)
    val_count = int(total_images * val_ratio)

    # 划分数据集
    train_images = image_files[:train_count]
    val_images = image_files[train_count:train_count + val_count]
    test_images = image_files[train_count + val_count:]

    # 创建输出目录
    for subset in ['train', 'val', 'test']:
        os.makedirs(os.path.join(output_dir, 'images', subset), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'labels', subset), exist_ok=True)

    # 复制文件
    for subset, images in zip(['train', 'val', 'test'], [train_images, val_images, test_images]):
        for image in images:
            shutil.copy(os.path.join(images_dir, image), os.path.join(output_dir, 'images', subset, image))
            label = os.path.splitext(image)[0] + '.txt'
            if os.path.exists(os.path.join(labels_dir, label)):
                shutil.copy(os.path.join(labels_dir, label), os.path.join(output_dir, 'labels', subset, label))

if __name__ == '__main__':
    images_dir = r'C:\Users\12700\PycharmProjects\yolov5\cf_monster\cf'
    labels_dir = r'C:\Users\12700\PycharmProjects\yolov5\cf_monster\yolocf'
    output_dir = r'C:\Users\12700\PycharmProjects\yolov5\cf_monster\out_dir'

    split_data(images_dir, labels_dir, output_dir)
