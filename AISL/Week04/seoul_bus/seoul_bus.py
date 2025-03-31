import pandas as pd

file_path = '/Users/ramy/Desktop/Python/AISL/Week04/seoul_bus/서울시버스노선별정류소정보(20250204).xlsx'
df = pd.read_excel(file_path)


# 정류장 키워드 입력 -> 해당 정류장에 정차하는 버스 출력
def print_buses_by_stop_name(stop_keyword):
    matched = df[df["정류소명"].str.contains(stop_keyword, na=False)]

    if matched.empty:
        print(f"[{stop_keyword}]을(를) 포함하는 정류소가 없습니다.")
        return
    
    grouped = matched.groupby("정류소명")["노선명"].unique()

    for stop_name, buses in grouped.items():
        for bus in buses:
            print(f"[{stop_name}]에 [{bus}] 버스가 정차합니다")


# 버스 번호 입력 -> 해당 버스가 정차하는 정류장 출력
def print_stops_by_bus_number(bus_number):
    matched = df[df["노선명"] == bus_number]

    if matched.empty:
        print(f"[{bus_number}] 버스를 찾을 수 없습니다.")

        return

    matched_sorted = matched.sort_values("순번")

    for _, row in matched_sorted.iterrows():
        print(f"[{bus_number}] 버스가 [{row["정류소명"]}]에 정차합니다")


def init():
    command = input_command()

    if command == "1":
        stop_name = input("정류장 이름 키워드를 입력하세요: ")
        print_buses_by_stop_name(stop_name)

        return init()

    elif command == "2":
        bus_number = input("버스 번호를 입력하세요: ")
        print_stops_by_bus_number(bus_number)

        return init()
    
    elif command == "3":
        print("프로그램을 종료합니다.")

        return

    else:
        print("목록에 있는 정수를 입력해주세요.")

        return init()


def input_command():
    print("=" * 30)
    print("1. 정류장 정차 버스 찾기")
    print("2. 버스 노선의 정차 정류장 찾기")
    print("3. 종료")
    print("=" * 30)

    print("정수값을 선택하시오:", end = " ")
    command = input().strip()

    return command


init()