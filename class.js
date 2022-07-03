class Person{
    constructor(name, age){
        //필드
        this.name = name;
        this.age = age;
    }

    //메소드
    speak(){
        console.log(`${this.name}: hello`);
    }
}

const jw = new Person('jw', 23);
console.log(jw.name, jw.age);
jw.speak();

//getter, setter
class user{
    constructor(firstName, lastName, age, sex){
        this.fristName = firstName;
        this.lastName = lastName;
        this.age = age;
    }

    get age() {
        return this._age;
    }

    set age(value) {
        if(value < 0) {
            console.log('잘못된 나이');
        }
        this._age = value;
    }
}
const user1 = new user('Steve', 'woong', 1);

user1.age = 2;
console.log(user1.age);

//public, private
class Experiment{
    publicField = 3; //public
    #privateField = 3; //private
}
const ex = new Experiment();
console.log(ex.publicField);
console.log(ex.privateField);

//static
class Article {
    static publisher = 'coding';
    constructor(articlenumber){
        this.articlenumber = articlenumber;
    }

    static printPublisher() {
        console.log(Article.publisher);
    }
}

const article1 = new Article(1);
const article2 = new Article(2);
// console.log(Article1.publisher);
console.log(Article.publisher);
Article.printPublisher();

//상속과 다형성
class Shape {
    constructor(width, heigth, color){
        this.width = width;
        this.height = heigth;
        this.color = color;
    }

    draw() {
        console.log(`drawing ${this.color} color`);
    }

    getArea(){
        return this.width * this.height;
    }
}

class Rectangle extends Shape {}
class Triangle extends Shape {
    draw(){
        console.log("override");
        super.draw(); //부모 draw 호출
    }
    getArea(){
        return (this.width * this.height) / 2;
    }
}

const rectangle = new Rectangle(20, 20, 'blue');
rectangle.draw();
console.log(rectangle.getArea());

const triangle = new Triangle(20, 20, 'red');
triangle.draw();
console.log(triangle.getArea());

//instanceof
console.log(rectangle instanceof Rectangle);
console.log(triangle instanceof Triangle);
console.log(triangle instanceof Rectangle);
console.log(triangle instanceof Shape); //상속받았기 때문
console.log(triangle instanceof Object); //클래스는 모두 object 상속받음