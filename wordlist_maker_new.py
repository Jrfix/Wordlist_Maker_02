#! \usr\bin\env python
# -*- coding: UTF-8 -*-
import os
from os import system
from time import sleep
import time
import re

chars = []

choice = raw_input("1) all (aA1!)\n2) write (john,flipper,1998,a,b,...)")
if choice == 1:
	chars =["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e",
	"f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş",
	"t","u","ü","v","y","z","q","w","x","A","B","C","D","E","F",
	"G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S",
	"Ş","T","U","Ü","V","Y","Z","Q","W","X","!","_","-","#","$","%","&","£"]
else:
	os.system("clear")
	str_chars = raw_input("USAGES (char1,char2,char3,.....) || (char1 char2 char3 .....)\n\nchars : ")
	chars = re.split("\,|\ ",str_chars)  


digit = int(input("digit (max #11 digit): "))
file_path = raw_input("ex: /root/Desktop/tosavehere.txt ---> ")




start = time.time()




def main():
	
	if(digit == 0 or digit < 0):
		print("You can't type less than 0 or 0 ")
	else:
		
		sleep(1)
		system('clear')
		hane1()
	




dosya = open(file_path,"a")

def hane1():
	
	
	l_e = chars[-1] 
	g_e = l_e
	for oku in chars:
		harf1=oku
		toplam=harf1
		dosya.write(toplam+"\n")
		print("\033[91m"+toplam)
		if(digit > 1 and toplam == g_e):
			
			hane2()

def hane2():
	print("hane2")
	l_e = chars[-1] 
	g_e = l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2	
			toplam=harf1+harf2
			dosya.write(toplam+"\n")
			print("\033[91m"+toplam)
			if(digit > 2 and toplam == g_e):
				
				hane3()
			

def hane3():
	
	l_e = chars[-1] 
	g_e = l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3	
				toplam=harf1+harf2+harf3
				dosya.write(toplam+"\n")
				print("\033[91m"+toplam)
				if(digit > 3 and toplam == g_e):
					
					hane4()
				
				

def hane4():
	
	l_e = chars[-1] 
	g_e = l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4	
					toplam=harf1+harf2+harf3+harf4
					dosya.write(toplam+"\n")
					print("\033[91m"+toplam)
					if(digit > 4 and toplam == g_e):
						
						hane5()
					
					

def hane5():
	
	l_e = chars[-1] 
	g_e = l_e+l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4
					for oku5 in chars:
						harf5=oku5	
						toplam=harf1+harf2+harf3+harf4+harf5
						dosya.write(toplam+"\n")
						print("\033[91m"+toplam)
						if(digit > 5):
							
							hane6()
						
def hane6():
	
	l_e = chars[-1] 
	g_e = l_e+l_e+l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4
					for oku5 in chars:
						harf5=oku5
						for oku6 in chars:
							harf6=oku6	
							toplam=harf1+harf2+harf3+harf4+harf5+harf6
							dosya.write(toplam+"\n")
							print("\033[91m"+toplam)
							if(digit > 6):
								
								hane7()
							

def hane7():
	
	l_e = chars[-1] 
	g_e = l_e+l_e+l_e+l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4
					for oku5 in chars:
						harf5=oku5
						for oku6 in chars:
							harf6=oku6
							for oku7 in chars:
								harf7=oku7	
								toplam=harf1+harf2+harf3+harf4+harf5+harf6+harf7
								dosya.write(toplam+"\n")
								print("\033[91m"+toplam)
								if(digit > 7):
									
									hane8()
def hane8():
	
	l_e = chars[-1] 
	g_e = l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4
					for oku5 in chars:
						harf5=oku5
						for oku6 in chars:
							harf6=oku6
							for oku7 in chars:
								harf7=oku7	
								for oku8 in chars:
									harf8=oku8	
									toplam=harf1+harf2+harf3+harf4+harf5+harf6+harf7+harf8
									dosya.write(toplam+"\n")
									print("\033[91m"+toplam)
									if(digit > 8):
										
										hane9()
def hane9():
	
	l_e = chars[-1]
	g_e = l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4
					for oku5 in chars:
						harf5=oku5
						for oku6 in chars:
							harf6=oku6
							for oku7 in chars:
								harf7=oku7	
								for oku8 in chars:
									harf8=oku8	
									for oku9 in chars:
										harf9=oku9	
										toplam=harf1+harf2+harf3+harf4+harf5+harf6+harf7+harf8+harf9
										dosya.write(toplam+"\n")
										print("\033[91m"+toplam)
										if(digit > 9):
											
											hane10()
def hane10():
	
	l_e = chars[-1] 
	g_e = l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4
					for oku5 in chars:
						harf5=oku5
						for oku6 in chars:
							harf6=oku6
							for oku7 in chars:
								harf7=oku7	
								for oku8 in chars:
									harf8=oku8	
									for oku9 in chars:
										harf9=oku9
										for oku10 in chars:
											harf10=oku10	
											toplam=harf1+harf2+harf3+harf4+harf5+harf6+harf7+harf8+harf9+harf10
											dosya.write(toplam+"\n")
											print("\033[91m"+toplam)
											if(digit > 10):
												
												hane11()
def hane11():
	
	l_e = chars[-1] 
	g_e = l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e+l_e
	for oku in chars:
		harf1=oku
		for oku2 in chars:
			harf2=oku2
			for oku3 in chars:
				harf3=oku3
				for oku4 in chars:
					harf4=oku4
					for oku5 in chars:
						harf5=oku5
						for oku6 in chars:
							harf6=oku6
							for oku7 in chars:
								harf7=oku7	
								for oku8 in chars:
									harf8=oku8	
									for oku9 in chars:
										harf9=oku9
										for oku10 in chars:
											harf10=oku10
											for oku11 in chars:
												harf11=oku11	
												toplam=harf1+harf2+harf3+harf4+harf5+harf6+harf7+harf8+harf9+harf10+harf11
												dosya.write(toplam+"\n")
												print("\033[91m"+toplam)
												if(digit > 11):
													hane12()
main()
												








