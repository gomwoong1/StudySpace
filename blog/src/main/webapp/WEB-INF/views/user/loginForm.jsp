<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<%@ include file="../layout/header.jsp"%>

<div class="container">

	<!-- 시큐리티가 /auth/loginProc를 자동으로 검사하게 대상 설정하면 C, S 에 별도 api 만들지 않아도 됨 -->
	<form action="/auth/loginProc" method="post">
		<div class="form-group">
			<label for="Username">Username</label> 
			<input type="text" name="username" class="form-control" placeholder="Enter username" id="username">
		</div>
		
		<div class="form-group">
			<label for="password">Password:</label> 
			<input type="password" name="password" class="form-control" placeholder="Enter password" id="password">
		</div>

		<button id="btn_login" class="btn btn-primary">로그인</button>
	</form>

</div>

<%@ include file="../layout/footer.jsp"%>