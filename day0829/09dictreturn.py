#09dictreturn.py

#함수의 매개인자딕트,리턴값여러개


#함수의 리턴값을 1개이상 처리
#함수의 매개인자 1개이상 처리(*args)
def  score_procedure():
    pass
#kor_list=[]
#eng_list=[]
    #return  국어점수 합계, 영어점수 합계, 국어평균, 영어평균

score= {
    'kim':[100,60], 
    'lee':[90,77],
    'goo':[82,34]
    }


a,b,c,d= score_procedure(score)

#----------------------------------------------------------------

def  score_procedure():
    pass
#kor_list=[]
#eng_list=[]

# 성적을 담은 딕셔너리
score_dict = {
    'kim':[100,60], 
    'lee':[90,77],
    'goo':[82,34]
    }

# 학생의 이름과 성적을 수정하기 위한 매핑
name_mapping = {
    'kim': 'kim',
    'lee': 'lee',
    'goo': 'goo',
}

# 각 학생의 총점과 평균을 계산 후 출력
for name, scores in score_dict.items():
    kor_score, eng_score = scores
    total = kor_score + eng_score  # 총점 계산
    average = total // 2  # 평균 계산 (정수 나누기)

# 결과 출력
    print(f"{corrected_name:<8} {total:<4} {average:<4}")

# 추가적으로 구분선을 출력
print('-' * 50)
    
#-----------------------------------------------------------------

    # 이름 수정
    corrected_name = name_mapping.get(name, name)  # name_mapping에서 이름 수정
    
    # 결과 출력
    print(f"{corrected_name:<8} {total:<4} {average:<4}")

# 추가적으로 구분선을 출력
print('-' * 50)






