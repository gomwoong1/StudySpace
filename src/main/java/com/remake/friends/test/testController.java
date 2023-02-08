package com.remake.friends.test;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class testController {
    @GetMapping("/test")
    public String test(Model model) {
        int val = 3;
        int val2 = 4;
        model.addAttribute("value", val);
        model.addAttribute("value2", val2);
        return "index";
    }
}
