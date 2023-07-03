package com.gpt.servicegpt.api;

import com.gpt.servicegpt.dto.ResponseDto;
import com.gpt.servicegpt.model.User;
import com.gpt.servicegpt.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserApiController {

    @Autowired
    UserService userService;

    @PostMapping("/auth/joinProc")
    public ResponseDto<Integer> join(@RequestBody User user){
        userService.회원가입(user);

        return new ResponseDto<Integer>(HttpStatus.OK.value(), 1);
    }
}
