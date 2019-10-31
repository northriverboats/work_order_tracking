<?php
/*** PREVENT THE PAGE FROM BEING CACHED BY THE WEB BROWSER ***/header("Cache-Control: no-cache, must-revalidate");
header("Expires: Sat, 26 Jul 1997 05:00:00 GMT");
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'http://10.10.200.96:8080');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$page = curl_exec($ch);
curl_close($ch);

$html = (explode("\n",$page));
$size = count($html);
$head = array_search("  </head>", $html);

?>
<!DOCTYPE html>
<html lang="en">
<head>
<?php 
for($i = 3; $i < $head; $i++) {
    echo $html[$i] . "\n";
}
?>
</head>
<body>
<?php
for($i = $head + 2; $i < $size -2; $i++) {
    echo $html[$i] . "\n";
}
?>
</html>
