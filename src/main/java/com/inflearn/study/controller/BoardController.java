package com.inflearn.study.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class BoardController {
    @GetMapping("/hello")
    public String method(Model model) {
        model.addAttribute("data", "hello!");
        return "index.html";
    }
}
