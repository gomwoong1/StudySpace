class UserStorage {
    loginUser(id, password){
        return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (
                (id === 'jw' && password === 'dream') ||
                (id === 'coder' && password === 'school')
            ) {
                resolve(id);
            } else {
                reject(new Error('not found'));
            }
            }, 2000);
        });
    }

    getRoles(user){
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                if(user === 'jw') {
                    resolve({name: 'jw', role: 'admin'});
                } else {
                    reject(new Error('no access'));
                }
            }, 1000);
        })
    }
}

const userStorage = new UserStorage();
const id = prompt('enter your id');
const password = prompt('enter your password');
userStorage.loginUser(id, password)
.then(user => userStorage.getRoles(user))
.then(user => alert(`hello ${user.name}, you have a ${user.role} role`))
.catch(console.log);