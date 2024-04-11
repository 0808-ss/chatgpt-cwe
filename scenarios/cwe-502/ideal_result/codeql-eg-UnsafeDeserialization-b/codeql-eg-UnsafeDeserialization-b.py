from flask import Flask, request, redirect
import yaml

app = Flask(__name__)


# 反序列化传入的 YAML 负载并返回字段 "name"
@app.route('/api', methods=['GET'])
def api():
    # 获取 URL 参数中的 YAML 负载
    yaml_payload = request.args.get('payload', None)

    # 检查 YAML 负载是否为空
    if yaml_payload is None:
        return "Payload is missing", 400

    try:
        # 使用更安全的反序列化方法 safe_load()
        data = yaml.safe_load(yaml_payload)

        # 检查是否存在必要的字段
        if 'name' in data and isinstance(data['name'], str):
            return data['name']
        else:
            return "Invalid or missing 'name' field in payload", 400
    except yaml.YAMLError as e:
        return "Error parsing YAML: " + str(e), 400


if __name__ == "__main__":
    app.run(debug=True)