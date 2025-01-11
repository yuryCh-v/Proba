from cProfile import label
from gettext import textdomain

from kivy.app import App
from kivy.uix.label import Label
class MainApp(App):
    def build(self):
        label = Label(text = 'Состав',
                      size_hint = (.5, .5),
                      pos_hint = {'center_x': .5, 'center_y': .5})
        return label


xv = {'С', 'Е', 'П', 'Л', 'К'}
lv = {'Б', 'ОС', 'ЛП', 'ИВ', 'ОЛС', 'ОЛЧ'}
koef = set('0123456789+')


def sostav_out(sost):  # расписывает состав по составляющим элементам
    i = 0
    kof = ''
    por = ''
    sum_kof = 0
    el = []
    el_all = []
    for ch in sost:
        if (ch in koef):
            if (por != ''):
                print(por)
                if not por in xv.union(lv):
                    print('Порода ' + por + ' отсутсвует в справочнике')
                el = el + [por]
                el_all = el_all + [el]
                el = []
            kof = kof + ch
            if kof == '+':
                kof = '0'
            por = ''
        else:
            if kof != '':
                print(kof)
                el = [kof]
                sum_kof = sum_kof + int(kof)
            kof = ''
            por = por + ch
            if (i == len(sost) - 1):
                print(por)
                el = el + [por]
                el_all = el_all + [el]
                if not por in xv.union(lv):
                    print('Порода ' + por + ' отсутсвует в справочнике')
        i += 1
    print(el_all)
    if sum_kof % 10 != 0:
        print('Сумма коэффициентов = ' + str(sum_kof))
        #        print(el_all[2][1])
        result = el_all
    return el


sostav_out('10С+ЛП')  # вызов функции с аргуменом - состав для разложения
input()


if __name__ == '__main__':
    app = MainApp()
    app.run()

