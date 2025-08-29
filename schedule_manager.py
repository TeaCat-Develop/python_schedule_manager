from pydoc import describe

import pymysql

from pymysql.cursors import Cursor

# db 연결하는 함수
def get_db_connection() -> pymysql.Connection:
    try:
        return pymysql.connect(host="localhost", port=3307, user="root", password='1234', database='schedule_db')
    except Exception as e:
        print(f"데이터베이스 연결 실패: {e}")
        exit(1)

def add_schedule(cursor: Cursor):
    # Todo: 여기에 일정 추가 코드를 작성합니다.
    title = input('title:')
    description = input('desc:')
    start_datetime = input('start(yyyymmddhhmmss):')
    end_datetime = input('end(yyyymmddhhmmss):')
    sql = """INSERT INTO schedules(title, description, start_datetime, end_datetime)
             VALUES (%s, %s, %s, %s)"""

    cursor.execute(sql, (title, description, start_datetime, end_datetime))
    print('일정이 추가됨.')

def get_schedules(cursor: Cursor):
    # Todo: 여기에 일정 정보를 가져오는 코드를 작성합니다.
    sql = """SELECT id, title, description, start_datetime, is_completed FROM schedules"""

    cursor.execute(sql)
    schedules = cursor.fetchall()

    if not schedules:
        print('일정없음')
        return

    # 출력하기
    for schedule in schedules:
        id, title, description, start_datetime, is_completed = schedule
        status = '완료' if is_completed else '진행중'

        print(f'{id}: {title}')
        print(f'진행상황: {status}')
        print(f'일시:{start_datetime}')
        if description:
            print(f'내용:{description}')
        print()

def complete_schedule(cursor: Cursor):
    # Todo: 여기에 일정을 완료처리하는 코드를 작성합니다.
    id = input('완료 일정의 id: ') #id값 입력받기

    sql = """UPDATE schedules SET is_completed = true WHERE id = %s"""

    cursor.execute(sql, id)
    print('일정완료')

# 메뉴 나타내기
def show_menu() -> str:
    print("1. 일정 추가")  # insert
    print("2. 일정 보기")  # select
    print("3. 일정 완료")  # update
    print("4. 종료")
    return get_user_choice()

# 선택한 메뉴 입력받는 함수
def get_user_choice() -> str:
    return input("선택: ")

def main():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        while True:
            choice = show_menu()
            if choice == "1":
                add_schedule(cursor)
                conn.commit()
            elif choice == "2":
                get_schedules(cursor)
            elif choice == "3":
                complete_schedule(cursor)
                conn.commit()
            elif choice == "4":
                print("종료합니다.")
                break
            else:
                print("다시 선택해주세요")

    except Exception as e:
        print(f"프로그램 실행 중 오류 발생: {e}")

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    main()