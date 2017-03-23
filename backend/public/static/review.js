$(function(){
	var query = location.href.split("?")[1];
	$.ajax({
		url:"/review?"+query,
		type:"get",
		contentType:"application/json",
		success: function(res){
			var reviews = res.reviews;
			initTable(reviews);
		}
	});

	$(document).on("click", "a.btn-delete", function(){
		var $tr = $(this).closest("tr");
		var id = $(this).data("id");
		deleteReview($tr,id);
	});

	$("#save").click(function(e){
		e.preventDefault();
		var id = $("#id").val();
		if(id){
			updateReview(id);
		}else{
			addReview();
		}
		
	});

	$(document).on("click", "a.btn-edit", function(){
		var id = $(this).data("id");
		$("#title").text("Edit review");
		editReview(id);
	})

	function initTable(reviews){
		var $data = $("#data");
		for(var i=0; i<reviews.length; i++){
			addReviewToTable(reviews[i]);
		}	
	}

	function addReviewToTable(review){
		var $data = $("#data");
		var $tr = $("<tr>");
		$tr.append($("<td>").text(review._id));
		$tr.append($("<td>").text(review.storeID));
		$tr.append($("<td>").text(review.userID));
		$tr.append($("<td>").text(review.rate));
		$tr.append($("<td>").text(review.comment));
		var $td = $("<td>");
		var $button = $("<a class='btn btn-sm btn-edit' data-id='" + review._id + "'>edit</a>");
		$td.append($button);
		$button = $("<a class='btn btn-sm btn-delete' data-id='" + review._id + "'>delete</a>");
		$td.append($button);
		$tr.append($td);
		$data.append($tr);
	}

	function updateReview(id){
		var firstname = $("#firstname").val();
		var lastname = $("#lastname").val();
		var sex =  $('input:radio[name="sex"]:checked').val();
		var age = $("#age").val();
		var data = {
			reviewname:lastname + " " + firstname,
			firstname:firstname,
			lastname:lastname,
			sex:sex,
			age:age
		}
		$.ajax({
			url:"/review?id=" + id ,
			type:"put",
			data:JSON.stringify(data),
			contentType:"application/json",
			success: function(res){
				location.reload();
			}
		});
		$("#id").val("");
		$("#title").text("Add review");
	}

	function deleteReview($tr, id){
		$.ajax({
			url:"/review?id=" +id,
			type:"delete",
			success: function(res){
				$tr.remove();
			}
		});
	}

	function editReview(id){
		$.ajax({
			url:"/review?id=" +id,
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