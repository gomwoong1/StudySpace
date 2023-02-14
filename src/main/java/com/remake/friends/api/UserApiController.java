package com.remake.friends.api;

import com.remake.friends.model.RoleType;
import com.remake.friends.model.User;
import com.remake.friends.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserApiController {

    @Autowired
    UserService userService;

    @PostMapping("/api/join")
    public void join(@RequestBody User user){
        userService.회원가입(user);
    }
}
