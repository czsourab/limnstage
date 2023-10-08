/**
 * @license Copyright (c) 2003-2018, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
  config.uiColor = '#99d6ff';
	config.height = 300;
          config.image_previewText = ' ';


	config.toolbarGroups = [
		{ name: 'styles', groups: [ 'styles' ] },
		{ name: 'document', groups: [ 'mode', 'document', 'doctools' ] },
		{ name: 'insert', groups: [ 'insert', 'youtube', 'embed', 'tabletools', 'Templates' ] },
		{ name: 'clipboard', groups: [ 'clipboard', 'undo' ] },
		{ name: 'editing', groups: [ 'find', 'selection', 'spellchecker', 'editing'  ] },
		{ name: 'basicstyles', groups: [ 'basicstyles', 'cleanup'] },
		{ name: 'forms', groups: [ 'forms' ] },
		{ name: 'paragraph', groups: [ 'list', 'indent', 'blocks', 'align', 'bidi', 'paragraph' ] },
		{ name: 'colors', groups: [ 'colors' ] },
		{ name: 'links', groups: [ 'links' ] },
		{ name: 'tools', groups: [ 'tools' ] },
		'/',
		'/',
		'/',
		'/',
		{ name: 'others', groups: [ 'others' ] },
		{ name: 'about', groups: [ 'about' ] }
	];

	config.removeButtons = 'Flash,HorizontalRule,Iframe,Save,NewPage,Preview,Paste,Source,Copy,PasteText,PasteFromWord,Cut,Undo,Redo,Replace,Find,Form,Checkbox,Radio,TextField,Textarea,Select,Button,ImageButton,HiddenField,CopyFormatting,RemoveFormat,CreateDiv,Outdent,Indent,Anchor,About,Scayt,SelectAll,PageBreak,Superscript,Subscript,Strike,Print,SpecialChar,BidiLtr,BidiRtl,Language,JustifyLeft,JustifyCenter,JustifyRight,JustifyBlock,BulletedList,NumberedList,Blockquote,ShowBlocks';
	config.extraPlugins = 'youtube','table','tabletools','dialog','dialogui','panel','floatpanel','contextmenu','tableresize';
	config.removePlugins = 'IFrame';
	config.youtube_responsive = true;
	config.filebrowserImageBrowseUrl = "uploader";
	config.image_previewText = " "
	
};
