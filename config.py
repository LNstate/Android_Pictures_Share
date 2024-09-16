import os

class Config:
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploaded_images')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'  # 使用SQLite数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭Flask-SQLAlchemy的修改跟踪功能
