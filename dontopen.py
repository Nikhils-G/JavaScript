<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Emotional Love Letter</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #ffb6c1, #ff8a65);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Arial', sans-serif;
        }

        .letter-container {
            position: relative;
            width: 350px;
            height: 450px;
            background-color: #fff;
            border: 2px solid #ff69b4;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            animation: letterFadeIn 2s ease-in-out;
        }

        .letter-container h1 {
            font-size: 36px;
            color: #ff69b4;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .letter-content {
            font-size: 18px;
            color: #ff6347;
            line-height: 1.6;
            opacity: 0;
            animation: letterReveal 5s forwards;
        }

        .scissors {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 50px;
            height: 50px;
            background: url('https://image.shutterstock.com/image-vector/scissors-icon-design-template-260nw-1067599749.jpg') no-repeat center center;
            background-size: cover;
            animation: scissorCut 5s forwards;
            transform: translate(-50%, -50%);
        }

        @keyframes letterFadeIn {
            0% {
                opacity: 0;
                transform: scale(0.5);
            }
            100% {
                opacity: 1;
                transform: scale(1);
            }
        }

        @keyframes letterReveal {
            0% {
                opacity: 0;
            }
            80% {
                opacity: 0;
            }
            100% {
                opacity: 1;
            }
        }

        @keyframes scissorCut {
            0% {
                transform: translate(-50%, -50%) rotate(0deg);
            }
            50% {
                transform: translate(-50%, -50%) rotate(45deg);
            }
            100% {
                transform: translate(-50%, -50%) rotate(90deg);
            }
        }

        .hidden-message {
            display: none;
            font-size: 22px;
            font-family: 'Cursive', sans-serif;
            color: #fff;
            text-align: center;
            position: absolute;
            top: 70%;
            left: 50%;
            transform: translateX(-50%);
            opacity: 0;
            animation: messageReveal 3s 5s forwards;
        }

        @keyframes messageReveal {
            0% {
                opacity: 0;
            }
            100% {
                opacity: 1;
                transform: translateX(-50%) translateY(-20px);
            }
        }
    </style>
</head>
<body>
    <div class="letter-container">
        <h1>ప్రియమైన అనుస్రీ</h1>
        <p class="letter-content">
            
        </p>
        <div class="scissors"></div>
        <div class="hidden-message">
            
        </div>
    </div>

    <script>
        window.onload = function() {
            setTimeout(function() {
                document.querySelector('.letter-content').style.opacity = 1;
                document.querySelector('.hidden-message').style.display = 'block';
            }, 5000);  // Delay before the letter content appears and the hidden message is revealed
        }
    </script>
</body>
</html>
