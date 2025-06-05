import time
from opcua import Server
from datetime import datetime

# OPC 서버 생성
server = Server()

# 서버의 엔드포인트 설정 (IP와 포트)
server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

# 서버 시작
server.start()
print("Server started at {}".format(server.endpoint))

# 네임스페이스 추가
uri = "http://example.org"
idx = server.register_namespace(uri)

# 객체 생성
objects = server.nodes.objects
myobj = objects.add_object(idx, "ThermalCamera")
temperature_var = myobj.add_variable(idx, "Temperature", 0.0)  # 초기 온도 값 0.0

# 변수 초기화
temperature_var.set_writable()

# 데이터 변경 예시 (주기적으로 값을 변경)
while True:
    # 여기서 IR 카메라로부터 온도 값을 받아옵니다.
    temperature = 25.5  # 예시로 25.5°C
    temperature_var.set_value(temperature)  # 온도 값 갱신
    print(f"Updated Temperature: {temperature} °C")
    time.sleep(1)

# 서버 종료
server.stop()