//자바 스크립트는 동기적인 언어(synchronous)
//var 선언 혹은 함수 선언 등의 hoisting
//hoisting 이후부터 작성한 순서대로 실행됨.

console.log('1');
setTimeout(() => console.log('2'), 1000);
console.log('3');

//동기적인 callback
function printImmediately(print) {
    print();
}

printImmediately(() => console.log('hello'));

//비동기적인 callback
function printWithDelay(print, timeout){
    setTimeout(print, timeout);
}

printWithDelay(() => console.log('async callback'), 2000);

//콜백지옥

class UserStorage {
    loginUser(id, password, onSuccess, onError){
        setTimeout(() => {
            if (
                (id === 'jw' && password === 'dream') ||
                (id === 'coder' && password === 'school')
            ) {
                onSuccess(id);
            } else {
                onError(new Error('not found'));
            }
        }, 2000);
    }

    getRoles(user, onSuccess, onError){
        setTimeout(() => {
            if(user === 'jw') {
            onSuccess({name: 'jw', role: 'admin'});
            } else {
                onError(new Error('no access'));
            }

        }, 1000);
    }
}

const userStorage = new UserStorage();
const id = prompt('enter your id');
const password = prompt('enter your password');
userStorage.loginUser(
    id,
    password,
    user => {
        userStorage.getRoles(
            user,
            userWithRole => {
                alert(
                    `hello ${userWithRole.name}, you have a ${userWithRole.role} role`
                );
            },
            error => {
                console.log(error);
            }
        );
    },
    error => {
        console.log(error);
    }
);