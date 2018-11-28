function Render(){
	var a = document.getElementsByClassName("markdown")
	for( var i = 0 ; i < a.length ; i++ ){//a[i].innerhtml
		console.log(a[i].innerHTML)
		a[i].innerHTML = marked(a[i].innerHTML)
	}
}
