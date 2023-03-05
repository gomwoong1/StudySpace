package com.gpt.servicegpt.api;

import com.gpt.servicegpt.service.GptService;
import com.gpt.servicegpt.service.OpenAiService;
import com.theokanning.openai.completion.CompletionRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping("/gpt")
@RestController
public class GptApiController {

    @Autowired
    GptService gptService;

    private final String key = "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";
    @PostMapping("/question")
    public ResponseEntity<?> sendQuestion() {
        OpenAiService openAiService = new OpenAiService(key);
        CompletionRequest completionRequest = CompletionRequest.builder()
                .prompt("스프링부트는 뭐야?")
                .model("text-davinci-003")
                .echo(false)
                .maxTokens(2048)
                .temperature(1.0)
                .build();
        return ResponseEntity.ok(openAiService.createCompletion(completionRequest).getChoices());
    }
}
