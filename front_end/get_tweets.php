<?php
$parameters = $_GET['parameters'];
$parameters = urldecode($parameters);
echo file_get_contents('http://datapool-preview.zz-demos.net/en/dolly_data/?' . $parameters);
