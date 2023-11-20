from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Manager_Model
import snap7
import datetime
import json
import requests

# Create your views here.
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


def Not_Login(req):
    return redirect('/')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        if request.method == "POST":
            username = request.POST.get('User_Name')
            Password = request.POST.get('Password')
            user = authenticate(username=username, password=Password)
            if user is not None:
                # Kiểm tra điều kiện hợp lệ ==> Đăng nhập thành công
                login(request, user)
                return redirect('/index_HTML')
            else:
                try:
                    # Kiểm tra điều kiện tên người dùng nhập vào có tồn tại hay không
                    User.objects.get(username=username)
                    # Nếu người dùng có tồn tại, nhưng mật khẩu sai ==> Reload lại trang web để người dùng đăng nhập lại
                    messages.error(request, "Sai thông tin đăng nhập!!!!")
                    return redirect('/')
                except User.DoesNotExist:
                    messages.error(request, "Không tồn tại tài khoản này")
                    return redirect('/')

def index_HTML(req):
    Month = str(datetime.datetime.now().month)
    session = login_to_growatt()
    payload = {
        "plantId": "2283430"
    }
    response_getInvTotalData = session.post("https://server.growatt.com/indexbC/inv/getInvTotalData", data=payload)
    if response_getInvTotalData.status_code == 200:
        response_json = response_getInvTotalData.json()
        epvToday = response_json['obj']['epvToday']
    else:
        print(f"Lỗi lấy dữ liệu từ getInvTotalData: {response_getInvTotalData.status_code}")
    response_getTotalData = session.post("https://server.growatt.com/indexbC/getTotalData", data=payload)
    if response_getTotalData.status_code == 200:
        response_json = response_getTotalData.json()
        response_getTotalData = json.loads(response_getTotalData.content)
        eMonth = response_getTotalData['obj']['eMonth']
    else:
        print(f"Lỗi lấy dữ liệu từ getTotalData: {response_getInvTotalData.status_code}")
    return render(req, 'index.html', {'MONTH':Month, 'epvToday':epvToday, 'eMonth':eMonth})


def solars_HTML(req):
    # client = snap7.client.Client()
    # client.connect("192.168.1.202", 0, 0, 102)
    # reading = client.db_read(1, 0, 220)

    # vi_tri_1 = snap7.util.get_int(reading, 0)
    # vi_tri_2 = snap7.util.get_int(reading, 2)
    # vi_tri_3 = snap7.util.get_int(reading, 4)
    # vi_tri_4 = snap7.util.get_int(reading, 6)
    # vi_tri_5 = snap7.util.get_int(reading, 8)
    # vi_tri_6 = snap7.util.get_int(reading, 10)
    # vi_tri_7 = snap7.util.get_int(reading, 12)
    # vi_tri_8 = snap7.util.get_int(reading, 14)
    # vi_tri_9 = snap7.util.get_int(reading, 16)
    # vi_tri_10 = snap7.util.get_int(reading, 18)
    # vi_tri_11 = snap7.util.get_int(reading, 20)
    # vi_tri_12 = snap7.util.get_int(reading, 22)
    # vi_tri_13 = snap7.util.get_int(reading, 24)
    # vi_tri_14 = snap7.util.get_int(reading, 26)
    # vi_tri_15 = snap7.util.get_int(reading, 28)
    # vi_tri_16 = snap7.util.get_int(reading, 30)

    # DienAp_1 = snap7.util.get_real(reading, 32)
    # DienAp_2 = snap7.util.get_real(reading, 36)
    # DienAp_3 = snap7.util.get_real(reading, 40)
    # DienAp_4 = snap7.util.get_real(reading, 44)
    # DienAp_5 = snap7.util.get_real(reading, 48)
    # DienAp_6 = snap7.util.get_real(reading, 52)
    # DienAp_7 = snap7.util.get_real(reading, 56)
    # DienAp_8 = snap7.util.get_real(reading, 60)
    # DienAp_9 = snap7.util.get_real(reading, 64)
    # DienAp_10 = snap7.util.get_real(reading, 68)
    # DienAp_11 = snap7.util.get_real(reading, 72)
    # DienAp_12 = snap7.util.get_real(reading, 76)
    # DienAp_13 = snap7.util.get_real(reading, 80)
    # DienAp_14 = snap7.util.get_real(reading, 84)
    # DienAp_15 = snap7.util.get_real(reading, 88)
    # DienAp_16 = snap7.util.get_real(reading, 92)

    # DongDien_1 = snap7.util.get_real(reading, 96)
    # DongDien_2 = snap7.util.get_real(reading, 100)
    # DongDien_3 = snap7.util.get_real(reading, 104)
    # DongDien_4 = snap7.util.get_real(reading, 108)
    # DongDien_5 = snap7.util.get_real(reading, 112)
    # DongDien_6 = snap7.util.get_real(reading, 116)
    # DongDien_7 = snap7.util.get_real(reading, 120)
    # DongDien_8 = snap7.util.get_real(reading, 124)
    # DongDien_9 = snap7.util.get_real(reading, 128)
    # DongDien_10 = snap7.util.get_real(reading, 132)
    # DongDien_11 = snap7.util.get_real(reading, 136)
    # DongDien_12 = snap7.util.get_real(reading, 140)
    # DongDien_13 = snap7.util.get_real(reading, 144)
    # DongDien_14 = snap7.util.get_real(reading, 148)
    # DongDien_15 = snap7.util.get_real(reading, 152)
    # DongDien_16 = snap7.util.get_real(reading, 156)

    # CongSua_1 = snap7.util.get_real(reading, 160)
    # CongSua_2 = snap7.util.get_real(reading, 164)
    # CongSua_3 = snap7.util.get_real(reading, 168)
    # CongSua_4 = snap7.util.get_real(reading, 172)
    # CongSua_5 = snap7.util.get_real(reading, 176)
    # CongSua_6 = snap7.util.get_real(reading, 180)
    # CongSua_7 = snap7.util.get_real(reading, 184)
    # CongSua_8 = snap7.util.get_real(reading, 188)
    # CongSua_9 = snap7.util.get_real(reading, 182)
    # CongSua_10 = snap7.util.get_real(reading, 196)
    # CongSua_11 = snap7.util.get_real(reading, 200)
    # CongSua_12 = snap7.util.get_real(reading, 204)
    # CongSua_13 = snap7.util.get_real(reading, 208)
    # CongSua_14 = snap7.util.get_real(reading, 212)
    # CongSua_15 = snap7.util.get_real(reading, 216)
    # CongSua_16 = snap7.util.get_real(reading, 220)

    








    vi_tri_1 = 1
    vi_tri_2 = 2
    vi_tri_3 = 3
    vi_tri_4 = 4
    vi_tri_5 = 5
    vi_tri_6 = 6
    vi_tri_7 = 7
    vi_tri_8 = 8
    vi_tri_9 = 9
    vi_tri_10 = 10
    vi_tri_11 = 11
    vi_tri_12 = 12
    vi_tri_13 = 13
    vi_tri_14 = 14
    vi_tri_15 = 15
    vi_tri_16 = 16

    DienAp_1 = 115.9034
    DienAp_2 = 125.9034
    DienAp_3 = 135.9034
    DienAp_4 = 145.9034
    DienAp_5 = 155.9034
    DienAp_6 = 165.9034
    DienAp_7 = 175.9034
    DienAp_8 = 185.9034
    DienAp_9 = 195.9034
    DienAp_10 = 110.59034
    DienAp_11 = 111.59034
    DienAp_12 = 112.59034
    DienAp_13 = 113.59034
    DienAp_14 = 114.59034
    DienAp_15 = 115.59034
    DienAp_16 = 116.59034

    DongDien_1 = 101.203
    DongDien_2 = 201.203
    DongDien_3 = 301.203
    DongDien_4 = 401.203
    DongDien_5 = 501.203
    DongDien_6 = 601.203
    DongDien_7 = 701.203
    DongDien_8 = 801.203
    DongDien_9 = 901.203
    DongDien_10 = 100.1203
    DongDien_11 = 110.1203
    DongDien_12 = 120.1203
    DongDien_13 = 130.1203
    DongDien_14 = 140.1203
    DongDien_15 = 150.1203
    DongDien_16 = 160.1203

    CongSua_1 = 101.203
    CongSua_2 = 201.203
    CongSua_3 = 301.203
    CongSua_4 = 401.203
    CongSua_5 = 501.203
    CongSua_6 = 601.203
    CongSua_7 = 701.203
    CongSua_8 = 801.203
    CongSua_9 = 901.203
    CongSua_10 = 100.1203
    CongSua_11 = 110.1203
    CongSua_12 = 120.1203
    CongSua_13 = 130.1203
    CongSua_14 = 140.1203
    CongSua_15 = 150.1203
    CongSua_16 = 160.1203




    Solal = {
        'So_1':vi_tri_1,
        'Dien_Ap_1':round(DienAp_1, 4),
        'Dong_Dien_1':round(DongDien_1, 4),
        'Cong_Suat_1':round(CongSua_1, 4),
        'So_2':vi_tri_2,
        'Dien_Ap_2':round(DienAp_2, 4),
        'Dong_Dien_2':round(DongDien_2, 4),
        'Cong_Suat_2':round(CongSua_2, 4),
        'So_3':vi_tri_3,
        'Dien_Ap_3':round(DienAp_3, 4),
        'Dong_Dien_3':round(DongDien_3, 4),
        'Cong_Suat_3':round(CongSua_3, 4),
        'So_4':vi_tri_4,
        'Dien_Ap_4':round(DienAp_4, 4),
        'Dong_Dien_4':round(DongDien_4, 4),
        'Cong_Suat_4':round(CongSua_4, 4),
        'So_5':vi_tri_5,
        'Dien_Ap_5':round(DienAp_5, 4),
        'Dong_Dien_5':round(DongDien_5, 4),
        'Cong_Suat_5':round(CongSua_5, 4),
        'So_6':vi_tri_6,
        'Dien_Ap_6':round(DienAp_6, 4),
        'Dong_Dien_6':round(DongDien_6, 4),
        'Cong_Suat_6':round(CongSua_6, 4),
        'So_7':vi_tri_7,
        'Dien_Ap_7':round(DienAp_7, 4),
        'Dong_Dien_7':round(DongDien_7, 4),
        'Cong_Suat_7':round(CongSua_7, 4),
        'So_8':vi_tri_8,
        'Dien_Ap_8':round(DienAp_8, 4),
        'Dong_Dien_8':round(DongDien_8, 4),
        'Cong_Suat_8':round(CongSua_8, 4),
        'So_9':vi_tri_9,
        'Dien_Ap_9':round(DienAp_9, 4),
        'Dong_Dien_9':round(DongDien_9, 4),
        'Cong_Suat_9':round(CongSua_9, 4),
        'So_10':vi_tri_10,
        'Dien_Ap_10':round(DienAp_10, 4),
        'Dong_Dien_10':round(DongDien_10, 4),
        'Cong_Suat_10':round(CongSua_10, 4),
        'So_11':vi_tri_11,
        'Dien_Ap_11':round(DienAp_11, 4),
        'Dong_Dien_11':round(DongDien_11, 4),
        'Cong_Suat_11':round(CongSua_11, 4),
        'So_12':vi_tri_12,
        'Dien_Ap_12':round(DienAp_12, 4),
        'Dong_Dien_12':round(DongDien_12, 4),
        'Cong_Suat_12':round(CongSua_12, 4),
        'So_13':vi_tri_13,
        'Dien_Ap_13':round(DienAp_13, 4),
        'Dong_Dien_13':round(DongDien_13, 4),
        'Cong_Suat_13':round(CongSua_13, 4),
        'So_14':vi_tri_14,
        'Dien_Ap_14':round(DienAp_14, 4),
        'Dong_Dien_14':round(DongDien_14, 4),
        'Cong_Suat_14':round(CongSua_14, 4),
        'So_15':vi_tri_15,
        'Dien_Ap_15':round(DienAp_15, 4),
        'Dong_Dien_15':round(DongDien_15, 4),
        'Cong_Suat_15':round(CongSua_15, 4),
        'So_16':vi_tri_16,
        'Dien_Ap_16':round(DienAp_16, 4),
        'Dong_Dien_16':round(DongDien_16, 4),
        'Cong_Suat_16':round(CongSua_16, 4)
    }
    return render(req, 'solars.html', Solal)

def configuration_HTML(req):
    return render(req, 'configuration.html')

def manager_HTML(req):
    if req.method == "POST":
        Name = req.POST.get('add_name')
        userName = req.POST.get('add_userName')
        Password = req.POST.get('add_password')
        Press = req.POST.get('add_press')
        print(Name, userName, Password, Press)
        if Name and userName and Password and Press:
            create_user = User.objects.create_user(userName, password=Password)
            create_user.is_staff = True
            save_info = Manager_Model(Name=Name, userName=userName, Password=Password, Jurisdiction=Press)
            save_info.save()
            create_user.save()
        return redirect('/manager_HTML/')
    user_ = Manager_Model.objects.all()
    return render(req, 'manager.html', {'user_list': user_})

def manager_Delete(request, id):
    if request.method == 'POST':
        id_delete = Manager_Model.objects.get(pk=id)
        id_delete.delete()
        user_to_delete = User.objects.filter(id=id + 1).first()
        if user_to_delete:
            print(f"Thực hiện xóa user có ID {user_to_delete.id} và tên là {user_to_delete.username}")
            user_to_delete.delete()
        return redirect('/manager_HTML/')

def manager_Update(request, id):
    if request.method == "POST":
        edit_name = request.POST.get('edit_name')
        edit_user = request.POST.get('edit_userName')
        edit_password = request.POST.get('edit_password')
        edit_permission = request.POST.get('edit_permission')
        int_detele = int(id) + 1
        # print(int_detele)
        if edit_name and edit_user and edit_password and edit_permission:
            id_delete = Manager_Model.objects.get(pk=id)
            id_delete.delete()
            user_to_delete = User.objects.filter(id=int_detele).first()
            if user_to_delete:
                print(f"Thực hiện xóa user có ID {user_to_delete.id} và tên là {user_to_delete.username}")
                user_to_delete.delete()
            create_user = User.objects.create_user(edit_user, password=edit_password)
            create_user.is_staff = True
            create_user.save()
            save_info = Manager_Model(id=id, Name=edit_name, userName=edit_user, Password=edit_password, Jurisdiction=edit_permission)
            save_info.save()
            return redirect('/manager_HTML/')
    return render(request, 'manager.html')

def changepass_HTML(request):
    context = {}
    if request.method=='POST':
        pass_old = request.POST['pass_old']
        pass_new  = request.POST['pass_new']
        user = User.objects.get(id=request.user.id)
        check = user.check_password(pass_old)
        print(check)
        if check==True:
            user.set_password(pass_new)
            user.save()
            context['mess'] = 'Thay đổi mật khẩu thành công!!!'
            context['error'] = 'success_mess'
        else:
            context['mess'] = 'Mật khẩu bạn nhập không đúng'
            context['error'] = 'error_mess'


    return render(request, 'changepass.html', context)

def Logout(request):
    logout(request)
    messages.error(request, "Bạn đã đăng xuất")
    return redirect('/')