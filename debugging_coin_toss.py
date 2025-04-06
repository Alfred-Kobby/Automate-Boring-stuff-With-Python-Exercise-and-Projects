import random
import logging

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')

guess = ''
try:
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
        logging.info(f'guess is {guess}')
        toss = random.randint(0, 1)  # 0 is tails, 1 is heads
        if toss == 0:
            toss = 'tails'
        else:
            toss = 'heads'
        logging.info(f'toss is {toss}')
        if toss == guess:
            logging.info('Toss is equal to guess (in first if statement)')
            print('You got it!')
        else:
            logging.info('Toss is not equal to guess (in first else statement)')
            logging.info('Toss is not equal to guess')
            print('Nope! Guess again!')
            guess = input()
            logging.info(f'guess is {guess}')
            logging.info(f'toss is {toss}')
            if toss == guess:
                logging.info('Toss is equal to guess (in second if statement)')
                print('You got it!')
            else:
                logging.info('Toss is not equal to guess (in second else statement)')
                print('Nope. You are really bad at this game.')
except Exception as err:
    logging.error(f'An error occured: {err}')