from math import *
from main import input_val_list, output_val_list, find_W

def check(lst_1, N):

    count = 0
    for i in range(N):
        if lst_1[i] >= 0.3: continue
        else: count += 1

def calc(val):

    return pow(10, round((val/10), 2))

def calc_lg(val):

    return log10(val)

def calc_level_signal(list_L_sh_i, list_L_h_i, N):

    res_list = []
    for i in range(N): res_list.append(10*calc_lg(calc(list_L_sh_i[i])-calc(list_L_h_i[i])))
    return res_list

def calc_coeff_high_level(list_L_tc, list_L_n, N):

    res_list = []
    for i in range(N): res_list.append(list_L_tc[i] - list_L_n[i])
    return res_list

def menu(msg):

    N = int(input('Введите количество октав: '))
    list_L_tc = input_val_list('Введите значения тестируемого ' + msg + ' сигнала (Ltci)', N)
    list_L_sh = input_val_list('Введите значения сигнал + шум ' + msg + ' сигнала (Lc+hi)', N)
    list_L_h = input_val_list('Введите значения шумa ' + msg + ' сигнала (Lhi)', N)
    list_L_c = calc_level_signal(list_L_sh, list_L_h, N)
    output_val_list('Значения уровня сигнала за ограждающей конструкцией', list_L_c)
    list_L_n = input_val_list('Введите нормированные значения ' + msg + ' сигнала (Lni)', N)
    list_L_i = calc_coeff_high_level(list_L_tc, list_L_n, N)
    output_val_list('Значения коэффициента превышения уровня создаваемого звукового давления', list_L_i)
    list_L_priv = calc_coeff_high_level(list_L_c, list_L_i, N)
    output_val_list('Значения уровня сигнала, приведенному к нормированному уровню звукового давления', list_L_priv)
    list_E_i = calc_coeff_high_level(list_L_priv, list_L_h, N)
    output_val_list('Значения отношения сигнал/шум', list_E_i)
    if check(list_E_i, N) == 0:
        print('Нет необходимости рассчитывать словесную разборчивость речи'
              'поскольку отношение сигнал/шум для рассматриваемых 5 октав!!!')
    else:
        list_A_i = input_val_list('Введите значения форматного параметра речи', N)
        list_k_i = input_val_list('Введите значения весового коэффициента', N)
        val_W = find_W(list_E_i, list_A_i, list_k_i, N, count=2)

if __name__ == '__main__':

    menu('акустического')
    menu('вибрационного')