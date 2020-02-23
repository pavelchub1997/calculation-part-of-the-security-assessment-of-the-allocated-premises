from main import *
from PR_2 import *

def okt_level_info_signal(list_U_c, N):

    res_lst = []
    for i in range(N): res_lst.append(0.7*list_U_c[i])
    return res_lst

def coeff_K_z(len_wave, val_R, val_D):

    if val_D > 0 and val_D <= (len_wave/(2*pi)):
        if val_R <= (len_wave/(2*pi)): return pow(round((val_D/val_R), 2), 3)
        elif (len_wave/(2*pi)) < val_R and val_R <= 6*len_wave: return round(((2*pi*pow(val_D, 3))/(len_wave*pow(val_D, 3))), 2)
        elif val_R > 6*len_wave: return round(((2*pi*pow(val_D, 3))/(6*pow(len_wave, 2)*val_R)), 2)
    elif val_D > (len_wave/(2*pi)) and val_D <= 6*len_wave:
        if val_R <= (len_wave/(2*pi)): return round(((len_wave*pow(val_D, 2))/(2*pi*pow(val_D, 3))), 2)
        elif (len_wave/(2*pi)) < val_R and val_R <= 6*len_wave: return round(pow((val_D/val_R), 2), 2)
        elif val_R > 6*len_wave: return round(((pow(val_D, 2))/(6*len_wave*val_R)), 2)
    elif val_D > 6*len_wave:
        if val_R <= (len_wave/(2*pi)): return round(((6*pow(len_wave, 2)*val_D)/(2*pi*pow(val_R, 3))), 2)
        elif (len_wave/(2*pi)) < val_R and val_R <= 6*len_wave: return round(((6*len_wave*val_D)/(pow(val_R, 2))), 2)
        elif val_R > 6*len_wave: return round((val_D/val_R), 2)

def calc_len_wave(val_F):

    return round((300/val_F), 2)

def calc_napr_field_info_signal(list_U_c_priv, coeff_K_z, coeff_K_ant, N):

    res_list = []
    for i in range(N): res_list.append(round((list_U_c_priv[i]/coeff_K_z)*coeff_K_ant, 3))
    return res_list

def station_type_of_razv(val_f):

    if val_f >= 5.8*pow(10, 3) and val_f < 5*pow(10, 4):
        val_x = round(4*((1.18/(pow((0.78*log10(val_f)), (2/3))))-1), 3)
        return pow(10, val_x)
    elif val_f >= 5*pow(10, 4) and val_f < 3*pow(10, 5):
        val_x = round((0.636*log10(val_f)-5), 3)
        return pow(10, val_x)
    else: return 0.03

def port_voz_sred_razv(val_f):

    if val_f >= 5.8*pow(10, 3) and val_f < 18*pow(10, 3):
        val_x = round(4*((1.18/(pow((0.78*log10(val_f)), (2/3))))-1), 3)
        return pow(10, val_x)
    elif val_f >= 18*pow(10, 3) and val_f < 3*pow(10, 5):
        val_x = round((0.505*log10(val_f)-4.03), 3)
        return pow(10, val_x)
    else:
        val_x = round((0.7*log10(val_f)-5.09), 3)
        return pow(10, val_x)

def port_nos_sred_razv(val_f):

    if val_f >= 5.8*pow(10, 3) and val_f < 3*pow(10, 4):
        val_x = round((0.682*log10(val_f) - 4.26), 3)
        return pow(10, val_x)
    elif val_f >= 3*pow(10, 4) and val_f < 3*pow(10, 5):
        val_x = round((0.29*log10(val_f) - 2.5), 3)
        return pow(10, val_x)
    else:
        val_x = round((0.66*log10(val_f) - 4.53), 3)
        return pow(10, val_x)

def napr_elect_magn_shum(list_F_i, val_E_sh, N):

    res_lst = []
    for i in range(N): res_lst.append(round(val_E_sh*sqrt(list_F_i[i]*pow(10, -3)), 3))
    return res_lst

def func_for_calc_norm_napr(val_E_sh, list_F_i, list_E_c, list_A_i, list_k_i, msg, N):

    list_E_h_oct = napr_elect_magn_shum(list_F_i, val_E_sh, N)
    output_val_list(
        'Напряженность электромагнитного шума для электрической составляющей с использованием ' + msg,
        list_E_h_oct)
    list_E = count_level_info_signal(list_E_c, list_E_h_oct, N)
    output_val_list('Информативный сигнал/шум для ' + msg, list_E)
    if check(list_E) == 0: print('******************\nДля всех октав норма противодействия выполняется!!!\n******************************\n')
    else:
        val_W = find_W(list_E, list_A_i, list_k_i, N, count=3)
        if val_W > 0.3: print('Норма противодействия не выполняется!!! Необходимо использовать средства активной защиты')
        else: print('Норма противодействия выполняется!!!')

def method_calc_norm_electr_magn_shum(val_F, list_F_i, list_E_c, list_A_i, list_k_i, N):

    val_f = val_F*pow(10, 3)
    while True:
        print('\n1)Cтационарный СР\n2)Портативное возимое СР\n3)Портативное носимое СР\n0)Закончить расчет нормированных электромагнитных шумов')
        key = int(input('\nВведите значение значение ключа: '))
        if key == 1:
            val_E_sh = station_type_of_razv(val_f)
            print('\n*****************************\nЗначение нормированного шума для стационарных СР\n', val_E_sh,
                  '\n*****************************\n')
            func_for_calc_norm_napr(val_E_sh, list_F_i, list_E_c, list_A_i, list_k_i, 'стационарных СР', N)
        elif key == 2:
            val_E_sh = port_voz_sred_razv(val_f)
            print('\n*****************************\nЗначение нормированного шума для возимых СР\n', val_E_sh,
                  '\n*****************************\n')
            func_for_calc_norm_napr(val_E_sh, list_F_i, list_E_c, list_A_i, list_k_i, 'возимых СР', N)
        elif key == 3:
            val_E_sh = port_nos_sred_razv(val_f)
            print('\n*****************************\nЗначение нормированного шума для носимых СР\n', val_E_sh,
                  '\n*****************************\n')
            func_for_calc_norm_napr(val_E_sh, list_F_i, list_E_c, list_A_i, list_k_i, 'носимых СР', N)
        elif key == 0: break

def menu():

    N = int(input('Введите количество октав: '))
    list_U_sh = input_val_list('Введите значения измеренного напряжения "сигнал/шум"', N)
    list_U_h = input_val_list('Введите значение измеренного напряжения шума', N)
    list_U_c = info_signal(list_U_sh, list_U_h, N)
    list_U_c = okt_level_info_signal(list_U_c)
    output_val_list('Значения октавного уровня информационного сигнала', list_U_c)
    list_L_i = input_val_list('Введите значения уровня звукового давления', N)
    list_L_n = input_val_list('Введите значение нормированного уровня звукового давления', N)
    list_K_i = count_sqr_zvuk_davl(list_L_i, list_L_n, N)
    output_val_list('Значение степени превышения создаваемого акустического давления над нормированным звуковым давлением', list_K_i)
    list_U_c_priv = count_level_info_signal(list_U_c, list_K_i, N)
    output_val_list('Значения октавного уровня информативного сигнала', list_U_c_priv)
    val_F = float(input('***********************\nВведите значение частоты обнаруженного сигнала автогенератора F (МГц)\n'))
    print('\n********************************')
    len_wave = calc_len_wave(val_F)
    print('\n******************************\nДлина волны имеет следующее значение\n', len_wave, '\n***********************************')
    val_R = float(input('********************\nВведите значение размера антенны\n'))
    print('***************************\n')
    val_D = float(input('********************\nВведите значение удаления границы КЗ от корпуса ТС\n'))
    print('*****************************\n')
    val_K_z = coeff_K_z(len_wave, val_R*2, val_D)
    print('*****************************\n\nЗначение коффициента затухания\n', val_K_z,
          '\n*****************************\n')
    val_coeff_K_ant = float(input('**************************\nВведите значение колибровочного коэффициента антенны\n'))
    print('\n****************************\n')
    list_E_c = calc_napr_field_info_signal(list_U_c_priv, val_K_z, val_coeff_K_ant, N)
    output_val_list('Значение E_c', list_E_c)
    list_F_i = input_val_list('Введите значение широты полосы частот (Гц)', N)
    list_A_i = input_val_list('Введите значения форматного параметра речи', N)
    list_k_i = input_val_list('Введите значения весового коэффициента', N)
    method_calc_norm_electr_magn_shum(val_F, list_F_i, list_E_c, list_A_i, list_k_i, N)

if __name__ == '__main__':

    menu()