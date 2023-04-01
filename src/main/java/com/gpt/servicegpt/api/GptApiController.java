package com.gpt.servicegpt.api;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.gpt.servicegpt.service.GptService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping("/gpt")
@RestController
public class GptApiController {

    @Autowired
    GptService gptService;

    @PostMapping("/question")
    public String sendQuestion(@RequestBody String question) throws JsonProcessingException {
        String answer = gptService.createCompletion(question);

        return answer;
    }

    @PostMapping("/chat/question")
    public void sendChatQeustion(@RequestBody String question) throws JsonProcessingException {
        gptService.createChatCompletion();
//        gptService.createChatCompletion(question);
    }
}
