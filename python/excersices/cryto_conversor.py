# !/usr/bin/python3

def main():
    print('BITCOIN CONVERTER\n')

    ammount = float(input('Input for Bitcoin: '))
    result = cryptoExchangeCalculator(ammount)

    print('{} Bitcoin son {} pesos colombianos'.format(ammount, result))
    print('')

def cryptoExchangeCalculator(ammount):
   btc_to_cop = 20000000

   return btc_to_cop*ammount

if __name__=='__main__':
    main()

