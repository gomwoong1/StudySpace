//배열 생성
//1. 
const arr1 = new Array();

//2.
const arr2 = [1, 2];

//인덱스 접근
const fruits = ['apple', 'banana'];
console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[fruits.length - 1]);

for(value of fruits){
    console.log(value);
}

for(value in fruits){
    console.log(fruits[value]);
}

for(let i = 0; i < fruits.length; i++){
    console.log(fruits[i]);
}

fruits.forEach((fruits) => console.log(fruits))

// fruits.forEach(function(fruits){
//     console.log(fruits);
// })

//요소 추가(push), 삭제(pop), 복사
fruits.push('lemon','apple');
console.log(fruits);

fruits.pop();
fruits.pop();

//unshift, shift
fruits.unshift('lemon','apple'); //앞에서부터 추가
console.log(fruits);

fruits.shift();
fruits.shift();
console.log(fruits); //앞에서부터 삭제
//unshift와 shift는 push, pop보다 느림
//앞에서부터 추가, 삭제하려면 뒤의 전체 데이터를 당겨오거나 밀어내야 하기 때문

//splice, 중간에서 삭제, 추가
fruits.push('apple', 'lemon', 'melon');
console.log(fruits);
fruits.splice(1, 1, 'grapes', 'watermelon'); //splice(시작 인덱스, 삭제할 개수, 추가할 요소)
console.log(fruits);

//concat, 다른 배열 붙이기
const fruits2 = ['banana', 'melon'];
const newArr = fruits.concat(fruits2);
console.log(newArr);

newArr.forEach((newArr) => console.log(newArr));

//array.indexOf, 검색
//값이 있다면 인덱스 값 리턴, 없으면 -1 리턴
console.clear();
console.log(fruits.indexOf('apple'));
console.log(fruits.indexOf('banana'));
console.log(fruits.indexOf('lemon'));

//includes, 있다면 true, 없다면 false
console.log(fruits.includes('banana'));
console.log(fruits.includes('apple'));

//같은 요소가 있다면 그 중 가장 마지막 인덱스 리턴, lastIndexOf
console.log(fruits.lastIndexOf('apple'));