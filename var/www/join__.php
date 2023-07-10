<?php
	$t = time();
	if(True or $_SERVER['REMOTE_ADDR'] == "211.229.218.185" || (1657869331 <= $t && $t <= 1659704400)) {	// 2016/07/24 01:00:00 KST ~ 2016/08/05 22:00:00 KST
?>
<html>
<head>
<meta charset="utf-8">
<style>
body { text-align: center; }
#info { text-align: center; }
table { margin: 0 auto; }
input[type=password],
textarea { width: 500px; }
input[type=submit] { padding: 3px 15px; border: 1px solid #000; cursor: pointer; }
</style>
<script type="text/javascript" src="sha512.js"></script>
<script>
function gen(form) {
	if(form.password.value == "") {
		alert("비밀번호를 입력하세요.");
		form.password.value = form.hash.value = "";
	} else {
		var shaObj = new jsSHA("SHA-512", "TEXT");
		shaObj.update(form.password.value);
		form.hash.value = shaObj.getHash("HEX");
	}
	return false;
}
</script>
</head>
<body>
<br>
<div id="info">
	<img src='/yisf2022/[2022]_YISF_Facebook_Banner.png' width=700px>
<br><br>
</div>
<br>
아래의 양식에 맞추어 <b><ins>"yisf.sch@gmail.com"</ins></b>로 메일 보내주세요.
<br>
<br>
<a href="./yisf2024/register.zip">2024 YISF 신청서 다운로드</a>

</body>
</html>
<?php
	} else {
?>
<script>alert("참가신청 기간이 마감되었습니다.");history.go(-1);</script>
<?php
	}
