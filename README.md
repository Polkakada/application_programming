База данных видео, хранящая информацию об авторе, жанре, стране производства, название видео и ссылку на него.
Реализована с помощью 5 таблиц(см. db_model)  

Реализован простой пользовательский интерфейс для управления базой данных.
Основная функция-облегчить пользователям работу с базой данных, за счет использования ключевых слов.


Основная программа реализована в виде бесконечного цикла с прерыванием,
 который последовательно принимает от пользователя поток заранее определенных команд. 
Основных команд 5: 
ДОБАВИТЬ-внести видео в базу данных
ПОИСК-поиск по базе данных
ПОКАЗАТЬ-показать все записи в базе данных
ВЫХОД-остановить работу базы данных
СПРАВКА-узнать об основных командах и их функциях.

Так же при выполнении поиска доступны еще 2 команды:
ПОКАЗАТЬ и УДАЛИТЬ, позволяюшие, соответственно, посмотреть результат поиска и удалить найденные данные из базы.

Сбор информации с пользователя выполнен с помощью input(). В местах, где поле является обязательным для заполнения
или требует определенный формат ввода, используется бесконечный цикл с прерыванием.

Для сбора информации используются функции def get_..._information()
Для приведения этой информации к определенному шаблону -- def call_...()
Работа с базой данных выполнено в функциях def ..._video()
Так же используется функция для очистки всей базы -- def remake_db()
и для создания базы данных -- def create_db()
для вывода найденной информации --def output()
так же присутствуют вспомогательные функции, например def yes_or_no()