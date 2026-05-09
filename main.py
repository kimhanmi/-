p_name = input('여행자의 이름을 알려주세요: ')

p_hp = 150
p_mhp = 150
p_ap = 50
p_drug = 5
p_drug_capacity = 25

monster = [['조커', 100, 15], ['다스베이더', 150, 20], ['장원영', 200, 30], ['홍진호홍진호', 222, 22], ['미친 불의 왕', 500, 50]]
remain_monster = len(monster)

print('----에이플 스토리 시작----\n')
print(f'{p_name}의 모험!\n')
flag = True
while flag:
    for i in monster:
        if i[0] == '미친 불의 왕':
            print('시간은 죽었고 의미는 그 의미를 잃었다\n'
                  '존재는 뒤집어졌고 그리고 내가 모든 것을 지배한다...\n\n 최종보스가 등장합니다!')
        print(f'{i[0]}을 마주쳤다!\n')
        while True:
            print('1. 공격 2. 도망 3. 힐\n')
            choice = input('행동을 선택해주세요: ')
            if choice == '1':
                i[1] -= p_ap

                if i[1] <= 0:
                    print('승리하였습니다!\n')
                    remain_monster -= 1
                    p_ap += 10
                    if remain_monster == 0:
                        print('공주/왕자님을 구했습니다!')
                        flag = False
                    break

                p_hp -= i[2]

                if p_hp <= 0:
                    print('패배하였습니다')
                    break

                print(f'\n{i[0]}의 체력: {i[1]} \n'
                      f'{p_name}의 체력: {p_hp} 남은 포션 개수: {p_drug}\n')


            if choice == '2':
                print('도망가는데 성공했습니다!')
                remain_monster -= 1

                if remain_monster == 0:
                    print('도망가!')
                    flag = False
                    break
                break

            if choice == '3':
                print('체력포션(소)을/를 섭취했다')
                p_drug -= 1
                if p_mhp - p_hp < p_drug_capacity:
                    p_hp = p_mhp
                else:
                    p_hp += p_drug_capacity

                print(f'\n{i[0]}의 체력: {i[1]} \n'
                      f'{p_name}의 체력: {p_hp} 남은 포션 개수: {p_drug}\n')

