package com.gpt.servicegpt.service;

import com.theokanning.openai.completion.CompletionChoice;
import com.theokanning.openai.completion.CompletionRequest;
import com.theokanning.openai.completion.chat.ChatCompletionChoice;
import com.theokanning.openai.completion.chat.ChatCompletionRequest;
import com.theokanning.openai.completion.chat.ChatMessage;
import com.theokanning.openai.image.CreateImageEditRequest;
import com.theokanning.openai.image.CreateImageRequest;
import com.theokanning.openai.image.Image;
import com.theokanning.openai.image.ImageResult;
import io.reactivex.Single;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import org.springframework.stereotype.Service;
import retrofit2.http.Body;
import retrofit2.http.POST;

import java.util.List;

@Service
public class GptService {
    private final String api = "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";

    OpenAiService openAiService = new OpenAiService(api);

    // Q&A Service
    // 질문 문자열을 전달받는다.
    public String createCompletion(String question) {
        // Completion Request DTO 생성. 빌더로 모델 및 옵션 설정
        CompletionRequest completionRequest = CompletionRequest.builder()
                .prompt(question)
                .model("text-davinci-003")
                .echo(false)
                .maxTokens(2048)
                .temperature(1.0)
                .build();

        // openAiServcie 클래스의 Completion Request 메서드 수행
        // 반환 객체의 CompletionResult 중, 텍스트가 있는 CompletionChoie만 가져옴
        List<CompletionChoice> res = openAiService.createCompletion(completionRequest).getChoices();

        // 0번 인덱스에 해당하는 text만 가져와서 데이터 재가공 및 반환
        CompletionChoice res_list = res.get(0);
        String answer = res_list.getText().trim();

        return answer;
    }

    // ChatCompletion Service
    public ChatMessage createChatCompletion(List<ChatMessage> log) {
        String answer_json = "";

        // ChatCompletionRequest 객체를 Builder로 생성
        ChatCompletionRequest chatCompletionRequest = ChatCompletionRequest.builder()
                .model("gpt-3.5-turbo")
                .messages(log)
                .build();

        // ChatCompletionResult 객체 중, 값을 가지고 있는 ChatCompletionChoice 객체만 가져옴
        // 해당 객체에서 Message에 해당하는 0번 인덱스만 가져와서 반환
        List<ChatCompletionChoice> res = openAiService.createChatCompletion(chatCompletionRequest).getChoices();
        ChatMessage answer = res.get(0).getMessage();

        return answer;
    }

    public String createImage(String requirement){
        CreateImageRequest ImgReq = new CreateImageRequest().builder()
                .prompt(requirement) // 생성할 이미지에 대한 설명
                .n(1) // 생성할 이미지의 개수로, 기본은 1
                .size("512x512")   // 생성할 이미지의 크기를 지정, 기본은 1024*1024
                .responseFormat("b64_json") // 이미지 반환 방식을 지정, 기본은 url.
                .build();

        ImageResult res = openAiService.createImage(ImgReq);
        List<Image> listImg = res.getData();
        String b64 = listImg.get(0).getB64Json();

        return b64;
    }

//   ImageEdit의 openAiService 메서드
//    @POST("/v1/images/edits")
//    Single<ImageResult> createImageEdit(@Body RequestBody requestBody);

//    오버로딩, 자료형을 받아서 파싱 및 진짜 메서드 호출
//    public ImageResult createImageEdit(CreateImageEditRequest request, String imagePath, String maskPath) {
//        java.io.File image = new java.io.File(imagePath);
//        java.io.File mask = null;
//        if (maskPath != null) {
//            mask = new java.io.File(maskPath);
//        }
//        return createImageEdit(request, image, mask);
//    }
//
//    public ImageResult createImageEdit(CreateImageEditRequest request, java.io.File image, java.io.File mask) {
//        RequestBody imageBody = RequestBody.create(MediaType.parse("image"), image);
//
//        MultipartBody.Builder builder = new MultipartBody.Builder()
//                .setType(MediaType.get("multipart/form-data"))
//                .addFormDataPart("prompt", request.getPrompt())
//                .addFormDataPart("size", request.getSize())
//                .addFormDataPart("response_format", request.getResponseFormat())
//                .addFormDataPart("image", "image", imageBody);
//
//        if (request.getN() != null) {
//            builder.addFormDataPart("n", request.getN().toString());
//        }
//
//        if (mask != null) {
//            RequestBody maskBody = RequestBody.create(MediaType.parse("image"), mask);
//            builder.addFormDataPart("mask", "mask", maskBody);
//        }
//
//        return execute(api.createImageEdit(builder.build()));
//    }

}
