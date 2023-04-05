package com.gpt.servicegpt.api;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.gpt.servicegpt.dto.ResponseDto;
import com.gpt.servicegpt.service.GptService;
import com.theokanning.openai.completion.chat.ChatMessage;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RequestMapping("/gpt")
@RestController
public class GptApiController {

    @Autowired
    GptService gptService;

    // Completion Service Req Controller
    @PostMapping("/question")
    public String sendQuestion(@RequestBody String question) throws JsonProcessingException {
        String answer = gptService.createCompletion(question);

        return answer;
    }

    // Chat Completion Service Req Controller
    @PostMapping("/chat/question")
    public ResponseDto<ChatMessage> sendChatQeustion(@RequestBody List<ChatMessage> log) throws JsonProcessingException {
        ChatMessage answer = gptService.createChatCompletion(log);

        return new ResponseDto<ChatMessage>(HttpStatus.OK.value(), answer);
    }

    // ImageCreate Service Req Controller
    @PostMapping("/image/create")
    public ResponseDto<String> sendImgCreate(@RequestBody String requirement) {
        String img = gptService.createImage(requirement);
        System.out.println("Service 요청됨!");

        return new ResponseDto<String>(HttpStatus.OK.value(), img);
    }

    // ImageEdit Service Req Controller
    @PostMapping("/image/edit")
    public void sendImgEdit(){

    }
}
