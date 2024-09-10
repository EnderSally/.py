p=1

print("""                                  ---ИНСТРУКЦИЯ---

-Введите "insert" и любую строку после, она в свою очередь будет добавлена в базу данных.

-При вводе "select", будет показан весь список строк.

-"delete" удалит первую соответсувующую строку, указанную после команды.
 Если перед командой написать "!", то удалится первая указанная строка с конца.
 Если после любой из команд указать скобки и вписать число,
 то удалится нужная строка под порядковым номером, написананым в скобках.

 Команды и строки разделяются любым одним знаком.


 Для выхода из программы введите "exit".
""")

base=[]

while p==1:
    a=input("-")
    if a[0:6]=="insert":
        base.append(a[7:])
    elif a=='select':
        print(base)
    elif a[0:6]=='delete':
        q=7
        c=1
        try:
            if a[6:7]=='(':
                c=''
                while a[q]!=")":
                    c=c+a[q]
                    q+=1
                q+=2
        except IndexError:
            q = 7
            c = 1
        i=0
        try:
            c=int(c)
            for b in range (len(base)):
                if base[b]==a[q:]:
                    if c==1:
                        base.pop(b)
                        break
                    else: c-=1
        except ValueError:
            print("Синтаксическая ошибка!")
    elif a[0:7]=='!delete':
        q=8
        c=1
        if a[7:8]=='(':
            c=''
            while a[q]!=")":
                c=c+a[q]
                q+=1
            q+=2
        try:
            c=int(c)
            i=0
            l=len(base)-1
            for b in range (len(base)):
                if base[l-b]==a[q:]:
                    if c==1:
                        base.pop(l-b)
                        break
                    else: c-=1
        except ValueError:
            print("Синтаксическая ошибка!")
    elif a=="exit":
        exit(print("""
        Выход из программы..."""))
    else:
        print("Не обнаружена существующая команда!")
input()