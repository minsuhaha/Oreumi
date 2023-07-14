// for 문
// for (초기값; 종료값; 증감식)
// for (let i=0; i<5; i++) {
//     console.log(i)
// }

// // i 초기화
// let i = 0
// while (i<5) {
//     console.log(i);
//     i++;
// }

// 조건문
let x = 1;
if (x>0) {
    console.log('x는 양수입니다.');
} else if (x<0) {
    console.log('x는 음수입니다.');
} else {
    console.log("x는 0입니다");
};


let color = 'black';
switch (color) {
    case 'red':
        console.log('빨간색입니다.');
        break;
    case 'blue':
        console.log('파란색입니다.');
        break;
    case 'black':
        console.log('검은색입니다.');
        break;
    default:
        console.log("리스트에 없습니다.");
        break;
}



// animal = "cat"
// if animal == "dog":
//     print("Bark")
// elif animal == "cat":
//     print("Meow")
// elif animal == "bird":
//     print("Tweet")
// else:
//     print("Unknown animal")

let animal = "cat";

// if
if (animal === 'cat') {
    console.log('Meow')
} else if (animal === 'dog') {
    console.log('Bark');
} else if (animal === 'bird') {
    console.log('Tweet') 
} else {
    console.log("Unknown animal");
}

// switch
switch (animal) {
    case 'dog':
        console.log('Bark');
        break;
    case 'cat':
        console.log('Meow.');
        break;
    case 'bird':
        console.log('Tweet');
        break;
    default:
        console.log("Unknown animal");
        break;
}