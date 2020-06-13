document.addeventListener('DOMContentLoaded',function(){
	document.querySelector('#form').onsubmit=function(){
		const request=newXMLHttpRequest();
		const currency=document.querySelector('#currency').value;
		request.open('POST','/convert');
	}
})