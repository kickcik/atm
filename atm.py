balance = 10000

while (num := input('기능 선택| 1.입금, 2.출금, 3.영수증 보기, 4. 종료 : ')) != '4':
    if num == '1': # 입금 기능 구현 feat/deposit
        try:
            balance += (deposit_amount := int(input('입금할 급액을 입력해주세요: ')))
            print(f'입금하신 금액: {deposit_amount:,}원')
            print(f'현재 잔액 : {balance:,}원')
        except Exception as e:
            print(f'예외 발생 : {type(e)}')
            print(f'내용 : {e}')

    if num == '2':
        pass

    if num == '3':
        pass

print(f'서비스가 종료되었습니다.')
print(f'현재 잔액 : {balance:,}원')



