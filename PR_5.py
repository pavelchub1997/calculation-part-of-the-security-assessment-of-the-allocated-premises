from main import *
from PR_2 import *

def val_U_in_point_proved_izm(list_U_s_i_h, list_U_h):

    res_lst = []
    for i in range(2): res_lst.append(round((20*log10(sqrt(calc(list_U_s_i_h[i]) - calc(list_U_h[i])))), 3))
    return res_lst

def count_sqr_zvuk_davl_1(list_L_i, list_L_H_i):

    list_K_i = []
    for i in range(2): list_K_i.append(round((list_L_i[i] - list_L_H_i[i]), 3))
    return list_K_i

def count_velich_udel_coeff_zatuh_naved_sign(list_U_1, list_U_2, val_l):

    res_lst = []
    for i in range(2): res_lst.append(round(((20*log10(count(list_U_1[i])/count(list_U_2[i])))/val_l), 3))
    return res_lst

def count_max_length_prob(list_P_i, list_K_y):

    res_lst = []
    val = int(input('Введите 0, если не имеются видеоконтрольных устройств, либо 1, если имеются: '))
    if val == 1:
        for i in range(2): res_lst.append(round(((list_P_i[i]+10)/list_K_y[i]), 3))
    elif val == 0:
        for i in range(2): res_lst.append(round((list_P_i[i]/list_K_y[i]), 3))
    return res_lst

def srav_count_max_length_with_min_R(list_R, min_R):

    val = list_R[0]
    for i in range(1, 2):
        if val < list_R[i]:
            val = list_R[i]
    if val < min_R: print('Информация защищена от утечки за счет наводок')
    else: print('Информация не защищена от утечки за счет наводок')
if __name__ == '__main__':

    list_U_s_i_h, list_U_h, list_U_1, list_U_2, min_R_KZ, val_l = [35, 32], [22, 21], [33, 30], [12, 10], 6.5, 6
    list_U_c_i = val_U_in_point_proved_izm(list_U_s_i_h, list_U_h)
    print('********************************')
    output_val_list('Рассчитанные значения напряжения сигнала в точке проведения измерений для каждой частотной компоненты', list_U_c_i)
    list_P_i = count_sqr_zvuk_davl_1(list_U_c_i, list_U_h)
    output_val_list('Рассчитанные значения показателей защищенности в точке проведения измерений для каждой из частотных компонент', list_P_i)
    list_K_y = count_velich_udel_coeff_zatuh_naved_sign(list_U_1, list_U_2, val_l)
    output_val_list('Рассчитанные значения величины удельного коэффициента затухания наведенных сигналов в исследуемой цепи', list_K_y)
    list_R = count_max_length_prob(list_P_i, list_K_y)
    output_val_list('Рассчитанные значения максимальной длины пробега исследуемой цепи для каждой из частот', list_R)
    srav_count_max_length_with_min_R(list_R, min_R_KZ)