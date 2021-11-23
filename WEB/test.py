def recursive(data):
    if data < 0:
        print('ended')  # 호출 후 함수가 끝납니다.
    else:
        print(data)
        recursive(data - 1)
        print('returned', data)  # 함수가 끝난 후 나중에 쌓인 순서대로 print 합니다.

recursive(4)