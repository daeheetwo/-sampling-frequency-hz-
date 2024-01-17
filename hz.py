import pandas as pd

# 데이터 로드
data = pd.read_csv('300rpm(diff)/Normal/normal_data_2023_12_7_18_0.csv')

# 시간 데이터를 datetime 객체로 변환
data['time'] = pd.to_datetime(data['time'])  # 'time'을 실제 시간 컬럼 이름으로 변경

# 시간 간격 계산
time_diff = data['time'].diff().dt.total_seconds()

# 샘플링 빈도 계산
sampling_frequency = 1 / time_diff.mean()

print(sampling_frequency)
