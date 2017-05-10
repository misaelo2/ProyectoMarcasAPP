<!DOCTYPE HTML>
<html>

<head>
  <title>BBuveame</title>
  <meta name="description" content="website description" />
  <meta name="keywords" content="website keywords, website keywords" />
  <meta http-equiv="content-type" content="text/html; charset=windows-1252" />
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
          <li class="selected"><a href="index.html">Inicio</a></li>
        </ul>
      </div>
    </div>
    <div id="content_header"></div>
    <div id="site_content">

        <!-- insert the page content here -->
    <TABLE BORDER>
      <TR>
        <TH>ID</TH> <TH>Cantidad</TH> <TH>Fecha</TH> <TH>Concepto</TH>
      </TR>
      %for elem in movimientos :
      <TR>
        <TD>elem["id"]</TD>elem["amount"] elem["currency"] <TD>elem["operationDate"].split("T")[0]</TD> <TD>elem["description"]</TD>
      </TR>
    </TABLE>  
      </div>
    </div>
</body>
</html>