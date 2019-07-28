dictsched = {'siang1':['O','O','O','O','O','O','O','O','O','O'],
             'malam1':['O','O','O','O','O','O','O','O','O','O'],
             'siang3':['O','O','O','O','O','O','O','O','O','O'],
             'malam3':['O','O','O','O','O','O','O','O','O','O'],
             'input1':[],
             'input4':[],
             'row1':[],
             'row2':[],
             'seat1':[],
             'seat2':[]}
dictsched2 = {'siang2':['O','O','O','O','O','O','O','O','O','O'],
              'malam2':['O','O','O','O','O','O','O','O','O','O'],
              'siang4':['O','O','O','O','O','O','O','O','O','O'],
              'malam4':['O','O','O','O','O','O','O','O','O','O'],
              'input2':[],
              'input3':[],
              'row3':[],
              'row4':[],
              'seat3':[],
              'seat4':[]}

def tempatduduk():
  print('''
Pilih Jadwal The Incredibles: 
1. Siang
2. Malam ''')
  schedule = int(input('Pilih Jadwal Film : '))
  if schedule == 1 :
    inputs1 = int(input('Pesan berapa kali : '))
    dictsched['input1'].append(inputs1)
    angka = 0
    while (angka< inputs1):
        angka += 1
        row = int(input('Pilih row : '))
        dictsched['row1'].append(row)
        seat = int(input('Pilih seat :'))
        dictsched['seat1'].append(seat)
        if row == 1 :
          if dictsched['siang1'][seat-1] == 'X':
            print('Kursi Telah Terisi!')
            break
          dictsched['siang1'][seat-1]='X'
        if row == 2 :
          if dictsched['siang3'][seat-1] == 'X':
            print('Kursi Telah Terisi!')
            break
          dictsched['siang3'][seat-1]='X'
        print(*dictsched['siang1'])
        print(*dictsched['siang3'])
  if schedule == 2 :
    inputs2 = int(input('Pesan berapa kali : '))
    dictsched['input4'].append(inputs2)
    angka = 0
    while (angka< inputs2):
        angka += 1
        row = int(input('Pilih row : '))
        dictsched['row2'].append(row)
        seat = int(input('Pilih seat :'))
        dictsched['seat2'].append(seat)
        if row == 1 :
          if dictsched['malam1'][seat-1] == 'X':
            print('Kursi Telah Terisi!')
            break
          dictsched['malam1'][seat-1]='X'
        if row == 2 :
          if dictsched['malam3'][seat-1] == 'X':
            print('Kursi Telah Terisi!')
            break
          dictsched['malam3'][seat-1]='X'
        print(*dictsched['malam1'])
        print(*dictsched['malam3'])

def tempatduduk1():
  print('''
Pilih Jadwal Film Toy Story: 
1. Siang
2. Malam ''')
  schedule = int(input('Pilih Jadwal Film : '))  
  if schedule == 1 :
    inputs3 = int(input('Pesan berapa kali : '))
    dictsched2['input2'].append(inputs3)
    angka = 0
    while (angka< inputs3):
        angka += 1
        row = int(input('Pilih row : '))
        dictsched2['row3'].append(row)
        seat = int(input('Pilih seat :'))
        dictsched2['seat3'].append(seat)
        if row == 1 :
          if dictsched2['siang2'][seat-1] == 'X':
            print('Kursi Telah Terisi!')
            break
          dictsched2['siang2'][seat-1]='X'
        if row == 2 :
          if dictsched2['siang4'][seat-1] == 'X':
            print('Kursi Telah Terisi!')
            break
          dictsched2['siang4'][seat-1]='X'
        print(*dictsched2['siang2'])
        print(*dictsched2['siang4'])
  if schedule == 2 :
    inputs4 = int(input('Pesan berapa kali : '))
    dictsched2['input3'].append(inputs4)
    angka = 0
    while (angka< inputs4):
        angka += 1
        row = int(input('Pilih row : '))
        dictsched2['row4'].append(row)
        seat = int(input('Pilih seat :'))
        dictsched2['seat4'].append(seat)
        if row == 1 :
          if dictsched2['malam2'][seat-1] == 'X':
            print('Kursi Telah Terisi!')
            break
          dictsched2['malam2'][seat-1]='X'
        if row == 2 :
          if dictsched2['malam4'][seat-1] == 'X':
            print('Kursi Telah Terisi!')
            break
          dictsched2['malam4'][seat-1]='X'
        print(*dictsched2['malam2'])
        print(*dictsched2['malam4'])

def menu ():
  pilihan = 1
  while (pilihan <= 2):
    print('''
Menu :
1. Pesan Tiket
2. Lihat History
3. Keluar ''')
    pilihan = int(input('Tentukan Pilihan : '))
    if pilihan == 1:
      print('''
List Film :
1. The Incredibles
2. Toy Story''')
      film = int(input('Silahkan Pilih Film : '))
      if film == 1 :
        tempatduduk()
      elif film == 2:
        tempatduduk1()
    elif pilihan == 2:
      if len(dictsched['input1']) == 0 and len(dictsched['input4'])==0:
        print('')
      elif len(dictsched['input1']) > 0 or len(dictsched['input4'])>0:
        for item in range(0,*dictsched['input1']):
          print('Film The Incredibles Jadwal Siang Row {} Seat {}'.format(dictsched['row1'][item],dictsched['seat1'][item]))
        for item1 in range(0,*dictsched['input4']):
          print('Film The Incredibles Jadwal Malam Row {} Seat {}'.format(dictsched['row2'][item],dictsched['seat2'][item]))
      if len(dictsched2['input2']) == 0 and len(dictsched2['input3'])==0:
        print('')
      elif len(dictsched2['input2']) > 0 or len(dictsched2['input3'])>0:
        for item in range(0,*dictsched2['input2']):
          print('Film Toy Story Jadwal Siang Row {} Seat {}'.format(dictsched2['row3'][item],dictsched2['seat3'][item]))
        for item in range(0,*dictsched2['input3']):
          print('Film Toy Story Jadwal Malam Row {} Seat {}'.format(dictsched2['row4'][item],dictsched2['seat4'][item]))
    elif pilihan == 3:
      print('Terima Kasih!')
      
menu()
