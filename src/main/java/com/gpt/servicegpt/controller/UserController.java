package com.gpt.servicegpt.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class UserController {

    @GetMapping("/auth/login")
    public String login(){
        return "auth/login";
    }

    @GetMapping("/auth/signup")
    public String join(){
        return "auth/signup";
    }
}
