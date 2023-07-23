// 자바스크립트 파일 시스템 불러오기
const fs = require('fs');

fs.readFile('file.txt', 'utf8', (err, data) => {
    if (err){
        console.error(err);
        return;
    }
    console.log("File Content: ", data);
});