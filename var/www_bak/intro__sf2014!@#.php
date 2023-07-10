<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<title>Untitled Document</title>
</head>

<body>
<script>
function doIframe(){
    o = document.getElementsByTagName('iframe');

    for(var i=0;i<o.length;i++){  
        if (/\bautoHeight\b/.test(o[i].className)){
            setHeight(o[i]);
            addEvent(o[i],'load', doIframe);
        }
    }
}

function setHeight(e){
    if(e.contentDocument){
        e.height = e.contentDocument.body.offsetHeight + 35; //높이 조절
    } else {
        e.height = e.contentWindow.document.body.scrollHeight;
    }
}

function addEvent(obj, evType, fn){
    if(obj.addEventListener)
    {
    obj.addEventListener(evType, fn,false);
    return true;
    } else if (obj.attachEvent){
    var r = obj.attachEvent("on"+evType, fn);
    return r;
    } else {
    return false;
    }
}

if (document.getElementById && document.createTextNode){
 addEvent(window,'load', doIframe); 
} 
</script>

<div id="menu2">
<ul><li><a target="frame" href="./img/intro2.png"><img src="./img/button4.png" border="0"/></a></li></ul>
<ul><li><a target="frame" href="./img/intro.png"><img src="./img/button3.png" border="0"/></a></li></ul>
<ul>
<li><a target="frame" href="./img/org.png"><img src="./img/button1.png" border="0"/></a></li></ul>
<ul><li><a target="frame" href="./pri.php"><img src="./img/button2.png" border="0"/></a></li></ul>

</div>
<div id="content">

<div align="center"><iframe src="./img/intro2.png" name="frame" class="autoHeight" width="800" height="650" frameborder="0" scrolling="no">
</iframe></div>

</div>
</body>
</html>
