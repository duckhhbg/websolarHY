import requests
from datetime import datetime

now = datetime.now()
format_datetime = now.strftime("%Y-%m-%d")

def login_to_growatt():
    # xác định URL đăng nhập
    login_url = "https://server.growatt.com/login"

    # Xác định thông tin đăng nhập
    payload = {
        "account": "CDT_TNUT",
        "password": "Cdt@12345",
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

# =================================================================================================================================

def getInvTotalData():
    session = login_to_growatt()
    payload = {
        "plantId": "2283430"
    }
    response_getInvTotalData = session.post("https://server.growatt.com/indexbC/inv/getInvTotalData", data=payload)
    if response_getInvTotalData.status_code == 200:
        response_json = response_getInvTotalData.json()
        print(response_json)
    else:
        print(f"Failed to retrieve data. Status Code: {response_getInvTotalData.status_code}")

# =================================================================================================================================
import json
def getTotalData():
    session = login_to_growatt()
    payload = {
        "plantId": "2283430"
    }
    response_getTotalData = session.post("https://server.growatt.com/indexbC/getTotalData", data=payload)
    if response_getTotalData.status_code == 200:
        response_json = response_getTotalData.json()
        print(response_json)
    else:
        print(f"Failed to retrieve data. Status Code: {response_getTotalData.status_code}")

# =================================================================================================================================

def getWeatherByPlantId():
    session = login_to_growatt()
    payload = {
        "plantId": "2283430"
    }
    response_getWeatherByPlantId = session.post("https://server.growatt.com/indexbC/getWeatherByPlantId", data=payload)
    if response_getWeatherByPlantId.status_code == 200:
        response_json = response_getWeatherByPlantId.json()
        print(response_json)
    else:
        print(f"Failed to retrieve data. Status Code: {response_getWeatherByPlantId.status_code}")

# =================================================================================================================================

def getInvEnergyDayChart():
    session = login_to_growatt()
    payload = {
        "plantId": "2283430",
        "date": format_datetime
    }
    response_getInvEnergyDayChart = session.post("https://server.growatt.com/indexbC/inv/getInvEnergyDayChart", data=payload)
    if response_getInvEnergyDayChart.status_code == 200:
        response_json = response_getInvEnergyDayChart.json()
        print(response_json)
        # for i in range(1, 289):
        #     field_name = f"InvEnergyDayChart_{i}"
        #     Name = response_json['obj']['pac'][i - 1]
        #     print(Name)
    else:
        print(f"Failed to retrieve data. Status Code: {response_getInvEnergyDayChart.status_code}")

# =================================================================================================================================

def getInvEnergyMonthChart():
    session = login_to_growatt()
    payload = {
        "plantId": "2283430",
        "date": now.strftime("%Y-%m")
    }
    response_getInvEnergyMonthChart = session.post("https://server.growatt.com/indexbC/inv/getInvEnergyMonthChart", data=payload)
    if response_getInvEnergyMonthChart.status_code == 200:
        response_json = response_getInvEnergyMonthChart.json()
        print(response_json)
        # for i in range(1, 32):
        #     field_name = f"InvEnergyMonthChart_{i}"
        #     if 'energy' in response_json['obj'] and i - 1 < len(response_json['obj']['energy']):
        #         Name = response_json['obj']['energy'][i - 1]
        #     else:
        #         Name = None
        #     print(f'Number: {i}', Name)
    else:
        print(f"Failed to retrieve data. Status Code: {response_getInvEnergyMonthChart.status_code}")

# =================================================================================================================================

def getInvEnergyYearChart():
    session = login_to_growatt()
    payload = {
        "plantId": "2283430",
        "date": now.strftime("%Y")
    }
    response_getInvEnergyYearChart = session.post("https://server.growatt.com/indexbC/inv/getInvEnergyYearChart", data=payload)
    if response_getInvEnergyYearChart.status_code == 200:
        response_json = response_getInvEnergyYearChart.json()
        print(response_json)
    else:
        print(f"Failed to retrieve data. Status Code: {response_getInvEnergyYearChart.status_code}")

# =================================================================================================================================

def getYearEnergyChart():
    session = login_to_growatt()
    payload = {
        "plantId": "2283430"
    }
    response_getYearEnergyChart = session.post("https://server.growatt.com/indexbC/getYearEnergyChart", data=payload)
    if response_getYearEnergyChart.status_code == 200:
        response_json = response_getYearEnergyChart.json()
        print(response_json)
        # years_list = []

        # for i, year in enumerate(response_json['obj']['years']):
        #     field_dict = {'years': year}
        #     for j in range(1, 13):
        #         field_name = f"charts_{j}"
        #         chart_value = response_json['obj']['charts'][str(i)][j - 1]
        #         field_dict[field_name] = [chart_value]
        #     years_list.append(field_dict)


        # for entry in years_list:
        #     # Move the line inside the loop to create a new field_dict for each year
        #     field_dict = {'years': entry['years']}
        #     years_ = field_dict['years']
        #     for i in range(1, 13):
        #         field_name = f"charts_{i}"
        #         field_dict[field_name] = entry.get(field_name, [])
        #         chars_ = field_dict[field_name]

            
        #         print(years_, chars_)
            

    else:
        print(f"Failed to retrieve data. Status Code: {response_getYearEnergyChart.status_code}")