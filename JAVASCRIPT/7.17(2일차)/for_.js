// for in == python 에서 range  -> index

// const fruits = ['사과', '바나나', '수박'];

// for (const fruit in fruits) {
//     console.log(fruit, typeof fruit, fruits[fruit])
// };


// for of == python에서 in -> value
// const fruits = ['사과', '바나나', '수박'];

// for (const fruit of fruits) {
//     console.log(fruit, typeof fruit, fruits[fruit])
// };


// forEach   -> break를 사용할수없다..
// const fruits = ["사과", "바나나", "수박"];

// fruits.forEach((fruit, index) => {
//     console.log(fruit, typeof fruit, index)
// });


// 고차함수
// map
// const numbers = [1, 2, 3, 4, 5];

// const square = numbers.map((number) => {
//     return number ** 2;
// })

// console.log(square);

// reduce
// const numbers = [1, 2, 3, 4, 5];

// const sum = numbers.reduce((accumulator, number) => { 
//     return accumulator + number;
// }, 0); // 0은 accumulator의 초기값

// console.log(sum);

// filter
const numbers = [1, 2, 4, 5, 10];

const even = numbers.filter((number) => {
    return number % 2 == 0;
});

console.log(even);


var multiply = (a, b) => {
    return a * b;
};