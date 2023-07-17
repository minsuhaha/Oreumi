// function Person(name, age){
//     this.name = name;
//     this.age = age;

//     this.sayHello = function(){
//         console.log(`안녕하세요! 제 이름은 ${name}, 그리고 나이는 ${age}입니다.`);
//     };
// }

// const human = new Person('김도언', 20);
// human.sayHello();


// class 만들기

// class Person{
//     // 생성자 부분 -> constructor
//     constructor(name, age){
//         this.name = name;
//         this.age = age;
//     } 

//     sayHello() {
//         console.log(`안녕하세요! 제 이름은 ${this.name}, 그리고 나이는 ${this.age}입니다.`);
//     };
// }

// const human = new Person('김도언', 20);

// human.sayHello();

let rectangle = class {
    constructor(height, width) {
        this.height = height
        this.width = width
    }
    calcArea(){
        return this.height * this.width;
    }
};


const square = new rectangle(10, 20);
console.log(square.calcArea());

// 자바스크립트는 camel 케이스 -> 모양이 낙타를 닮았다해서 camelCaseList
// 파이썬 스네이크 케이스 -> 단어 아이에 뱀이 있다고 해서 snake_case_list