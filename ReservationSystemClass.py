class ReservationSystem:

    total = 0

    # 1. 지점이름을 초기화, 예약 리스트를 관리하는??? 객체 생성
    def __init__(self, chain_name):
        self.chain = PointChain(chain_name) # 체인점 인스턴스 생성후 chain에 할당
        self.chain.Reserv_list.append(self.chain) # 체인점예약 리스트에 인스턴스를 추가


    # 2. 새로운 예약을 추가합니다. 이 메서드는 예약자 이름, 예약 일시, 인원 수를 받아 저장합니다.
    def add_reservation(self, people_name, date_time, people_numbers):
        # 생성한 인스턴스의 메서드를 이용하여 예약
        self.chain.reserv_point_chain(people_name, date_time, people_numbers)
        print(f'{self.chain.chain_name}에 {self.chain.people_name}님의 예약이 추가되었습니다. 예약일: {self.chain.date_time}, 인원 수: {self.chain.people_numbers}명')
        self.total += 1

    # 3. cancel_reservation: 지정된 예약을 취소하고 리스트에서 제거합니다.
    # 예약 취소: 고객이 예약을 취소할 수 있으며, 해당 예약을 시스템에서 제거합니다.
    def cancel_reservation(self, people_name, date_time, people_numbers):
        if self.chain.people_name == people_name and self.chain.date_time == date_time and self.chain.people_numbers == people_numbers:
            self.chain.Reserv_list.remove(self.chain)
            print(f'{self.chain.chain_name} 예약을 취소합니다')
            self.total -= 1



    # 4. list_reservations: 현재 지점의 모든 예약 상태를 출력합니다
    # 예약 조회: 특정 지점의 모든 예약 상황을 확인할 수 있습니다.
    # 모든 출력 메시지는 한국어로 제공되어야 합니다.
    def list_reservations(self):
        print(f'{self.chain.chain_name}점 예약목록:\n- {self.chain.people_name}, {self.chain.date_time} {self.chain.people_numbers}명')


    # 5. sum_reservations: 주어진 ReservationSystem 인스턴스 리스트에서 모든 예약 수를 합산합니다
    # sum_reservations 클래스 메서드는 모든 지점에서의 예약 수를 효과적으로 합산하여 전체 예약 상태를 중앙에서 확인할 수 있게 합니다.
    @classmethod
    def sum_reservations(cls, rest_list):
        sum = 0
        for rest in rest_list:
            sum += rest.total
        return sum
