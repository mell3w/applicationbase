<h2>Click</h2>
<form action="" method="POST">
    <button name="click" class="click">Click me!</button>
</form>

<?php
if(isset($_POST['click']))
{
    $date_clicked = date('Y-m-d H:i:s');;
    echo "Time the button was clicked: " . $date_clicked . "<br>";
}
?>