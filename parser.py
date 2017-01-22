import lxml.html as html
from pandas import DataFrame

# page = html.parse(string_x % (main_domain_stat))
f = open('text.txt', 'w')

weather_list = list()
weather = list()


############################################################3
def parser_smile():
    class_table = 'table table-bordered table-striped'
    main_domain_stat = 'http://apps.timwhitlock.info/emoji/tables/unicode'
    q=int()
    page = html.parse(main_domain_stat)
    e = page.getroot().find_class(class_table)
    for i in e:
        # f.write('_____________________')
        t = i.getchildren()
        m= t[1]
        for i in m:
           q=q+1
           f.write(i[7].text_content())

    # for j in range(len(t)):
    #     m = j.text_content()
    #     # m = m.text
    #     f.write(''+m)
#############################################################
def parser_weather():
    class_table = 'forecastTable'
    main_domain_stat = 'http://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A3%D0%BB%D1%8C%D1%8F%D0%BD%D0%BE%D0%B2%D1%81%D0%BA%D0%B5'
    page = html.parse(main_domain_stat)
    e = page.getroot().find_class(class_table)
    for i in e[0]:
        c='0000'
        # print c
        i= i.getchildren()
        # print i
        for j in i[1]:
             weather_list.append(j.text_content())
    weather.append(weather_list[7])
    weather.append((weather_list[9]))
    return weather




#############################################################

f.close()

