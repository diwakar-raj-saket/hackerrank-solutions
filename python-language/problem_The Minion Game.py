def minion_game(string):
    vowels = 'AEIOU'
    kev = 0
    stu = 0
    for i in range(len(string)):
        if s[i] in vowels:
            kev += (len(string)-i)
        else:
            stu += (len(string)-i)
    if kev > stu:
        print("Kevin", kev)
    elif kev < stu:
        print("Stuart", stu)
    else:
        print("Draw")
       

if __name__ == '__main__':
    s = input()
    minion_game(s)
