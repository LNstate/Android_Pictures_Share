from flask import Flask, jsonify, url_for
import os

app = Flask(__name__)

# 假设图片存放在 'uploads' 文件夹中
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/images', methods=['GET'])
def get_images():
    # 列出 uploads 文件夹中的所有图片文件
    image_list = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):  # 你可以根据需求扩展图片类型
            # 使用 url_for 函数生成图片的完整 URL
            image_url = url_for('static', filename=f'{UPLOAD_FOLDER}/{filename}', _external=True)
            image_list.append({'imageUrl': image_url})

    # 返回 JSON 响应
    return jsonify(image_list)

if __name__ == '__main__':
    app.run(debug=True)
