//오브젝트 만드는법

//1. object literal
const jw = {name: 'jw', age: 23};

function print2(person) {
    console.log(person.name);
    console.log(person.age);
}

print2(jw);

jw.job = 'student'; //뒤늦게 추가 가능함.
console.log(jw.job);

delete jw.job;
console.log(jw.job); //뒤늦게 삭제도 가능함.

//2. 클래스
class person {
    constructor(name, age){
        this.name = name;
        this.age = age;
    }

    print(){
        console.log(this.name);
        console.log(this.age);
    }
}

const person1 = new person('jw', 23);
person1.print();

//computed properties
//object['key']의 형식, 단 key는 무조건 string
console.log(person1.name); //'.'을 이용해 접근 가능하지만
console.log(person1['name']); //이렇게도 접근 가능함.

person1['name'] = 'jw2'
console.log(person1.name);

//사용 예
//runtime(동작)일 때 값을 받아오기 때문에 당장 코딩할 때 값을 알 수 없을 경우 사용함.
function printValue(obj, key){
    //console.log(obj.key); //이렇게 하면 undefined
    console.log(obj[key]);
}

printValue(person1, 'name');

//shorthand
//key와 value의 이름이 동일하면 생략할 수 있는 기능
const user1 = {name: 'bob', age: 2};
const user2 = {name: 'steve', age: 3};
const user3 = {name: 'dave', age: 4};

function MakePerson(name, age){
    return{
        name,
        age
    };
}

const user4 = MakePerson('jw', 23);
console.log(user4);

//constructor function
//자바스크립트 엔진이 알아서 오브젝트 생성해줌
//새 오브젝트 만들고 리턴해주는 것을 생략했을 뿐임
function Newperson(name, age){
    this.name = name;
    this.age = age;
}
const user5 = new Newperson('jw3', 23);

//in operator
//해당 키가 오브젝트 내에 있는지를 확인
console.log('name' in jw);
console.log('name' in person);

//for ...in, for... of
//for (key in obj)
console.clear(); //콘솔창 지우기
for (key in person1) {
    console.log(key);
}

for (key in jw) {
    console.log(key);
}

//for of
const array = [1, 2, 3, 4, 5];
for (value of array){
    console.log(value);
}

//cloning
const man = {name: 'jw', age: 23};
const man2 = man;
man2.name = 'coder';
console.log(man);

//1. for문 사용
const man3 = {};
for (key in man){
    man3[key] = man[key];
}
console.log(man3);

//2. object.assign()
const man4 = {};
Object.assign(man4, man); //타겟, 복사할 대상
console.log(man4);
//복사 대상이 여러 개이고, 같은 properties가 있다면 뒤에 파라미터가 계속 덮어씌워짐