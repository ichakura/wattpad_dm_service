
function search(ele) {
    if(event.key === 'Enter') {
        message = ele.value;        
		document.getElementById('nandaomaewa').value = ''
		$.ajax({
          type: "POST",
          contentType: "application/json",
          url: "/parse_data/",
          traditional: "true",
          data: JSON.stringify(message),
          dataType: "json"
          })
		


	}
}

     