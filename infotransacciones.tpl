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
 <TABLE >
      %for elem in movimientos :
  <TR><TH>ID</TH>
    <TD>Item 1</TD> <TD>Item 2</TD> <TD>Item 3</TD></TR>
  <TR><TH>Cantidad</TH>
    <TD>Item 4</TD> <TD>Item 5</TD> <TD>Item 6</TD></TR>
  <TR><TH>Fecha</TH>
    <TD>Item 7</TD> <TD>Item 8</TD> <TD>Item 9</TD></TR>
   <TR><TH>Concepto</TH> 
    <TD>Item 7</TD> <TD>Item 8</TD> <TD>Item 9</TD></TR>
</TABLE>

      </div>
    </div>
</body>
</html>
