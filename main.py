from wyniki import srednie_wyniki

if __name__ == "__main__":

    wyniki = srednie_wyniki(5, 5, 50)

    for key, value in wyniki.items():
        print(key, value)
