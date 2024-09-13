# {체인점 인스턴스: 체인점 예약점보 인스턴스} 로 저장 하고싶었지만 오류가 생겨서 포기
# PointChain클래스는 예약정보를 가지고 있으며 ReservationSystem은 기능을 담당

class PointChain:

    chain_name = ''
    people_name = ''
    date_time= ''
    people_numbers = 0

    Reserv_list = []
    total = 0


    def __init__(self, chain_name):
        self.chain_name = chain_name

    def reserv_point_chain(self, people_name, date_time, people_numbers):
        self.people_name = people_name
        self.date_time = date_time
        self.people_numbers = people_numbers
