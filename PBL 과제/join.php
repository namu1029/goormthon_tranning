<?php
include "db_conn.php";

if($_SERVER['REQUEST_METHOD'] === 'POST'){
    $username = $_POST['username'];
    $userid = $_POST['userid'];
    $userpw = $_POST['userpw'];
    $userpw_ch = $_POST['userpw_ch'];
    $Email = $_POST['Email'];

    if($userpw === $userpw_ch){
        $sql = "INSERT INTO User (username, userid, userpw, Email) VALUES ('$username', '$userid', '$userpw', '$Email')";
        $result = $conn->query($sql);

        echo "<script>alert('회원가입 되었습니다! 로그인을 시도해 주세요.');</script>";
        echo "<script>location.href='login.html'</script>";
    }
}
?>