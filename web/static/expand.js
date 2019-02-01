function Close(obj,cnt){
	$(obj).slideUp("fast");
	obj.attributes.show_or_hide.nodeValue = "hide"
}
function Expand(obj){
	$(obj).slideDown("fast");
	obj.attributes.show_or_hide.nodeValue = "show"
}

function Click(id){
	classname = "dropdown-"+id.toString()
	var obj = document.getElementsByClassName(classname)[0]
	if( obj.attributes.show_or_hide.nodeValue == "show" ){
		Close(obj,0)
	}else{
		Expand(obj)
	}
}
