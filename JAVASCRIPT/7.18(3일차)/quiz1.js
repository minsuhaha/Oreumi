// callback 형태로

function squareWithCallback(number, callback) {
    if (isNaN(number)) {
        // 에러 객체 생성
        const error = new Error('유효하지 않은 숫자입니다!');
        callback(error, undefined);
    } else {
        const result = number**2;
        callback(null, result);
    }
}

function callbackFunction(error, result) {
    if (error != null) {
        console.log(error);
    } else {
        console.log(result);
    }
}

squareWithCallback(4, callbackFunction);
squareWithCallback('hello', callbackFunction); 