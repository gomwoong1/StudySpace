// 31강 - 에러 출력 페이지 만들기
// 사용자에게 스택 트레이서를 전부 보여줄 필요가 없기 때문.
package com.cos.blog.handler;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestController;

import com.cos.blog.dto.ResponseDto;

/*
 	MEMO
 	
 	@ControllerAdvice
 	Exception 발생하면 해당 어노테이션이 붙은 클래스로 이동시킴.
 	
 */

@ControllerAdvice
@RestController
public class GlobalExceptionHandler {
	
	@ExceptionHandler(value=Exception.class)
	public ResponseDto<String> handleAgumentException(Exception e) {
		return new ResponseDto<String>(HttpStatus.INTERNAL_SERVER_ERROR.value(), e.getMessage());
	}
}
