'''
- GET 방식으로 데이터 전송하기
    - 클라이언트
        - 링크 (화면 전환)
            <a href="http://127.0.0.1:5000/link?name=hello&age=100">링크</a>
        - form 전송 (화면 깜빡임 -> 화면 전환)
            <form action="http://127.0.0.1:5000/link" method="get">
                <input name="name" value="hello"/>
                <input name="age" value="100"/>
                <input type="submit" value="전송"/>
            </form>
        - ajax (jQuery로 표현, 화면 유지)
            $.get({
                url: "http://127.0.0.1:5000/link",
                data: "name=hello&age=100",
                success: (res)=>{},
                error: (res)=>{}
            })
    
    - 서버
        - get 방식 데이터 추출
            name = request.args.get('name')
            age = request.args.get('age')

- /link 로 요청하는 방식은 다양할 수 있다. 단, 사이트 설계 상 1가지로만 정의되어 있다면
    다른 방식의 접근은 모두 비정상적인 접근이다(웹크롤링, 스크래핑, 해킹 등이 대상)
    이런 접근을 필터링할 것인지가 보안의 기본사항
'''

from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/link')
def link():
    # name = request.args['name'] -> 데이터 누락시 서버가 셧다운됨. 사용X
    # name = request.args.get('name') -> 데이터 누락시 None이 나와서 예외처리 가능 
    name = request.args.get('name')
    age = request.args.get('age')
    return "name: [ %s ], age: [ %s ]" % (name, age)

@app.route('/test')
def test():
    # 엔트리 포인트(진입로, 프로그램 시작점)와 같은 경로에 templates/test.html
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)