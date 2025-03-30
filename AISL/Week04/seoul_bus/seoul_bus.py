import pandas as pd

# 엑셀 파일 경로
file_path = '/Users/ramy/Desktop/Python/AISL/Week04/seoul_bus/서울시버스노선별정류소정보(20250204).xlsx'
df = pd.read_excel(file_path)

# 1. 정류장 키워드 입력 → 해당 정류장에 정차하는 버스 출력
def print_buses_by_stop_name(stop_keyword):
    matched = df[df['정류소명'].str.contains(stop_keyword, na=False)]

    if matched.empty:
        print(f"'{stop_keyword}'을(를) 포함하는 정류소가 없습니다.")
        return
    
    grouped = matched.groupby('정류소명')['노선명'].unique()
    for stop_name, buses in grouped.items():
        for bus in buses:
            print(f"버스 {bus}가 {stop_name}에 정차합니다")

# 2. 버스 번호 입력 → 해당 버스가 정차하는 정류장 출력
def print_stops_by_bus_number(bus_number):
    matched = df[df['노선명'] == bus_number]

    if matched.empty:
        print(f"버스 '{bus_number}'을(를) 찾을 수 없습니다.")
        return

    matched_sorted = matched.sort_values('순번')
    for _, row in matched_sorted.iterrows():
        print(f"버스 {bus_number}가 {row['정류소명']}에 정차합니다")

# 메인 함수
def main():
    mode = input("1: 정류장 이름으로 버스 찾기 / 2: 버스 번호로 정류장 찾기\n입력: ")

    if mode == '1':
        stop_name = input("정류장 이름 키워드를 입력하세요: ")
        print_buses_by_stop_name(stop_name)

    elif mode == '2':
        bus_number = input("버스 번호를 입력하세요: ")
        print_stops_by_bus_number(bus_number)

    else:
        print("잘못된 입력입니다. 1 또는 2를 선택해주세요.")

if __name__ == "__main__":
    main()