
       
       
       
   
if __name__ == '__main__':

    birthdays =    {
        'volkan': '09/07/1996',
        'oltan': '06/07/1996' ,
        'selim toptekin': '15/12/1995',
        'furkan': '27/11/1997',
        'samet': '06/10/1996',
        'barış' : '22/01/1996' ,
        'emre'  :  '22/09/1994'}

    print('Kolpa grubunun doğum  tarihlerine hoş geldiniz')
    for name in birthdays:
        print(name)

    print('Kimin doğum gününü öğrenmek istersin ?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('yanlış isim girdin keko.'.format(name))       
