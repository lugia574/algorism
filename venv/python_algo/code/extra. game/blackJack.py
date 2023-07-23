# 1. 만들게 된 계시
# 알고리즘 푸는 것도 물리고
# 공부하기도 싫으니
# 재미있는 게임 만들기나 합시다
# 오늘 할 게임은 블랙잭을 만들어보자
# 블랙잭은 기본적으로
# 딜러와 참가자가 카드를 한장씩 받아 21에 가까운 수를 만드는 사람이 이기며 21을 초과하면 지는 게임

# 2. 디자인
# 어떻게 디자인을 할까
# 먼저 기본 자금 만원을 가지고 시작해서 그만두기를 했을때 얼마를 벌었냐 를 표시해주는 게 어떨까

# 3. 규칙
# 배당율은 건 금액만큼을 받는 게 기본 100원을 걸어 이기면 200원을 받고 지면 건 금액인 100원을 잃는다.
# K, Q, J는 10에 해당하며, A는 1 혹은 11 어느 쪽으로도 계산할 수 있다.
# 카드 두 장을 기본적으로 지급받게 되며 처음 받은 2장 합쳐 21이 나오는 경우 블랙잭
# 블랙잭의 경우 베팅액의 1.5배를 얻는다.
# 딜러가 블랙잭이라면 같은 블랙잭을 가진 사람 이외의 플레이어는 전부 패배하며 베팅액을 잃는다.
# 딜러와 참가자가 동시에 블랙잭인 경우에는 푸시(Push)라 하여 무승부 이 경우 베팅한 금액만 돌려받는다.

# 21이 되지 않았을 경우 원한다면 얼마든지 카드를 계속 뽑을 수 있다. 하지만 카드 숫자의 합이 21을 초과하게 되는 순간 '버스트'라고 하며 딜러의 결과에 관계없이 플레이어가 패배한다.
# 카드는 조커를 제외한 52장
# 숫자 카드인 2~9는 그 숫자대로 점수를 세고, K·Q·J,10은 10점으로 계산한다. A는 1점 또는 11점 둘 중의 하나로 계산
# 4. 게임 플레이
# - 1. 게임을 시작하기 전에 먼저 플레이어들은 카드를 받기 전에 걸고 싶은 액수의 돈을 건다
# - 2. 딜러는 플레이어들에게 각각 2장의 카드를 배부한다. 딜러도 2장의 카드를 받아, 1번째 카드를 비공개해 둔 것 이외에는 모든 참가자의 카드는 공개된다
# - 3. 참가자들은 블랙잭이 아닌 경우, 합계가 21점에 가까워지도록 하기 위해 딜러로부터 카드를 추가로 받을 수 있다.(힛(Hit)) 추가 카드는 합계가 21이 되거나,
#      초과하지 않는 한 제한없이 몇 장이라도 요구할 수 있다.  한편 카드를 더 받지 않는 것이 유리하다고 판단되면 카드를 더 받지 않아도 된다.(스탠드, 스테이(Stand, Stay))
import sys, math, random

def playGame():
    print("환영합니다.")
    print("대충 개요")

def bet():
    global Betting_money, Player_money

    print("현재 금액: ", Player_money)
    ok = False
    while not ok:
        print("베팅할 금액을 입력하세요 :", end=" ")
        tmp = input().strip()
        if not tmp.isdigit():
            print("올바른 금액을 다시 입력해수길 바랍니다.")
            continue

        Betting_money = int(tmp)
        if Betting_money > Player_money:
            print("보유 금액보다 많은 금액을 베팅하셨습니다.")
        elif Betting_money == 0:
            print("0원을 베팅하실수 없습니다.")
        else:
            ok = True

def cardDraw():
    while True:
        face = random.randint(0, 3)
        num = random.randint(0, 12)
        if DECK[face][num]:
            DECK[face][num] = False
            break
    return [face, num]

def printCard(deck, r):
    faceDeck = {0: "♠", 1: "◈", 2: "♣", 3: "♥"}
    numDeck = {0: "A", 10: "J", 11: "Q", 12: "K"}

    printStr = []
    for f, i in deck:
        face = faceDeck[f]
        num = numDeck[i] if i in numDeck else str(i + 1)
        printStr.append(face + " " + num)
    if r == 0:
        print(*printStr)
    if r == 1:
        print("XXX", end=" ")
        print(*printStr[1:])

def cmd():
    order = 0
    while True:
        tmp = input().strip()
        if not tmp.isdigit():
            print("올바른 숫자를 다시 입력해수길 바랍니다.")
            continue

        order = int(tmp)
        break
    return order

def isBlackJack(deck):
    sumScore = 0
    ace = 0
    for _, num in deck:
        if num > 9:
            sumScore += 10
        elif num == 0:
            ace += 1
        else:
            sumScore += (num + 1)

    for i in range(ace):
        if i == 0:
            sumScore += 11 if sumScore + 11 <= 21 else 1
        else:
            sumScore += 1
    return sumScore

def init():
    card1 = []
    card2 = []

    card1.append(cardDraw())
    card2.append(cardDraw())
    card1.append(cardDraw())
    card2.append(cardDraw())

    return card1, card2

def bustCheck(score):
    bust = False
    if score > 21:
        bust = True
    return bust

def dealerPlaying(card, score, Player_Bust):
    BUST = False
    print("====== 딜러 ======")
    if Player_Bust:
        print("딜러: Stay")
        printCard(card, 0)
        return card, score, BUST

    while score < 17:
        print("딜러: Hit")
        card.append(cardDraw())
        score = isBlackJack(card)
        printCard(card, 0)

    if bustCheck(score):
        BUST = True
        print("딜러 Bust")
    return card, score, BUST

def playerPlaying(card):
    global Betting_money
    hit = True
    check = True
    score = 0
    Dealer_WIN = False
    while hit:
        # 스탠드, 히트 물어보기
        print("====== 플레이어 ======")
        print("어떻게 하시겠습니까?")
        if check:
            print("1: 히트 2: 스탠드 3: 더블다운 >>>", end=" ")
        else:
            print("1: 히트 2: 스탠드 >>>", end=" ")
        hs = cmd()

        if hs == 1:
            print("플레이어: Hit")
            card.append(cardDraw())
            check = False

        elif hs == 3 and check:
            print("플레이어: Buble Down")
            card.append(cardDraw())
            Betting_money *= 2
            hit = False
            check = False
        else:
            print("플레이어: Stay")
            hit = False

        print("====== 현재 플레이어 카드 ======")
        printCard(card, 0)
        
        # 버스터 체크
        score = isBlackJack(card)
        if bustCheck(score):
            hit = False
            print("Bust")
            Dealer_WIN = True
        if score == 21:
            hit = False
        print("현재 점수: ", score)
    return card, score, Dealer_WIN
def jump():
    for _ in range(2):
        print()

def BlackJack():
    global Player_money, Betting_money
    WIN = False
    # 베팅하기
    bet()

    # 카드 배부
    Player_card, Dealer_card = init()

    while True:
        # 블랙잭인지 확인
        #print(Player_card)
        Player_score = isBlackJack(Player_card)

        # 각 점수
        print("========= 플레이어 카드 =========")
        print("점수:", Player_score, end=" ")
        printCard(Player_card, 0)
        print("========= 딜러 카드 =========")
        printCard(Dealer_card, 1)

        if Player_score == 21:
            print("BLACK JACK")
            WIN = True
            break

        # 플레이어 ㄱㄱ
        Player_card, Player_score, Player_Bust = playerPlaying(Player_card)

        # 딜러 움직임
        print("========= 딜러 카드 공개=========")
        printCard(Dealer_card, 0)
        Dealer_score = isBlackJack(Dealer_card)
        Dealer_card, Dealer_score, Dealer_Bust = dealerPlaying(Dealer_card, Dealer_score, Player_Bust)
        #print("테스트", Dealer_card, Dealer_score, Dealer_Bust)



        print()
        # 카드 보여주기
        print("플레이어 점수: ",Player_score, end=" ")
        printCard(Player_card, 0)
        print("딜러 점수: ", Dealer_score, end=" ")
        printCard(Dealer_card, 0)

        if Dealer_Bust:
            print("이겼습니다.")
            WIN = True
        elif Player_Bust:
            print("졌습니다.")
        elif Player_score == Dealer_score:
            Betting_money = 0
            print("비겼습니다.")
        else:
            if Player_score > Dealer_score:
                print("이겼습니다.")
                WIN = True
            else:
                print("졌습니다.")
        break

    Player_money += Betting_money * 2 if WIN else Betting_money * -1


if __name__ == "__main__":
    input = sys.stdin.readline
    Player_money = 10000
    Betting_money = 0
    DECK = [[True] * 13 for _ in range(4)]
    CONTINUE_GAME = True
    playGame()
    while CONTINUE_GAME and Player_money > 0:
        BlackJack()

        print("현재 금액: ", Player_money)
        if Player_money == 0:
            print("금액이 없습니다.")
            print("플레이를 하실 수 없습니다.")
            break

        print("베팅하시겠습니까?")
        print("1: Yes, 2: No", end=" ")
        CONUTNUE = cmd()
        CONTINUE_GAME = True if CONUTNUE == 1 else False

    # 정산
    # 할려고 했느데 귀찮