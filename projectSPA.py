from flask import Flask,redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/spa", code=302)


@app.route("/spa")
def spa():
    return """
   <!DOCTYPE html>
<html lang="bg">

<head>

<meta charset="UTF-8">
<title>Rossi</title>
</head>
<style>
						 * {
    box-sizing: border-box;
}

body {
  margin: 0;
  
}

	
div.container1{
	width:50:%;
	float:left;
	margin-left: 40px;
	   
}
div.container2{
	width::50%;
	float:right;
	  margin-right: 60px;
}
h1 {
    color:  #b8b894;
    margin: 10px;
    text-align: left;
}
.header {
 
    background-color: white;
    padding: 10px;
    text-align: center;
	 
	}

.topnav {
	
    overflow: hidden;
    background-color: #333;
}

.topnav a {
	
    float: left;
    display: block;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

.topnav a:hover {
    background-color: #ddd;
    color: black;
}
h2{
    color: red;
    margin: 10px;
    text-align: center;
	}
div.gallery {
	
    margin: 5px;
    border: 1px solid #ccc;
    float: left;
    width: 180px;
}

div.gallery:hover {
    border: 5px solid #777;
}

div.gallery img {
    width: 100%;
    height: auto;
}

div.desc {
    padding: 15px;
    text-align: center;
}
div.gallery1 {
    margin: 5px;
    border: 1px solid #ccc;
    float: left;
    width: 180px;
}

div.gallery1:hover {
    border: 1px solid #777;
}

div.gallery1 img {
    width: 100%;
    height: auto;
}

div.desc1 {
    padding: 15px;
    text-align: center;
}


#h1MP {
	color:  #e60000;
	text-align: center;
	margin-right:70px;
}
#MP1{
	border-radius: 50%;
	float: right;
	margin-right: 70px;
}
#MP-page{
	  background-image: url("MP1.jpg");
	background-size: 1560px 1000px;

}
div.MPleft {
	float:left;
	width:500px;
}
#textMP{ 
    float:left;
	width::40%;
}
div.MP-right {
	float:right;
	width:500px;
}
h5{
	margin-left: 70px;
}
div.border{
    width: 320px;
    padding: 10px;
    border: 5px solid gray;
    margin: 0;
	margin-left: 30px;
	margin-top: 7px;
}
#P-page{

	  background-image: url("pedikyur.jpg");
	background-size: 20588px 1900px;
	
}
div.P {
	text-align: center;
	
}
#tel{
	height: 500px;
    width: 500px;

}
div.telefon{
	
	position: absolute;
    top: 150px;
    margin-left: 650px;
	
}
#odi {
	margin-left: 30px;
}
.footer {
 
   position: fixed;
   left: 0;
   bottom: 0;
   width: 100%;
   background-color: red;
   color: white;
   text-align: center;
  opacity: 0.3;
    filter: alpha(opacity=30);
}
div.snimka{
	display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%;
	 max-width: 500px;
    height: 100px;
	
}
#textClasic{
	margin-left: 60px;
	margin-right: 60px;
}

	 
    

</style>
 <body>
<div class="header">
<h1> Комплекс Одисей - СПА </h1>

</div>
<div class="topnav">
  <a href="http://127.0.0.1:5000/spa">Начало</a>
  
  <a href="http://127.0.0.1:5000/MP"> Маникюр </a>
  
  <a href="http://127.0.0.1:5000/kont">Контакти</a>
  <a href="http://127.0.0.1:5000/reg">Регистрация</a>
</div>
 
 <br/>
<div class="container1" >
<h2> МАСАЖИ </h2>
</br>

<div class="gallery">


   <a target="_blank" href="http://yogamandala.net/team-member/classical-massage/">
    <img src="https://bodylab.studio/wp-content/uploads/2017/09/Classic-Massage-Relaxing-Massage.jpg" >
  </a>
  <div class="desc"> Класически масаж  </div>
</div>

<div class="gallery">
  <a target="_blank" href="http://www.spademetra.com/kozmetichni-uslugi/137.html" chocolate.jpg">
    <img src="http://www.hotelmarinetta.it/wp-content/uploads/massaggio-al-cioccolato-1024x643.jpg" alt="chocolate" width="600" height="400">
  </a>
  <div class="desc">Шоколадова терпия</div>
</div>

<div class="gallery">
  <a target="_blank" href="https://www.infinity-clinic.com/medena-terapiya">
    <img src="http://gradcontent.com/lib/600x350/honey3.jpg" alt="HT" width="600" height="400">
  </a>
  <div class="desc">Медена терапия </div>
</div>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

<br/>

<div class="gallery">
  <a target="_blank" href="https://spademetra.bg/antistres-masazh/">
    <img src="http://recepty.bg/upl_pict/2011/1299508910_9bJsf_1.jpg" alt="Anti" width="600" height="400">
  </a>
  <div class="desc1">Анти стрес</div>
  
</div>
<div class="gallery">
  <a target="_blank" href="https://www.dnesbg.com/zdrave/masazhat-s-topli-vulkanitchni-kamani-harmoniya-na-duha-i-tyaloto.html">
    <img src="https://cheti.info/wp-content/uploads/2014/10/masazh-goreshti-vulkanichni-kamani.jpg" alt="storm" width="600" height="400">
  </a>
  <div class="desc1">Вулканични камъни</div>
  
</div>
<div class="gallery">
  <a target="_blank" href="http://www.spademetra.com/kozmetichni-uslugi/spa-terapii/132.html">
    <img src="http://www.zdrave.ws/wp-content/uploads/2011/12/10.jpg" alt="golden" width="600" height="400">
  </a>
  <div class="desc1">Златна терапия</div>
  
</div>
  </div>
  <div class="container2" >
<h2> Козметика </h2>
</br>
  <div class="gallery">
  <a target="_blank" href="clean.jpg">
    <img src="data:image/jpeg;base64,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" alt="clean" width="600" height="450">
  </a>
  <div class="desc">Почистване на лице</div>
</div>

<div class="gallery">
  <a target="_blank" href="piling.jpg">
    <img src="https://vitalaiz.com/wp-content/uploads/2015/07/ximicheski-piling-burgas-ceni.jpg" alt="piling" width="600" height="400">
  </a>
  <div class="desc">Пилинг</div>
</div>

<div class="gallery">
  <a target="_blank" href="water.jpg">
    <img src="https://img3.stockfresh.com/files/s/simplefoto/m/78/116136_stock-photo-bubbles-and-waves.jpg" alt="ae" width="600" height="400">
  </a>
  <div class="desc">Анти ейдж </div>
</div>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

<br/>

<div class="gallery">
  <a target="_blank" href="facemassage.jpg">
    <img src="https://static.beautyforce.bg/resources/160106145536facemassage.jpg" alt="facemassage" width="600" height="400">
  </a>
  <div class="desc1">Козметичен масаж лицe </div>
  
</div>
<div class="gallery">
  <a target="_blank" href="obnovqvane.jpg">
    <img src="https://beautyforce.bg/resources/lice.jpg" alt="kot" width="600" height="400">
  </a>
  <div class="desc1">Клетъчно обновяваща терапия</div>
  
</div>
<div class="gallery">
  <a target="_blank" href="fitkletki.jpg">
    <img src="https://s.rozali.com/p/m/a/masaj-lice-licev-masaj-maslo-olio-308295-500x334.jpg" alt="fitkletki" width="600" height="400">
  </a>
  <div class="desc1">Лифтинг терапия с Фитостволови клетки</div>
  
</div>
  </div>
<div class="footer">
  <p> 2018 </p>
  </div>
  </body>
</html>
      """
@app.route("/MP")
def manikur():
    return """
    


<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="Style.css">

<title>Rossi</title>
</head>
<style>
																																																																																																																																																																																																																																																																																																																																																																															 * {
    box-sizing: border-box;
}

body {
  margin: 0;
  
}

	
div.container1{
	width:50:%;
	float:left;
	margin-left: 40px;
	   
}
div.container2{
	width::50%;
	float:right;
	  margin-right: 60px;
}
h1 {
    color:  #b8b894;
    margin: 10px;
    text-align: left;
}
.header {
 
    background-color: white;
    padding: 10px;
    text-align: center;
	 
	}

.topnav {
	
    overflow: hidden;
    background-color: #333;
}

.topnav a {
	
    float: left;
    display: block;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

.topnav a:hover {
    background-color: #ddd;
    color: black;
}
h2{
    color: red;
    margin: 10px;
    text-align: center;
	}
div.gallery {
	
    margin: 5px;
    border: 1px solid #ccc;
    float: left;
    width: 180px;
}

div.gallery:hover {
    border: 5px solid #777;
}

div.gallery img {
    width: 100%;
    height: auto;
}

div.desc {
    padding: 15px;
    text-align: center;
    }
    #h1MP {
	color:  #e60000;
	text-align: center;
	margin-right:70px;
}
#MP1{
	border-radius: 50%;
	float: right;
	margin-right: 70px;
}
#MP-page{
	  background-image: url("https://cf.ltkcdn.net/skincare/images/std/217911-675x450-Lilac-French-manicure.jpg");
	background-size: 1560px 1000px;

}
div.MPleft {
	float:left;
	width:500px;
}
#textMP{ 
    float:left;
	width::40%;
	
}
div.MP-right {
	float:right;
	width:500px;
}
h5{
	margin-left: 70px;
}
div.border{
    width: 320px;
    padding: 10px;
    border: 5px solid gray;
    margin: 0;
	margin-left: 30px;
	margin-top: 7px;
}
.footer {
 
   position: fixed;
   left: 0;
   bottom: 0;
   width: 100%;
   background-color: red;
   color: white;
   text-align: center;
  opacity: 0.3;
    filter: alpha(opacity=30);
</style>
<body id="MP-page">
<div class="header">
<h1> Комплекс Одисей - СПА   </h1>

</div>
<div class="topnav">
  <a href="http://127.0.0.1:5000/spa"> Начало</a>

  <a href="http://127.0.0.1:5000/MP"> Маникюр </a>
  

  <a href="http://127.0.0.1:5000/kont">Контакти</a>
    <a href="http://127.0.0.1:5000/reg">Регистрация</a>
</div>

 <h1 id= "h1MP"> Маникюр </h1>
<div class="MPleft">
<h2> Услуги: </h2>

 <div class="border"><h5> Маникюр + восстанавливающе покрытие </h5>
 <br/>
 <h5> Маникюр + лак </h5>
 <br/>
 <h5> Маникюр + Shellac френч</h5>
 <br/>
 <h5> Маникюр + Shellac </h5>
 <br/>
 <h5> Снятие Shellac </h5>
 </div>

 </div>
<div class="MP-right">
</div>
<div class="footer">
  <p>2018</p>
</div>

</body>
</html>
"""
@app.route("/kont")
def kont():
    return """
    
    <!DOCTYPE html>
<html lang="bg">
<head>

<link rel="stylesheet" type="text/css" href="Style.css">

<title>Rossi</title>
</head>

<style>
}

body {
  margin: 0;
  
}

	
div.container1{
	width:50:%;
	float:left;
	margin-left: 40px;
	   
}
div.container2{
	width::50%;
	float:right;
	  margin-right: 60px;
}
h1 {
    color:  #b8b894;
    margin: 10px;
    text-align: left;
}
.header {
 
    background-color: white;
    padding: 10px;
    text-align: center;
	 
	}

.topnav {
	
    overflow: hidden;
    background-color: #333;
}

.topnav a {
	
    float: left;
    display: block;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

.topnav a:hover {
    background-color: #ddd;
    color: black;
}
h2{
    color: red;
    margin: 10px;
    text-align: center;
	}
div.telefon{
	
	position: absolute;
    top: 190px;
    margin-left: 650px;
	
}
#odi {
	margin-left: 30px;
}
.footer {
 
   position: fixed;
   left: 0;
   bottom: 0;
   width: 100%;
   background-color: red;
   color: white;
   text-align: center;
  opacity: 0.3;
    filter: alpha(opacity=30);
}
div.snimka{
	display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%;
	 max-width: 500px;
    height: 100px;
	
}
</style>
	
	
 <body>
<div class="header">
<h1> Комплекс Одисей - СПА </h1>

</div>
<div class="topnav">
  <a href="http://127.0.0.1:5000/spa">Начало</a>

  <a href="http://127.0.0.1:5000/MP"> Маникюр</a>
  <a href="http://127.0.0.1:5000/kont">Контакти</a>

  <a href="http://127.0.0.1:5000/reg">Регистрация</a>
    
</div>
<div class="border">
<h1 id="h1konkatkti" > Контакти </h1>
<h4> Телефон за връзка:  0878816606   </h4>
<h4> <a target="_blank" href="https://www.abv.bg/"> Email:  </a> rossi.gimisheva@abv.bg   </h4>
<h4> Facebook: Росица Гимишева   </h4>
<h4> Адрес: сдпсйдпсй   </h4>
</div>
<br/>
<img id="odi" src="https://lh5.googleusercontent.com/p/AF1QipPKQkNvNLMZDTDgkpQtMmxuW4TCJrWPrJBETWnG=w213-h160-k-no">
<div class="telefon"> 
<img id="tel" src="https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX2587691.jpg"> </div>
<br/>
<br/>

<div class="P">
<h3>Карта</h3>
 <a target="_blank" href="https://www.google.bg/maps/place/%D0%A5%D0%BE%D1%82%D0%B5%D0%BB+%22%D0%9E%D0%B4%D0%B8%D1%81%D0%B5%D0%B9%22/@42.6557516,27.69024,16.18z/data=!4m7!3m6!1s0x40a69f3693d041a9:0x7827803e31b6b1cb!5m1!1s2018-06-04!8m2!3d42.654735!4d27.6952921">
<img src="http://karta.bg360.net/bulgaria/%D0%BA%D0%B0%D1%80%D1%82%D0%B0-%D0%BD%D0%B0-%D0%B1%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D0%B8%D1%8F.jpg">
</a>
</div>
<div class="footer">
  <p> 2018 </p>
</div>
</body>
</html>
    """

@app.route("/reg")
def reg():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
    font-family: Arial, Helvetica, sans-serif;
    background-color: black;
}

* {
    box-sizing: border-box;
}

/* Add padding to containers */
.container {
    padding: 16px;
    background-color: white;
}

/* Full-width input fields */
input[type=text], input[type=password] {
    width: 100%;
    padding: 15px;
    margin: 5px 0 22px 0;
    display: inline-block;
    border: none;
    background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus {
    background-color: #ddd;
    outline: none;
}

/* Overwrite default styles of hr */
hr {
    border: 1px solid #f1f1f1;
    margin-bottom: 25px;
}

/* Set a style for the submit button */
.registerbtn {
    background-color: #4CAF50;
    color: white;
    padding: 16px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 100%;
    opacity: 0.9;
}

.registerbtn:hover {
    opacity: 1;
}

/* Add a blue text color to links */
a {
    color: dodgerblue;
}
.topnav {
	
    overflow: hidden;
    background-color: #333;
}

.topnav a {
	
    float: left;
    display: block;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

.topnav a:hover {
    background-color: #ddd;
    color: black;
}
h2{
    color: red;
    margin: 10px;
    text-align: center;
	}

/* Set a grey background color and center the text of the "sign in" section */
.signin {
    background-color: #f1f1f1;
    text-align: center;
}
</style>
</head>
<body>
<div class="topnav">
  <a href="http://127.0.0.1:5000/spa">Начало</a>

  <a href="http://127.0.0.1:5000/MP"> Маникюр</a>
  <a href="http://127.0.0.1:5000/kont">Контакти</a>

  <a href="http://127.0.0.1:5000/reg">Регистрация</a>
    
</div>

<form action="/action_page.php">
  <div class="container">
    <h1>Register</h1>
    <p>Please fill in this form to create an account.</p>
    <hr>

    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>

    <label for="psw-repeat"><b>Repeat Password</b></label>
    <input type="password" placeholder="Repeat Password" name="psw-repeat" required>
    <hr>


    <button type="submit" class="registerbtn">Register</button>
  </div>
  

  </div>
</form>

</body>
</html>
"""

if __name__ == "__main__":
    app.run()
