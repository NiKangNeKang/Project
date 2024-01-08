from flask import Flask, request, render_template
import requests, json

app = Flask(__name__)

import requests, json

def Kakao_Geocoding(address):
    if not address: # 사용자가 주소를 아무것도 입력하지 않았을 때
        return "empty"
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    # 주소를 string으로 받아서 위경도 좌표를 list로 반환함.
    # 'KaKaoAK ' 뒤에 개인키만 입력함.
    # ex) KakaoAK 21ba322daf2d740f327e6b8316b81333
    headers = {"Authorization": "KakaoAK 21ba322daf2d740f327e6b8316b81857"}
    # try , except 문법을 추가하여 에러가 나더라도 프로그램이 진행될 수 있도록 설계함.
    # 에러가 발생하면 [0,0]을 위경도로 설정함.
    try:
        api_json = json.loads(str(requests.get(url,headers=headers).text))
        address = api_json['documents'][0]['address']
        coordinate = [str(address['x']), str(address['y'])]
        # address_name = address['address_name']
        return coordinate
    
    except:
        return [0,0]

@app.route('/', methods=['GET'])
def index():
    return render_template('kakao.html')

@app.route('/result', methods=['POST'])
def result():
    address = request.form['address']
    result = Kakao_Geocoding(address)
    if result == "empty":
        return "hey you didn't type anything!"
    elif result == [0,0]:
        return "Plz check the address"
    else:
        return render_template('kakao.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80',debug = True)