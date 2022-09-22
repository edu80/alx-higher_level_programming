#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    prf = "__"
    for x in dir(hidden_4):
        if prf not in x:
            print(x)
