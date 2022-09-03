#Importing all the libraries that are going to be used at the project
import PySimpleGUI as sg
import requests
import numpy as np
#Variables used in the program
numero=[]
cont,calc,oper,num=0,0,0,0
evento=[]
visor2=str('')
output3=sg.Text('_')
output2=sg.Text(visor2)
output=sg.Text(oper)
output4=sg.Text()
sg.theme('Reds')
sinal=''
n,j,pv,fv=0,0,0,0
per=sg.Text(n,font=('Any 5'))
jur=sg.Text(j,font=('Any 5'))
fut=sg.Text(fv,font=('Any 5'))
pre=sg.Text(pv,font=('Any 5'))
juros=False
layout=[[sg.Text('='), output],
			[sg.Text("                                                                                                                      ",font=('Any 5')),sg.Text("N :",font=('Any 5')), per] , 
			[sg.Text("                                                                                                                       ",font=('Any 5')),sg.Text("J :",font=('Any 5')),jur],
			[sg.Text("                                                                                                                     ",font=('Any 5')),sg.Text("PV:",font=('Any 5')),pre],
			 [sg.Text("                                                                                                                      ",font=('Any 5')),sg.Text("FV:",font=('Any 5')),fut ],
            [sg.Text(':>'),output2],
            [sg.Button('n  ', button_color =('white', 'black')),sg.Button('Sin ', button_color =('white', 'black')), sg.Button('C', button_color =('white', 'black')), sg.Button('7',button_color =('white', 'black')), sg.Button('8',button_color =('white', 'black')),sg.Button('9',button_color =('white', 'black')), sg.Button('÷', button_color =('white', 'black'))],
            [sg.Button('j   ', button_color =('white', 'black')),sg.Button('Cos', button_color =('white', 'black')),sg.Button('£',button_color =('white', 'black')), sg.Button('4',key='4',button_color =('white', 'black')), sg.Button('5',key='5',button_color =('white', 'black')), sg.Button('6',button_color =('white', 'black')),sg.Button('x',button_color =('white', 'black')) ],
            [sg.Button('pv', button_color =('white', 'black')),sg.Button('Tan',button_color =('white', 'black')), sg.Button('$',button_color =('white', 'black')), sg.Button('1',button_color =('white', 'black')), sg.Button('2',button_color =('white', 'black')), sg.Button('3',button_color =('white', 'black')),sg.Button(' -',button_color =('white', 'black')) ],
            [sg.Button('fv', button_color =('white', 'black')),sg.Button('Log',button_color =('white', 'black')),sg.Button('ENTER',button_color =('white', 'black'),size=(7,1)),sg.Button('0',button_color =('white', 'black')),sg.Button('. ',button_color =('white', 'black')),sg.Button('+',button_color =('white', 'black'))]]

# Create the window
window = sg.Window('CALCULADORA DO MARIO', layout, size=(520,400))  
def soma(y, x):
	y+=x
	return y
def mult(y, x):
	y*=x
	return y
def menos(y, x):
	y-=x
	return y
def div(y, x):
	y/=x
	return y

while True:
	event, values = window.read()
	oper=soma
	if event=='+':
		calc=soma(calc,float(visor2))
		output.update(value=calc)
		numero=[]
		visor2=0
		event=''
		output2.update(value=visor2)
	elif(event=='n  '):
		n=float(visor2)
		visor2=0
		output.update(value=n)
		output2.update(value=visor2)
		numero=[]
		per.update(value=n)
	elif(event=='j   '):
		j=float(visor2)
		visor2=0
		calc=0
		output.update(value=j)
		output2.update(value=visor2)
		numero=[]
		jur.update(value=j)
	elif(event=='pv'):
		pv=float(visor2)
		visor2=0
		output.update(value=pv)
		output2.update(value=visor2)
		numero=[]
		pre.update(value=pv)
	elif(event=='fv'):
		fv=float(visor2)
		visor2=0
		output.update(value=fv)
		output2.update(value=visor2)
		numero=[]
		fut.update(value=fv)
	elif event=='*':
		calc=mult(calc,float(visor2))
		output.update(value=calc)
		numero=[]
		visor2=0
		event=' '
		output2.update(value=visor2)	
	elif event== ' -':
		calc=menos(calc,float(visor2))
		output.update(value=calc)
		numero=[]
		visor2=0
		event=' '
		output2.update(value=visor2)
	elif event=='÷':
		if(float(visor2)!=0):
			calc=div(calc,float(visor2))
			output.update(value=calc)
			numero=[]
			visor2=0
			event=' '
			output2.update(value=visor2)
		else:
			visor2='Operação inválida'
			output.update(value=visor2)
	elif event=='x':
		calc=mult(calc,int(visor2))
		output.update(value=calc)
		numero=[]
		visor2=0
		event=' '
		output2.update(value=visor2)
	elif event=='g':
		arred=int(numero[0])
		visor2=float(visor2)
		output.update(value=visor2)
		numero=[]
		visor2=0
		output2.update(value=visor2)
	elif event=='C':
		cont+=1
		visor2=0
		output2.update(value=visor2)
		numero=[]
		if(cont==2):
			calc=0
			output.update(value=visor2)
			cont=0
		event=' '
	elif event=='$':
		requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
		cotacao = requisicao.json()
		dolar=dict(cotacao['USD'])
		cot=dolar['high']
		cambio=float(cot)*float(visor2)
		visor2=cambio
		output2.update(value=cambio)
		numero=[]
	elif event=='£':
		requisicao = requests.get('https://economia.awesomeapi.com.br/all/GBP-BRL')
		cotacao = requisicao.json()
		dolar=dict(cotacao['GBP'])
		cot=dolar['high']
		cambio=float(cot)*float(visor2)
		visor2=cambio
		output2.update(value=cambio)
		numero=[]
	elif event=='. ':
		numero.append('.')
		visor2=('').join(numero)
		output2.update(value=visor2)
	elif event=='Sin ':
		calc=np.sin(float(visor2))
		visor2=calc
		output2.update(value=visor2)
		numero=[]
	elif event=='Cos':
		calc=np.cos(float(visor2))
		visor2=calc
		numero=[]
		output2.update(value=visor2)
	elif event=='Tan':
		calc=np.tan(float(visor2))
		visor2=calc
		numero=[]
		output2.update(value=visor2)
	elif event=='Log':
		calc=np.log(float(visor2))
		visor2=calc
		numero=[]
		output2.update(value=visor2)
	elif event=='ENTER':
			if(j and n and fv) !=0:
				presente="R$: "+ str(round((fv)/(((100+j)/100)**n),2))
				output.update(value=presente)
				j,n,fv=0,0,0
				per.update(value='0')
				jur.update(value='0')
				fut.update(value='0')
				pre.update(value='0')
			elif(j and n and pv) !=0:
				futuro="R$: "+ str(round(pv*(((100+j)/100)**n),2))
				output.update(value=futuro)
				j,n,pv=0,0,0
				per.update(value='0')
				jur.update(value='0')
				fut.update(value='0')
				pre.update(value='0')
			elif(n and fv and pv) !=0:
				juros=(((fv**(1/n))*100)/pv)-100
				output.update(value=juros)
				n,pv,fv=0,0,0
				per.update(value='0')
				jur.update(value='0')
				fut.update(value='0')
				pre.update(value='0')
			elif(j and fv and pv) !=0:
				nper=np.log(fv/pv)/np.log(1+j/100)
				output.update(value=nper)
				j,pv,fv=0,0,0
				per.update(value='0')
				jur.update(value='0')
				fut.update(value='0')
				pre.update(value='0')
			else:
				calc=float(visor2)
				visor2=0
				output.update(value=calc)
				output2.update(value=visor2)
				numero=[]
				event=' '
	else:
		numero.append(event[-1])
		if numero[0]=='0' and len(numero)==1:
			numero.append('.')			
		visor2=('').join(numero)
		output2.update(value=visor2)
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		break