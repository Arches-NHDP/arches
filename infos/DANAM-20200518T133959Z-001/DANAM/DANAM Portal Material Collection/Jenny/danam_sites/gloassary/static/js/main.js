$(document).ready(function(){
	//$('.text-term').richText();
	$('.text-description').Editor();
	reset();
	
	
	
	$('.reset-terms').click(function(){
		
		reset();
		//let test = JSON.stringify($('.text-description'))
		//alert($('.text-description').Editor("getText"));
		
		/*
		$.ajax({
			type: "GET",
			url: "/glossary/more/",
			success: function(data){
				for (i= 0; i < data.length; i++){
					$('ul').append('<li>' + data[i] + '</li>');
				}
			}
		});
		*/
	});
		
	//AJAX POST
	$('.add-glossary').click(function(){
		
		$.ajax({
			type: "POST",
			url: "/glossary/add/",
			dataType: 'json',
			data: {"term-roman": $('.text-term-roman').val(), "term-dev": $('.text-term-dev').val(), "image_link": img_link, "thumb": thumb, "heidicon": heidicon_link,
				"description": $('.text-description').Editor("getText")},
			success: function(data){
				alert(data.message);
				reset();
				
			}
		});

	});
	
	function reset(){
		//$('.text-description').Editor('');
		$('.text-description').Editor("setText", "");
		$('.text-term-roman').val('');
		$('.text-term-dev').val('');
		$('.div-img').html('');
	
	}
	
	//CSRF code
	function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
	var csrftoken = getCookie('csrftoken');
	function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});


});