package com.inflearn.study.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

// Swagger 설정 파일
@Configuration
@EnableSwagger2
public class SwaggerConfiguration {

    // 설정 핵심 파일
    @Bean
    public Docket api() {
        // 생성자의 DocumentaionType는 Swagger 버전에 따라 적절한 값을 선택할 것.
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(apiInfo()) // API 기본정보 설정 메서드
                .select() // 문서화 할 API를 선택하는 메서드로, 다음의 메서드들과 이어짐
                .apis(RequestHandlerSelectors.basePackage("com.inflearn.study")) //
                .paths(PathSelectors.any())
                .build();
    }

    // Swagger UI에 표시되는 API의 기본정보를 설정하는데 사용되는 클래스
    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title("SprintBoot Swagger2 Test")
                .description("Swagger2 테스트")
                .version("1.0.0")
                .build();
    }
}
