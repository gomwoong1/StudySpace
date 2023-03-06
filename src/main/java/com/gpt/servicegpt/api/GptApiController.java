package com.gpt.servicegpt.api;

import com.google.gson.JsonObject;
import com.gpt.servicegpt.service.GptService;
import com.gpt.servicegpt.service.OpenAiService;
import com.theokanning.openai.completion.CompletionRequest;
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
    public ResponseEntity sendQuestion(@RequestBody String question) {

        ResponseEntity val = gptService.createCompletion(api, question);

        return val;
    }
}
