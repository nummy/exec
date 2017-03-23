$(function(){
	$.ajax({
		url:"/users",
		type:"get",
		contentType:"application/json",
		success: function(res){
			var users = res.users;
			initTable(users);
		}
	});

	$(document).on("click", "a.btn-delete", function(){
		var $tr = $(this).closest("tr");
		var id = $(this).data("id");
		deleteUser($tr,id);
	});

	$("#save").click(function(e){
		e.preventDefault();
		var id = $("#id").val();
		if(id){
			updateUser(id);
		}else{
			addUser();
		}
		
	});

	$(document).on("click", "a.btn-edit", function(){
		var id = $(this).data("id");
		$("#title").text("Edit User");
		editUser(id);
	})

	function initTable(users){
		var $data = $("#data");
		for(var i=0; i<users.length; i++){
			addUserToTable(users[i]);
		}	
	}

	function addUserToTable(user){
		var $data = $("#data");
		var $tr = $("<tr>");
		$tr.append($("<td>").text(user._id));
		var $a = $("<a>").attr("href","/review.html?userid="+user._id).text(user.username);
		$tr.append($("<td>").append($a));
		$tr.append($("<td>").text(user.firstname));
		$tr.append($("<td>").text(user.lastname));
		$tr.append($("<td>").text(user.sex));
		$tr.append($("<td>").text(user.age));
		var $td = $("<td>");
		var $button = $("<a class='btn btn-sm btn-edit' data-id='" + user._id + "'>edit</a>");
		$td.append($button);
		$button = $("<a class='btn btn-sm btn-delete' data-id='" + user._id + "'>delete</a>");
		$td.append($button);
		$tr.append($td);
		$data.append($tr);
	}

	function addUser(){
		var firstname = $("#firstname").val();
		var lastname = $("#lastname").val();
		var sex =  $('input:radio[name="sex"]:checked').val();
		var age = $("#age").val();
		var data = {
			username:lastname + " " + firstname,
			firstname:firstname,
			lastname:lastname,
			sex:sex,
			age:age
		}
		$.ajax({
			url:"/user",
			type:"post",
			data:JSON.stringify(data),
			contentType:"application/json",
			success: function(res, status){
				addUserToTable(res);
			},
			error: function(res){
				alert("username already exists");
			}
		});
	}

	function updateUser(id){
		var firstname = $("#firstname").val();
		var lastname = $("#lastname").val();
		var sex =  $('input:radio[name="sex"]:checked').val();
		var age = $("#age").val();
		var data = {
			username:lastname + " " + firstname,
			firstname:firstname,
			lastname:lastname,
			sex:sex,
			age:age
		}
		$.ajax({
			url:"/user?id=" + id ,
			type:"put",
			data:JSON.stringify(data),
			contentType:"application/json",
			success: function(res){
				location.reload();
			}
		});
		$("#id").val("");
		$("#title").text("Add User");
	}

	function deleteUser($tr, id){
		$.ajax({
			url:"/user?id=" +id,
			type:"delete",
			success: function(res){
				console.log(res);
				console.log(12);
				$tr.remove();
			}
		});
	}

	function editUser(id){
		$.ajax({
			url:"/user?id=" +id,
			type:"get",
			success: function(res){
				$("#id").val(res._id);
				$("#firstname").val(res.firstname);
				$("#lastname").val(res.lastname);
				$("input[value=" + res.sex + "]").attr("checked",true);
				$("#age").val(res.age);
			}
		});
	}
});