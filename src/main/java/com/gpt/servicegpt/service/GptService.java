package com.gpt.servicegpt.service;

import com.theokanning.openai.completion.CompletionRequest;
import com.theokanning.openai.completion.CompletionResult;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class GptService {

    public ResponseEntity<?> createCompletion(String api){
        OpenAiService openAiService = new OpenAiService(api);
        CompletionRequest completionRequest = CompletionRequest.builder()
                .prompt("쓰레드를 활용한 간단한 게임을 파이썬 코드로 짜줘")
                .model("text-davinci-003")
                .echo(false)
                .maxTokens(2048)
                .temperature(1.0)
                .build();

        return ResponseEntity.ok(openAiService.createCompletion(completionRequest).getChoices());
    }

}
