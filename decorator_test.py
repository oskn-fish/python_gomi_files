
def add_print(func):
    # ラップする関数を定義
    def wrapper(*args): # *argsはラップされる関数に渡すもの
        print("This is added functionality")
        func(*args)
    # ラッパー関数を返す
    return wrapper


@add_print
def myfunc():
    print("Hello!")
    
myfunc()