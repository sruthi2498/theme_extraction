 <?php session_start(); ?>
<!DOCTYPE html>
<html>
	<head> <link rel="stylesheet" type="text/css" href="../css/stylesheet.css"></head>
<body>

<?php
	
	$target_dir = "/home/sruthi/dev/scikit-workspace/sklearn_tut_workspace/uploads/";
	$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
	//echo $_FILES["fileToUpload"]["name"]." ".$_FILES['fileToUpload']['tmp_name'];
	//echo $target_file;
	$uploadOk = 1;
	if ($_FILES['fileToUpload']['error'] == UPLOAD_ERR_OK               //checks for errors
	      && is_uploaded_file($_FILES['fileToUpload']['tmp_name'])) { //checks that file is uploaded
	  //echo file_get_contents($_FILES['fileToUpload']['tmp_name']); 
	}
	$info = pathinfo($_FILES['fileToUpload']['name']);
	$ext = $info['extension']; // get the extension of the file
	$newname = "PDFFormat.".$ext; 

	$target = '/home/sruthi/dev/scikit-workspace/sklearn_tut_workspace/uploads/'.$newname;
	move_uploaded_file( $_FILES['fileToUpload']['tmp_name'], $target);
	/*$text=file_get_contents($_FILES['fileToUpload']['tmp_name']);
	//echo $text;
	/*$text=$_POST["text"];
	$filename="/home/sruthi/dev/UIMA-NLP-Platform/MyWorkspace/data/text_files/Apache_UIMA.pdf";
	$myfile=fopen($filename,"w")or die("Unable to open file!");x
	//echo fread($myfile,filesize($filename));
	//echo "ok";
	fclose($myfile);*/
	 
	$exec='cd /home/sruthi/dev/scikit-workspace/sklearn_tut_workspace && python categorize_rev_user.py';
	$op=shell_exec($exec);
	#echo $op;
	$_SESSION['upload']=$target;
	echo "<div id='div4'><br><br><a id='sub' href=\"javascript:history.go(-1)\">GO BACK</a><br>";
	echo "<p id='p2'>Process complete</p><br>";
	echo "<form id='form1' method='POST' action='../php/displayResults.php'>";
	echo "<input id='sub' type='submit' value='click to view results'></form></div>";
	
?>

</body>
</html> 