// 자바스크립트에서는 == 는 데이터형태와 달라도 값만 같으면 true, === 데이터형태와 값이 모두 같아야 true
if (false == []) {
    console.log('true')
} else {
    console.log('false')
}

// 리스트가 비어있을 때 false
if (false == [[]]) {
    console.log('true')
} else {
    console.log('false')
}

// 숫자에서 -> 문자형으로
let a = '4' + 1
console.log(a)

// 문자형에서 -> 숫자형으로
let a = '4' - 1 
console.log(a)

// const examples = [
//     [0, ''],
//     [false, 'false'],
//     [null, undefined],
//     [NaN, NaN],
//     [0, false],
//     [0, '\n'],
//     ['', '0'],
//     ['false', false],
//     [[], false],
//     [[], ''],
//     [[], 0],
//     [[0], false],
//     [[null], false],
//     [[undefined], false],
//     [{}, false],
//     [true, 1],
//     [true, '1'],
//     [true, [1]],
//     [true, { value: 1 }],
//     ['1', [1]],
//     [undefined, null],
//     [Infinity, Infinity],
//     [() => {}, () => {}],
// ];

// examples.forEach(([a, b]) => {
//     console.log(`${a} == ${b} : ${a==b}`);
//     console.log(`${a} == ${b} : ${a===b}`);
// });