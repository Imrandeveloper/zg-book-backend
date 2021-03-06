# Generated by Django 2.0.4 on 2018-04-05 13:22

import uuid

import django.contrib.postgres.fields.jsonb
import django.utils.timezone
from django.db import migrations, models

import books.utils
import books.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('country', models.CharField(help_text='Список через запятую [ISO-3166-1]', max_length=255,
                                             verbose_name='Страна(ы)')),
                ('link', models.URLField(blank=True, verbose_name='Страница на сайте')),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Возраст')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(blank=True, default=0, verbose_name='Позиция')),
                ('structure', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=[], validators=[
                    books.validators.JsonSchemaValidator(schema={'$schema': 'http://json-schema.org/draft-04/schema#',
                                                                 'definitions': {'image_lvl1': {'properties': {
                                                                     'content': {'items': {'anyOf': [
                                                                         {'$ref': '#/definitions/textfragment'},
                                                                         {'$ref': '#/definitions/image_lvl2'}]},
                                                                                 'type': 'array'},
                                                                     'id': {'type': 'integer'},
                                                                     'title': {'type': 'string'},
                                                                     'type': {'enum': ['image']}}, 'required': ['type',
                                                                                                                'id',
                                                                                                                'title',
                                                                                                                'content']},
                                                                                 'image_lvl2': {'properties': {
                                                                                     'id': {'type': 'integer'},
                                                                                     'type': {'enum': ['image']}},
                                                                                                'required': ['type',
                                                                                                             'id']},
                                                                                 'textfragment': {'properties': {
                                                                                     'id': {'type': 'string'}, 'type': {
                                                                                         'enum': ['textfragment']}},
                                                                                                  'required': ['type',
                                                                                                               'id'],
                                                                                                  'type': 'object'}},
                                                                 'items': {
                                                                     'anyOf': [{'$ref': '#/definitions/textfragment'},
                                                                               {'$ref': '#/definitions/image_lvl1'}]},
                                                                 'type': 'array'})], verbose_name='Структура')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Author',
                                             verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ('position', 'id'),
            },
        ),
        migrations.CreateModel(
            name='BookLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified',
                 models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата последнего изменения')),
                ('hidden', models.BooleanField(default=True, verbose_name='Скрыт')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_languages',
                                           to='books.Book', verbose_name='Книга')),
            ],
            options={
                'verbose_name': 'Перевод',
                'verbose_name_plural': 'Переводы',
                'ordering': ('-last_modified',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='img/', verbose_name='Файл изображения')),
                ('position', models.IntegerField(blank=True, default=0, verbose_name='Позиция')),
                ('type', models.CharField(choices=[('preview', 'Превью книги'), ('body', 'Содержимое')], max_length=10,
                                          verbose_name='Тип')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                             to='books.Author', verbose_name='Автор')),
                ('book',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='books.Book',
                                   verbose_name='Книга')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(
                    choices=[('aa', 'aa - Afar'), ('ab', 'ab - Abkhazian'), ('ae', 'ae - Avestan'),
                             ('af', 'af - Afrikaans'), ('ak', 'ak - Akan'), ('am', 'am - Amharic'),
                             ('an', 'an - Aragonese'), ('ar', 'ar - Arabic'), ('as', 'as - Assamese'),
                             ('av', 'av - Avaric'), ('ay', 'ay - Aymara'), ('az', 'az - Azerbaijani'),
                             ('ba', 'ba - Bashkir'), ('be', 'be - Belarusian'), ('bg', 'bg - Bulgarian'),
                             ('bh', 'bh - Bihari languages'), ('bi', 'bi - Bislama'), ('bm', 'bm - Bambara'),
                             ('bn', 'bn - Bengali'), ('bo', 'bo - Tibetan'), ('br', 'br - Breton'),
                             ('bs', 'bs - Bosnian'), ('ca', 'ca - Catalan'), ('ce', 'ce - Chechen'),
                             ('ch', 'ch - Chamorro'), ('co', 'co - Corsican'), ('cr', 'cr - Cree'),
                             ('cs', 'cs - Czech'), ('cu', 'cu - Church Slavic'), ('cv', 'cv - Chuvash'),
                             ('cy', 'cy - Welsh'), ('da', 'da - Danish'), ('de', 'de - German'), ('dv', 'dv - Dhivehi'),
                             ('dz', 'dz - Dzongkha'), ('ee', 'ee - Ewe'), ('el', 'el - Modern Greek (1453-)'),
                             ('en', 'en - English'), ('eo', 'eo - Esperanto'), ('es', 'es - Spanish'),
                             ('et', 'et - Estonian'), ('eu', 'eu - Basque'), ('fa', 'fa - Persian'),
                             ('ff', 'ff - Fulah'), ('fi', 'fi - Finnish'), ('fj', 'fj - Fijian'),
                             ('fo', 'fo - Faroese'), ('fr', 'fr - French'), ('fy', 'fy - Western Frisian'),
                             ('ga', 'ga - Irish'), ('gd', 'gd - Scottish Gaelic'), ('gl', 'gl - Galician'),
                             ('gn', 'gn - Guarani'), ('gu', 'gu - Gujarati'), ('gv', 'gv - Manx'), ('ha', 'ha - Hausa'),
                             ('he', 'he - Hebrew'), ('hi', 'hi - Hindi'), ('ho', 'ho - Hiri Motu'),
                             ('hr', 'hr - Croatian'), ('ht', 'ht - Haitian'), ('hu', 'hu - Hungarian'),
                             ('hy', 'hy - Armenian'), ('hz', 'hz - Herero'),
                             ('ia', 'ia - Interlingua (International Auxiliary Language Association)'),
                             ('id', 'id - Indonesian'), ('ie', 'ie - Interlingue'), ('ig', 'ig - Igbo'),
                             ('ii', 'ii - Sichuan Yi'), ('ik', 'ik - Inupiaq'), ('io', 'io - Ido'),
                             ('is', 'is - Icelandic'), ('it', 'it - Italian'), ('iu', 'iu - Inuktitut'),
                             ('ja', 'ja - Japanese'), ('jv', 'jv - Javanese'), ('ka', 'ka - Georgian'),
                             ('kg', 'kg - Kongo'), ('ki', 'ki - Kikuyu'), ('kj', 'kj - Kuanyama'),
                             ('kk', 'kk - Kazakh'), ('kl', 'kl - Kalaallisut'), ('km', 'km - Central Khmer'),
                             ('kn', 'kn - Kannada'), ('ko', 'ko - Korean'), ('kr', 'kr - Kanuri'),
                             ('ks', 'ks - Kashmiri'), ('ku', 'ku - Kurdish'), ('kv', 'kv - Komi'),
                             ('kw', 'kw - Cornish'), ('ky', 'ky - Kirghiz'), ('la', 'la - Latin'),
                             ('lb', 'lb - Luxembourgish'), ('lg', 'lg - Ganda'), ('li', 'li - Limburgan'),
                             ('ln', 'ln - Lingala'), ('lo', 'lo - Lao'), ('lt', 'lt - Lithuanian'),
                             ('lu', 'lu - Luba-Katanga'), ('lv', 'lv - Latvian'), ('mg', 'mg - Malagasy'),
                             ('mh', 'mh - Marshallese'), ('mi', 'mi - Maori'), ('mk', 'mk - Macedonian'),
                             ('ml', 'ml - Malayalam'), ('mn', 'mn - Mongolian'), ('mr', 'mr - Marathi'),
                             ('ms', 'ms - Malay (macrolanguage)'), ('mt', 'mt - Maltese'), ('my', 'my - Burmese'),
                             ('na', 'na - Nauru'), ('nb', 'nb - Norwegian Bokmål'), ('nd', 'nd - North Ndebele'),
                             ('ne', 'ne - Nepali (macrolanguage)'), ('ng', 'ng - Ndonga'), ('nl', 'nl - Dutch'),
                             ('nn', 'nn - Norwegian Nynorsk'), ('no', 'no - Norwegian'), ('nr', 'nr - South Ndebele'),
                             ('nv', 'nv - Navajo'), ('ny', 'ny - Nyanja'), ('oc', 'oc - Occitan (post 1500)'),
                             ('oj', 'oj - Ojibwa'), ('om', 'om - Oromo'), ('or', 'or - Oriya (macrolanguage)'),
                             ('os', 'os - Ossetian'), ('pa', 'pa - Panjabi'), ('pi', 'pi - Pali'),
                             ('pl', 'pl - Polish'), ('ps', 'ps - Pushto'), ('pt', 'pt - Portuguese'),
                             ('qu', 'qu - Quechua'), ('rm', 'rm - Romansh'), ('rn', 'rn - Rundi'),
                             ('ro', 'ro - Romanian'), ('ru', 'ru - Russian'), ('rw', 'rw - Kinyarwanda'),
                             ('sa', 'sa - Sanskrit'), ('sc', 'sc - Sardinian'), ('sd', 'sd - Sindhi'),
                             ('se', 'se - Northern Sami'), ('sg', 'sg - Sango'), ('si', 'si - Sinhala'),
                             ('sk', 'sk - Slovak'), ('sl', 'sl - Slovenian'), ('sm', 'sm - Samoan'),
                             ('sn', 'sn - Shona'), ('so', 'so - Somali'), ('sq', 'sq - Albanian'),
                             ('sr', 'sr - Serbian'), ('ss', 'ss - Swati'), ('st', 'st - Southern Sotho'),
                             ('su', 'su - Sundanese'), ('sv', 'sv - Swedish'), ('sw', 'sw - Swahili (macrolanguage)'),
                             ('ta', 'ta - Tamil'), ('te', 'te - Telugu'), ('tg', 'tg - Tajik'), ('th', 'th - Thai'),
                             ('ti', 'ti - Tigrinya'), ('tk', 'tk - Turkmen'), ('tl', 'tl - Tagalog'),
                             ('tn', 'tn - Tswana'), ('to', 'to - Tonga (Tonga Islands)'), ('tr', 'tr - Turkish'),
                             ('ts', 'ts - Tsonga'), ('tt', 'tt - Tatar'), ('tw', 'tw - Twi'), ('ty', 'ty - Tahitian'),
                             ('ug', 'ug - Uighur'), ('uk', 'uk - Ukrainian'), ('ur', 'ur - Urdu'), ('uz', 'uz - Uzbek'),
                             ('ve', 've - Venda'), ('vi', 'vi - Vietnamese'), ('vo', 'vo - Volapük'),
                             ('wa', 'wa - Walloon'), ('wo', 'wo - Wolof'), ('xh', 'xh - Xhosa'), ('yi', 'yi - Yiddish'),
                             ('yo', 'yo - Yoruba'), ('za', 'za - Zhuang'), ('zh', 'zh - Chinese'), ('zu', 'zu - Zulu')],
                    max_length=2, unique=True, verbose_name='Код ISO-639-1')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('flag', models.FileField(help_text='*.svg', upload_to='flag/', validators=[books.utils.validate_svg],
                                          verbose_name='Флаг')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='TextFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(blank=True, default=uuid.uuid4, verbose_name='UUID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('type', models.CharField(choices=[('title', 'Заглавие'), ('ann', 'Анотация'), ('body', 'Содержимое')],
                                          default='body', max_length=10, verbose_name='Тип')),
                ('book',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='Книга')),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Language',
                                           verbose_name='Язык')),
            ],
            options={
                'verbose_name': 'Фрагмент текста',
                'verbose_name_plural': 'Фрагменты текста',
                'ordering': ('book', 'lang', 'uuid'),
            },
        ),
        migrations.AddField(
            model_name='booklanguage',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Language',
                                    verbose_name='Язык'),
        ),
        migrations.AddField(
            model_name='book',
            name='languages',
            field=models.ManyToManyField(through='books.BookLanguage', to='books.Language',
                                         verbose_name='Доступные языки'),
        ),
        migrations.AlterUniqueTogether(
            name='textfragment',
            unique_together={('lang', 'uuid')},
        ),
        migrations.AlterUniqueTogether(
            name='booklanguage',
            unique_together={('lang', 'book')},
        ),
    ]
