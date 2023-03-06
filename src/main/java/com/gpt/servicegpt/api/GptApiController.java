package com.gpt.servicegpt.api;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.gson.JsonObject;
import com.gpt.servicegpt.service.GptService;
import com.gpt.servicegpt.service.OpenAiService;
import com.theokanning.openai.completion.CompletionRequest;
import net.bytebuddy.implementation.bind.MethodDelegationBinder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
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

    private final String api = "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";

    @PostMapping("/question")
    public String sendQuestion(@RequestBody String question) throws JsonProcessingException {

        ResponseEntity val = gptService.createCompletion(api, question);

        ObjectMapper objectMapper = new ObjectMapper();

        String jsonString = objectMapper.writeValueAsString(val.getBody());
        JsonNode jsonNode = objectMapper.readTree(jsonString);

        String answer = jsonNode.get(0).get("text").asText().substring(2);

//        if(answer.contains("answer")) {
//            answer = answer.substring(answer.charAt(3),)
//        }

        return answer;
    }
}
