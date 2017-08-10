 <!DOCTYPE html>
<html>
<head> <link rel="stylesheet" type="text/css" href="../css/stylesheet.css">
<script src="../js/myScript.js"></script></head>
<body>

<div id='div5'>
<form id='buttons' method="post" action="../php/displayResults.php"> 
		
		<?php
			echo "<a id='sub' href=\"javascript:history.go(-1)\">GO BACK</a><br>";
			$filelist="/home/sruthi/dev/UIMA-NLP-Platform/MyWorkspace/data/text_files/op/list.txt";
			$myfile1=fopen($filelist,"r")or die("Unable to open file!");
			echo "<p id='p2'>Choose :</p>";
			echo "<br>";
			echo "<div id='div6'>";
			$count=1;
			while(!feof($myfile1)) {
				$an=trim(fgets($myfile1));
				//echo $an;
				if($an && $an!="DocumentAnnotation")echo "<input type='radio' id='b".$count ."' value=".$an." name='Option'>".$an."<br>";
				$count++;

			}

			fclose($myfile1);
		?>	
		<br><br>
		<input id='sub' type='submit' value='View'>

		<br>
	</div>
	
	
</form>
</div>

</body>
</html> 