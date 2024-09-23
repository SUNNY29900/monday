# homeworkdict.py

score_dict = {
    '김자바':[100,60],
    '이합격':[90,77],
    '강수능':[82,74],
    '박이썬':[90,34]
}
list_kor = []
list_eng = []

# for j in range(len(score_dict)):
#     for i,k in score_dict.items():
#         list_kor = score_dict
#         list_eng = score_dict
#         print(i,':',list_kor)

# print(score_dict['김자바'])

# for i in range(len(score_dict)):
#     for j,k in score_dict.items():
#         list_kor = [160,167,116,124]
#         list_eng = [80,83,58,62]
#         print(j,':',list_kor[i],list_eng[i])

for j,k in score_dict.items():
    print(j,sum(score_dict[j]),int(sum(score_dict[j])/len(score_dict[j])))


# 김자바 - 160,80
# 이합격 - 167,83
# 강수능 - 116,58
# 박이썬 - 124,62