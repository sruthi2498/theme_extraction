 <?php 
 session_start();
  extract ($_SESSION);
   ?>
 <!DOCTYPE html>
<html>
<head> <link rel="stylesheet" type="text/css" href="../css/stylesheet.css"></head>
<body>

		
		
		<?php
		

		echo "<div id='div7'><div id='div9'><a id='sub1' href=\"javascript:history.go(-1)\">GO BACK</a></div><br>";

			/*$filelist="/home/sruthi/dev/UIMA-NLP-Platform/MyWorkspace/data/text_files/op/list.txt";
			$myfile1=fopen($filelist,"r")or die("Unable to open file!");
			echo "The annotators are\n";
			echo "<br>";

			$count=1;
			while(!feof($myfile1)) {
				$an=trim(fgets($myfile1));
				//echo $an;
				if($an)echo "<input type='checkbox' id='b'".$count ." value=".$an." name=".$an."><br>";
				$count++;

			}
			fclose($myfile1);*/
			//echo $an;
			//if($an !="DocumentAnnotation"){
		//$an = str_replace(array("\r\n", "\r", "\n"), "<br />", $an);
		   //echo $an."<br>";
		    $fileop="/home/sruthi/dev/scikit-workspace/sklearn_tut_workspace/data/op.txt";
		   // echo "filename ".$fileop."<br>";
			$myfile2=fopen($fileop,"r")or die("Unable to open file!");

			$uploaded=$_SESSION['upload'];
			#echo $uploaded;
			$myfile3=fopen($uploaded,"r")or die("Unable to open file!");
			echo "<div id='container'><div id='each_rev'> <div id='actual_rev'>REVIEW</div><div id='res'>RESULT</div></div></div>	";

			echo "<div id='container'>";
			while(!feof($myfile2) && !feof($myfile3)) {
				$arr=fgets($myfile3);
				echo "<div id='each_rev'>";
				echo "<div id='actual_rev'>".$arr."</div>";
				$arr2=fgets($myfile2);
				$b=explode("/", $arr2);
				$n=sizeof($b);
				echo "<div id='res'>";
				for($i=0;$i<$n;$i++){
					#echo $b[$i];
					$a=explode("=>", $b[$i]);
					
					#echo $a[1];
					if(sizeof($a)==2){
						$a[0] =str_replace("\n", " ", $a[0]);
						echo $a[0]."=><span style='background-color:#33ffff'>".$a[1]."</span>";
					}
					
					
					echo "<br>";
				}
				echo "</div></div><br>";
			}
			echo "</div>";
			fclose($myfile2);

		//echo "ok";
		//}
		?>	

</table>
</div>
<br><br><br>
</div>	
</form>


</body>
</html> 