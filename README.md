/admin доступ к панели администратора. Логин admin, пароль admin

api/directories/date=all - получить все справочники

api/directories/?date=all&page=number - получить указанную страницу. Атрибут page распространяется на любой тип запроса за исключением валидации.

(api/directories/?date=all&page=1)


api/directories/?date=yearmonthday - получить справочники, действующие на дату.

(api/directories/?date=20200225&page=1)


api/units/?action=get&version=actual&id=0 - получить элементы актуального справочника, где version=версия справочника, id = идентификатор справочника


api/units/?action=get&version=1&id=0 - получить элементы справочника указанной 


api/units/?action=validate&version=1&id=0&code=1&value=123 - валидация элемента справочника. Принцип выбора справочника тот же, что и в оперции получения элементов. code - код элемента, value - значение элемента.
