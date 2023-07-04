import json

with open('Python/7.4(클래스and라이브러리)/라이브러리/password.json', 'r') as f:
    # json 파일은 json.load 로 열어야 한다!
    json_data = json.load(f)
json_data['delivery'] = '만두'

with open('Python/7.4(클래스and라이브러리)/라이브러리/password.json', 'w') as f:
    # dump -> 내보낸다. json.dump()를 통해 내보낼 수 있다 (dict로 변환시킴)
    json.dump(json_data, f, ensure_ascii=False)
