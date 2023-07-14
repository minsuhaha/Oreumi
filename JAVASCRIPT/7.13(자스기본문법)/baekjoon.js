// // 분해합
// const fs = require('fs');
// // map(Number) 함수를 통해 입력값 number 데이터로 바꿔주기
// const N = fs.readFileSync('/dev/stdin').map(Number);

// let M = 0
// // 0부터 숫자 N까지 돌기
// for (let i=0; i<N; i++){

//     // 분해합 총합을 담을 sum 배열 초기화
//     let sum = 0;
    
//     // 해당 i 숫자 -> 문자열로 변환 (각 자리수의 합을 구해주기 위해)
//     const stringValue = i.toString()
    
//     // stringValue의 자리수의 합을 구해주기 위해 해당 stringValue의 인덱스만큼 for문 돌기
//     for (let j=0; j<stringValue.length; j++){
        
//         // 문자형이니깐 sum에 합해주기 위해 자릿수 하나씩 정수형으로 변환해서 합해주기 (parseInt 이용)
//         sum += parseInt(stringValue[j])
//     }

//     // 각 자릿수의 합 sum과 해당 숫자 i를 합해줌
//     sum += i;

//     // 최종 sum과 N이 같을 경우 -> i는 0부터 돌기 때문에 처음으로 같을 경우의 i가 문제에서 원하는 최소 N의 생성자임
//     if (sum == N){
//         M = i
//         break;
//     }
// }
// console.log(M)


// // 블랙잭 백준문제

// const fs = require('fs');
// // 줄바꿈을 기준으로 input에 입력받기 (string으로 먼저)
// const input = fs.readFileSync('example.txt').toString().split('\n')

// // 입력받은 input에서 첫번째 string을 띄어쓰기를 기준으로 배열로 나누기
// const firstLine = input[0].split(' ')
// // 두번째 input에서 띄어쓰기를 기준으로 나눠주고 각각 parseInt를 사용하여 number로 형 변환
// const cardArr = input[1].split(' ').map(i => parseInt(i))
 
// // N, M에 parseInt 형변환해서 각각 담아주기
// const N = parseInt(firstLine[0])
// const M = parseInt(firstLine[1])


// // max 값을 담을 공간 초기화
// let max = 0;

// // i 는 cardArr의 맨 처음부터 (맨 마지막 -2) 만큼만 움직이도록
// for (let i = 0; i< cardArr.length - 2; i++) {
// // j 는 i+1 부터 cardArr의 (맨 마지막으로 -1) 만큼만 움직이도록
//     for (let j = i+1; j <cardArr.length-1; j++) {
// // k 는 j+1 부터 cardArr의 맨 마지막까지 움직이도록
// // 완탐을 하기 위해 -> 서로 겹치필요가 없다
//         for (let k = j+1; k < cardArr.length; k ++) {
//             // total 변수에 경우의 수들 다 담아주기
//             let total = cardArr[i] + cardArr[j] + cardArr[k]
//             // total 이 현재 max보다 크고 total이 M보다는 작거나 같다면 -> max = 현재 total 으로 바꿔주고 계속 반복
//             if (total > max && total <= M) {
//                 max = total
//             }
//         }
//     }
// }

// console.log(max)

const end = 100;
let sum = 0;
for (let i=1; i<=end; i++){
   if (end % 2 === 0){
       sum += i;
   }
}
console.log(`전체 합은 ${sum}입니다.`)



// const -> let 으로
// " " -> ` ` 으로 
// i<end -> i<=end