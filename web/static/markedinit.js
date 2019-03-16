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
