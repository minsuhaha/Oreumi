function wakeUp() {
    return console.log('아침에 일어나서 강의듣기!');
}

function eatLunch(){
    return new Promise((resolve, reject) => 
        setTimeout(() => {
            const data = "점심시간에 점심먹기!";
            resolve(data);
    }, 3000));
}

function endClass(){
    return console.log('강의가 끝났다!');
}

async function startDay(){
    wakeUp();
    const data = await eatLunch(); // await -> promise가 끝날때까지 기다려줌
    console.log(data);
    endClass();
};

startDay();