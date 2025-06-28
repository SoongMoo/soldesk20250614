startgop = int(input("시작곱 숫자를 입력하세요 : "))
endgop = int(input("마지막곱 숫자를 입력하세요 : "))
dan =  int(input("단 숫자를 입력하세요 : "))
while startgop <= endgop:
    print( "%d * %d = %d " % (dan, startgop , dan * startgop ))
    startgop = startgop + 1