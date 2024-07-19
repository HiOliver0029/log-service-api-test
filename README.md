### 後端執行(port=5001)
python app.py

### 自動產生模擬 Log(傳送至port 5001)
python simulate.py 

### 前端執行(port=3000)
node index.js

### 從swagger UI看openAPI的規則(用yaml檔改設定)
podman run -p 8080:8080 -e SWAGGER_JSON=/foo/openapi.yaml -v C:\Users\OliverLin\Desktop\OpenAPI\openapi.yaml:/foo/openapi.yaml swaggerapi/swagger-ui

### 看後端log是否傳送成功
http://localhost:5001/logs
或
curl http://localhost:5001/logs