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

	$.ajax({
		url:"/users",
		type:"get",
		contentType:"application/json",
		success: function(res){
			var users = res.users;
			initSelect(users);
		}
	});

	$(document).on("click", "a.btn-delete", function(){
		var $tr = $(this).closest("tr");
		var id = $(this).data("id");
		deleteStore($tr,id);
	});

	$(document).on("click", "a.btn-review", function(){
		var $tr = $(this).closest("tr");
		var id = $(this).data("id");
		$("#store").val(id);
		var $modal = $("#modal");
		$modal.modal("show");
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

	$("#saveReview").click(function(){
		var storeid = $("#store").val();
		var userid = $("#users").val();
		var rate = $("#rate").val();
		var comment = $("#comment").val();
		var data = {
			storeID:storeid,
			userID:userid,
			rate:parseInt(rate),
			comment:comment
		};
		console.log(JSON.stringify(data));
		$.ajax({
			url:"/review",
			type:"POST",
			contentType:"application/json",
			data:JSON.stringify(data),
			success: function(){
				$("#modal").modal("hide");
			}
		})
	});

	$(document).on("click", "a.btn-edit", function(){
		var id = $(this).data("id");
		$("#title").text("Edit store");
		editStore(id);
	})

	function initTable(stores){
		var $data = $("#data");
		for(var i=0; i<stores.length; i++){
			addStoreToTable(stores[i]);
		}	
	}

	function initSelect(users){
		var $users = $("#users");
		var options= [];
		for(var i=0;i<users.length; i++){
			options.push($("<option>").val(users[i]._id).text(users[i].username));
		}
		$users.append(options);
	}

	function addStore(){
		var storename = $("#storename").val();
		var category = $("#category").val();
		var address = $("#address").val();
		var data = {
			storename:storename,
			category:category,
			address:address
		}
		$.ajax({
			url:"/store",
			type:"POST",
			data:JSON.stringify(data),
			contentType:"application/json",
			success: function(res){
				addStoreToTable(res);
			}
		});
	}

	function addStoreToTable(store){
		var $data = $("#data");
		var $tr = $("<tr>");
		$tr.append($("<td>").text(store._id));
		var $a = $("<a>").attr("href","/review.html?storeid="+store._id).text(store.storename);
		$tr.append($("<td>").append($a));
		$tr.append($("<td>").text(store.category));
		$tr.append($("<td>").text(store.address));
		var $td = $("<td>");
		var $button = $("<a class='btn btn-sm btn-edit' data-id='" + store._id + "'>edit</a>");
		$td.append($button);
		$button = $("<a class='btn btn-sm btn-delete' data-id='" + store._id + "'>delete</a>");
		$td.append($button);
		$button = $("<a class='btn btn-sm btn-review' data-id='" + store._id + "'>add review</a>");
		$td.append($button);
		$tr.append($td);
		$data.append($tr);
	}

	function updateStore(id){
		var storename = $("#storename").val();
		var category = $("#category").val();
		var address = $("#address").val();
		var data = {
			storename:storename,
			category:category,
			address:address
		}
		$.ajax({
			url:"/store?id=" + id ,
			type:"put",
			data:JSON.stringify(data),
			contentType:"application/json",
			success: function(res){
				console.log(res);
				$("#id").val("");
				$("#title").text("Add store");
				location.reload();
			}
		});

	}

	function deleteStore($tr, id){
		$.ajax({
			url:"/store?id=" +id,
			type:"delete",
			success: function(res){
				console.log(res);
				$tr.remove();
			}
		});
	}

	function editStore(id){
		$.ajax({
			url:"/store?id=" +id,
			type:"get",
			success: function(res){
				$("#id").val(res._id);
				$("#storename").val(res.storename);
				$("#category").val(res.category);
				$("#address").val(res.address);

			}
		});
	}
});