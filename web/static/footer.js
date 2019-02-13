function Footer_position(){
	if( $(document).height() < $(window).height()-30 ){
		$("#footer").css("position","fixed")
		$("#footer").css("bottom","0px")
	}else{
		$("#footer").css("position","absoute")
		$("#footer").css("bottom","0px")
	}
}
