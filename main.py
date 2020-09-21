
def main():
    print("="*30)
    print("1. add a stock to portfolio: type 'a'")
    print("2. m: type 'e'")
    print("3. exit: type 'e'")
    print("="*30)
    stock_codes = []
    while(True):
        cmd = input("Command: ")
        if cmd == 'e':
            print("exit!")
            exit(1)
        elif cmd == 'a':
            stock_codes = list(map(int, input("stock codes: ").split()))
        else:
            print("wrong command")



if __name__ == '__main__':
    main()