//함수 정의하기
//이렇게 정의한 함수는 자바 스트립트 엔진에 의해 자동으로 hoisting됨
function printHello(){
    console.log('hello');
}

printHello();


function log(message){
    console.log(message);
}

log('hello@@');
log(13); //숫자는 문자열로 변환됨.

//오브젝트가 매개변수로 넘어가면 레퍼런스값이 넘어감
//보통의 자료형이 넘어간다면 기존과 같이 값이 넘어감.
function changeName(obj){
    obj.name = 'coder';
}

const jw = {name: 'jw', age: 23};
console.log(jw.name);

changeName(jw);
console.log(jw.name);

//매개변수 여러 개 지정하기
//매개변수 기본값 지정하기
function showMessage(message, from = 'unknown'){
    console.log(`${message} by ${from}`)
}

showMessage('Hi');
showMessage('Hi', 'JW');

//매개변수를 배열로 받기
function printAll(...args){
    for(let i = 0; i < args.length; i++){
        console.log(args[i]);
    }

    for(const i of args) {
        console.log(i);
    }
}
printAll('coder', 'JW', 'inha');

//리턴값 지정하기
function sum(a, b){
    return a+b;
}

const result = sum(1,2);
console.log(result);
console.log(sum(3,4));

//function expression
//선언된 이후에 호출할 수 있음.
//정의된 함수와는 다르게 hoisting이 안됨.
const print = function (){ //익명 함수
    console.log('print');
};
print();

const printAgain = print;
printAgain();

const sumAgain = sum;
console.log(sumAgain(1, 3));

//콜백 함수
function randomQuiz(answer, printYes, printNo){
    if(answer === 'love'){
        printYes();
    }
    else{
        printNo();
    }
}

//익명 함수
const printYes = function (){
    console.log('yes');
}

//네임드 함수
//디버깅 할 때 이름이 찍히도록 할 때 쓰임
//아니면 자기 자신 호출해서 재귀함수처럼 쓰일 때
const printNo = function pt(){
    console.log('no');
}

randomQuiz('hi', printYes, printNo);
randomQuiz('love', printYes, printNo);

//arrow function
const simplePrint = () => console.log('simplePrint');

// function simplePrint() {
//     console.log('simplePrint');
//}

const add2 = (a, b) => a+b;

// function add2(a, b) {
//     return a + b;
//}

//IIFE
(function hello(){
    console.log('hello')
})();