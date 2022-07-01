// string 연산
console.log('java' + 'script'); //문자열과 문자열끼리 연산 가능.
console.log('1' + 2);
console.log(`string literals: 1 + 2 = ${1 + 2}`);

//+, -, /, *, %, ** 연산
console.log(1+1);
console.log(1-1);
console.log(1/1);
console.log(1*1);
console.log(5%2);
console.log(2**3);

//증감연산자
let count = 1;
console.log(count); 

const count2 = ++count;
console.log(count2);

const count3 = count++;
console.log(count3);

//복합연산자
let x = 3;
let y = 6;
x += y;
console.log(x);
x -= y;
console.log(x);
x *= y;
console.log(x);
x /= y;
console.log(x);

//비교연산자
console.log(3 > 6);
console.log(6 <= 6);

//논리연산자
// ||(or), &&(and), !(not)

const value1 = false;
const value2 = 4 < 2;

console.log(`or: ${value1 || value2 || check()}`);

function check(){
    return true;
}

const value3 = true;
const value4 = 4 > 2;

console.log(`and: ${value1 && value4 && check()}`);
console.log(`and: ${value3 && value4 && check()}`);

console.log(!value1);

const stringFive = '5';
const numberFive = 5;

// '==' 타입 신경쓰지 않고 비교, '==='는 타입까지 신경써서 비교
console.log(stringFive == numberFive);
console.log(stringFive != numberFive);
console.log(stringFive === numberFive);
console.log(stringFive !== numberFive);

const jw = {name: 'jw'};
const jw2 = {name: 'jw'};
const jw3 = jw;

console.log(jw == jw2); //레퍼런스가 다르기 때문에 false
console.log(jw === jw2);
console.log(jw == jw3); //레퍼런스가 같기 때문에 모두 true
console.log(jw === jw3);

console.log(0 == false);
console.log(0 === false);
console.log('' == false);
console.log('' === false);
console.log(null == undefined); //같은 것으로 취급
console.log(null === undefined);

//if, else if. else

const name3 = 'coder';
if (name3 === 'jw'){
    console.log('Welcome, JW');
} else if(name3 === 'coder'){
    console.log('Welcome, coder');
} else {
    console.log('Welcome');
}

//조건연산자
console.log(5 > 3 ? 'true' :  'false');

//switch문
const browser = 'Chrome';

switch(browser){
    case 'IE':
        console.log("IE");
        break;

    case 'Chrome':
    case 'Firefox':
        console.log("other");
        break;
    default :
        console.log("default");
        break;
}

//while
let i = true;
while(i){
    console.log("1");
}