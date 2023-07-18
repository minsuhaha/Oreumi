function wakeUp() {
    console.log('아침에 일어나서 강의듣기!');
}

function eatLunch_promise(){
    return new Promise(function(resolve) {
        setTimeout(() => {
            console.log('점심시간에 점심먹기!');
            resolve();
        }, 3000);
    });
}

function endClass(){
    console.log('강의가 끝났다!');
}

wakeUp();
// 비동기식으로 변환 -> then 함수사용 then 해당하는 부분이 resolve로 들어감
eatLunch_promise().then(function(){
    endClass();
});