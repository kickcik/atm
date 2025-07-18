balance = 10000
receipts = []

while (num := input('기능 선택| 1.입금, 2.출금, 3.영수증 보기, 4. 종료 : ')) != '4':
    if num == '1': # 입금 기능 구현 feat/deposit
        try:
            balance += (deposit_amount := int(input('입금할 급액을 입력해주세요: ')))
            print(f'입금하신 금액: {deposit_amount:,}원')
            print(f'현재 잔액 : {balance:,}원')
            receipts.append(('입금', f'입금액: {deposit_amount:,}원', f'잔액: {balance:,}원'))
        except Exception as e:
            print(f'예외 발생 : {type(e)}')
            print(f'내용 : {e}')

    if num == '2':
        try:
            if (withdraw_amount := min(int(input('출금할 금액을 입력해주세요: ')), balance)) >= 0:
                print(f'출금액 : {withdraw_amount:,}원')
                balance -= withdraw_amount
                print(f'현재 잔액 : {balance:,}원')
                receipts.append(('출금', f'입금액: {withdraw_amount:,}원', f'잔액: {balance:,}원'))
            else:
                print('출금액 입력 오류')
        except Exception as e:
            print(f'예외 발생 : {type(e)}')
            print(f'내용 : {e}')


    if num == '3':
        print('--영수증--')
        if receipts:
            for i in receipts:
                print(*i, sep=', ')
        else:
            print('영수증 내력이 없습니다.')


print(f'서비스가 종료되었습니다.')
print(f'현재 잔액 : {balance:,}원')



