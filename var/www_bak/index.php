<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=Edge" />
<link href="./css.css" type="text/css" rel="stylesheet" />

<script src="./jquery-1.7.1.min.js"></script>
<script src="./jquery.form.js"></script>
<script src="./common.js"></script>
<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
<link href="http://code.jquery.com/ui/1.10.2/themes/smoothness/jquery-ui.css" rel="stylesheet">

<title>순천향대학교 제 16회 정보보호 페스티벌</title>
</head>
<body>
<?
	if(!$_GET[page]){
#		echo '<div id="notice">';
#		@include("./notice__sf2014!@#.php");
#		echo '<div id="poster" style="width:560px">';
#		@include("./poster__sf2014!@#.php");
		echo '<div id="prize" style="width:560px">';
		@include("./notice_prize.php");
		echo '</div>';
#		@include("./reg_notice.php");
#		echo '</div>';
	}
?>

<br /><br>
<a href="./">
<div id="top">
<img src="./img/logo_top.png" / border="0">
</div>
</a>
<div id="all" align="center">
<hr /><br /><br />
<div id="menu">
<ul>
<li><a href="./?page=intro"><font size="4" color="#000" face="Malgun Gothic">대회 소개</font></a></li>
<li><a href="./?page=poster"><font size="4" color="#000" face="Malgun Gothic">포스터</font></a></li>
<li><a href="./?page=prize"><font size="4" color="#000" face="Malgun Gothic">역대 수상자</font></a></li>
<li><a href="<?php $t = time(); echo (True) ? "http://yisf.online" : "javascript:alert('대회 기간이 아닙니다.');"?>"><font size="4" color="#000" face="Malgun Gothic">시작</font></a></li>
<?php #<li><a href="./?page=join"><font size="4" color"#000" face="Malgun Gothic">참가신청</font></a></li> ?>
</ul>
</div> <!-- menu -->
<hr />
<div align="center">
<br /><br />
</div>
<div id="body">
<?
	if( $_GET['page'] == "intro"){
		@include("./".$_GET['page']."__sf2014!@#.php");
	}
	else if( $_GET['page'] == "poster"){
		echo '<div id="poster">';
		@include("./".$_GET['page']."__sf2014!@#.php");
		echo '</div>';
		@include("./intro__sf2014!@#.php");
	}
	else if( $_GET['page'] == "prize"){
		@include("./".$_GET['page']."__sf2014!@#.php");

	}
	else if($_GET['page'] == 'join'){
		@include("./join__.php");
	}
	else{
		@include("main.html");
	}
?>
<br /><br />
<hr />
<div align="center">
<img src="./img/logo_bottom.png" />
</div>
<hr />
</div>
<?
//if(!$_GET[page])
//{
//	echo '<div id="qnwjd">';
//	@include "./qnwjd.php";
//	echo '</div>';
//}
?>
</div> <!-- all -->
</body>
</html>
