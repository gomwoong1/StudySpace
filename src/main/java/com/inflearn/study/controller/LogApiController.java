package com.inflearn.study.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LogApiController {

    private final Logger LOGGER = LoggerFactory.getLogger(LogApiController.class);
    @GetMapping("/test")
    public String getTest(){

        LOGGER.info("getTest 메서드가 호출되었습니다.");
        return "TEST!";
    }

    @GetMapping("/test/{name}")
    public String getArguTest(@PathVariable String name){

        LOGGER.info("getArguTest 메서드가 호출되었습니다. : " + name);
        return "TEST " + name;
    }
}
