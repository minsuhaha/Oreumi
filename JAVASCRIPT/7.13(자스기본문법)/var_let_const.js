function example() {
    let x = 10;
    // let x = 20; -> 중복 선언은 안된다.
    console.log(x)
    if (true) {
        // let x = 20;  // 블록 스코프
        let x = 20;
        console.log(x);
    }
    console.log(x);
}
example();

// let -> 블록 스코프, 먼저 선언되고 출력해야됨
// var -> 함수 스코프(전역 스코프), 호이스팅(변수가 뒤에 나와도 선언은 되어짐)
