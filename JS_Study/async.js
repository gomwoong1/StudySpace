//async 사용
//async 키워드 사용하면 블록 내부 코드를 Promise로 변환함.
async function fetchUser() {
    return 'jw';
}

const user = fetchUser();
user.then(console.log)
console.log(user);

//await
//async 키워드 붙은 함수에서만 사용할 수 있음.

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function getApple() {
    await delay(1000);
    return 'apple';
}

async function getBanana(){
    await delay(1000);
    return 'banana';
}

async function pickFruits(){
    const apple = await getApple();
    const banana = await getBanana();
    return `${apple} + ${banana}`;
}

