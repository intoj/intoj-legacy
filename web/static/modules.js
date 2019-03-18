function Codeinput(){
	var lst
	lst = document.getElementsByClassName("codeinput")
	for( var i = 0 ; i < lst.length ; i++ )
		var editor = CodeMirror.fromTextArea(lst[i],{
			mode: "text/x-c++src",
			lineNumbers: true,
			theme: "solarized light",
			lineWrapping: true,
			foldGutter: true,
			gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
			matchBrackets: true,
			indentUnit: 4,
			indentWithTabs: true,
			cursorHeight: 0.85
		});
	lst = document.getElementsByClassName("markdowninput")
	for( var i = 0 ; i < lst.length ; i++ )
		var editor = CodeMirror.fromTextArea(lst[i],{
			mode: "text/x-markdown",
			lineNumbers: false,
			theme: "solarized light",
			lineWrapping: true,
			foldGutter: true,
			gutters: ["CodeMirror-foldgutter"],
			matchBrackets: true,
			indentUnit: 4,
			indentWithTabs: true,
			cursorHeight: 0.85
		});
}

function Click(id){
	classname = ".dropdown-"+id.toString()
	$(classname).slideToggle("fast");
}



marked.setOptions({
	renderer: new marked.Renderer(),
		gfm: true,
		tables: true,
		escaped : true,
		breaks: false,
		pedantic: false,
		smartLists: true,
		smartypants: false,
		xhtml: true,
		sanitize: false,
		highlight: function(code,lang){
			if( lang == "plain" ){
				return "<code class=\"hljs plaintext\">" + code + "</code>"
			}
			return hljs.highlightAuto(code).value;
		}
});

function Messagerinit(){
	Messenger.options = {
	    extraClasses: 'messenger-fixed messenger-on-bottom messenger-on-right',
		showCloseButton: true,
	    theme: 'air'
	}
}
function Message_Ok(message){
	Messenger().post({
		message: message,
		showCloseButton: true
	});
}
function Message_Error(message){
	Messenger().post({
		message: message,
		type: 'error',
		showCloseButton: true
	});
}

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

function Icheck_Init(){
	$('input').iCheck({
		checkboxClass: 'icheckbox_square-blue',
		radioClass: 'iradio_square-blue'
	});
}
