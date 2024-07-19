from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 啟用跨域支持
api = Api(app)

logs = []

class Log(Resource):
    def post(self):
        log = request.get_json()
        log['timestamp'] = datetime.now().isoformat()  # 添加時間戳
        logs.append(log)
        print(f"Received log: {log}")  # 調試打印接收到的日誌
        return {"message": "Log recorded successfully"}, 201

    def get(self):
        transaction_id = request.args.get('transactionId')
        if transaction_id:
            filtered_logs = [log for log in logs if log['transactionId'] == transaction_id]
            if filtered_logs:
                return jsonify(filtered_logs)
            else:
                return {"message": "No logs found for the given transaction ID"}, 404
        else:
            return jsonify(logs)  # 如果沒有提供transactionId，返回所有日誌

api.add_resource(Log, '/logs')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
