package com.gpt.servicegpt.config.api;

import com.gpt.servicegpt.dto.ResponseDto;
import com.gpt.servicegpt.model.User;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserApiController {

    @PostMapping("/auth/joinProc")
    public ResponseDto<Integer> join(@RequestBody User user){

        return new ResponseDto<Integer>(HttpStatus.INTERNAL_SERVER_ERROR.value(), 1);
    }
}
