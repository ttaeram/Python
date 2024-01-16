information = dict()
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]

information[authors[0]] = books[1]
information[authors[1]] = books[3]
information[authors[2]] = books[4]
information[authors[3]] = books[0]
information[authors[4]] = books[2]

print(f'김시습 : {information[authors[0]]}')
print(f'허균 : {information[authors[1]]}')
print(f'남영로 : {information[authors[2]]}')
print(f'작자 미상 : {information[authors[3]]}')
print(f'임제 : {information[authors[4]]}')
