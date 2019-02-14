function Footer_position(){
	if( $(document.body).outerHeight() < $(window).height()-50 ){
		$("#footer").css("position","fixed")
		$("#footer").css("bottom","0px")
	}else{
		$("#footer").css("position","static")
		$("#footer").css("bottom","0px")
	}
}
