"""
囚徒困境
1 首先自定义三种策略
    1.1 始终保持沉默
    1.2 怎么都会出卖
    1.3 根据上一轮对方的选择做选择（例如对方上一轮选择合作本轮选择合作，
                                反之亦然，默认第一轮选择沉默）
    
2 定义计算结果的函数， n为总轮数，s1，s2分别为犯人做出的策略选择
    （注：在Python中函数也是一种对象，所以我们可以直接传递不同的策略，）
"""


def nice(last_turn):
    return '就是不说话！'


def rat(last_turn):
    return '出卖你啦~'


def tit_for_tat(last_turn):
    if last_turn == '出卖你啦~':
        return '出卖你啦~'
    else:
        return '就是不说话！'


def prison_dilemma(n, s1, s2):
    """
    
    :param n:博弈总轮数  
    :param s1: 犯人一选择的策略
    :param s2: 犯人二选择的策略
    :return: 返回犯人一二的获刑年数
    
    """
    p1_years, p2_years = 0, 0
    p1_last_turn, p2_last_turn = '', ''

    for i in range(n):
        p1_choice = s1(p2_last_turn)
        p2_choice = s2(p1_last_turn)

        if p1_choice == p2_choice == '出卖你啦~':
            p1_years += 2
            p2_years += 2
        elif p1_choice == p2_choice == '就是不说话！':
            p1_years += 1
            p2_years += 1
        elif p1_choice == '出卖你啦~' != p2_choice:
            p2_years += 5
        else:
            p1_years += 5
        p1_last_turn, p2_last_turn = p1_choice, p2_choice
    return p1_years, p2_years


print(prison_dilemma(4, nice, nice))  # 这两个人都不招，真兄弟！
print(prison_dilemma(4, rat, rat))    # 大难临头，互相捅刀— —
print(prison_dilemma(4, tit_for_tat, tit_for_tat))  # 这是一种策略
print(prison_dilemma(4, nice, rat))   # 这种情况下就尴尬了..
print(prison_dilemma(6, nice, rat))   # 这种情况下就很尴尬了...
print(prison_dilemma(8, nice, rat))   # 这种情况下就非常尴尬了....
