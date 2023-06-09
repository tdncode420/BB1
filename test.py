from doc import Doc

raw = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./styles.css">
</head>
<body>
    <div class="wrapper" style="width: 100%;height: 100%;">
        <canvas id="cvs" style="width: 100%;height: 100%;"></canvas>
    </div>
    <script src="./index.js"></script>
</body>
</html>'''

doc = Doc(raw)
ele = doc.querySelector('.wrapper')
print(ele.querySelector('canvas'))
