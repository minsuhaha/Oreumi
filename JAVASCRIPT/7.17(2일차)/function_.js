// 1. 함수 선언 -> 호이스팅 가능
function add (a, b) {
    return a + b;
}

let addNumbers = add(3, 5);
console.log(addNumbers);


// 2. 함수 표현식 (변수 선언 과 동시에 함수 만들어서 변수에 담아주기)
const subtract = function(a, b) {
    return a - b;
}

// 3. 화살표 함수
let subtract2 = (a, b) => {
    return a - b;
};
console.log(subtract2(3, 5));
