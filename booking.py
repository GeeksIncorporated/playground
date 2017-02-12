result  ;
$prev = $values[0];
$result[] = $prev;
$num_vals = count($values);
for ($i=1; $i<$num_vals; $i++) {
    $diff = $values[$i] - $prev;
    if (abs($diff) > 127) {
        $result[] = ESCAPE_TOKEN;
    }
    $result[] = $diff;
    $prev = $values[$i];

}
fwrite(STDOUT, implode(" ", $result));