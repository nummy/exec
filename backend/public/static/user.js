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
		editUser(id);
	})

	function initTable(users){
		var $data = $("#data");
		for(var i=0; i<users.length; i++){
			var $tr = $("<tr>");
			$tr.append($("<td>").text(users[i]._id));
			$tr.append($("<td>").text(users[i].username));
			$tr.append($("<td>").text(users[i].firstname));
			$tr.append($("<td>").text(users[i].lastname));
			$tr.append($("<td>").text(users[i].sex));
			$tr.append($("<td>").text(users[i].age));
			var $td = $("<td>");
			var $button = $("<a class='btn btn-sm btn-edit' data-id='" + users[i]._id + "'>edit</a>");
			$td.append($button);
			$button = $("<a class='btn btn-sm btn-delete' data-id='" + users[i]._id + "'>delete</a>");
			$td.append($button);
			$tr.append($td);
			$data.append($tr);
		}	
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
			success: function(res){
				console.log(res);
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
				console.log(res);
			}
		});
		$("#id").val("");
	}

	function deleteUser($tr, id){
		$.ajax({
			url:"/user?id=" +id,
			type:"delete",
			success: function(res){
				console.log(res);
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