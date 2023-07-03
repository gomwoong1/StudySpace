package com.gpt.servicegpt.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class BoardController {

    @GetMapping({"/", ""})
    public String index(){
        return "index";
    }

    @GetMapping("/chat")
    public String Chatting(){
        return "chatCompletion.html";
    }

    @GetMapping("/image")
    public String imagePage(){
        return "image.html";
    }

    @GetMapping("/edit")
    public String imageEdit(){
        return "imageEdit.html";
    }
}
