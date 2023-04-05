package com.inflearn.study.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;
@RestController
public class BoardController {
    @GetMapping("/hello")
    public String sayHello() {
        return "Hello!";
    }

    @GetMapping("/hello/{name}")
    public String sayHelloName(@PathVariable String name) {
        return "Hello " + name;
    }

    @GetMapping("/hello/param")
    public String sayParamHello(@RequestParam String name, @RequestParam String pwd) {
        return name + "님의 비밀번호 : " + pwd;
    }

    @GetMapping("/hello/varArgument")
    public String sayVarArgument(@RequestParam Map<String, String> param){
        StringBuilder sb = new StringBuilder();

        param.entrySet().forEach(map->{
            sb.append(map.getKey() + ":" + map.getValue() + "\n");
        });

        return sb.toString();
    }
}

