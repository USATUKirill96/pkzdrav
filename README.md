/admin доступ к панели администратора. Логин admin, пароль admin

api/directories/date=all - получить все справочники

api/directories/?date=all&page=number - получить указанную страницу. Атрибут page распространяется на любой тип запроса за исключением валидации.

(api/directories/?date=all&page=1)


api/directories/?date=yearmonthday - получить справочники, действующие на дату.

(api/directories/?date=20200225&page=1)


api/units/?action=get&version=actual&id=0 - получить элементы актуального справочника, где version=версия справочника, id = идентификатор справочника


api/units/?action=get&version=1&id=0 - получить элементы справочника указанной версии
