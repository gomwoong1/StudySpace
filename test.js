// 1. 덧셈, 뺄셈, 곱셈, 나눗셈
{
    function calculate(oper, a, b){
        switch(oper){
            case '+':
                return a+b;
                break;
            case '-':
                return a-b;
                break;
            case '*':
                return a*b;
                break;
            case '/':
                return a/b;
                break;
            default :
                console.log('잘못된 값을 입력했습니다.');
                break;
        }
    }

    console.log(calculate('+',2,3));
    console.log(calculate('-',2,3));
    console.log(calculate('*',2,3));
    console.log(calculate('/',6,3));
}



// 2. 클래스가 있고 학생 성적이 50이상인 학생 성적만 출력하시오. 
//    학생 성적을 역순으로 출력하시오.
{
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

    //성적이 50점 이상인 학생만 출력하기
    const result = students
    .map((students) => students.score)
    .filter((students) => students >= 50);
    console.log(`result: ${result}`);

    //결과값 역순으로 출력하기
    const result_reverse = students
        .map((students) => students.score)
        .filter((students) => students >= 50)
        .reverse();
    console.log(`reverse result: ${result_reverse}`)

    //50점 이상인 학생만 뽑아서 내림차순 정렬하기
    const result_desc = students
        .map((students) => students.score)
        .filter((students) => students >= 50)
        .sort((a,b) => b-a);
    console.log(`result desc: ${result_desc}`);
}

//3.
// 1뒤에 50삽입하고, 맨앞에 10삽입, 맨뒤에 20삽입
// 1, 50, 2, 3 해당하는 부분만 추출해서 list2 만들어 출력하기
{
    const array = [1, 2, 3];
    array.unshift(10);
    array.push(20);
    array.splice(2, 0, 50);
    console.log(`array: ${array}`);

    const result = array.slice(1,5)
    console.log(`result: ${result}`);
}


//4. JSON으로 생성한 후 출력하시오.
//다시 JSON을 파싱한 후 키와 값을 출력하시오.
{
    const rabbit = {
    name: 'tori',
    color: 'white',
    size: null,
    birthDate: new Date(),
    jump:function() {
        console.log(`${this.name} can jump!`);
    }
    };

    const json = JSON.stringify(rabbit);
    console.log(json);

    const parse = JSON.parse(json, (key, value) => console.log(`key:${key} value:${value}`));
}