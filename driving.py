country = input('請問你是哪國人/Where are you from：')
age = input('請輸入年齡/Age: ')
age = int(age)
if country == '台灣/Taiwan':
    if age >= 18:
        print('你可以考駕照/You can apply for driving licence')
    else:
        print('你還不能考駕照/You cannot apply for driving licence')
elif country == '美國/US':
    if age >= 16:
        print('你可以考駕照/You can apply for driving licence')
    else:
        print('你還不能考駕照/You cannot apply for driving licence')
else:
    print('只能輸入台灣或美國/Please choose either Taiwan or US')


