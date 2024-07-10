function showDay(a){
	if(a==1){  
	document.write("Sunday");  
	}  
	else if(a==2){  
	document.write("Monday");  
	}else if(a==3){  
	document.write("Tuesday");  
	}else if(a==4){  
	document.write("Wednesday");  
	}else if(a==5){  
	document.write("Thursday");  
	}else if(a==6){  
	document.write("Friday");  
	}else if(a==7){  
	document.write("Saturday");  
	}else{  
	document.write("invalid day");  
	}  
} 
function showMonth(m){
	switch(m){
		case 1:
			document.write("Baisakh");
			break;
		case 2:
			document.write("Jestha");
			break;
		case 3:
			document.write("Asadh");
			break;
		case 4:
			document.write("Shrawan");
			break;
		case 5:
			document.write("Bhadra");
			break;
		case 6:
			document.write("Asoj");
			break;
		case 7:
			document.write("Kartik");
			break;
		case m=8:
			document.write("Mangsir");
			break;
		case m=9:
			document.write("Paush");
			break;
		case m=10:
			document.write("Magh");
			break;
		case m=11:
			document.write("Falgun");
			break;
		case m=12:
			document.write("Chaitra");
			break;
		default:
			document.write("Invalid Month");
		

	}
} 

