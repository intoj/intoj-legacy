function Render(){
	var a = document.getElementsByClassName("markdown")
	for( var i = 0 ; i < a.length ; i++ ){
		//console.log(a[i].innerHTML)
		a[i].innerHTML = marked(a[i].innerHTML)
		//console.log(a[i].innerHTML)
		a[i].innerHTML = a[i].innerHTML.replace(/&amp;lt;/g,'<')
		a[i].innerHTML = a[i].innerHTML.replace(/&amp;gt;/g,'>')
		a[i].innerHTML = a[i].innerHTML.replace(/&amp;amp;/g,'&')
		a[i].innerHTML = a[i].innerHTML.replace(/<pre><code>.*<span class="hljs-section">.*/g,'')
		//console.log(a[i].innerHTML)
	}
}
