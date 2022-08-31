# Интернет магазин
___

*(еще в разработке)*

Этот проект представляет из себя сервер интернет магазина
написанный с использованием фреймворка __Django__. 

В проекте есть такие сущности как ***категория товара*** 
(одна категория может наследоваться от другой категории, тем  самым делая 
сортировку товаров более детальной), ***товар***, ***фотография товара*** 
(вынесена в отдельную таблицу в бд, можно делать неограниченное количество 
фотографий для каждого товара),  ***производитель***, ***покупатель***, 
***адрес*** (для покупателя), ***корзина***, ***заказ***, ***статус заказа***,
***элемент(товар) заказа***

У каждой сущности есть все необходимые атрибуты, но если их не хватает, то 
без проблем можно её расширить.


## Структура проекта
___
```online_store_back/``` - исходный код 

## Структура исходников
___
- ```apps``` - приложения
   - ```account``` - аккаунт покупателя
   - ```address``` - список адресов для доставки
   - ```cart``` - корзина для товаров
   - ```catalog``` - каталог товаров, включая распределение товаров 
  по категориям и производителям 
   - ```order``` - заказы
- ```config``` - настройки
- ```media``` - сюда будут попадать все изображения для товаров и находиться
в папках по названиям категорий, в будующем возможно будут и другие файлы
- ```resources``` - html, css, статические изображения
- ```manage.py``` - запуск и управление сервером