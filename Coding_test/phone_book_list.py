phone_book = ["1","152","1223","14235","567","88"]

def solution(phone_book):
    phone_book = sorted(phone_book)
    print(phone_book)
    wow = []

    for p1, p2 in zip(phone_book[:-1], phone_book[1:]):
        wow.append([p1,p2])

    print(wow)
solution(phone_book)