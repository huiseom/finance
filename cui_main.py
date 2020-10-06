from portfolio import Portfoilo 

def main_cmd_list():
    print("--exit: terminate the program")
    print("--create: create a new portfolio")
    print("--manage: deal with the given number of portfolio")
    print("--status: current number of portfolios")
    
def inner_cmd_list():
    print("")
    print("--add: add a stock to given portfolio")
    print("--del: delete a stock from given portfolio")
    print("--view: show all of the stocks in current portfolio")
    print("--quit: escape from managing mode")


def loop_for_each_pf(pf):
    inner_cmd_list()
    cmd = None
    stock_code = -1
    stock_name = None

    while(True):
        cmd = input("Enter a command:")

        if cmd == 'quit':
            break
        elif cmd == 'add':
            stock_code = input("Enter a stock code:")
            stock_name = input("Enter a stock name:")
            pf.add_stock_to_pf(stock_name=stock_name, stock_code=stock_code)
        elif cmd == 'del':
            stock_code = input("Enter a stock code:")
            pf.del_stock_from_pf(stock_code=stock_code)
        elif cmd == 'view':
            pf.view_pf()
        else:
            print("invalid command!")
            

def cui_main():
    cmd = None
    portfolios = []
    pf_idx = -1
    pf_nums = 0
    pf_name = None
    print("Welcome! This is Portfolio manager ver__0.0")

    main_cmd_list()
    while(True):
        cmd = input("Enter a command:")

        if cmd == 'exit':
            break

        elif cmd =='create':
            pf_name = input("portfolio name: ")
            pf = Portfoilo()
            portfolios.append({'pf':pf,'name':pf_name})
            pf_nums +=1

        elif cmd =='manage':
            pf_idx = input("Enter a portfolio number: ")
            if pf_idx.isdigit():
                loop_for_each_pf(portfolios[pf_idx])
            

        elif cmd == 'status':
            print("There are {} portfolios".format(pf_nums))
            for pf in portfolios:
                print(pf['name'])

        else:
            print("invalid command!")



     
if __name__ == '__main__':
    cui_main()