# test_unified_information_system
Aptitude test with to task. First task in task.py in root. Second task in folder task2 (Django ORM project).


### First task
The 'Account' user collection contains documents.
```
   {
        'number': '7800',
        'name': 'Пользователь №',
        'sessions': [
            {
                'created_at': ISODate('2016-01-01T00:00:00'),
                'session_id': '6QBnQhFGgDgC2FDfGwbgEaLbPMMBofPFVrVh9Pn2quooAcgxZc',
                'actions': [
                    {
                        'type': 'read',
                        'created_at': ISODate('2016-01-01T01:20:01'),
                    },
                    {
                    ...
                          ]
           }  
                    ]
   }
```
 For these documents, you need to write an aggregation query that will display the last action for each user and the total for each of the 'actions' types. The resulting data should be list of documents like.
```
    {
        'number': '7800000000000',
        'actions': [
            {
                'type': 'create',
                'last': 'created_at': ISODate('2016-01-01T01:33:59'),
                'count': 12,
            },
            {
                'type': 'read',
                'last': 'created_at': ISODate('2016-01-01T01:21:13'),
                'count': 12,
            },
            .....
                   ]
    }

```
### Second task
There are two data tables: accrual and payment. Both collections have fields:
- id
- date (date)
- month (month)
It is necessary to write a function that will make a request for payments and find for each payment the debt that will be paid by them. A payment can only pay off a debt that has an earlier date. One payment can only pay one debt, and each debt can only be paid in one payment. The payment must first select a debt with the same month (field month). If there is none, then the oldest by date (date field) debt.The result should be a table of found matches, as well as a list of payments that did not find a debt.

### Tested
on Ubuntu 20.04 and is compatable with
```Python==3.8.10
asgiref==3.5.2
backports.zoneinfo==0.2.1
Django==4.1
mongoengine==0.24.2
pymongo==4.2.0
sqlparse==0.4.2
```

### Build

#### Git

Clone the repository
```
git clone https:https://github.com/Alexander671/test_unified_information_system/
```

#### Dependencies

Install, using `pip`:

```
pip install -r requirements.txt
```

Makemigrations in Django ORM task
```
python3 manage.py makemigrations
python3 manage.py migrate
```
