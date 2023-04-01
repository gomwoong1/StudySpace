package com.gpt.servicegpt.service;

import com.theokanning.openai.completion.CompletionChoice;
import com.theokanning.openai.completion.CompletionRequest;
import com.theokanning.openai.completion.chat.ChatCompletionRequest;
import com.theokanning.openai.completion.chat.ChatMessage;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class GptService {

    private final String api = "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";

    OpenAiService openAiService = new OpenAiService(api);

    public String createCompletion(String question) {
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

    public String createChatCompletion(List<ChatMessage> log) {
        List<ChatMessage> chat_list = new ArrayList<>();
        ChatMessage chatMessage = new ChatMessage();

//        chat_list.add();
//
//        ChatCompletionRequest chatCompletionRequest = ChatCompletionRequest.builder()
//                .model("gpt-3.5-turbo")
//                .messages()
//                .build();

        return "test";
    }
}
