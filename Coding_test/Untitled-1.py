집에서 = {'귀찮은가?': '귀찮음'}
밖에서 = {'귀찮은가?': '안_귀찮음'}
안먹음 = {'다이어트_상태':'다이어트중'}
술먹음 = {'다이어트_상태':'처절한_실패'}

def 전운기(어디서,뭐하냐):
    어디서.update(뭐하냐)
    print(어디서)

전운기(밖에서,술먹음)