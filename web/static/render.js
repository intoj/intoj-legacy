function Render(){
	var a = document.getElementsByClassName("markdown")
	for( var i = 0 ; i < a.length ; i++ ){
		// console.log(a[i].innerHTML)
		a[i].innerHTML = marked(a[i].innerHTML)
		// console.log(a[i].innerHTML)
		a[i].innerHTML = a[i].innerHTML.replace(/<code class="language-/g,'<code class="hljs language-')
		a[i].innerHTML = a[i].innerHTML.replace(/&amp;lt;/g,'&lt;')
		a[i].innerHTML = a[i].innerHTML.replace(/&amp;gt;/g,'&gt;')
		a[i].innerHTML = a[i].innerHTML.replace(/&amp;amp;/g,'&amp;')
		// console.log(a[i].innerHTML)
	}
}
