<?php
$parameters = $_GET['parameters'];
$parameters = urldecode($parameters);
echo file_get_contents('http://datapool-preview.zz-demos.net/en/tweets_per_day/?' . $parameters);