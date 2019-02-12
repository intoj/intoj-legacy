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
