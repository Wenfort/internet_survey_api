# Как развернуть проект
+ git clone https://github.com/Wenfort/internet_survey_api.git
+ cd internet_survey_api
+ Создать виртуальное окружение
+ pip install -r requirements.txt
+ python manage.py makemigrations
+ python manage.py migrate
+ python manage.py createsuperuser
+ python manage.py runserver

# Документация API
## Получение Token
#### Метод: GET
#### URL: http://127.0.0.1:8000/api/log/
#### Пример JSON запроса:
> {  
> &nbsp;&nbsp;&nbsp;&nbsp;"username": "admin",  
> &nbsp;&nbsp;&nbsp;&nbsp;"password": "pass"  
> }

## Создать новый опрос
#### Метод: POST
#### URL: http://127.0.0.1:8000/api/survey/
#### Пример JSON запроса:
> {  
> &nbsp;&nbsp;&nbsp;&nbsp;"name": "Имя опроса",  
> &nbsp;&nbsp;&nbsp;&nbsp;"start_date": "2021-12-05T10:00",  
> &nbsp;&nbsp;&nbsp;&nbsp;"end_date": "2021-12-06T10:00",  
> &nbsp;&nbsp;&nbsp;&nbsp;"description": "Описание опроса"  
> }

## Изменение опроса
#### Метод: PUT
#### URL: http://127.0.0.1:8000/api/survey/[id опроса]/
#### Пример JSON запроса:
> {  
> &nbsp;&nbsp;&nbsp;&nbsp;"name": "Новое имя опроса",  
> &nbsp;&nbsp;&nbsp;&nbsp;"end_date": "2029-12-0T10:00",  
> &nbsp;&nbsp;&nbsp;&nbsp;"description": "Новое описание опроса"  
> }  

Примечание:   
+ после создания опроса дату старта изменить нельзя.

## Удалить опрос  
#### Метод: DELETE  
#### URL: http://127.0.0.1:8000/api/survey/[id опроса]/  

## Получение всех опросов  
#### Метод: GET  
#### URL: http://127.0.0.1:8000/api/survey/  

## Получение всех активных опросов:
#### Метод: GET
#### URL: http://127.0.0.1:8000/api/active_survey/

## Получение всех вопросов
#### Метод: GET
#### URL: http://127.0.0.1:8000/api/question/

## Создать новый вопрос
#### Метод: POST
#### URL: http://127.0.0.1:8000/api/question/
#### Пример JSON запроса:
> {  
> &nbsp;&nbsp;&nbsp;&nbsp;"text": "Текст вопроса",  
> &nbsp;&nbsp;&nbsp;&nbsp;"type": 1,  
> &nbsp;&nbsp;&nbsp;&nbsp;"survey": 5  
}  
    
Примечание:
+ type - тип вопроса. В данный момент реализованы 3 типа (1 - выбор одного варианта, 2 - выбор нескольких вариантов, 3 - ввод текста)
+ survey - id опроса, к которому относится вопрос

## Изменить вопрос
#### Метод: PUT
#### URL: http://127.0.0.1:8000/api/question/[id вопроса]/
#### Пример JSON запроса:
> {  
> &nbsp;&nbsp;&nbsp;&nbsp;"text": "Новый текст вопроса",  
> &nbsp;&nbsp;&nbsp;&nbsp;"type": 2,  
> &nbsp;&nbsp;&nbsp;&nbsp;"survey": 6  
}  
    
Примечание:
+ type - тип вопроса. В данный момент реализованы 3 типа (1 - выбор одного варианта, 2 - выбор нескольких вариантов, 3 - ввод текста)
+ survey - id опроса, к которому относится вопрос

## Удалить вопрос
#### Метод: DELETE
#### URL: http://127.0.0.1:8000/api/question/[id вопроса]/

## Создать новый вариант ответа
#### Метод: POST
#### URL: http://127.0.0.1:8000/api/choice/
#### Пример JSON запроса:
> {  
> &nbsp;&nbsp;&nbsp;&nbsp;"text": "Текст ответа",  
> &nbsp;&nbsp;&nbsp;&nbsp;"question": 5  
}  
    
Примечание:
+ question - id вопроса, к которому относится вариант ответа

## Изменить вариант ответа
#### Метод: PUT
#### URL: http://127.0.0.1:8000/api/choice/[id варианта ответа]/
#### Пример JSON запроса:
> {  
> &nbsp;&nbsp;&nbsp;&nbsp;"text": "Новый текст ответа",  
> &nbsp;&nbsp;&nbsp;&nbsp;"question": 6  
> }  
    
Примечание:
+ question - id вопроса, к которому относится вариант ответа

## Удалить вариант ответа
#### Метод: DELETE
#### URL: http://127.0.0.1:8000/api/choice/[id варианта ответа]/

## Посмотреть все пройденные опросы всех пользователей
#### Метод: GET
#### URL: http://127.0.0.1:8000/api/user_choice/

## Посмотреть все пройденные опросы конкретного пользователя
#### Метод: GET
#### URL: http://127.0.0.1:8000/api/user_choice/[id пользователя]/

## Пользователь делает выбор
#### Метод: POST
#### URL: http://127.0.0.1:8000/api/user_makes_choice/
#### Пример JSON запроса:
> {  
> &nbsp;&nbsp;&nbsp;&nbsp;"survey": 5,  
> &nbsp;&nbsp;&nbsp;&nbsp;"question": 4,  
> &nbsp;&nbsp;&nbsp;&nbsp;"choice": 1,  
> &nbsp;&nbsp;&nbsp;&nbsp;"respondent": 1  
> }  
    
Примечание:
+ survey - id опроса, в котором учавствует пользователь
+ question - id вопроса, на который отвечает пользователь
+ choice - id ответа, который выбрал пользователь
+ respondent - id пользователя

## Пользователь меняет выбор
#### Метод: PUT
#### URL: http://127.0.0.1:8000/api/user_makes_choice/[id сделанного пользователем ответа]/
#### Пример JSON запроса:
> {  
> &nbsp;&nbsp;&nbsp;&nbsp;"survey": 5,  
> &nbsp;&nbsp;&nbsp;&nbsp;"question": 4,  
> &nbsp;&nbsp;&nbsp;&nbsp;"choice": 2,  
> &nbsp;&nbsp;&nbsp;&nbsp;"respondent": 1  
> }  
    
Примечание:
+ survey - id опроса, в котором учавствует пользователь
+ question - id вопроса, на который отвечает пользователь
+ choice - id ответа, который выбрал пользователь
+ respondent - id пользователя
