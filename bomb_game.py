import time,random,logging
logging.basicConfig(filename= 'bombgame_logfile.txt',level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('start of a program')

def randomize_cables():
    cable_list = ['r','y','b','g']
    random.shuffle(cable_list)
    #logging.debug('list shuffled',cable_list)
    return cable_list

def main():
    print("WELCOME TO BOMB GAME! You have 13s to find the correct place for cables(r,y,g,b). If you can't the bomb will exlpode and you will DIE desperately.")
    print("Enter start when you are ready: ")
    start_string = input("")

    cable_order = randomize_cables()
    
    
    if start_string.lower() =='start':
        print('time started. enter your cable order')
        start_time = time.time()
    
    
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= 17:
            print('!!!BOMB EXPLODED!!!')
            break

        user_row =input("")

        true_count = 0
        for i in range(len(user_row)):
            if user_row[i] == cable_order[i]:
                true_count += 1
        
        if true_count == 4:
            print("Order is true. You won, bomb stopped.")
            break
        else:
            print('You got',true_count,'true. Try again.')

if __name__ == '__main__':
    main()