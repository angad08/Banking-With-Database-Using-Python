def Modulus_no(m,n):
	mod=((m/n)-(int)(m/n))*n
	return mod;
def Round_Off(n):
	point=n-(int)(n)
	if(point>=0.5):
		n=(int)(n+1)
	else:
		n=(int)(n)
	return n;
def Count_No(m):
	count=0;
	while(m>0):
		m=m//10;
		count+=1
	return count;
def Max_Equal_Min(c,size):
	min=c[0];
	max=c[0];
	eq=c[0];
	eql=[];
	eql_loc=[];
	eqnt=0;
	max_loc=0;
	min_loc=0;
	for i in range(1,size):
		if(c[i]<min):
			min=c[i];
			min_loc=i+1;
		elif(c[i]>max):
			max=c[i];
			max_loc=i+1;
	for i in range(size):
		for j in range((i+1),size):
			if(c[i]==c[j]):
				eqnt=eqnt+1;
				eql.append(c[j])
				eql_loc.append(j)
				break;
	if(min_loc!=0):
		print("Smallest No Is %d at Index %d"%(min,min_loc));
	else:
		print("Smallest No Is %d at Index %d"%(min,(min_loc+1)));
	if(max_loc==0):
		print("Max No Is %d at Index %d"%(max,(max_loc+1)));
	else:
		print("Max No Is %d at Index %d"%(max,max_loc));
	print("No Of Equals %d"%(eqnt))
	print("Equal Nos:-")
	for i in range(len(eql)):
		print("%d At index %d"%(eql[i],(eql_loc[i]+1)))
def Decimal_Chckpt(n):
	checkersum=n-(int)(n);
	if(checkersum!=0.0):
		return n;
	else:
		return (int)(n);
def Deci_Pts(m,n):
	m=(int)(m*pow(10,n))/(pow(10,n))
	if(Decimal_Chckpt(m)==int(m)):
		return (int)(m);
	else:
		return m;
def Rounded_Deci_Pts(m,n):
	m=Round_Off(m*pow(10,n))/(pow(10,n))
	if(Decimal_Chckpt(m)==int(m)):
		return (int)(m);
	else:
		return m;
def Reverse_No(m):
	rev=0;
	while(m!=0):
		rem=Modulus_no(m,10)
		rev=(rev*10)+rem;
		m=m//10
	return Round_Off(rev)
if __name__=="__main__":
	Modulus_no(m,n);
	Reverse_No(m);
	Count_No(m);
	Max_Equal_Min(c,size);
	Round_Off(n);
	Rounded_Deci_Pts(m,n);
	Deci_Pts(m,n);
	Decimal_Chckpt(n);