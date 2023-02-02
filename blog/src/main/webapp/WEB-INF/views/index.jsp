<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@include file="layout/header.jsp" %>

<div class="container">
	
	<c:forEach var="board" items="${boards}">   <!-- 컨트롤러에서 넘어온 model 정보 -->
	 	<div class="card m-2" >
	  		<div class="card-body">
	    		<h4 class="card-title">${boards.title}</h4>   <!-- board 클래스의 getter 호출 -->
	    		<a href="#" class="btn btn-primary">${boards.content}</a>
	  		</div>
		</div>
	</c:forEach>
	
</div>

<%@include file="layout/footer.jsp" %>