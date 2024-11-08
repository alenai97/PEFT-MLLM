import os
import subprocess
import json

# 指定存储图片的根文件夹
root_folder = "datasets/CALTECH/test"
# 获取根文件夹内的子文件夹列表
subfolders = [f.path for f in os.scandir(root_folder) if f.is_dir()]

# 设置结果文件保存的根目录
result_root_folder = "test"

for folder_path in subfolders:
    # 获取当前文件夹的名称
    folder_name = os.path.basename(folder_path)

    # 获取当前文件夹中所有图片的文件路径
    image_paths = sorted([os.path.join(root, file) for root, dirs, files in os.walk(folder_path) for file in files if file.endswith((".jpg", ".jpeg", ".png"))])
    # 创建一个空的列表以存储每张图片的名称和回复，作为字典
    results = []

    # 使用 cli.py 进行模型推理
    for image_path in image_paths:
        # 获取图片文件的名称
        image_name = os.path.basename(image_path)

        # 启动 cli.py 进程
        command = [
            "python", "-m", "llava.serve.cli",
            "--model-path", "liuhaotian/llava-v1.5-13b",
            "--image-file", image_path,
            "--load-8bit"
        ]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, text=True, bufsize=1)

        assistant_response = ""
        while True:
            output = process.stdout.readline()
            if not output:
                break
            assistant_response += output

        # 等待 cli.py 进程结束
        process.communicate()

        # 创建一个字典，用于存储每张图片和回复
        sample_data = {"name": image_name, "response": assistant_response}

        # 将字典添加到结果列表
        results.append(sample_data)

        # 构建结果文件的完整路径
        save_file_name = folder_name + "_caltech.json"
        save_path = os.path.join(result_root_folder, save_file_name)

        # 保存结果到指定路径
        with open(save_path, "w") as json_file:
            json.dump(results, json_file, ensure_ascii=False, indent=4)  

print("所有图片已处理完毕")


