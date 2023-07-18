console.log('안녕하세요!');

// 해당하는 시간만큼 딜레이가 생김     1000 -> 1초
setTimeout(() => {
    console.log('타임아웃1!');
}, 5000);

setTimeout(() => {
    console.log('타임아웃2!');
}, 3000);

console.log('반갑습니다!');