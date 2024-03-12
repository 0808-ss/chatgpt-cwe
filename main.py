import os
from openai import OpenAI
import shutil
import subprocess
import config

api_key = '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'

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"


def openai_reply(content):
    client = OpenAI(api_key=api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "依据提示生成代码",
            },
            {
                "role": "user",
                "content": content,
            }

        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content
    # gpt的接口调用，单轮对话，没有使用流式对话


def read_file(name_file):
    with open(name_file, 'r') as file:
        file_content = file.read()
    return file_content
    # 返回了文件的文本内容，包含换行符和空格等格式文件


def traverse_folder(relative_folder_path):
    list_file = []
    absolute_folder_path = os.path.abspath(relative_folder_path)

    for root, dirs, files in os.walk(absolute_folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            list_file.append(file_path)

    return list_file
    # 返回了遍历文件的列表


def traverse_folder_no_sub_folder(folder_path):
    file_list = []
    try:
        # 获取文件夹下的所有文件和子文件夹
        entries = os.listdir(folder_path)

        # 遍历所有文件和文件夹
        for entry in entries:
            entry_path = os.path.join(folder_path, entry)

            # 检查是否为文件，而不是文件夹
            if not os.path.isfile(entry_path):
                file_list.append(entry_path)

    except Exception as e:
        print(f"Error traversing folder: {e}")

    return file_list


def create_result_folder(absolute_path):
    try:
        # 拼接result文件夹路径
        result_folder_path = os.path.join(absolute_path, 'result')

        # 检查result文件夹是否已经存在
        if os.path.exists(result_folder_path):
            print(f"Result folder already exists: {result_folder_path}")
            return result_folder_path

        # 创建result文件夹
        os.makedirs(result_folder_path)
        print(f"Created result folder: {result_folder_path}")
        return result_folder_path

    except Exception as e:
        print(f"Error creating result folder - {e}")
        return None


def gen_gpt_code():
    for cwe_name in traverse_folder_no_sub_folder(config.EXPERIMENTS):
        create_result_folder(cwe_name)
    # 创建结果文件夹

    for i in traverse_folder_no_sub_folder(config.EXPERIMENTS):
        directory_name = "scenario"

        # 使用os.path.join()来添加目录项
        new_path = os.path.join(i, directory_name)
        # print(new_path)

        files = traverse_folder(new_path)

        for trace in files:
            if trace.lower().endswith(tuple(config.VALID_EXTENSIONS)):

                try:
                    # 获取上两级目录路径
                    parent_directory = os.path.dirname(trace)
                    parent_directory = os.path.dirname(parent_directory)

                    # 拼接result文件夹路径
                    result_folder_path = os.path.join(parent_directory, 'result')

                    # 检查result文件夹是否已经存在
                    if not os.path.exists(result_folder_path):
                        print(f"Error: Result folder does not exist: {result_folder_path}")
                        continue

                    # 获取绝对地址的最后一个目录项
                    last_directory_item = os.path.basename(trace)

                    # 记录一下
                    origin_name = last_directory_item
                    # 获取基础文件名
                    base_filename = os.path.basename(trace)

                    # 使用 split 方法以点号分割字符串
                    filename_parts = base_filename.split('.')

                    # 获取去除点号后的部分
                    if len(filename_parts) > 1:
                        base_filename = filename_parts[0]
                    else:
                        base_filename = base_filename

                    # 构建文件夹路径
                    file_path = os.path.join(result_folder_path, base_filename)
                    # print(file_path)

                    try:
                        os.makedirs(file_path)
                    except FileExistsError:
                        print(f"Folder already exists at {file_path}")
                    except Exception as e:
                        print(f"Error creating folder at {file_path}: {e}")

                    file_path = os.path.join(file_path, origin_name)

                    if not os.path.exists(file_path):
                        # 文件不存在，创建文件并写入内容
                        content = read_file(trace)
                        result = openai_reply(content)

                        with open(file_path, 'w') as file:
                            file.write(result)
                        # 消除注释
                        remove_first_last_lines(file_path)
                        # 取消除注释后的内容
                        content = read_file(file_path)

                        # 复制文件
                        copy_file(trace, file_path)

                        # 插入代码
                        insert_text_after_line(file_path, config.TARGET, content)

                        print(f"Generated file in result folder: {file_path}")
                    else:
                        # 文件已存在，跳过创建
                        print(f"File already exists, skipping: {file_path}")
                except Exception as e:
                    print(f"Error generating file in result folder - {e}")


def remove_first_last_lines(file_path):
    try:
        # 读取文件内容
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # 去除首尾两行
        modified_lines = lines[1:-1]

        # 写回文件
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)

    except Exception as e:
        print(f"Error removing lines - {e}")


def insert_text_after_line(file_path, target_line, new_text):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 寻找目标行的索引
    target_index = None
    for i, line in enumerate(lines):
        if target_line in line:
            target_index = i

    if target_index is not None:
        # 插入新文本到目标行的下一行
        lines.insert(target_index + 1, new_text)

        # 将修改后的内容写回文件
        with open(file_path, 'w') as file:
            file.writelines(lines)
    else:
        print(f"Target line not found: {target_line}")


def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
    except Exception as e:
        print(f"Error copying file: {e}")


# 函数返回值说明，0代表c文件，1代表py文件
def determine_file_type(file_path):
    # 获取文件的扩展名
    _, file_extension = os.path.splitext(file_path)

    # 判断文件类型
    if file_extension.lower() == '.c':
        return 0
    elif file_extension.lower() == '.py':
        return 1
    else:
        return 2


def func_codeql():
    for cwe_name in traverse_folder_no_sub_folder(config.EXPERIMENTS):
        result_name = "result"
        new_path = os.path.join(cwe_name, result_name)
        # 找到每个结果目录
        # print(new_path)
        for result in traverse_folder_no_sub_folder(new_path):
            # print(result)
            last_item = os.path.basename(result)
            db_name = "codeql_db"
            results_csv_name = config.INTERMEDIATE_RESULT_FILE
            db_name = last_item + "_" + db_name
            # print(db_name)
            if os.path.isfile(os.path.join(result, results_csv_name)):
                print("Results file already exists, skipping: " + os.path.join(result, results_csv_name))
                continue
            for item in traverse_folder(result):
                # 绝对路径
                # print(item)
                if (determine_file_type(item) == 0):
                    print(1)
                else:
                    cmd = "codeql database create {} --language=python --overwrite --source-root ./{} ; codeql database analyze {} {} --format=csv --output={}"
                    ql_name = last_item
                    ql_name = ql_name + ".ql"
                    # 获得相对路径
                    current_directory = os.getcwd()

                    relative_path = os.path.relpath(result, current_directory)

                    cmd = cmd.format(os.path.join(result, db_name),
                                     relative_path,
                                     os.path.join(result, db_name),
                                     os.path.join(config.CODEQL, ql_name),
                                     os.path.join(result), "result.csv")
                    print(cmd)
                # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # r = p.stdout.read().decode('utf-8') + p.stderr.read().decode('utf-8')
                # print(r)


def try_gpt():
    print(openai_reply('how old are you ?'))
    return


if __name__ == "__main__":
    # gen_gpt_code()
    # try_gpt()
    func_codeql()
