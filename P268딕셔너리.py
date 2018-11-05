phone_book={}
phone_book["홍길동"]="010-1234-5678"
phone_book["강감찬"]="010-1234-5678"

for key in sorted(phone_book.keys()):
    print(key, phone_book[key])
    
