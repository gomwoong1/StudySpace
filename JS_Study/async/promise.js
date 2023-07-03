//promise는 비동기적인 콜백함수에서 쓰이는 자바 스크립트 내부에 내장된 오브젝트
//state: pending(진핸중) -> fulfilled(완료) or rejected(문제 발생)

//producer vs consumer

//1. producer
//Promise(excutor(resolve, reject))
//resolve: 기능 정상적으로 수행해서 데이터 최종적으로 수행하는 callback 함수 
//reject: 기능 수행하다 문제 생기면 호출할 callback 함수

//새로운 promise가 만들어지면 전달한 excutor가 자동으로 실행됨
const promise = new Promise((resolve, reject) => {
    //promise는 네트워크 작업이나 파일 입출력 등 무거운 작업을 함.
    //이러한 무거운 작업을 동기적으로 처리하면 시간복잡도 손해
    console.log('doing something'); 
    setTimeout(() => {
        //resolve('jw');
        reject(new Error('no network'));
    }, 2000);
})

//2. Consumers: than, catch, finally
promise.then(value => {
    console.log(value);
})
.catch(error => {
    console.log(error);
})
.finally(() => {console.log('finally');
});

//3. promise chaining
const fetchNumber = new Promise((resolve, reject) => {
    setTimeout(() => resolve(1), 1000);
});

fetchNumber
.then(num => num * 2)
.then(num => num * 3)
.then(num => {
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve(num - 1), 1000);
    });
})
.then(num => console.log(num));

//4. Error Handling
const getHen = () =>
    new Promise((resolve, reject) => {
        setTimeout(() => resolve('chicken'), 1000);
    });
const getEgg = hen =>
    new Promise((resolve, reject) => {
        setTimeout(() => reject(new Error(`error ${hen} => egg`)),1000);
    });
const cook = egg =>
    new Promise((resolve, reject) => {
        setTimeout(() => resolve(`${egg} => 'fri`), 1000);
    });

console.clear();
getHen()
.then(hen => getEgg(hen))
.catch(error => {
    return 'bread';
})
.then(egg => cook(egg))
.then(meal => console.log(meal));

