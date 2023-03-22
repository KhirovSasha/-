<?php

$file = fopen("/app/app.py", "r");

print_r(fgets($file));

fclose($file);