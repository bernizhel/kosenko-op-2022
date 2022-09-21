# -- coding: utf-8 --
def formattedTimeFromMinutes(n):
  n = n % (60 * 24)
  hours = str(int(n / 60)).zfill(2)
  print(f'{hours}:{str(n % 60).zfill(2)}')

formattedTimeFromMinutes(int(input()))
