# 성적을 담은 딕셔너리
score_dict = {
    '김자바': [100, 60],
    '이합격': [90, 77],
    'lee': [82, 34],
    'park': [90, 34]
}

# 학생의 이름과 성적을 수정하기 위한 매핑
name_mapping = {
    '김자바': '김자반',
    '이합격': '이합격',
    'lee': '박패스',
    'park': '박이썬',
}

# 각 학생의 총점과 평균을 계산 후 출력
for name, scores in score_dict.items():
    kor_score, eng_score = scores
    total = kor_score + eng_score  # 총점 계산
    average = total // 2  # 평균 계산 (정수 나누기)
    
    # 이름 수정
    corrected_name = name_mapping.get(name, name)  # name_mapping에서 이름 수정
    
    # 결과 출력
    print(f"{corrected_name:<8} {total:<4} {average:<4}")

# 추가적으로 구분선을 출력
print('-' * 50)