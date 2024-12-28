import os
import json


def labelme_to_yolo(labelme_file, output_dir, class_mapping):
    """
    将 LabelMe JSON 文件转换为 YOLO 格式文件
    :param labelme_file: LabelMe JSON 文件路径
    :param output_dir: 输出目录
    :param class_mapping: 类别名称到 YOLO 类别 ID 的映射
    """
    # 加载 LabelMe JSON 文件
    with open(labelme_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 获取图片尺寸
    image_width = data['imageWidth']
    image_height = data['imageHeight']

    # 输出文件路径
    output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(labelme_file))[0] + '.txt')

    with open(output_file, 'w') as out_file:
        for shape in data['shapes']:
            label = shape['label']
            points = shape['points']

            # 如果类别不存在于映射中，跳过
            if label not in class_mapping:
                class_mapping[label] = len(class_mapping)

            # 计算边界框
            x_min = min(p[0] for p in points)
            y_min = min(p[1] for p in points)
            x_max = max(p[0] for p in points)
            y_max = max(p[1] for p in points)

            # 转换为 YOLO 格式
            x_center = (x_min + x_max) / 2 / image_width
            y_center = (y_min + y_max) / 2 / image_height
            width = (x_max - x_min) / image_width
            height = (y_max - y_min) / image_height

            # 写入 YOLO 格式
            class_id = class_mapping[label]
            out_file.write(f"{class_id} {x_center} {y_center} {width} {height}\n")


if __name__ == '__main__':
    # 示例：类别映射
    class_mapping = {'僵尸士兵': 0, '苍蝇头': 1, '蛇女': 2, '蓝色泰坦': 3, '放屁虫': 4, '忍者': 5, '大胖子': 6,
                     '地行鬼': 7, '泰坦Boss': 8}

    # LabelMe JSON 文件目录
    labelme_dir = r"C:\Users\12700\PycharmProjects\yolov5\cf_monster\cf"
    # 输出目录
    yolo_output_dir = r"C:\Users\12700\PycharmProjects\yolov5\cf_monster\yolocf"
    os.makedirs(yolo_output_dir, exist_ok=True)

    # 遍历目录中的 JSON 文件
    for filename in os.listdir(labelme_dir):
        if filename.endswith('.json'):
            labelme_file = os.path.join(labelme_dir, filename)
            labelme_to_yolo(labelme_file, yolo_output_dir, class_mapping)
