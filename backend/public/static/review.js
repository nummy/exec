$(function(){
	var query = location.href.split("?")[1];
	// init review table
	$.ajax({
		url:"/review?"+query,
		type:"get",
		contentType:"application/json",
		success: function(res){
			var reviews = res.reviews;
			initTable(reviews);
		}
	});

	// init user select
	$.ajax({
		url:"/users",
		type:"get",
		contentType:"application/json",
		success: function(res){
			var users = res.users;
			initUserSelect(users);
		}
	});

	// init store select
	$.ajax({
		url:"/stores",
		type:"get",
		contentType:"application/json",
		success: function(res){
			var stores = res.stores;
			initStoreSelect(stores);
		}
	});

	// delete review
	$(document).on("click", "a.btn-delete", function(){
		var $tr = $(this).closest("tr");
		var id = $(this).data("id");
		deleteReview($tr,id);
	});

	// update review
	$("#save").click(function(e){
		e.preventDefault();
		updateReview();
	});

	$(document).on("click", "a.btn-edit", function(){
		var id = $(this).data("id");
		$("#modal").modal("show");
		editReview(id);
	})

	function initTable(reviews){
		var $data = $("#data");
		for(var i=0; i<reviews.length; i++){
			addReviewToTable(reviews[i]);
		}	
	}

	function initUserSelect(users){
		var $users = $("#users");
		var options= [];
		for(var i=0;i<users.length; i++){
			options.push($("<option>").val(users[i]._id).text(users[i].username));
		}
		$users.append(options);
	}

	function initStoreSelect(stores){
		var $stores = $("#store");
		var options= [];
		for(var i=0;i<stores.length; i++){
			options.push($("<option>").val(stores[i]._id).text(stores[i].storename));
		}
		$stores.append(options);
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

	function updateReview(){
		var id = $("#review_id").val();
		var storeID = $("#store").val();
		var userID = $("#users").val();
		var rate = $("#rate").val();
		var comment = $("#comment").val();
		var data = {
			storeID:storeID,
			userID:userID,
			rate:rate,
			comment:comment
		}
		console.log(34);
		$.ajax({
			url:"/review?id=" + id ,
			type:"put",
			data:JSON.stringify(data),
			contentType:"application/json",
			success: function(res){
				$("#modal").modal("hide");
				toastr.success("successful");
				location.reload();
			}
		});
	}

	function deleteReview($tr, id){
		$.ajax({
			url:"/review?id=" +id,
			type:"delete",
			success: function(res){
				$tr.remove();
				toastr.success("successful");
			}
		});
	}

	function editReview(id){
		$("#review_id").val(id);
		$.ajax({
			url:"/review?id=" +id,
			type:"get",
			success: function(res){
				$("#users").val(res.userID);
				$("#store").val(res.storeID);
				$("#rate").val(res.rate);
				$("#comment").val(res.comment);
			}
		});
	}
});