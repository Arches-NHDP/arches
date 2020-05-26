$(document).ready(function(){
		
		
		$.ajax({
			type: "GET",
			url: "https://heidicon.ub.uni-heidelberg.de/api/v1/session",
			crossDomain:true,
			dataType: "json",
			headers: {
				'Access-Control-Allow-Origin': 'https://heidicon.ub.uni-heidelberg.de/api/v1/session'
				},
			success: function(data){
				//var datast  = JSON.stringify(data);
				//alert("zest");
				console.log(data);
				}
			
			})
			
	
});
			