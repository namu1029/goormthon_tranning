<?php
include "db_conn.php";

if($_SERVER['REQUEST_METHOD'] === 'POST'){
    $userid = $_POST['userid'];
    $userpw = $_POST['userpw'];

    $sql = "SELECT userid, userpw FROM User WHERE userid='$userid' AND userpw='$userpw'";
    $result = $conn->query($sql);

    if(mysqli_num_rows($result)){
        echo "<script>alert('로그인을 성공하였습니다!');</script>";
        echo "<script>location.href='main.html'</script>";
    }
    else{
        echo "<script>alert('로그인을 실패하였습니다!');</script>";
        echo "<script>location.href='login.html'</script>";
    }
}
?>