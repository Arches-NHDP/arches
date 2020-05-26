$(document).ready(function(){
	//$('.text-term').richText();
	var txtDef = decodeEntities($('#defn').html());
	
	$('.text-term-roman').val($('#eng').html());
	$('.text-term-dev').val($('#np').html());
	$('.text-description').Editor();
	//$('.text-description').Editor("setText", "<div><em>test</em></div>");
	$('.text-description').Editor("setText", txtDef);
	let divImg = document.getElementById('div-image');
	console.log($('#imag').html());
	img_link = $('#imag').html();
	thumb = $('#thumb').html();
	heidicon_link = $('#heidicon').html();
	divImg.innerHTML = "<table width='50%'><tr><td><img src='" + thumb + "'></img></td>"
							  + "<td align='right'><a href='" + img_link + "' target='_blank'>enlarge the image</a><br>"
							  + "<a href='https://heidicon.ub.uni-heidelberg.de/detail/" 
							  + heidicon_link + "' target='_blank'>link to heidICON</a></td></tr></table>"; 
	
	
	//$('.text-description').Editor(setText, {{ uuid }});
	//reset();
/*	
	$.ajax({
			type: "GET",
			url: "/glossary/upload/",
			//data: { get_param: 'value' },
			dataType: 'json',
			success: function(data){
				alert(data.Stringify());
			
			}

	});
*/
	$('.update-glossary').click(function(){
		
		
		$.ajax({
			type: "POST",
			url: "/glossary/do_update/",
			dataType: 'json',
			data: {"uuid": $('#uuid').html(), "term-roman": $('.text-term-roman').val(), "term-dev": $('.text-term-dev').val(), 
				"description": $('.text-description').Editor("getText"), "thumb": thumb, "image_link": img_link, "heidicon": heidicon_link},
				
			
			success: function(data){
				alert(data.message);
				//reset();
				
			}
		});

	});
	function decodeEntities(encodedString) {
		var translate_re = /&(nbsp|amp|quot|lt|gt);/g;
		var translate = {
			"nbsp":" ",
			"amp" : "&",
			"quot": "\"",
			"lt"  : "<",
			"gt"  : ">"
		};
		return encodedString.replace(translate_re, function(match, entity) {
			return translate[entity];
		}).replace(/&#(\d+);/gi, function(match, numStr) {
			var num = parseInt(numStr, 10);
			return String.fromCharCode(num);
		});
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