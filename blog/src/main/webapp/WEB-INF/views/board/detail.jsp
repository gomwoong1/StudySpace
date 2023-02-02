<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@include file="../layout/header.jsp" %>

<div class="container">
	
	<button class="btn btn-secondary" onclick="history.back()">돌아가기</button>
	<button id="btn_update" class="btn btn-warning">수정</button>
	
	 <c:if test="${board.user.id == principal.user.id}">
		<button id="btn_delete" class="btn btn-danger">삭제</button><br><br>
	</c:if>
	<div>
		글 번호 : <span id="id"><i>${board.id } </i></span>
		작성자 : <span><i>${board.user.username } </i></span>  <!-- EAGAR 전략이라 가능 -->
	</div> <br>
	
	<div>
		<h3>${board.title}</h3>
	</div>
	<hr>
	<div>
		<div>${board.content}</div>
	</div>
	<hr>
</div>

<script src="/js/board.js"></script>
<%@include file="../layout/footer.jsp" %>