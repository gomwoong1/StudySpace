package com.gpt.servicegpt.service;

import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.theokanning.openai.completion.CompletionChoice;
import com.theokanning.openai.completion.CompletionRequest;
import com.theokanning.openai.completion.chat.ChatCompletionChoice;
import com.theokanning.openai.completion.chat.ChatCompletionRequest;
import com.theokanning.openai.completion.chat.ChatCompletionResult;
import com.theokanning.openai.completion.chat.ChatMessage;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class GptService {

    String json;
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

    public ChatMessage createChatCompletion(List<ChatMessage> log) {
        String answer_json = "";

        // ChatCompletionRequest 객체를 Builder로 생성
        ChatCompletionRequest chatCompletionRequest = ChatCompletionRequest.builder()
                .model("gpt-3.5-turbo")
                .messages(log)
                .build();

        List<ChatCompletionChoice> res = openAiService.createChatCompletion(chatCompletionRequest).getChoices();
        ChatMessage answer = res.get(0).getMessage();

//        try{
//            ObjectMapper mapper = new ObjectMapper();
//            mapper.configure(JsonGenerator.Feature.ESCAPE_NON_ASCII, false);
//            answer_json = mapper.writeValueAsString(answer);
//        } catch(JsonProcessingException e){
//            System.out.println(e.getMessage());
//        }

        return answer;
    }
}
