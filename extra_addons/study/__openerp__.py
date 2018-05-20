# -*- coding: utf-8 -*-

{
    'name': 'Study module',
    # name (str, обязательное)
    # удобочитаемое имя модуля

    'description': "Study module",
    # description (str)
    # Расширенное описание модуля, в формате reStructuredText

    'author':   'Alexa',
    # author (str)
    # Имя автора модуля

    'maintainer': 'Simbioz Holding',
    'summary': '#SimbiozOdooDevCourse',
    'category': 'Tools',
    # category (str, по умолчанию: Uncategorized)
    # Категория классификации в Odoo, примерная область применения модуля.

    'website': 'http://www.simbioz.ua',
    # website (str)
    # URL веб-сайта автора модуля

    'version': '08.0.2.1.0',
    # version (str)
    # Версия этого модуля

    'license': 'AGPL-3',
    # license (str, по-умолчанию: AGPL-3)
    # Лицензия на распространение для модуля

    'sequence': 1,
    'depends': ['base', 'web'],
    # depends (list(str))
    # Модули Odoo, которые должны быть загружены для работы данного модуля, либо потому, что этот модуль использует
    # их функции, либо потому, что он изменяет ресурсы, которые они определяют.
    # Когда модуль установлен, все его зависимости устанавливаются перед ним.
    # Аналогично, зависимости загружаются до загрузки модуля.

    'data': [
        'views/study.xml',
        'views/study_menu.xml',
            ],
    # data (list(str))
    # Список файлов данных, которые необходимо всегда устанавливать или обновлять с помощью модуля.
    # Список путей из корневого каталога модуля.

    'installable': True,
    'auto_install': False,
    # auto_install (bool, по умолчанию: False)
    # Если значение True, этот модуль будет автоматически установлен, если все его зависимости установлены.
    # Он обычно используется для «связующих модулей», реализующих синергетическую интеграцию
    # между двумя независимыми друг от друга модулями.
}