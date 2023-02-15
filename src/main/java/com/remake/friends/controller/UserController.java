package com.remake.friends.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class UserController {

    @GetMapping("/auth/join")
    public String join(){
        return "auth/signup";
    }

    @GetMapping("/auth/login")
    public String login(){
        return "auth/login";
    }
}
