from math import *

def input_val_list(msg, N):

    buff_lst = [0 for i in range(N)]
    i = 0
    while i < N:
        try:
            print('Значение' + str(i) + 'октавы.')
            buff_lst[i] = float(input())
            i+=1
        except ValueError:
            print('Некорректно введены данные! Повторите ввод!')
            if i == 0: i=0
    #for i in range(5): buff_lst[i] = float(buff_lst[i])
    return buff_lst

def output_val_list(msg, list_1):

    print(msg)
    for i in list_1: print(i)
    print('\n****************************************\n')

def count(val):

    val_to_mkV = pow(10, (val/20))
    print('\n********************\nЗначение напряжения в микровольтах', val_to_mkV, '\n***********************************\n')
    return round(val_to_mkV, 2)

def info_signal(list_U_ch, list_U_h, N):

    list_U_c = []
    for i in range(N):
        if (list_U_ch[i] - list_U_h[i]) < int(1): list_U_c.append(count(list_U_ch[i] - 7))
        else: list_U_c.append(round(sqrt((pow(count(list_U_ch[i]), 2) - pow(count(list_U_h[i]), 2))), 2))
    return list_U_c

def count_sqr_zvuk_davl(list_L_i, list_L_H_i, N):

    list_K_i = []
    for i in range(N): list_K_i.append(round(count(list_L_i[i] - list_L_H_i[i]), 2))
    return list_K_i

def count_level_info_signal(list_U_c, list_K_i, N):

    list_U_c_priv = []
    for i in range(N): list_U_c_priv.append(round(list_U_c[i]/list_K_i[i], 3))
    return list_U_c_priv

def slov_razb_rechi(R):

    if R >= 0.15: return round(1 - exp((-1)*round((11*R)/1+0.7*R, 2)), 2)
    else: return round(1.54*pow(R, 0.25)*(1-exp((-1)*round(11*R, 2))), 2)

def integr_ind(p_i, k_i, N):

    R = 0
    for i in range(N): R+=p_i[i]*k_i[i]
    return round(R, 3)

def find_p_i(list_Q_i):

    list_p_i = []
    for i in list_Q_i:
        if i > 0:
            val = pow((27.3 - abs(i)), 2)
            val_1 = exp((-1)*4.3*pow(10, -3) * val)
            val_2 = 5.46 * val_1
            val_3 = val_2+0.78
            val_4 = pow(10, 0.1*abs(i))
            val_5 = 1 + val_4
            val_6 = 1 - (val_3/val_5)
            list_p_i.append(round(val_6, 4))
        else: list_p_i.append(round((0.78+5.46*exp((-1)*4.3*pow(10, -3)*pow((27.3 - abs(i)), 2)))/(1+pow(10, 0.1*abs(i))), 4))
    return list_p_i

def find_Q_i(list_E_i, list_A_i, N, count):

    list_Q_i = []
    for i in range(N):
        if count == 2: list_Q_i.append(round(list_E_i[i] - list_A_i[i], 2))
        elif count == 3: list_Q_i.append(round(20*log10(list_E_i[i]) - list_A_i[i], 2))
    return list_Q_i

def find_W(buff_lst_3, list_A_i, list_k_i, N, count):

    list_Q_i = find_Q_i(buff_lst_3, list_A_i, N, count)
    output_val_list('Значения Q_i', list_Q_i)
    list_p_i = find_p_i(list_Q_i)
    output_val_list('Значения p_i', list_p_i)
    val_R = integr_ind(list_p_i, list_k_i, N)
    print('******************\nПолученное значение интеграции речи\n', val_R, '\n*********************')
    val_W = slov_razb_rechi(val_R)
    print('\n***************\nСловесная разборчивость речи\n', val_W, '\n*********************')
    return val_W

def main():

    N = int(input('Введите количество октав: '))
    list_L_i = input_val_list('Введите значение измеренного уровня звукового давления', N)
    list_U_ch = input_val_list('Введите значение напряжения "сигнал/шум"', N)
    list_U_h = input_val_list('Введите значение напряжения шума', N)
    val_W_n = 0.3
    print('*********************************')
    buff_lst = info_signal(list_U_ch, list_U_h, N)
    output_val_list('Значения в микровольтах информационного сигнала', buff_lst)
    list_L_H_i = input_val_list('Введите нормированные значения звукового давления', N)
    buff_lst_1 = count_sqr_zvuk_davl(list_L_i, list_L_H_i, N)
    output_val_list('Значения рассчитанного степени превышения создаваемого акустического давления', buff_lst_1)
    buff_lst_2 = count_level_info_signal(buff_lst, buff_lst_1, N)
    output_val_list('Значения рассчитанного уровня информативного сигнала', buff_lst_2)
    list_U_n = input_val_list('Введите нормированные значения электрических шумов в зависимости от вида линии', N)
    buff_lst_3 = count_level_info_signal(buff_lst_2, list_U_n, N)
    output_val_list('Рассчитанное значение "сигнал/шум"', buff_lst_3)
    list_A_i = input_val_list('Введите значения форматного параметра речи', N)
    list_k_i = input_val_list('Введите значения весового коэффициента', N)
    val_W = find_W(buff_lst_3, list_A_i, list_k_i, N, count=3)
    if val_W > val_W_n:
        list_U_1_i = input_val_list('Введите значение напряжения в линии связи вблизи подачи сигнала в точке Т1', N)
        list_U_2_i = input_val_list('Введите значение напряжения в линии связи на границе КЗ в точке Т2', N)
        list_K_i = count_level_info_signal(list_U_1_i, list_U_2_i, N)
        output_val_list('Коэффициент затухания', list_K_i)
        list_E_i_1 = count_level_info_signal(buff_lst_3, list_K_i, N)
        output_val_list('Рассчитанное значение "сигнал/шум"', list_E_i_1)
        val_W_c = find_W(list_E_i_1, list_A_i, list_k_i, N, count=3)
        if val_W_c > val_W_n:
            print('Необходимо использовать средства пассивной и активной защиты!!!\n')

if __name__ == '__main__':

    main()