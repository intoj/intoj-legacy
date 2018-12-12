function Tab(obj,event){
	if( event.keyCode == 9 ){
		obj.value = obj.value + "\t"
		event.returnValue = false
	}
}
