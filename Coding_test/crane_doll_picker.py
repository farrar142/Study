board = [[0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    queue = []
    answer = 0
    for i in moves:
        i -= 1
        for j in range(0,len(board)):
            if board[j][i] != 0:
                queue.append(board[j][i])
                board[j][i] = 0
                break
        if len(queue) > 1:
            if queue[-1] == queue [-2]:
                queue.pop(-1)
                queue.pop(-1)
                answer+=2
    return answer

solution(board,moves)