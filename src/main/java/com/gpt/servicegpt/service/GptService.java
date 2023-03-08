package com.gpt.servicegpt.service;

import com.theokanning.openai.completion.CompletionChoice;
import com.theokanning.openai.completion.CompletionRequest;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class GptService {

    public String createCompletion(String api, String question){
        OpenAiService openAiService = new OpenAiService(api);
        CompletionRequest completionRequest = CompletionRequest.builder()
                .prompt(question)
                .model("text-davinci-003")
                .echo(false)
                .maxTokens(2048)
                .temperature(1.0)
                .build();

        List<CompletionChoice> res = openAiService.createCompletion(completionRequest).getChoices();
        CompletionChoice res_list = res.get(0);
        String answer = res_list.getText().trim();

        return answer;
    }

}
