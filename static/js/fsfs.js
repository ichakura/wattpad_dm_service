var message = ""
function search(ele) {
    if(event.key === 'Enter') {
        message = ele.value;        
		$.ajax({
          type: "POST",
          contentType: "application/json",
          url: "/parse_data/",
          traditional: "true",
          data: JSON.stringify(message),
          dataType: "json"
          })
		  .done(function(result){     // on success get the return object from server
    console.log(result)     // do whatever with it. In this case see it in console
})
	
	
	
	}
}

