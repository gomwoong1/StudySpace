package com.gpt.servicegpt.api;

import com.theokanning.openai.completion.CompletionRequest;
import com.theokanning.openai.service.OpenAiService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping("/gpt")
@RestController
public class GptApiController {

    @PostMapping("/question")
    public ResponseEntity<?> sendQuestion() {
        OpenAiService openAiService = new OpenAiService("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");
        CompletionRequest completionRequest = CompletionRequest.builder()
                .prompt("hello?")
                .model("text-davinci-003")
                .echo(false)
                .build();
        return ResponseEntity.ok(openAiService.createCompletion(completionRequest).getChoices());
    }
}
