from pprint import pprint
import random
from operator import itemgetter
paircount = 0
samenumberpair = 0#연속되는 숫자의 종류
samepair = 0#연속되는 숫자의 수
straightox = False
semiroyal = False
justraight = 0
justraightox = False
flushox = False
twopair = False
triple = False
fullhouse = False
fourcards = False   
cards_A = 0
user1 = []
user2 = []
user3 = []
user4 = [] 
shared_cards = []
player_order = 1#플레이어 베팅 차례
rotate = 0 #플레이어 베팅의 총 순서
action_state = 0#체크콜벳중 하나
other_action = 0
sequence = 0

bet_cost = 500
bet_state = False

total_money = 0

player = [user1,user2,user3,user4]
player_fold = [False,False,False,False]
player_pair_list = []
pair_list = []

players_cards = player

player_money = [1000000,1000000,1000000,1000000]


winner = []


def Making_Card_Sets():
    global deck,shared_cards
    shared_cards = []
    deck = []
    deck.clear()
    deck = [[suit, k] for suit in ["♠", "♣", "♥", "◈"] for k in range(1,14)]
    random.shuffle(deck)


def Pre_flop():
    global player,deck,user1,user2,user3,user4,player,shared_cards    
    shared_cards = []
    for i in range(0,len(player)):
        player[i] = []
        player[i] = [deck[k] for k in range(0,2)]
        [deck.remove(player[i][j]) for j in range(0,2)]


def Flop():
    global shared_cards,deck
    shared_cards = []
    shared_cards = [deck[k] for k in range(0,3)]
    [deck.remove(shared_cards[j]) for j in range(0,3)]
    print("\nFlop\n")
    print("현재 공용패")
    print(shared_cards)
    print("현재 나의 패")
    print(player[0])
    print("\n")
    Action()


def Shared_cards():
    global shared_cards,deck,sequence,appendedcards
    appendedcards = [deck[k] for k in range(0,1)]
    shared_cards.append(appendedcards[0])    
    deck.remove(appendedcards[0])
    appendedcards = []
    if sequence == 2:
        print("\n턴\n")
    elif sequence == 3:
        print("\n리버\n")
    print("현재 공용패")
    print(shared_cards)
    print("현재 나의 패")
    print(player[0])
    print("\n")
    Action()


def Calc_cards(n):
    global player_pair_list,pair_list,num,player,samepair,samenumberpair,paircount,justraight,justraightox,semiroyal,flushox,samepair,twopair,triple,fullhouse,fourcards,shared_cards
    #카드패 합치기
    player[n] += shared_cards
    #initial
    paircount = 0
    samenumberpair = 0#연속되는 숫자의 종류
    samepair = 0#연속되는 숫자의 수
    pair_list = []
    straightox = False
    semiroyal = False
    justraight = 0
    justraightox = False
    flushox = False
    twopair = False
    triple = False
    fullhouse = False
    fourcards = False
    length = len(player[n])

    for n1 in range(0,length - 1):#Pair Counting
        for n2 in range(n1+1,length):#카드리스트중 검색 
            if player[n][n1][1] == player[n][n2][1]:

                if samenumberpair is not player[n][n1][1]:
                    paircount = paircount+1
                    samepair += 1
                    samenumberpair = player[n][n1][1]
                    pair_list.append(player[n][n1][1])

                elif samenumberpair == player[n][n1][1]:
                    paircount = paircount+1
    
    player_pair_list.append(list(str(n+1))+pair_list)

    num = [player[n][k][1] for k in range(length)] #Sort For Straight Counting
    num.sort()
    print(num)
    #print(num)
    num = list(set(num))
    length = len(num)

    if len(num) >= 5: #StraightCounting
        for s1 in range(0,length-4):
            
            if num[0] == 1 and num[4] ==5:#첫장이 1 5번째장이 5
                #for i in range(0,5):
                #    num[i] = i+1
                #    justraight += 1
                #if justraight == 5:
                justraightox = True##백스트레이트

            elif num[s1+4] - num[s1] == 4:
                straightox = True ##스트레이트 1+n~5+n 5 - 1 = 4 
            


            elif num[0] == 1 and num[length-4] == 10 and num[length-1] == 13:
                semiroyal = True ##마운틴 Ace and 10,j,q,k

    
    length = len(player[n])
    suit = [player[n][k][0] for k in range(length)] #Sort For Flush Counting
    suit.sort()
    print(suit)

    flushox = False
    if len(suit) >= 5:
        for f1 in range(0,len(suit)-4): #FlushCounting
            if suit[f1+len(suit)-3] == suit[f1]:
                flushox = True

    if paircount == 3 and samepair == 3:
        twopair= True
    if paircount == 2 and samepair == 2: #PairClassCounting
        twopair = True
    if paircount == 3:
        if samepair == 3:
            twopair = True
        if samepair == 1: 
            triple = True
    if paircount == 4:
        if samepair == 2:
            fullhouse = True
        if samepair ==1:
            fourcards = True
    Game_result(n)


def Game_result(n): #Class Counting
    global winner,semiroyal,flushox,straightox,justraightox,fourcards,fullhouse,triple,twopair,paircount
    #if semiroyal and flushox:
    #    rank_A = 1
    #    print("\n플레이어",n+1,"로열스트레이트플러시")
    #elif (straightox or justraightox) and flushox:
    #    rank_A = 2
    #    print("\n플레이어",n+1,"스트레이트 플러시")
    if fourcards:
        rank_A = 1
        print("\n플레이어",n+1,"포카드")
    elif fullhouse:
        rank_A = 2
        print("\n플레이어",n+1,"풀하우스")
    elif flushox:
        rank_A = 3
        print("\n플레이어",n+1,"플러시")
    elif semiroyal:
        rank_A = 4
        print("\n플레이어",n+1,"마운틴")
    elif justraightox:
        rank_A = 5
        print("\n플레이어",n+1,"백스트레이트 플러시")
    elif straightox:
        rank_A = 6
        print("\n플레이어",n+1,"스트레이트플러시")
    elif triple:
        rank_A = 7
        print("\n플레이어",n+1,"트리플")
    elif twopair:
        rank_A = 8
        print("\n플레이어",n+1,"투페어")
    elif paircount == 1:
        rank_A = 9
        print("\n플레이어",n+1,"원페어")
    else:
        rank_A = 10
        print("\n플레이어",n+1,"노페어")
    print("\n플레이어",n+1," 랭크 ",rank_A,"\n")
    winner.append([n+1,rank_A])
    if len(winner) >= 4: #결과비교로 넘어감
        if player_fold[0] == True:
            winner[0].clear()
        if player_fold[1] == True:
            winner[1].clear()
        if player_fold[2] == True:
            winner[2].clear()
        if player_fold[3] == True:
            winner[3].clear()

        if winner.count([]) >= 1:
            for i in range(0,winner.count([])):
                winner.remove([])
        Who_is_winner()
    else:
        pass


def Who_is_winner():
    global comparison,total_money,player_money,player_order,player_fold
    ##print(player_pair_list)
    comparison = []
    winner.sort(key=itemgetter(1))
    pprint(players_cards)
    if len(winner) >= 2:
        if winner[0][1]==winner[1][1]:
            if winner[0][1] >=7 and winner[0][1] != 10:
                comparison.append([winner[0][0],player_pair_list[winner[0][0]-1][1]])
                comparison.append([winner[1][0],player_pair_list[winner[1][0]-1][1]])
                comparison.sort(key=itemgetter(1))
                if comparison[0][1] == comparison[1][1]:
                    print("비겼습니다case 1")
                    winner.clear()
                    #player_order = int(comparison[0][0])
                    ##Game_start()
                else:
                    print(comparison[0][0],"번 플레이어 우승cas2")
                    player_money[comparison[0][0]-1]+=total_money
                    print(total_money,"는 ",winner[0][0],"의 주머니로")
                    total_money = 0
                    player_order = int(comparison[0][0])
                    winner.clear()
                    player_fold = [False,False,False,False]
            else:
                print("비겼습니다case3")
                winner.clear()
                #player_order = player_order - 1
                ##Game_start()
        else:
            print(winner[0][0],"번 플레이어 우승cas4")
            player_money[winner[0][0]-1]+=total_money
            print(total_money,"는 ",winner[0][0],"의 주머니로")
            total_money = 0
            player_order = int(winner[0][0])
            winner.clear()
            player_fold = [False,False,False,False]

    elif len(winner) == 1:
        print(winner[0][0],"번 플레이어 우승case5")
        player_money[winner[0][0]-1]+=total_money
        print(total_money,"는 ",winner[0][0],"의 주머니로")
        player_order = int(winner[0][0])
        winner.clear()
        player_fold = [False,False,False,False]
        total_money = 0

    for i in range(0,4):
        print(player_money[i])
    for i in range(0,4):
        players_cards[i]= []


    answer = input("다시 게임을 시작하시겠습니까?\n\n 1.예 2.아니오 3.디버그")
    if answer == "1":
        Game_start()
    elif answer == "3":
        Debug_mode()
    else:
        pass




def Game_start():
    global total_money,shared_cards,player,deck,user1,user2,user3,user4,player_money,bet_cost,player_order
    player_pair_list.clear()
    Small_blind()


def Small_blind():
    global total_money,shared_cards,player,deck,user1,user2,user3,user4,player_money,bet_cost,player_order
    print(player_order)
    bet_cost = 500
    if player_order == 5:
        player_order = 1  
        Small_blind()

    elif player_order <= 4:
        if player_fold[player_order-1] == False:
            if player_money[player_order-1] > bet_cost:
                print(player_order,"번 플레이어 스몰 블라인드")
                player_money[player_order-1] -= bet_cost ##돈 감소
                total_money+=bet_cost
                player_order += 1 ## 순서 증가
                bet_cost += bet_cost
                Big_blind()
            else:
                Fold_Action()
                Small_blind()
        elif player_fold[player_order-1] == True:
            player_order +=1
            Small_blind()


def Big_blind():
    global total_money,shared_cards,player,deck,user1,user2,user3,user4,player_money,bet_cost,player_order
    print(player_order)
    if player_order == 5:
        player_order = 1
        Big_blind()


    elif player_order <= 4:
        if player_fold[player_order-1] == False:
            if player_money[player_order-1] > bet_cost:
                print(player_order,"번 플레이어 빅 블라인드")
                player_money[player_order-1] -= bet_cost    
                total_money+=bet_cost
                player_order += 1
                Main_game()
            else:
                Fold_Action()
                Big_blind()
        elif player_fold[player_order-1] == True:
            player_order +=1
            print("플레이어 레인지 아웃")
            Big_blind()


def Main_game():
    global rotate,bet_state,total_money,shared_cards,player,deck,user1,user2,user3,user4,player_money,bet_cost,player_order
    print("카드를 셔플합니다")
    Making_Card_Sets()
    print("\n프리 플랍\n")
    Pre_flop()
    print("\n현재 판돈 : ", total_money)
    print("\n\n현재 나의 패\n")
    print(player[0])
    print("\n액션을 시작합니다\n")
    bet_state = False
    rotate = 0
    Action()


def Action():
    global sequence,total_money,player_money, rotate, action_state, bet_cost, player_order,player_fold,bet_state,other_action,sequence
    other_action = 0
    if player_order <= 4:
        print("\n",player_order,"플레이어 차례\n")

    if player_fold.count(False) == 1:        
        sequence = 0
        for i in range(0,4):
            Calc_cards(i)

    elif rotate != 4:
        if player_order == 5:
            player_order = 1
            Action()

        elif player_order <= 4 and player_fold[player_order-1] == False: ##플레이어가 폴드 하지 않음

            
            if player_order == 1:
                print("\n벳 상태",bet_state)
                print("\n벳 머니 : ",bet_cost)
                print("\n현재 소지금 : ",player_money[0])
                if bet_state == False:
                    print("\n1.체크 2.콜 3.벳 4.폴드\n")
                elif bet_state == True:
                    print("\n2.콜 3.레이즈 4.폴드\n")


                answer = input("")
                if answer == "1":
                    if bet_state == False:
                        print("1번 플레이어 체크")
                        player_order += 1
                        rotate += 1
                        Action()
                    elif bet_state == True:
                        print("베팅 금액이 올라가있습니다.")
                        Action()
                elif answer == "2":
                    if  bet_state == True:
                        if player_money[player_order-1] >= bet_cost:#콜
                            player_money[player_order-1] -= bet_cost
                            total_money += bet_cost
                            print(player_order,"번 플레이어 콜 : ",bet_cost)
                            player_order += 1
                            action_state = 3
                            rotate += 1
                            print("\n현재 판돈 : ", total_money)
                            Action()
                        elif player_money[player_order-1] < bet_cost and sequence >= 1 and player_money[player_order-1] >= 0 :
                            bet_cost = bet_cost + player_money[player_order-1]
                            total_money += player_money[player_order-1]
                            player_money[player_order-1] = 0
                            print(player_order, "번 올인 : ",bet_cost)
                            rotate += 1
                            action_state = 7            
                            bet_state = True   #벳 카운트 
                            player_order += 1 #다음차례
                            Action()
                        else:
                            Action()
                    else:
                        print("베팅된 금액이 없습니다.")
                        Action()
                elif answer == "3":
                    if player_money[player_order-1] > bet_cost:#벳을 함 벳~최대금액
                        max_cost = player_money[player_order-1] - bet_cost
                        print("베팅 가능 금액 : ",max_cost)

                        how_much = input("")
                        how_much = int(how_much)
                        if how_much > max_cost:
                            print(" 베팅 가능 금액 : ",max_cost)
                            Action()
                        elif how_much <= max_cost:
                            bet_cost += how_much
                            player_money[player_order-1] -= bet_cost #판돈만큼을 뺌
                            total_money += bet_cost
                            if bet_state == False:
                                print("1번 플레이어 벳")            
                            elif bet_state ==True:
                                print("2번 플레이어 레이즈")
                            
                            bet_state = True   #벳 카운트
                            player_order += 1
                            rotate += 1
                            Action()
                elif answer == "4":
                    print("1번 플레이어 폴드")                    
                    Fold_Action()
                    player_order += 1
                    rotate += 1
                    Action()
                elif answer == "k":
                    pass
                else:
                    Action()



            elif player_order <= 4:# and player_order != 0: ##다른 플레이어들
                other_action = random.randrange(1,30)
                #print(other_action,"랜덤 변수")

                if other_action <= 10:
                    if bet_state == False:#체크를 함
                        print(player_order,"번 플레이어 체크")
                        player_order += 1#다음 차례
                        action_state = 1
                        rotate += 1
                        print("\n현재 판돈 : ", total_money)
                        Action()
                    elif bet_state == True:#벳이 나와 쳌을 못함
                        Action()


                elif 10 < other_action <= 15:
                    if player_money[player_order-1] > bet_cost:#벳을 함 벳~최대금액
                        bet_cost = bet_cost + random.randrange(0,player_money[player_order-1]-bet_cost)
                        player_money[player_order-1] -= bet_cost #판돈만큼을 뺌
                        total_money += bet_cost
                        if bet_state == False:
                            print(player_order, "번 벳 : ",bet_cost)
                        elif bet_state == True:
                            print(player_order, "번 플레이어 레이즈 : ",bet_cost)
                        rotate += 1
                        action_state = 2            
                        bet_state = True   #벳 카운트 
                        player_order += 1 #다음차례
                        print("\n현재 판돈 : ", total_money)
                        Action()
                    
                    else:
                        Action()                        
                    

                elif other_action == 29:#폴드
                    print(player_order,"번 플레이어 폴드")
                    print("\n현재 판돈 : ", total_money)
                    Fold_Action()
                    player_order +=1
                    rotate += 1
                    Action()

                elif other_action <= 29:#콜
                    if  bet_state == True:
                        if player_money[player_order-1] >= bet_cost:#콜
                            player_money[player_order-1] -= bet_cost
                            total_money += bet_cost
                            print(player_order,"번 플레이어 콜 : ",bet_cost)
                            player_order += 1
                            action_state = 3
                            rotate += 1
                            print("\n현재 판돈 : ", total_money)
                            Action()
                        elif player_money[player_order-1] < bet_cost and player_money[player_order-1] >= 0 :
                            bet_cost = bet_cost + player_money[player_order-1]
                            total_money += player_money[player_order-1]
                            player_money[player_order-1] = 0
                            print(player_order, "번 올인 : ",bet_cost)
                            rotate += 1
                            action_state = 7            
                            bet_state = True   #벳 카운트 
                            player_order += 1 #다음차례
                            Action()
                        else:
                            Action()
                    else:
                        #pass
                        Action()


            
        else:
            action_state = 1
            player_order += 1
            rotate += 1
            Action()

    elif rotate == 4:##모든 벳이 끝남
        action_state = 0
        bet_state = False
        rotate = 0
        sequence += 1
        Sequence()
        if player_order == 5:
            player_order = 1


def Sequence():
    global sequence
    if sequence == 1:
        Flop()
    elif 2 <= sequence <= 3:
        Shared_cards()
    else:
        sequence = 0
        for i in range(0,4):
            Calc_cards(i)
            
def Fold_Action():
    global player_fold,player_order
    player_fold[player_order-1] = True
    

def Debug_mode():
    print("\n1.플레이어 머니 증가 2.게임 시작\n")
    answer = input("")
    if answer == "1":
        print("\n돈을 줄 플레이어를 선택\n")
        answer_player = input("")
        answer_player = int(answer_player)
        print("\n 할당할 금액을 선택")
        how_much_to_player = input("")
        how_much_to_player = int(how_much_to_player)
        player_money[answer_player-1] += how_much_to_player
        print(player_money)
        Debug_mode()
    else:
        Game_start()



##체크 콜 벳 레이즈 폴드


Game_start()
    
















