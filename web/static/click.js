function Div_click(obj,event){
	div_list = document.getElementsByClassName("div_canclick")
	for( var i = 0 ; i < div_list.length ; i++ ){
		if( div_list[i] != obj )
			div_list[i].innerHTML = "233"
	}
}
