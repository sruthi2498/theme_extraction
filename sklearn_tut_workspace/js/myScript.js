function whenLoading() {
	//alert("here");
   var div=document.getElementById("div3");
   div.style.display = "none";
   var d=document.getElementById("div2");
	d.style.display = "block"; 
}

function FormSubmitted() {
	var d=document.getElementById("div2");
	d.style.display = "none"; 
	var div=document.getElementById("div3");
	div.style.display = "block";
	//div.innerHTML="Processing...";
	var t=document.createTextNode("Processing...");

	//p.appendChild(t);
	div.appendChild(t);

}

function DrawPieChart(ListOfCat,ListOfVal){
	var myData = new Array([ListOfCat[0],ListOfVal[0]],[ListOfCat[1],ListOfVal[1]],[ListOfCat[2],ListOfVal[2]],[ListOfCat[3],ListOfVal[3]]);
	var colors = ['#FACC00', '#FB9900', '#FB6600', '#FB4800'];
	var myChart = new JSChart('chartid', 'pie');
	myChart.setDataArray(myData);
	myChart.colorizePie(colors);
	myChart.setTitleColor('#857D7D');
	myChart.setPieUnitsColor('#9B9B9B');
	myChart.setPieValuesColor('#6A0000');
	myChart.draw();
}