## 1. Python의 Pandas, Geopy 라이브러리 를 이용한 Geocoding Tool 프로그램 <br>

GIS를 통해 공간분석을 진행할 때, 객체의 공간정보를 파악하는 것은 매우 중요하다. 이는 보통 객체의 위경도 좌표를 사용해 GIS 상에 '투영'하기 때문이다. 공간분석 시 주로 오픈소스의 데이터 위주로 진행되는데, '정부 공공데이터 포털'이나 '서울시 열린 데이터 광장'에 게시된 데이터를 이용한다. 그러나 많은 데이터 표본을 살펴보면 도로명 주소만 있거나, 위경도 좌표만 있는 사례가 빈번하다. 이러한 데이터는 GIS상에 온전히 담아낼 수 없기 때문에 공간정보로서의 가치가 떨어진다.<br>

이때 사용할 수 있는 방법론이 지오코딩이다. 지오코딩은 객체의 도로명주소(또는 구 주소)를 위경도 좌표로 변환해주는 것을 뜻한다. 온라인에서 제공하는 상용 지오코딩 툴은 biz-gis, Geocoder-Xr 등이 있다. 그러나 이러한 서비스들은 개별 IP당 일일 변환개수 제한(1일 10000건)이 있어 지오코딩 과정에서 데이터의 용량이 크거나(10000건 초과), 수정사항으로 번복할 때(여러 번 수행) 제한사항이 존재한다.<br>

이때 지오코딩을 Python으로 구현하면 일일 변환 제한 없이, 데이터를 무제한으로 변환할 수 있기 때문에 공간분석에서 유용하게 활용할 수 있다. Python은 오픈 소스로 다양한 라이브러리가 제공되고 있어서 다루는 영역이 날로 커지고 있다. 지오코딩도 예외는 아니며, Geopy라는 라이브러리를 이용해 지오코딩을 구현할 수 있다. 또한 위,경도를 주소를 변환하는 과정을 역지오코딩이라고 하는데, 역지오코딩 또한 Geopy를 이용해 구현 가능하다. 이 프로그램은 지오코딩, 역지오코딩에 대한 코드를 제공하며 단일 데이터 뿐만 아니라 대용량 데이터를 대상으로 전처리를 진행할 수 있는 툴로 개발하였다. 사용하고자 하는 데이터를 pandas로 읽고 코드를 따라 실행하면 지오코딩 또는 역지오코딩이 적용된 데이터가 생성된다.(확장자는 csv) 마지막으로 지오코딩과 역지오코딩 함수를 적용한 새로운 Class를 만들어보며 Python의 객체 지향 특성과 상속 유전을 활용해 보았다.  <br>

해당 프로그램을 개발할 때, 여러 난관이 있었다. 첫 번째는 Geopy 라이브러리의 정확성이었다. 지오코딩을 실행했을 때, 에러가 발생하는 객체가 존재했다. 이를 방지하기 위해 지오코딩 함수에 try, except문법을 적용했다. 에러가 난 객체의 인덱스를 저장하고, 그 인덱스의 객체들만 다시 지오코딩을 돌려서 보완하는 식으로 개선했다. 그러나 "서울특별시 동대문구 보문로 6"는 수차례의 지오코딩에도 불구하고 에러가 발생하여 기존 방법이 아닌 Kakao Api를 이용한 지오코딩 툴로 위경도를 변환하고 데이터를 갱신했다. 두 번째는 소요 시간이었다. 1000개 미만의 객체를 지오코딩 하는데 10분 정도의 시간이 소요되었기 때문에 상당히 메리트가 떨어진다고 생각했다. 이를 개선하기 위한 목적으로 2번 프로그램을 개발했고 자세한 설명은 2번에서 서술했다.<br>


## 1-2. Python의 folium, matplotlib, seaborn 라이브러리를 이용한 데이터 분석과 표현<br>

공간분석에서 GIS가 용이한 이유는 중첩분석(Map 0verlay)인데, 이것을 python 내의 folium 라이브러리를 이용하여 표현했고 Json 파일을 이용해 배경지도를 설정했다. 이때 Github에서 request의 get 메소드를 사용하여 json 데이터를 얻는 과정을 알게 되었고 이를 적용해 직접 서울시의 json파일을 습득할 수 있었다. folium으로 가장 기본적인 map부터 만들어보며 더 나아가 icon, popup, tooltip의 요소를 추가해 풍성한 지도가 될 수 있도록 했다. 특히 popup에서는 웹/파이선프로그래밍 수업에서 배운 url을 연결하는 html을 작성했다.<br>

## 2. Kakao api를 이용한 Geocoding Tool (2023/12/24) <br>

1번 프로그램 Geopy 지오코딩 툴은 처리 속도가 느리다는 단점이 있다. 이것을 해결하기 위해 Python 라이브러리가 아니라 Kakao Api를 통해 지오코딩 할 수 있는 프로그램을 개발하게 되었다. Kakao Developers에서 개인 REST API 키를 발급받아 지오코딩 함수를 작성했다. 그러나 이 프로그램은 Python의 라이브러리를 이용한 것이 아니기 때문에 일일 변환 개수 제한이 존재한다는 한계점을 가지고 있다. 따라서 자신이 가지고 있는 데이터의 특성에 맞게 1번과 2번 프로그램을 병행하여 사용하기를 기대한다.

## 3. Kakap api를 python flask를 이용해 웹에서 구현한 것(2024/01/09) <br>

1번, 2번 프로그램을 직접 
