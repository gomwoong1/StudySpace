package com.remake.friends.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class UserController {

    @GetMapping("/user/join")
    public String join(){
        return "user/signup";
    }

    @GetMapping("/user/login")
    public String login(){
        return "user/login";
    }
}
