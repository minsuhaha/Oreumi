// 1. div 요소를 선택하고 변수 container 에 할당하세요
const container = document.querySelector('#container');

// 2. Hello, world에 클래스('boldText')를 추가하세요
const helloText = container.getElementsByTagName('a')[0];
helloText.classList.add('boldText');

// 3. forEach 메서드를 이용해 Item 1, 2, 3의 텍스트 컬러를 파랑색으로 바꾸세요
const items = container.querySelectorAll('ul li');

items.forEach((item) => {
    item.style.color = 'blue';
});

// 4. 버튼1, 2만 클릭시에 알림창이 뜨도록 바꾸세요

let AlertBtn = container.querySelectorAll('.alert');

AlertBtn.forEach((btn) => {
    btn.onclick = function() {
        alert('알림창이 뜹니다!');
    }
});

// 5. 'This is another paragraph.'를 '이것은 문장입니다'로 바꾸세요

const changeParagraph = container.querySelectorAll('.description')[1];
changeParagraph.textContent = '이것은 문장입니다.';

// 6. div 내에 <h2>Bye, world!</h2>를 추가하세요
const newH2 = document.createElement('h2');
newH2.textContent = 'Bye world!';
container.appendChild(newH2);

// 7. Item 2 요소를 제거하세요
// 두번째 items 선택합니다.
const item2 = items[1];
// 두번째 items를 삭제합니다.
item2.parentNode.removeChild(item2);
