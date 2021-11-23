def solution(new_id):
    ##1단계 소문자치환
    new_id = new_id.lower()
    ##2단계 알파벳,소문자,숫자,빼기,밑줄,마침표 제외한 모든것 삭제
    _nums = [chr(i) for i in range(ord('0'), ord('9')+1)]
    _chars = [chr(c) for c in range(ord('a'), ord('z')+1)]
    _spec = ['-','_','.']
    _esi = _nums + _chars + _spec
    for i in new_id:
        if i not in _esi:
            new_id = new_id.replace(str(i),"")
    ##3단계마침표 2개를 1개로바꿈
    while ".." in new_id:
        new_id = new_id.replace("..",".")
    ##4단계시작과 끝의 마침표를 없앰
    new_id = new_id.rstrip('.')
    new_id = new_id.lstrip('.')
    ##5단계 빈문자열일시 a 대입
    if new_id.replace(" ","") == '':
        new_id = 'a'
    ##6단계 길이가 16자라면 15개의 문자를 제외한 나머지 문자들을 제거.
    new_id = new_id[0:15]
    new_id = new_id.rstrip('.')
    ##7단계 길이가 2자 이하라면 new_id의 마지막 문자를 new_id의 길이가 3이 될때까지 반복해서 끝에 붙임
    print(len(new_id))
    if len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id = new_id + new_id[-1]
    return new_id



new_id = "...!@BaT#*..y.abcdefghijklm"
solution(new_id)