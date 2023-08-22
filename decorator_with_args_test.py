

def top_dec(added_what):
    def add_print(func):
        # ラップする関数を定義
        def wrapper(*args): # *argsはラップされる関数に渡すもの
            print(f"This is added {added_what}")
            func(*args)
        # ラッパー関数を返す
        return wrapper
    return add_print


@top_dec("shit")
def myfunc():
    print("Hello!")
    
myfunc()