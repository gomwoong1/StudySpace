{
    //배열 요소를 하나의 string으로 묶기
    //array.join('구분자');
    const fruits = ['apple', 'banana', 'orange'];
    const str = fruits.join();
    console.log(str);
}

{
    //string을 배열로 만들기
    //string.split('구분자', 개수)
    const fruits = 'apple,banana,orange';
    const array = fruits.split(',', 2);
    console.log(array);
}

{
    //배열 순서 거꾸로 뒤집기
    //array.reverse()
    //순간의 결과값만 뒤집는게 아니라 array 원본 자체를 뒤집기 때문에 이점 유의
    const array = [1, 2, 3, 4, 5];
    array.reverse();
    console.log(array);
}

{
    //1,2 번째 요소를 제거하고 나머지 요소를 이용해 새로운 배열 만들기
    //array.slice(시작 인덱스, 마지막 인덱스)
    //마지막 요소의 인덱스를 배제하기 때문에 -1을 할 필요가 없음
    const array = [1, 2, 3, 4, 5];
    const array2 = array.slice(2,array.length)
    console.log(array2);
    console.log(array);
}

class Student{
    constructor(name, age, enrolled, score){
        this.name = name;
        this.age = age;
        this.enrolled = enrolled;
        this.score = score;
    }
}

const students = [
    new Student('A', 29, true, 45),
    new Student('B', 28, false, 80),
    new Student('C', 30, true, 90),
    new Student('D', 40, false, 66),
    new Student('E', 18, true, 88)
];

{
    //점수가 90점 이상인 학생을 찾아라.
    //find(function(T, index) => T.score === 90);
    //find 함수는 반환형이 boolean이기 때문에 true 조건값을 만나면 멈추게 됨.
    const result = students.find((student) => student.score === 90);
    console.log(result);
}

{
    //수업에 등록한 학생만 찾아 배열로 만들어라.
    //filter(function(T,index) => T.enrolled);
    //반환형이 boolean이며, 알아서 배열로 만들어서 리턴해줌
    const result = students.filter((student) => student.enrolled);
    console.log(result);
}

{
    //학생 배열에서 점수만 뽑아내어 새로운 배열로 만들기
    //map()함수는 배열에 있는 요소들을 다른 요소로 변환시킴
    const result = students.map((student) => student.score);
    console.log(result);
}

{
    //점수가 50점보다 낮은 학생이 있는지 없는지 확인
    //배열의 요소중, 조건에 만족하는 것이 있으면 true
    //every는 모든 요소가 조건에 충족해야 true
    const result = students.some((student) => student.score < 50);
    console.log(result);

    const result2 = students.every((student) => student.score < 50);
    console.log(result2);
}

{
    //학생들의 평균 점수를 구하기
    //시작점부터 마지막까지 배열의 요소값을 누적할 때 사용
    //array.reduce((과거, 현재) => 리턴, 누적변수 초기값);

    //reduceRight는 순서를 거꾸로 하는것
    const result = students.reduce((prev, curr) => prev + curr.score, 0);
    console.log(result/students.length);
}

{
    //학생들의 점수를 string으로 변환
    const result = students
        .map((student) => student.score)
        .filter((score) => score >= 50)
        .join();
    console.log(result);
}

{
    //학생들 점수를 오름차순으로 정렬
    const result = students.map((student) => student.score).sort((a, b) => a-b).join();
    console.log(result);
}