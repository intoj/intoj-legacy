function Select_Changeto(id,status){
	if( status == -1 ){
		$("#select-answer-"+id.toString()).html("不限")
		$("#select-input-"+id.toString()).attr("value","")
	}else{
		$("#select-answer-"+id.toString()).html(Judge_Status(status))
		$("#select-input-"+id.toString()).attr("value",status)
	}
}

function Select_Changeto_Showactive(id,status){
	Select_Changeto(id,status)
	$(".select-"+id.toString()+"-item").removeClass("listline-active")
	$(".select-"+id.toString()+"-item-"+status.toString()).addClass("listline-active")
}
