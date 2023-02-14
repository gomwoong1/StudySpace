package com.remake.friends.api;

import com.remake.friends.dto.ResponseDto;
import com.remake.friends.model.User;
import com.remake.friends.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserApiController {

    @Autowired
    UserService userService;

    @PostMapping("/api/join")
    public ResponseDto<Integer> join(@RequestBody User user){
        userService.회원가입(user);

        return new ResponseDto<Integer>(HttpStatus.OK.value(), 1);
    }

    @PostMapping("/api/login")
    public ResponseDto<Integer> login(@RequestBody User user){
        userService.로그인(user);

        return new ResponseDto<Integer>(HttpStatus.OK.value(), 1);
    }
}
