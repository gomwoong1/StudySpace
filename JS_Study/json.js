//오브젝트를 JSON으로 변환하기
let json = JSON.stringify(true);
console.log(json);

json = JSON.stringify(['apple', 'banana']);
console.log(json);

const rabbit = {
    name: 'tori',
    color: 'white',
    size: null,
    birthDate: new Date(),
    jump: () => console.log(`${this.name} can jump`),
};

json = JSON.stringify(rabbit);
console.log(json);

json = JSON.stringify(rabbit, ['name', 'color']);
console.log(json);

//JSON을 오브젝트로 변환하기

console.clear();
json = JSON.stringify(rabbit);
const obj = JSON.parse(json, (key, value) => {
    console.log(`key: ${key}, value: ${value}`);
    return key === 'birthDate'? new Date(value) : value;
});
console.log(obj);

//obj.jump();
//object >> json 변환 시, 데이터만 변환하고 함수는 포함하지 않았기 때문에 함수가 날아감

console.log(rabbit.birthDate.getDate());
console.log(obj.birthDate.getDate());
//콜백함수로 데이터 값 다시 변환시켜서 재사용 가능함.