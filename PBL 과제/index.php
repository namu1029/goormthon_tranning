<head>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            text-align: center;
        }

        .container {
            width: 400px;
            margin: 100px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1, p {
            color: #333;
        }

        button {
            margin: 20px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border: none;
            border-radius: 4px;
            transition: opacity 0.3s ease;
            background-color: #3498db;
            color: #fff;
        }

        button:hover {
            opacity: 0.8;
        }

    </style>
</head>
<body>
<div class="container">
    <h1>Main Page</h1>
    <p>로그인이 필요합니다.</p>
    <button onclick="location.href='login.php'">로그인</button >
    <button onclick="location.href='join.php'">회원가입</button >
</div>
</body>

