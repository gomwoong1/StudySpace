package com.gpt.servicegpt.service;

import com.theokanning.openai.completion.CompletionRequest;
import com.theokanning.openai.completion.CompletionResult;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class GptService {

    public ResponseEntity<?> createCompletion(String api, String question){
        OpenAiService openAiService = new OpenAiService(api);
        CompletionRequest completionRequest = CompletionRequest.builder()
                .prompt(question)
                .model("text-davinci-003")
                .echo(false)
                .maxTokens(2048)
                .temperature(1.0)
                .build();

        return ResponseEntity.ok(openAiService.createCompletion(completionRequest).getChoices());
    }

}
