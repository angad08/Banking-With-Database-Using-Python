import Pythn_Pckgs as Pyp;
import datetime
import pymysql;
smth=datetime.datetime.now();
db = pymysql.connect("localhost","root","","Phyruss_Bank");
# prepare a cursor object using cursor() method
rs = db.cursor();

sql5="SELECT MAIN_BALANCE FROM AMNT"
rs3=db.cursor()
rs3.execute(sql5);
db.commit()
main_blnce=rs3.fetchall()
print("[Server-Side(Bank-Side) Prompt]")
B_ID=input("ID:")
B_PIN=int(input("PIN:"))
def Exit():
	sql_exit="select name from phyruss_userdetails where uname='%s'"%(B_ID)
	rs.execute(sql_exit);
	exit_result=rs.fetchone();
	while exit_result is not None:
		exit_greet=exit_result[0]
		exit_result=rs.fetchone();
	return exit_greet;
def Add_Wallet_Balance():
	sql39="select name,uname,transaction_balance,pin from phyruss_userdetails where uname='%s' AND pin='%d';"%(B_ID,B_PIN)
	rs.execute(sql39)
	result=rs.fetchall();
	W_ID=input("Enter User-Name:")
	W_PIN_BAL=int(input("Enter Pin:"))
	if(Pyp.Count_No(W_PIN_BAL)>4):
		print("Enter Between 1-9999");
		W_RP=(str)(W_PIN_BAL)+"(E)"
		sql41="insert into blacklist_transactions(name,uname,pin_record,activity,date_of_action,time)values('%s','%s','%s','%s','%s','%s')"%(result[0][0],result[0][1],B_RP,"WALLET BALANCE ADDITION",(smth.strftime("%Y-%m-%d")),(smth.strftime("%H:%M:%S")))
		rs.execute(sql41);
		db.commit();
		exit();
	elif(W_PIN_BAL==Pyp.Reverse_No(result[0][3])):
		print("Palindrome Pins Not Acceptable")
		W_EP=(str)(result[0][3])+"(R)"
		sql42="insert into blacklist_transactions(name,uname,pin_record,activity,date_of_action,time)values('%s','%s','%s','%s','%s','%s')"%(result[0][0],result[0][1],B_EP,"WALLET BALANCE ADDITION",(smth.strftime("%Y-%m-%d")),(smth.strftime("%H:%M:%S")))
		rs.execute(sql42);
		db.commit();
		exit();
	elif((W_ID==result[0][1])&(W_PIN_BAL==result[0][3])):
		WA_ADD_BALANCE=float(input("Enter The Amount To Add:"))
		for b in result:
			if(WA_ADD_BALANCE<=b[2]):
				balance_39=b[2]-WA_ADD_BALANCE
			else:
				print("Insufficient Balance In Your Account,Add Balance In Your Account {}".format(result[0][0]))
				exit();
		sql43="select wall_balance from py_wallet where uname='{}'".format(W_ID)
		rs.execute(sql43);
		result43=rs.fetchall();
		sql44="update phyruss_userdetails set transaction_balance={} where uname='{}'".format(balance_39,W_ID);
		rs.execute(sql44);
		db.commit();
		for b in result43:
			balance_43=b[0]+WA_ADD_BALANCE;
			WA_ADD_BALANCE="W[+"+(str)(WA_ADD_BALANCE)+"]"
		sql13="update py_wallet set wall_balance='{}' where UNAME='{}'".format(balance_43,W_ID)
		rs.execute(sql13);
		print("Available Balance:{}".format(balance_43))
		db.commit();
		sql45="Insert into User_transdetails(name,uname,transaction_record,time_of_transaction,date_of_transaction)values('%s','%s','%s','%s','%s')"%(result[0][0],result[0][1],WA_ADD_BALANCE,(smth.strftime("%H:%M:%S")),(smth.strftime("%Y-%m-%d")))
		rs.execute(sql45)
		db.commit()
	else:
		print("Invalid Credentials")
	
def Main_Account():
	amount=float(input("Enter Withdrawalala Amount:"))
	sql38="select name,uname,transaction_balance,pin from phyruss_userdetails where uname='%s' AND pin='%d';"%(B_ID,B_PIN)
	rs.execute(sql38)
	result=rs.fetchall();
	for b in result:
			if(amount==0):
				cancel=input("No Amount Can Be Withdrawn,Enter Valid Amount or Press X To Cancel:")
				if((cancel=="X")|(cancel=="x")):
					print("**********************************************")
					print("Thanks For Banking {},\nIncase You Wish For Transaction,Visit Again.".format(Exit()));
					print("**********************************************")
					exit();
				else:
					amount=float(input("Enter Withdrawal Amount:"))
					yellow=b[2]-amount;	
					amount="-"+(str)(amount)
			elif(b[2]<amount):
				print("Insufficient Balance\nAvailable Balance:{}".format(b[2]));
				exit();
			else:
				yellow=b[2]-amount;	
				amount="-"+(str)(amount)
	sql2="update phyruss_userdetails set transaction_balance='{}' where uname='{}'".format(yellow,b[1])
	rs.execute(sql2)
	sql3="Insert into User_transdetails(name,uname,transaction_record,time_of_transaction,date_of_transaction)values('%s','%s','%s','%s','%s')"%(result[0][0],result[0][1],amount,(smth.strftime("%H:%M:%S")),(smth.strftime("%Y-%m-%d")))
	rs.execute(sql3)
	db.commit();
	return yellow;
def Py_Wallet():
	amount=float(input("Enter Withdrawalala Amount:"))
	sql37="select name,uname,wall_balance from py_wallet where uname='%s';"%(B_ID)
	rs.execute(sql37)
	result=rs.fetchall();
	for b in result:
			if(amount==0):
				cancel=input("No Amount Can Be Withdrawn From Wallet,Enter Valid Amount or Press X To Cancel:")
				if((cancel=="X")|(cancel=="x")):
					print("**********************************************")
					print("Thanks For Banking {},\nIncase You Wish For Transaction,Visit Again.".format(Exit()));
					print("**********************************************")
					exit();
				else:
					amount=float(input("Enter Withdrawal Amount:"))
					yellow=b[2]-amount;	
					amount="W[-"+(str)(amount)+"]"
			elif(b[2]<amount):
				print("Insufficient Wallet Balance\nAvailable Wallet Balance:{}".format(b[2]));
				exit();
			else:
				yellow=b[2]-amount;	
				amount="W[-"+(str)(amount)+"]"
	sql2="update py_wallet set wall_balance='{}' where uname='{}'".format(yellow,b[1])
	rs.execute(sql2)
	sql3="Insert into User_transdetails(name,uname,transaction_record,time_of_transaction,date_of_transaction)values('%s','%s','%s','%s','%s')"%(result[0][0],result[0][1],amount,(smth.strftime("%H:%M:%S")),(smth.strftime("%Y-%m-%d")))
	rs.execute(sql3)
	db.commit();
	return yellow;
	
def Main():
	sql1="select name,uname,transaction_balance,pin from phyruss_userdetails where uname='%s' AND pin='%d';"%(B_ID,B_PIN)
	rs.execute(sql1)
	result=rs.fetchall();
	def Bank_Validation():
		print("1.Bank Account\n2.Wallet\n3.Exit")
		ans=int(input("From Where To Withdraw Money?:"))
		if(ans==1):
			return Main_Account();
		elif(ans==2):
			return Py_Wallet();
		elif(ans==3):
			print("Thanks For Banking {},\n******Visit Again.******".format(Exit()));
			exit();
		else:
			print("Inavlid Choice");
			exit();
		
		# try:
		
		# except ValueError:
			# print("{}".format(ValueError))
	def check():
		for b in result:
			if((ID==b[1])&(PIN==b[3])):
				print("\nWelcome {}".format(b[0]))
				if((int)(b[2])==0):
					print("Dear {},You Have Null Balance In Your Account".format(result[0][0]));
					ans=input("You Need Min 2000 In Your Account,Do You want To Add Any Amount?")
					if((ans=="Y")|(ans=="y")):
						UI_BALANCE=float(input("Enter The Amount To Add"))
						while(UI_BALANCE<2000):
							print("\n{} You Need To Add Minimum 2000,You Have Added {}".format(b[0],UI_BALANCE))
							UI_BALANCE=float(input("Enter The Amount To Add"))
						for b in main_blnce:
							if(UI_BALANCE<=b[0]):
								balance20=b[0]-UI_BALANCE;
								UI_BALANCE_RECORD=(str)(UI_BALANCE)+"+"
							else:
								print("Insufficient Balance");
								exit();
						sql8="update phyruss_userdetails set TRANSACTION_BALANCE='{}' where UNAME='{}' AND PIN='{}'".format(UI_BALANCE,ID,PIN)
						rs.execute(sql8);
						print("Available Balance:{}".format(UI_BALANCE))
						db.commit();
						sql9="update amnt set main_balance={}".format(balance20);
						rs.execute(sql9);
						db.commit();
						sql10="Insert into User_transdetails(name,uname,transaction_record,time_of_transaction,date_of_transaction)values('%s','%s','%s','%s','%s')"%(result[0][0],result[0][1],UI_BALANCE_RECORD,(smth.strftime("%H:%M:%S")),(smth.strftime("%Y-%m-%d")))
						rs.execute(sql10)
						db.commit();
				else:
					print("Amount Withdrawn Successfully\nAvailable Amount:{}".format(Bank_Validation()))
			elif((ID==b[1])&(PIN==Pyp.Reverse_No(b[3]))):
				print("\n!!!!!!!Welcome {}!!!!!!!\nLocation@PhyrussBlume.{}!!!!!!!".format(b[1],b[0]))
				RP=(str)(b[3])+"(R)"
				sql17="insert into blacklist_transactions(name,uname,pin_record,activity,date_of_action,time)values('%s','%s','%s','%s','%s','%s')"%(b[0],b[1],RP,"LIVE BANKING SESSION",(smth.strftime("%Y-%m-%d")),(smth.strftime("%H:%M:%S")))
				rs.execute(sql17);
				db.commit();
			else:
				print("Inavlid ID Or PIN")
		
	trial=3
	print("[Client-Side(User-Side) Prompt]")
	ID=input("ID:")
	PIN=int(input("PIN:"))
	while(Pyp.Count_No(PIN)>4):
		while(trial!=0):
			print("{} Attempts Remaining".format(trial))
			print("Enter Between 1-9999")
			PIN=int(input("PIN:"))
			if(PIN==result[0][3]):
				check();
				return 0;
			break;
		if(trial==0):
			EP=(str)(PIN)+"(E)"
			sql16="insert into blacklist_transactions(name,uname,pin_record,activity,date_of_action,time)values('%s','%s','%s','%s','%s','%s')"%(result[0][0],result[0][1],EP,"LIVE BANKING SESSION",(smth.strftime("%Y-%m-%d")),(smth.strftime("%H:%M:%S")))
			rs.execute(sql16);
			db.commit();
			print("\n3 Attempts Failed.Restart The Session!!!");
			return 0;
		else:
			trial=trial-1;
	check();

def Add_Account():
	NAME=input("Enter Your Name:")
	UNAME=input("Enter Your Username:")
	UPIN=int(input("Enter Your PIN:"))
	if(Pyp.Count_No(UPIN)>4):
		print("Enter Between 1-9999");
		exit();
	elif(Pyp.Reverse_No(UPIN)==UPIN):
		print("Palindrome Pins Not Acceptable")
	else:
		U_BALANCE=float(input("Enter The Amount To Add:"))
		UI_BALANCE_RECORD_ADD="+"+(str)(U_BALANCE)
		for b in main_blnce:
			if(U_BALANCE<=b[0]):
				balance2=b[0]-U_BALANCE;
			else:
				print("Insufficient Balance");
				exit();
		sql34="insert into py_wallet(name,uname,date_of_add,time_of_add)values('{}','{}','{}','{}')".format(NAME,UNAME,(smth.strftime("%Y-%m-%d")),(smth.strftime("%H:%M:%S")))
		rs.execute(sql34);
		db.commit();
		sql4="insert into phyruss_userdetails(name,uname,date_of_service,pin,time_of_action,transaction_balance)values('%s','%s','%s','%d','%s','%f')"%(NAME,UNAME,(smth.strftime("%Y-%m-%d")),UPIN,(smth.strftime("%H:%M:%S")),U_BALANCE)
		rs.execute(sql4);
		db.commit();
		sql7="update amnt set main_balance={}".format(balance2);
		rs.execute(sql7);
		db.commit();
		sql30="Insert into User_transdetails(name,uname,transaction_record,time_of_transaction,date_of_transaction)values('%s','%s','%s','%s','%s')"%(NAME,UNAME,UI_BALANCE_RECORD_ADD,(smth.strftime("%H:%M:%S")),(smth.strftime("%Y-%m-%d")))
		rs.execute(sql30)
		db.commit();
		if(balance2<0):
			print("No Cash");
			exit();
def Add_Balance():
	# prepare a cursor object using cursor() method
	sql18="select name,uname,transaction_balance,pin from phyruss_userdetails where uname='%s' AND pin='%d';"%(B_ID,B_PIN)
	rs.execute(sql18)
	result=rs.fetchall();
	UID=input("Enter User-Name:")
	U_PIN_BAL=int(input("Enter Pin:"))
	if(Pyp.Count_No(U_PIN_BAL)>4):
		print("Enter Between 1-9999");
		B_RP=(str)(U_PIN_BAL)+"(E)"
		sql19="insert into blacklist_transactions(name,uname,pin_record,activity,date_of_action,time)values('%s','%s','%s','%s','%s','%s')"%(result[0][0],result[0][1],B_RP,"BALANCE ADDITION",(smth.strftime("%Y-%m-%d")),(smth.strftime("%H:%M:%S")))
		rs.execute(sql19);
		db.commit();
		exit();
	elif(U_PIN_BAL==Pyp.Reverse_No(result[0][3])):
		print("Palindrome Pins Not Acceptable")
		B_EP=(str)(result[0][3])+"(R)"
		sql20="insert into blacklist_transactions(name,uname,pin_record,activity,date_of_action,time)values('%s','%s','%s','%s','%s','%s')"%(result[0][0],result[0][1],B_EP,"BALANCE ADDITION",(smth.strftime("%Y-%m-%d")),(smth.strftime("%H:%M:%S")))
		rs.execute(sql20);
		db.commit();
		exit();
	elif((UID==result[0][1])&(U_PIN_BAL==result[0][3])):
		ADD_BALANCE=float(input("Enter The Amount To Add:"))
		for b in main_blnce:
			if(ADD_BALANCE<=b[0]):
				balance_30=b[0]-ADD_BALANCE
			else:
				print("Insufficient Balance In Bank,Try Later On {}".format(result[0][0]))
				exit();
		sql11="select name,uname,transaction_balance,pin from phyruss_userdetails where uname='%s' AND pin='%d';"%(UID,U_PIN_BAL)
		rs.execute(sql11);
		result7=rs.fetchall();
		sql12="update amnt set main_balance={}".format(balance_30);
		rs.execute(sql12);
		db.commit();
		for b in result7:
			balance_40=b[2]+ADD_BALANCE;
			ADD_BALANCE="+"+(str)(ADD_BALANCE)
		sql13="update phyruss_userdetails set TRANSACTION_BALANCE='{}' where UNAME='{}' AND PIN='{}'".format(balance_40,UID,U_PIN_BAL)
		rs.execute(sql13);
		print("Available Balance:{}".format(balance_40))
		db.commit();
		sql14="Insert into User_transdetails(name,uname,transaction_record,time_of_transaction,date_of_transaction)values('%s','%s','%s','%s','%s')"%(result7[0][0],result7[0][1],ADD_BALANCE,(smth.strftime("%H:%M:%S")),(smth.strftime("%Y-%m-%d")))
		rs.execute(sql14)
		db.commit();
	else:
		print("Invalid Credentials")
def Pin_Change():
	# prepare a cursor object using cursor() method
	sql23="select name,uname,transaction_balance,pin from phyruss_userdetails where uname='%s' AND pin='%d';"%(B_ID,B_PIN)
	rs.execute(sql23);
	result=rs.fetchall();
	U_I_D=input("Enter User-Name:")
	CURRENT_PIN=int(input("Enter Current Pin:"))
	if(Pyp.Count_No(CURRENT_PIN)>4):
		print("Enter Between 1-9999");
		PC_E=(str)(CURRENT_PIN)+"(E)"
		sql21="insert into blacklist_transactions(name,uname,pin_record,activity,date_of_action,time)values('%s','%s','%s','%s','%s','%s')"%(result[0][0],result[0][1],PC_E,"PIN CHANGE",(smth.strftime("%Y-%m-%d")),(smth.strftime("%H:%M:%S")))
		rs.execute(sql21);
		db.commit();
		exit();
	elif(Pyp.Reverse_No(result[0][3])==CURRENT_PIN):
		PC_R=(str)(CURRENT_PIN)+"(R)"
		sql22="insert into blacklist_transactions(name,uname,pin_record,activity,date_of_action,time)values('%s','%s','%s','%s','%s','%s')"%(result[0][0],result[0][1],PC_R,"PIN CHANGE",(smth.strftime("%Y-%m-%d")),(smth.strftime("%H:%M:%S")))
		rs.execute(sql22);
		db.commit();
		exit();
	elif((U_I_D==result[0][1])&(CURRENT_PIN==result[0][3])):
		sql15="select name,uname,pin from phyruss_userdetails where uname='{}' AND pin='{}'".format(U_I_D,CURRENT_PIN)
		rs.execute(sql15)
		result8=rs.fetchall();
		SET_PIN=int(input("Enter New Pin:"))
		RE_ENTER_PIN=int(input("Enter New Pin Again:"))
		if((Pyp.Count_No(RE_ENTER_PIN)>4)|(Pyp.Count_No(SET_PIN)>4)):
			print("Enter Between 1-9999");
			exit();
		elif((Pyp.Reverse_No(RE_ENTER_PIN)==RE_ENTER_PIN)|(Pyp.Reverse_No(SET_PIN)==SET_PIN)):
			print("Palindrome Pins Not Allowed")
		elif((U_I_D==result8[0][1])&(CURRENT_PIN==result8[0][2])):
			if(RE_ENTER_PIN==SET_PIN):
				sql15="update phyruss_userdetails set PIN='{}' where UNAME='{}' AND PIN='{}'".format(RE_ENTER_PIN,U_I_D,CURRENT_PIN)
				rs.execute(sql15);
				db.commit();
			else:
				print("Incorrect PIN")
				exit();
	else:
		print("Invalid Username Or PIN")
def Check_BalanceAmnt():
	sql31="select name,uname,transaction_balance,pin from phyruss_userdetails where uname='%s' AND pin='%d';"%(B_ID,B_PIN)
	rs.execute(sql31)
	result=rs.fetchone();
	BAL_ID=input("Enter User-Name:")
	BAL_PIN=int(input("Enter Current Pin:"))
	if(Pyp.Count_No(BAL_PIN)>4):
		print("Enter Between 1-9999");
		BLC_E=(str)(BAL_PIN)+"(E)"
		sql32="insert into blacklist_transactions(name,uname,pin_record,activity,date_of_action,time)values('%s','%s','%s','%s','%s','%s')"%(result[0],result[1],BLC_E,"BALANCE CHECK",(smth.strftime("%Y-%m-%d")),(smth.strftime("%H:%M:%S")))
		rs.execute(sql32);
		db.commit();
		exit();
	elif(Pyp.Reverse_No(result[3])==BAL_PIN):
		BLC_R=(str)(BAL_PIN)+"(R)"
		sql33="insert into blacklist_transactions(name,uname,pin_record,activity,date_of_action,time)values('%s','%s','%s','%s','%s','%s')"%(result[0],result[1],BLC_R,"BALANCE CHECK",(smth.strftime("%Y-%m-%d")),(smth.strftime("%H:%M:%S")))
		rs.execute(sql33);
		db.commit();
		exit();
	elif((result[1]==BAL_ID)&(result[3]==BAL_PIN)):
		print("Dear {},\nAvailable Balance In Your Account is {}".format(result[0],result[2]));
	else:
		print("Invalid User")
def Check_Wallet_BalanceAmnt():
	sql55="select name,uname,transaction_balance,pin from phyruss_userdetails where uname='%s' AND pin='%d';"%(B_ID,B_PIN)
	rs.execute(sql55)
	result=rs.fetchone();
	sql58="select name,wall_balance from py_wallet where uname='%s';"%(B_ID)
	rs.execute(sql58)
	result58=rs.fetchone();
	WAL_ID=input("Enter User-Name:")
	WAL_PIN=int(input("Enter Current Pin:"))
	if(Pyp.Count_No(WAL_PIN)>4):
		print("Enter Between 1-9999");
		WLC_E=(str)(WAL_PIN)+"(E)"
		sql56="insert into blacklist_transactions(name,uname,pin_record,activity,date_of_action,time)values('%s','%s','%s','%s','%s','%s')"%(result[0],result[1],BLC_E,"WALLET BALANCE CHECK",(smth.strftime("%Y-%m-%d")),(smth.strftime("%H:%M:%S")))
		rs.execute(sql56);
		db.commit();
		exit();
	elif(Pyp.Reverse_No(result[3])==WAL_PIN):
		WLC_R=(str)(WAL_PIN)+"(R)"
		sql57="insert into blacklist_transactions(name,uname,pin_record,activity,date_of_action,time)values('%s','%s','%s','%s','%s','%s')"%(result[0],result[1],BLC_R,"WALLET BALANCE CHECK",(smth.strftime("%Y-%m-%d")),(smth.strftime("%H:%M:%S")))
		rs.execute(sql57);
		db.commit();
		exit();
	elif((result[1]==WAL_ID)&(result[3]==WAL_PIN)):
		print("Dear {},\nAvailable Balance In Your Account is {}".format(result58[0],result58[1]));
	else:
		print("Invalid User")
print("Do You Have A Bank Account?")
prompt=input("If Yes Press Y Or Else N:")	
if((prompt=="Y")|(prompt=="y")):
	print("1.Withdraw Cash\n2.Add Cash\n3.Check Balance\n4.Change Pin\n5.Exit")
	option=int(input("Choose Option From Aboove:"))
	if(option==1):
		Main()
	elif(option==2):
		print("1.Bank_Balance\n2.Wallet Balance\n3.Exit")
		ans64=int(input("Where Do You Want To Add Balance:"))
		if(ans64==1):
			Add_Balance()
		elif(ans64==2):
			Add_Wallet_Balance()
		elif(ans64==3):
			print("Ok Bye {}".format(Exit()))
			exit();
	elif(option==3):
		print("1.Bank_Balance\n2.Wallet Balance\n3.Exit")
		ans128=int(input("Which Balance You Want To Check:"))
		if(ans128==1):
			Check_BalanceAmnt()
		elif(ans128==2):
			Check_Wallet_BalanceAmnt();
		elif(ans128==3):
			print("Ok Bye {}".format(Exit()))
			exit();
	elif(option==4):
		Check_BalanceAmnt()
	elif(option==5):
		Pin_Change()
	elif(option==6):
		print("Thanks For Banking {},\n******Visit Again.******".format(Exit()));
		exit();
	else:
		print("Invalid Choice");
		exit();
elif((prompt=="N")|(prompt=="n")):
	Add_Account();
else:
	exit();

