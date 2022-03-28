<?php
    include 'config.php';
    error_reporting(0);

    if (isset($_POST['submit'])){
        $username = $_POST['username'];
        $email = $_POST['email'];
        $password = $_POST['password'];
        $cpassword = $_POST['cpassword'];
    }
    if ($password == $cpassword){
        $sql = "SELECT * FROM users WHERE email='$email' ";
        $result = mysqli_query($conn, $sql);
        if (!$result -> num_rows > 0){
            $sql = "INSERT INTO users (username, email, password) 
                VALUES ('$username','$email','$password')";
            $result = mysqli_query($conn, $sql);
            if($result){
                echo "<script>alert('Wow! Your regestration successed.')</script>";
            }else{
                echo "<script>alert('Whoops Something wrong went.')</script>";
        }
    }else{
            
            echo "<script>alert('Ooops! Email already exists.')</script>";
        }
        
    }else{
        echo "<script>alert('password not matched.')</script>";
    }

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link rel="stylesheet" href="login.css">
</head>
<body>
    <div class="container">
        <form action="" method="POST" class="login-email">
            <p class="login-text" style="font-size:2rem; font-weight:800">Register</p>
            <div class="input-group">
                <input type="text" name="username" id="" placeholder="Username"  required>
            </div>
            <div class="input-group">
                <input type="email" name="email" id="" placeholder="Email"  required>
            </div>
            <div class="input-group">
                <input type="password" name="password" id="" placeholder="password"  required>
            </div>
            <div class="input-group">
                <input type="password" name="cpassword" id="" placeholder="confirm password"  required>
            </div>
            <div class="input-group">
                <button name="submit" class="btn">Register</button>
            </div>
            <p class="login-register-text">Have an account <a href="login.php">Login Here</a></p>
        </form>
    </div>
</body>
</html>