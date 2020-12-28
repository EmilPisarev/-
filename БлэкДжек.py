импорт  ОС
 случайный импорт

колода  = [ 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 ] * 4

def  deal ( колода ):
    рука  = []
    для  i  в  диапазоне ( 2 ):
	    случайный . тасовать ( колода )
	    card  =  колода . поп ()
	    если  card  ==  11 : card  =  "J"
	    если  card  ==  12 : card  =  "Q"
	    если  card  ==  13 : card  =  "K"
	    если  card  ==  14 : card  =  "A"
	    рука . добавить ( карточка )
    ответная  рука

def  play_again ():
    again  =  input ( "Хотите сыграть ещё одну игру? (Д / Н):" ). нижний ()
    если  снова  ==  "д" :
	    дилер_hand  = []
	    player_hand  = []
	    колода  = [ 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 ] * 4
	    игра ()
    еще :
	    print ( "Пока!" )
	    выход ()

def  total ( рука ):
    всего  =  0
    для  карты  в  руке :
	    если  card  ==  "J"  или  card  ==  "Q"  или  card  ==  "K" :
	        итого + =  10
	    elif  card  ==  "A" :
	        если  всего  > =  11 : всего + =  1
	        иначе : всего + =  11
	    else : total  + =  card
     общая сумма возврата

def  hit ( рука ):
	card  =  колода . поп ()
	если  card  ==  11 : card  =  "J"
	если  card  ==  12 : card  =  "Q"
	если  card  ==  13 : card  =  "K"
	если  card  ==  14 : card  =  "A"
	рука . добавить ( карточка )
	ответная  рука

def  clear ():
	если  os . name  ==  'nt' :
		os . система ( 'CLS' )
	если  os . name  ==  'posix' :
		os . система ( 'ясно' )

def  print_results ( dil_hand , player_hand ):
	ясно ()
	print ( «У дилера»  +  str ( dilier_hand ) +  «в итоге»  +  str ( total ( diver_hand )))
	print ( "У тебя"  +  str ( player_hand ) +  "в итоге"  +  str ( total ( player_hand )))

def  блэкджек ( дилер_ханд , игрок_ханд ):
	если  total ( player_hand ) ==  21 :
		print_results ( игрок_хенд , игрок_ханд )
		print ( "Поздравляю! У вас Blackjack! \ n " )
		play_again ()
	elif  total ( diver_hand ) ==  21 :
		print_results ( игрок_хенд , игрок_ханд )		
		print ( "Простите, вы проиграли. У дилера Blackjack. \ n " )
		play_again ()

Защита  оценка ( dealer_hand , player_hand ):
	если  total ( player_hand ) ==  21 :
		print_results ( игрок_хенд , игрок_ханд )
		print ( "Поздравляю! У вас Blackjack! \ n " )
	elif  total ( diver_hand ) ==  21 :
		print_results ( игрок_хенд , игрок_ханд )		
		print ( "Простите, вы проиграли. У дилера Blackjack. \ n " )
	 Всего elif ( player_hand ) >  21 :
		print_results ( игрок_хенд , игрок_ханд )
		print ( "Прости. Ты попался и проиграл. \ n " )
	 Всего elif ( Dealer_hand ) >  21 :
		print_results ( игрок_хенд , игрок_ханд )			   
		print ( "Дилер попался. Ты победил! \ n " )
	elif  total ( player_hand ) <  total ( diver_hand ):
		print_results ( игрок_хенд , игрок_ханд )
        #print ("Извините. Ваш счет не выше, чем у дилера. Вы проиграли. \ n")
	elif  total ( player_hand ) >  total ( diver_hand ):
		print_results ( игрок_хенд , игрок_ханд )			   
		print ( "Поздравляю! Твой счёт выше, чем у дилера. Ты победил \ n " )		

def  game ():
	выбор  =  0
	ясно ()
	print ( "Добро пожаловать в игру Blackjack!! \ n " )
	diver_hand  =  сделка ( колода )
	player_hand  =  deal ( колода )
	при  выборе  ! =  "q" :
		print ( "Дилер показывает"  +  str ( diver_hand [ 0 ]))
		print ( "У тебя"  +  str ( player_hand ) +  "в итоге"  +  str ( total ( player_hand )))
		блэкджек ( дилер_ханд , игрок_хэнд )
		choice  =  input ( "Вы хотите [П] однять или [У] йти:" ). нижний ()
		ясно ()
		если  выбор  ==  "п" :
			удар ( player_hand )
			в то время как  сумма ( дилер_ханд ) <  17 :
				хит ( дилер_ханд )
			оценка ( игрока_хэнд , игрока_ханд )
			play_again ()
		elif  choice  ==  "у" :
			print ( "Пока!" )
			выход ()
	
если  __name__  ==  "__main__" :
    игра ()
