<!DOCTYPE html>
<html>
<body>
<h1>William's page</h1>

<?php

$output1 = system('python ~zhangwi/html/cgi-bin/display.cgi', $retval);
$output2 = system('python ~zhangwi/html/cgi-bin/modify.cgi', $retval);

echo date('Y-m-d H:i:s');
$date = date ('H');
$fl = fopen("timesheet.txt", "a+");
fwrite($fl, $date."\n");
fclose($fl);

$output3 = system('python ~zhangwi/html/cgi-bin/hour.cgi', $retval);
?>
 
</body>

</html>
