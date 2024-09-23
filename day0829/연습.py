
#하수의 매개인사딕트. 
#sum(), len(), . //몫추출
def  score_procedure(sd):
    pass
    kor_list=[]
    eng_list=[]
    for data in sd.values():
        kor_list.append(data[0])
        eng_list.append(data[1])

    kor_hap=sum(kor_list)
    eng_hap=sum(eng_list)
    kor_avg=kor_hap//len(kor_list)
    eng_avg=kor_hap//len( eng_list)
    return kor_hap. eng_hap, kor_avg, eng_avg


# 성적을 담은 딕셔너리
score_dict = {
    'kim':[100,60], 
    'lee':[90,77],
    'goo':[82,34]
}

a,b,c,d=score_procedure(score)

print('국어총점', a)
print('영어총점', b)
print('국어평균', c)
print('영어평균', d)

#hap=a+b+c+d
#avg=(a+b+c+d)/4

print(a+b)  #hap=a+b
print((a+b+c+d)/4)

print()


#--------------------------

# # 각 학생의 총점과 평균을 계산 후 출력
# for name, scores in score_dict.items():
#     kor_score, eng_score = scores
#     total = kor_score + eng_score  # 총점 계산
#     average = total // 2  # 평균 계산 (정수 나누기)

# # 결과 출력
# print(f"{total:<3} {average:<3}")

# # 추가적으로 구분선을 출력
# print('-' * 50)
    






