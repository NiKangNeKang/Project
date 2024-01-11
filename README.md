## 1. Python의 Pandas, Geopy 라이브러리를 이용한 Geocoding Tool 프로그램 <br>

GIS를 통해 공간분석을 진행할 때, 객체의 공간정보를 파악하는 것은 매우 중요하다. 이는 보통 객체의 위경도 좌표를 사용해 GIS 상에 '투영'하기 때문이다. 공간분석에서 주로 오픈소스의 데이터 위주로 진행되는데, '정부 공공데이터 포털'이나 '서울시 열린 데이터 광장'에 게시된 데이터를 이용한다. 그러나 많은 데이터 표본을 살펴보면 도로명 주소만 있거나, 위경도 좌표만 있는 사례가 빈번하다. 이러한 데이터는 GIS 상에 온전히 담아낼 수 없기 때문에 공간정보로서의 가치가 떨어진다.<br>

이때 사용할 수 있는 방법론이 지오코딩이다. 지오코딩은 객체의 도로명주소(또는 구 주소)를 위경도 좌표로 변환해주는 것을 뜻한다. 온라인에서 제공하는 상용 지오코딩 툴은 Biz-gis, Geocoder-Xr 등이 있다. 그러나 이러한 서비스들은 개별 IP당 일일 변환개수 제한(1일 10000건)이 있어 지오코딩 과정에서 데이터의 용량이 크거나(10000건 초과), 수정사항으로 번복할 때(여러 번 수행) 제약이 존재한다.<br>

이때 지오코딩을 Python으로 구현하면 일일 변환 제한 없이, 데이터를 무제한으로 변환할 수 있기 때문에 공간분석에서 유용하게 활용할 수 있다. Python은 오픈 소스로 다양한 라이브러리가 제공되고 있어서 다루는 영역이 날로 커지고 있다. 지오코딩도 예외는 아니며, Geopy라는 라이브러리를 이용해 지오코딩을 구현할 수 있다. 또한 위,경도를 주소로 변환하는 과정을 역지오코딩이라고 하는데, 역지오코딩 또한 Geopy를 이용해 구현 가능하다. 이 프로그램은 지오코딩, 역지오코딩에 대한 코드를 제공하며 단일 데이터 뿐만 아니라 대용량 데이터를 대상으로 전처리를 진행할 수 있는 툴로 개발하였다. 사용하고자 하는 데이터를 pandas 다루며 코드를 따라 실행하면 지오코딩 또는 역지오코딩이 적용된 데이터가 생성된다(확장자는 csv). 마지막으로 지오코딩과 역지오코딩 함수를 적용한 새로운 Class를 만들어보며 Python의 객체 지향 특성과 유전 상속을 활용해 보았다.  <br>

해당 프로그램을 개발할 때, 여러 난관이 있었다. 첫 번째는 Geopy 라이브러리의 정확성이었다. 지오코딩을 실행했을 때, 에러가 발생하는 객체가 존재했다. 이를 방지하고자 지오코딩 함수에 try, except문법을 적용했고 에러가 나더라도 프로그램이 실행되도록 했다. 그 후에 에러가 난 객체의 인덱스를 저장하고, 그 인덱스의 객체들만 다시 지오코딩을 실시해 개선했다. 그러나 "서울특별시 동대문구 보문로 6"는 수차례의 지오코딩에도 불구하고 에러가 발생하여 기존 방법이 아닌 Kakao Api를 이용한 지오코딩 툴로 위경도를 변환하고 데이터를 갱신했다. 두 번째는 소요 시간이었다. 1000개 미만의 객체를 지오코딩 하는데 10분 정도의 시간이 소요되었기 때문에 메리트가 떨어진다고 생각했다. 이를 개선하기 위한 목적으로 2번 프로그램을 개발했고 자세한 설명은 2번에서 서술했다.<br>


## 1-2. Python의 folium, matplotlib, seaborn 라이브러리를 이용한 데이터 분석과 표현<br>

공간분석에서 GIS가 용이한 이유는 중첩분석(Map 0verlay)인데, 이것을 python 내의 folium 라이브러리를 이용하여 표현했고 Json 파일을 이용해 배경지도를 설정했다. 이때 Github에서 request의 get 메소드를 사용하여 json 데이터를 얻는 과정을 알게 되었고 이를 적용해 직접 서울시의 json파일을 습득할 수 있었다. folium으로 가장 기본적인 map부터 단계구분도까지 만들어보며 더 나아가 지도에 icon, popup, tooltip의 요소를 추가해 풍성한 지도가 될 수 있도록 했다. 특히 popup에서는 url을 연결하는 html을 작성했다.<br>

## 2. Kakao api를 이용한 Geocoding Tool (2023/12/24) <br>

1번 프로그램 Geopy 지오코딩 툴은 처리 속도가 느리다는 단점이 있다. 이것을 해결하기 위해 Python 라이브러리가 아니라 Kakao Api를 통해 지오코딩 할 수 있는 프로그램을 개발하게 되었다. Kakao Developers에서 개인 REST API 키를 발급받아 지오코딩 함수를 작성했고 이 프로그램을 사용하고 싶다면 직접 개인 키를 삽입하면 된다. 그러나 이 프로그램은 Python의 라이브러리를 이용한 것이 아니기 때문에 일일 변환 개수 제한이 존재한다는 한계점을 가지고 있다. 따라서 자신이 가지고 있는 데이터의 특성에 맞게 1번과 2번 프로그램을 병행하여 사용하기를 기대한다.

## 3. Kakap api Geocoding Tool을 웹에서 이용가능한 애플리케이션 개발 (2024/01/09) <br>

웹/파이선프로그래밍 수업에서 접했던 python 웹 프레임워크 flask를 이용해 지오코딩 툴을 웹에서 이용할 수 있는 애플리케이션으로 개발했다. route() 데코레이터 이용하여 templates 속의 html을 랜더링하여 웹 페이지를 URL과 라우팅했다. Get, Post 요청을 통해 클라이언트가 주소를 입력하고 위도와 경도를 서버로부터 받을 수 있는 애플리케이션이다.<br>

애플리케이션은 프로그램에 대한 간략한 설명, 관리자 contact 정보, Kakao map 연결 링크, Geocoding Tool로 구성되어 있다. 관리자 contact 정보는 mailto를 이용해 메일 주소를 클릭하면 곧바로 구글 메일 작성 페이지로 연결되도록 했다. 그리고 사용자가 입력할 주소를 검색할 수 있도록 Kakao map 연결 링크를 설정했다. Geocoding Tool은 사용자가 주소를 입력하고 'Geocoding it!' 버튼을 누르면 위도와 경도를 반환한다. 만약 사용자가 아무런 주소값을 입력하지 않았을 때는 'hey you didn't type anything!' 문구를 반환할 수 있도록 했다. 또한 대한민국이 아니거나 올바른 주소 양식이 아니면 'Plz check the address'라는 문구를 반환하도록 설정했다. <br>

웹 프레임워크를 처음 사용하다 보니 간단한 웹사이트를 구현하는데도 많은 시간이 걸렸다. flask 문법을 처음 접해보기도 했고, html 내에서 변수명과 조건문 등이 python 문법과 다소 상이했다. 또한 가장 중요한 점은 templates 폴더명은 고유해야 하며, 이 폴더의 디렉토리가 flask로 만든 py파일의 디렉토리와 같아야 한다는 점이었다. 그럼에도 불구하고 flask 애플리케이션을 개발하며 느꼈던 점은 flask는 python으로 웹 구현이 가능한 마이크로 웹 프레임워크라는 것이다. python 언어를 기반으로 아주 단순한 정적 웹부터 복잡한 동적 웹까지 개발할 수 있고, python의 다양한 라이브러리를 활용하여 웹 개발을 더욱 확장할 수 있는 것이 최대의 장점이라고 느꼈다.  
