// common js 방식으로 모듈 불러오기
const months = require('./calender.js');

function hello(){
    console.log('안녕하세요!');
}

hello();
console.log(months[0] + '달 입니다');