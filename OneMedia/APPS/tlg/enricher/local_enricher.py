# this script service as enricher of channels, should be run locally
from APPS.tlg.dao_layer import retrieve_all_messages, add_anchor_empty

test1 = """**Министерство экономики Пензенской области запустило свой telegram-канал - @minecp_12enzaa. **Здесь будет размещаться актуальная информация о поддержке малого бизнеса, изменениях в налоговом законодательстве и социально-экономическом развитии региона.

#пензенскаяобласть
#экономика

@penzregru"""

test2 = """**В Жуковском открывается юбилейный авиасалон МАКС-2021

**Юбилейный 15-й авиасалон МАКС начинает работу сегодня во вторник, 20 июля в 12-00, в подмосковном Жуковском, выставку откроет президент России Владимир Путин.

Ожидается, что глава государства осмотрит передовые образцы отечественной авиатехники. Затем президент проведет совещание по вопросу реализации ключевых проектов в сфере гражданского авиастроения.

Последние новости о работе выставки, на которой аэрокосмическая отрасль представляет свою продукцию, можно узнать на официальном Telegram-канале авиасалона: https://t.me/aviasalonmaks
"""

test21 = """
**Запись Володина в Telegram о QR-кодах набрала 1 млн просмотров

**Пост спикера Госдумы Вячеслава Володина в его Telegram-канале о законопроектах про QR-коды [набрал](https://rg.ru/2021/12/06/zapis-volodina-v-telegram-o-qr-kodah-nabrala-1-mln-prosmotrov.html) миллион просмотров.

В [сообщении](https://t.me/vv_volodin/220), опубликованном 24 ноября, председатель ГД рассказал о рассмотрении правительственных законопроектов о QR-кодах в общественных местах и на транспорте. Он, в частности, сообщил, что к депутатам поступило более 120 тысяч официальных обращений по данному поводу, еще большее количество отзывов можно найти в социальных сетях.

Для получения обратной связи Володин открыл комментарии под постом, менее чем за сутки он набрал более 307 тыс. откликов. А на данный момент пользователи оставили там более 700 тысяч комментариев. Граждане спорили, соответствуют ли подготовленные кабмином поправки Конституции, да и так ли необходимы предлагаемые ограничения. Сторонники проектов напоминают, что необходимо стимулировать больше россиян вакцинироваться для создания коллективного иммунитета.

Комментируя ранее бурную реакцию пользователей на его сообщение в Telegram-канале, Вячеслав Володин подчеркнул, что депутаты Госдумы хотят услышать мнения граждан РФ. "Если увидим, что идеи и решения, которые нам предлагают принять для корректировки закона, правильные, его улучшат, конечно, будем обсуждать с вами. В итоге закон, надеюсь, станет лучше, более эффективно будет решать проблемы людей", - добавил политик."""

test3 = """
**🏢 Официальные Telegram-каналы госкорпораций и госкомпаний РФ

**@gazprom Газпром
@news_mrg Газпром межрегионгаз
@paogazprom_neft Газпром нефть
@transneftofficial Транснефть
@rosseti_official Россети
@rushydro_official Группа РусГидро
@sberbank Сбербанк
@bankvtb ВТБ
@roscosmos_gk Роскосмос
@rogozin_do Ген. директор Роскосмоса Дмитрий Рогозин
@domrf_life ДОМ.РФ
@corpmspof Корпорация МСП
@oi_press Фонд "Сколково"
@ERDCnews Корпорация развития Дальнего Востока и Арктики
@rfrit Российский фонд развития информационных технологий
@telerzd РЖД
@avtodorgk Автодор
@napochte Почта России
@rusgeology АО Росгеология
@Alrosa_news АЛРОСА
@ao_gtlk Государственная транспортная лизинговая компания
@rosgoscirc Росгосцирк
@doc_brown_channel Российская венчурная компания
@uvznews Уралвагонзавод

ℹ️ @GovInfo** Государство в Telegram**"""


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def getChannelsFromContent(content):
    channel_names = []
    acc = ""
    flag = False
    for char in content:
        if char == '@':
            flag = True
            continue
        if flag and (char.isalpha() or char == '_' or char.isdigit()):
            acc += char
        elif flag:
            if isEnglish(acc):
                channel_names.append(acc)
            acc = ""
            flag = False
    if flag and len(acc) != 0 and isEnglish(acc):
        channel_names.append(acc)
    return channel_names


def getChannelsFromContentFromUrl(content):
    channel_names = []
    url = "https://t.me/"
    occurrences = [i for i in range(len(content)) if content.startswith(url, i)]
    for index in occurrences:
        start = index + len(url)
        acc = ""
        while start < len(content):
            char = content[start]
            if char.isalpha() or char == '_' or char.isdigit():
                acc += char
            else:
                break
            start += 1
        if len(acc) != 0:
            channel_names.append(acc)
    return channel_names


messages = retrieve_all_messages("1458668252")
count = 0

# print(len(messages))
for message in messages:
    content = message[7]
    listToAdd = getChannelsFromContentFromUrl(content) + getChannelsFromContent(content)
    for channel_name in listToAdd:
        add_anchor_empty(channel_name)
        print("added channel_name: " + channel_name + ", count: " + str(count))
    count += 1
    print("----------------------------------------------")

print("count: " + str(count))
