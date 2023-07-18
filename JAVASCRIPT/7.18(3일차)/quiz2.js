// 주어진 숫자에서 10을 만들기 위해 얼마를 더해야 하는지 계산한 후, 
// 프로미스를 사용하여 결과를 반환하는 함수 makeTenWithPromise를 작성하세요.

function makeTenWithPromise(number) {
    return new Promise((resolve, reject) => {
    // number가 숫자라면
    if (typeof number === 'number') {
        const result = 10 - number;
        resolve(result);
// number가 숫자가 아니라면
    } else {
        const error = new Error('유효하지 않은 숫자입니다.');
        reject(error);
    }
    });
}

makeTenWithPromise(2)
// resolve 부분
.then(function(res){
    console.log(res + '만큼 더 해야 합니다.');
})
// reject 부분
.catch(function(e){
    console.log(e);
});
