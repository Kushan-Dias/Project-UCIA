<?php 

include 'config.php';

session_start();

error_reporting(0);

// if (isset($_SESSION['username'])) {
//     header("Location: login.php");
// }

if (isset($_POST['submit'])) {
	$email = $_POST['email'];
	$password = $_POST['password'];

	$sql = "SELECT * FROM users WHERE email='$email' AND password='$password'";
	$result = mysqli_query($conn, $sql);
	if ($result->num_rows > 0) {
		$row = mysqli_fetch_assoc($result);
		$_SESSION['username'] = $row['username'];
		header("Location: main.html");
	} else {
		echo "<script>alert('Woops! Email or Password is Wrong.')</script>";
	}
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>login</title>
    <link rel="stylesheet" href="login.css">
</head>
<body>
    <div class="container">
        <form action="" method="POST" class="login-email">
            <p class="login-text" sstyle="font-size:2rem; font-weight:800">Login</p>
            <div class="input-group">
                <input type="email" name="email" id="" placeholder="Email" required>
            </div>
            <div class="input-group">
                <input type="password" name="password" id="" placeholder="Password" required>
            </div>
            <div class="input-group">
                <button name="submit" class="btn">Login</button>
            </div>
            <p class="login-register-text">&nbsp&nbsp&nbsp&nbsp Don't have an account? <a href="register.php">Register Here</a></p>
        </form>
    </div>
</body>
</html>