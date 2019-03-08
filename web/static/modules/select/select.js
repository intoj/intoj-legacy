function Select_Changeto(id,status){
	if( status == -1 ){
		$("#select-answer-"+id.toString()).html("不限")
		$("#select-input-"+id.toString()).attr("value","")
	}else{
		$("#select-answer-"+id.toString()).html(Judge_Status(status))
		$("#select-input-"+id.toString()).attr("value",status)
	}
}
