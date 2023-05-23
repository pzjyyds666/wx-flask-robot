# 创建应用实例
import sys

from wxcloudrun import app

# 启动Flask Web服务
if __name__ == '__main__':
    app.run(host=sys.argv[1], port=80)
    # app.run(port='8080', debug=True)
