from datetime import datetime
from data.account import Account
from mongoengine import connect

# более простой протокол подключения к mongo,
# чем в pymongo
connect('pyloungedb')

# использование объектов стиля mongoengine 
# в этом задание было не обязательно
a = Account(**    {
        'number': '7800',
        'name': 'Пользователь №',
        'sessions': [
            {
                'created_at':  datetime.fromisoformat('2016-01-01T00:00:00'),
                'session_id': '6QBnQhFGgDgC2FDfGwbgEaLbPMMBofPFVrVh9Pn2quooAcgxZc',
                'actions': [
                    {
                        'type': 'read',
                        'created_at': datetime.fromisoformat('2016-01-01T01:20:01'),
                    },
                    {
                        'type': 'read',
                        'created_at': datetime.fromisoformat('2016-01-01T01:21:13'),
                    },
                    {
                        'type': 'update',
                        'created_at': datetime.fromisoformat('2016-01-01T01:33:59'),
                    }
                ],
            }
        ]
    }
)
a.save()

# в данном пайплайне используется 5 стейджей
# 1 - добавление нового поля
# 2 - свертка списка списков в один список
# 3 - разворачивание списка в набор элементов
# 4 - группировка с подсчетом количества элементов и выделения последнего
# 5 - дополнительная группировка
pipeline = [{"$addFields" : {"actions": "$sessions.actions"}},
            {'$project' : { '_id' : False,
                         'number': True, 
                         'actions' : {
                                 '$reduce': {
                                         'input': '$actions',
                                         'initialValue': [],
                                         'in': {'$concatArrays': ['$$value', '$$this']}
                                     }
                                 }                                    
                         }},
            {'$unwind' : "$actions"},
            {'$group' : { 
                       '_id' :  { 
                            'number': "$number",
                            'type': "$actions.type" 
                               },
                        'count': { '$sum' : 1 },
                        'last': {'$last' : "$actions.created_at"}
                        }
            },
             {'$group' : { 
                       '_id' :  "$_id.number",
                       'actions': { 
                            '$push': { 
                                'type':"$_id.type",
                                'last' : "$last",
                                'count':"$count",
                                    }
                                }
                        }
            }
           ]

# вывод информации по всем пользователям
for acc in Account.objects.aggregate(pipeline):
    print(acc)

# удаление
Account.objects.delete()    