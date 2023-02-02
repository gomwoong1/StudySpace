<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<%@ include file="../layout/header.jsp"%>

<div class="container">

	<form>
		<input type="hidden" value = "${principal.user.id }" id="id">
		<div class="form-group">
			<label for="Username">Username</label> 
			<input type="text" value="${principal.user.username }" class="form-control" placeholder="Enter username" id="username" readonly>
		</div>
		<div class="form-group">
			<label for="password">Password:</label> 
			<input type="password" class="form-control" placeholder="Enter password" id="password">
		</div>
		<div class="form-group">
			<label for="email">Email address:</label> 
			<input type="email" value="${principal.user.email }"class="form-control" placeholder="Enter email" id="email">
		</div>
	</form>
		
	<button id="btn_update" class="btn btn-primary">수정하기</button>

</div>

<script src="/js/user.js"></script>
<%@ include file="../layout/footer.jsp"%>