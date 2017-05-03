ç<!DOCTYPE HTML>
<html>

<head>
  <title>BBuveame</title>
  <meta name="description" content="website description" />
  <meta name="keywords" content="website keywords, website keywords" />
  <meta http-equiv="content-type" content="text/html; charset=windows-1252" />
  <link rel="stylesheet" type="text/css" href="style/style.css" />
</head>

<body>
  <div id="main">
    <div id="header">
      <div id="logo">
        <div id="logo_text">
          <!-- class="logo_colour", allows you to change the colour of the text -->
          <h1>Bienvenido a <span class="logo_colour">BBuveame</span></h1>
          <h2>Impresionante,Epico y Legen....espera un momento...dario</h2>
        </div>
      </div>
      <div id="menubar">
        <ul id="menu">
          <!-- put class="selected" in the li tag for the selected page - to highlight which page you're on -->
          <li class="selected"><a href="index.html">Inicio</a></li>
        </ul>
      </div>
    </div>
    <div id="content_header"></div>
    <div id="site_content">

        <!-- insert the page content here -->
        <h1>Bienvenido a la Aplicacion BBuveame , aqui podras acceder a la informacion de las cuentas del Banco BBVA.</h1>
        <p>Antes de comenzar , Recuerda que esta aplicacion es de prueba y solo es valida con unos usuarios inventados que pone a disposicion la API de BBVA</p>
        <p>Para Conceder Permiso a esta aplicacion a los distintos usuarios puedes acceder <a href= https://connect.bbva.com/sandboxconnect?client_id={{APPID}}&response_type=code&redirect_uri=https://bbuveame.herokuapp.com/callback target="_blank">aqui</a>.</p>
        <p>A continuacion , Te dejo una lista de los distintos usuarios que puedes consultar (recuerda que para todos la contraseña es "123456")</p>
        <ul>
          <li><strong>00000034B</li>
          <li>00001000B</li>
          <li>46757760W</li>
	  <li>78000000P</strong></li>
        </ul>
      </div>
    </div>

</body>
</html>
