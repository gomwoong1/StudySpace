// 1.
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
}

console.log(calculate('+',2,3));
console.log(calculate('-',2,3));
console.log(calculate('*',2,3));
console.log(calculate('/',6,3));

// 2.
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

    students.map((students) => {
        console.log(students);
    });
}

//3.

const array = [1, 2, 3];
array.unshift(10);
array.push(20);
array.splice(2, 0, 50);
console.log(array);



//4.
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

    rabbit2 = JSON.parse(json,  () => );
    
    for(item in rabbit2){
        console.log(item);
    }
}