$(function(){
	$.ajax({
		url:"/stores",
		type:"get",
		contentType:"application/json",
		success: function(res){
			var stores = res.stores;
			initTable(stores);
		}
	});

	$(document).on("click", "a.btn-delete", function(){
		var $tr = $(this).closest("tr");
		var id = $(this).data("id");
		deleteStore($tr,id);
	});

	$("#save").click(function(e){
		e.preventDefault();
		var id = $("#id").val();
		if(id){
			updateStore(id);
		}else{
			addStore();
		}
		
	});

	$(document).on("click", "a.btn-edit", function(){
		var id = $(this).data("id");
		editStore(id);
	})

	function initTable(Stores){
		var $data = $("#data");
		for(var i=0; i<Stores.length; i++){
			var $tr = $("<tr>");
			$tr.append($("<td>").text(Stores[i]._id));
			$tr.append($("<td>").text(Stores[i].Storename));
			$tr.append($("<td>").text(Stores[i].firstname));
			$tr.append($("<td>").text(Stores[i].lastname));
			$tr.append($("<td>").text(Stores[i].sex));
			$tr.append($("<td>").text(Stores[i].age));
			var $td = $("<td>");
			var $button = $("<a class='btn btn-sm btn-edit' data-id='" + Stores[i]._id + "'>edit</a>");
			$td.append($button);
			$button = $("<a class='btn btn-sm btn-delete' data-id='" + Stores[i]._id + "'>delete</a>");
			$td.append($button);
			$tr.append($td);
			$data.append($tr);
		}	
	}

	function addStore(){
		var firstname = $("#firstname").val();
		var lastname = $("#lastname").val();
		var sex =  $('input:radio[name="sex"]:checked').val();
		var age = $("#age").val();
		var data = {
			Storename:lastname + " " + firstname,
			firstname:firstname,
			lastname:lastname,
			sex:sex,
			age:age
		}
		$.ajax({
			url:"/Store",
			type:"post",
			data:JSON.stringify(data),
			contentType:"application/json",
			success: function(res){
				console.log(res);
			}
		});
	}

	function updateStore(id){
		var firstname = $("#firstname").val();
		var lastname = $("#lastname").val();
		var sex =  $('input:radio[name="sex"]:checked').val();
		var age = $("#age").val();
		var data = {
			Storename:lastname + " " + firstname,
			firstname:firstname,
			lastname:lastname,
			sex:sex,
			age:age
		}
		$.ajax({
			url:"/Store?id=" + id ,
			type:"put",
			data:JSON.stringify(data),
			contentType:"application/json",
			success: function(res){
				console.log(res);
			}
		});
		$("#id").val("");
	}

	function deleteStore($tr, id){
		$.ajax({
			url:"/Store?id=" +id,
			type:"delete",
			success: function(res){
				console.log(res);
				$tr.remove();
			}
		});
	}

	function editStore(id){
		$.ajax({
			url:"/Store?id=" +id,
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