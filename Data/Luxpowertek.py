import requests
from datetime import datetime

now = datetime.now()
format_datetime = now.strftime("%Y-%m-%d")

def login_to_luxpowertek():
    # xác định URL đăng nhập
    login_url = "https://server.luxpowertek.com/WManage/web/login"

    # Xác định thông tin đăng nhập
    payload = {
        "account": "tuan07081998",
        "password": "manhtuan98",
    }

    # Xác đinh Header, thể hiện rằng yêu cầu HTTP này được gửi từ một trình duyệt giả mạo, cụ thể là một trình duyệt giả mạo mô phỏng Chrome (58.0.3029.110) trên một máy tính chạy Windows (Windows NT 10.0; Win64; x64).
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    }

    # Tạo một phiên và đặt tiêu đề
    session = requests.Session()
    session.headers.update(headers)

    # Gửi yêu cầu POST và tự động xử lý cookie
    response = session.post(login_url, data=payload)

    # Kiểm tra phiên đăng nhập có thành công hay không
    if response.status_code == 200:
        return session
    else:
        print(f"Login Failed. Status Code: {response.status_code}")

def Config_Inverter_List():
    session = login_to_luxpowertek()
    payload = {
        "page": 1,
        "rows": 20,
        "plantId": 23127,
        "searchText": "",
        "targetSerialNum": 9192004039
    }
    response_List = session.post("https://server.luxpowertek.com/WManage/web/config/inverter/list", data=payload)
    if response_List.status_code == 200:
        response_json = response_List.json()
        print(response_json)
    else:
        print(f"Failed to retrieve data. Status Code: {response_List.status_code}")

def getInverterEnergyInfo():
    session = login_to_luxpowertek()
    payload = {
        "serialNum": 1233022323
    }
    response_getInverterEnergyInfo = session.post("https://server.luxpowertek.com/WManage/api/inverter/getInverterEnergyInfo", data=payload)
    if response_getInverterEnergyInfo.status_code == 200:
        response_json = response_getInverterEnergyInfo.json()
        print(response_json)
    else:
        print(f"Failed to retrieve data. Status Code: {response_getInverterEnergyInfo.status_code}")

def getInverterRuntime():
    session = login_to_luxpowertek()
    payload = {
        "serialNum": 1233022323
    }
    response_getInverterRuntime = session.post("https://server.luxpowertek.com/WManage/api/inverter/getInverterRuntime", data=payload)
    if response_getInverterRuntime.status_code == 200:
        response_json = response_getInverterRuntime.json()
        print(response_json)
    else:
        print(f"Failed to retrieve data. Status Code: {response_getInverterRuntime.status_code}")

def monthColumn():
    session = login_to_luxpowertek()
    payload = {
        "serialNum": 1233022323,
        "year": now.strftime("%Y"),
        "month": now.strftime("%m")
    }
    response_monthColumn = session.post("https://server.luxpowertek.com/WManage/api/inverterChart/monthColumn", data=payload)
    if response_monthColumn.status_code == 200:
        response_json = response_monthColumn.json()
        print(response_json)
    else:
        print(f"Failed to retrieve data. Status Code: {response_monthColumn.status_code}")

monthColumn()