<!DOCTYPE HTML>
<html>

<head>
  <title>BBuveame</title>
  <meta name="description" content="website description" />
  <meta name="keywords" content="website keywords, website keywords" />
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <link rel="stylesheet" type="text/css" href="/static/style.css" />
</head>

<body>
  <div id="main">
    <div id="header">
      <div id="logo">
        <div id="logo_text">
          <!-- class="logo_colour", allows you to change the colour of the text -->
          <h1>Bienvenido a <span class="logo_colour">BBuveame</span></h1>
          <h2>sigue siendo Impresionante y Epico</h2>
        </div>
      </div>
      <div id="menubar">
        <ul id="menu">
          <!-- put class="selected" in the li tag for the selected page - to highlight which page you're on -->
          <li class="selected"><a href="https://bbuveame.herokuapp.com/desloguearse">Log Off</a></li>
          <li class="selected"><a href="https://bbuveame.herokuapp.com/">Inicio</a></li>

        </ul>
      </div>
    </div>
    <div id="content_header"></div>
    <div id="site_content">

        <!-- insert the page content here -->
        <h1>Informacion de la cuenta : {{cuenta}} </h1>
        <ul>	
        <li>IBAN : {{info["data"]["account"]["formats"]["iban"]}}</li>
	      <li>CCC : {{ info["data"]["account"]["formats"]["ccc"]}}</li>
        <li>Saldo : {{info["data"]["account"]["balance"]}}  {{info["data"]["account"]["currency"]}}</li>
        </ul>
      <h3><a href="https://bbuveame.herokuapp.com/cuentas/movimientos/{{cuenta}}">Consulta las Transacciones</a></h3>
      </div>
    </div>
</body>
</html>
