import click

@click.command()
@click.option('-s',
              '--start',   
             type=click.DateTime(formats=['%Y%m']))
@click.option('-e',
               '--end',
             type=click.DateTime(formats=['%Y%m']))

def main(start, end):
    monthlist = []
    bigstart_month = datetime2bigmonth(start)
    bigend_month = datetime2bigmonth(end)
    for big_month in range(bigstart_month, bigend_month+1):
        month = bigmonth2str(big_month)
        monthlist.append(month)
    print(monthlist)

def datetime2bigmonth(date):
    '''
    datetime を bigmonth に変換する関数
    例
    202012 -> 2020*12 + 12 = 240252
    '''
    year = date.year
    month = date.month
    return year * 12 + month


def bigmonth2str(bigmonth):
    '''
    bigmonth を 文字列に変換する関数
    例
    240252 -> 202012
    '''
    year = int(bigmonth / 12)
    month = bigmonth % 12
    if month == 0:
        year -= 1
        month = 12
    return f'{year}{month:0>2}'
