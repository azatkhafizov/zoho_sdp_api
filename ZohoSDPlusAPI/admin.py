from .sdp_api_core import SDP


class Admin(SDP):

    # users
    def get_all_users(self, input_data=None):
        '''
        Получить всех пользователей 
        см. документацию для input_data
        https://ui.servicedeskplus.com/APIDocs3/index.html#get-all-users
        '''
        if input_data:
            return self.get_data('users', input_data)
        else:
            return self.get_data('users')
        
    def get_user_info(self, user_id):
        '''
        Получить информацию о пользователе
        https://ui.servicedeskplus.com/APIDocs3/index.html#get-an-user
        '''
        return self.get_data(f'users/{user_id}')

    def add_user(self, input_data):
        '''
        Добавить пользователя
        см. документацию для input_data
        https://ui.servicedeskplus.com/APIDocs3/index.html#add-an-user
        '''
        return self.post_data('users', input_data)
    
    def update_user(self, user_id, input_data):
        '''
        Обновить информацию о пользователе
        см. документацию для input_data
        https://ui.servicedeskplus.com/APIDocs3/index.html#update-an-user
        '''
        return self.put_data(f'users/{user_id}', input_data)
    
    def delete_user(self, user_id):
        '''
        Удалить пользователя
        https://ui.servicedeskplus.com/APIDocs3/index.html#delete-an-user
        '''
        return self.delete_data(f'users/{user_id}')
    
    def change_user_as_technician(self, user_id, input_data):
        '''
        Сделать пользователя техническим специалистом
        см. документацию для input_data
        https://ui.servicedeskplus.com/APIDocs3/index.html#update-an-user
        '''
        return self.put_data(f'users/{user_id}/change_as_technician', input_data)
    
    # hechnicians
    def get_all_technicians(self, input_data=None):
        '''
        Получить всех технических специалистов
        см. документацию для input_data
        https://ui.servicedeskplus.com/APIDocs3/index.html#get-all-technicians
        '''
        if input_data:
            return self.get_data('technicians', input_data)
        else:
            return self.get_data('technicians')

    def get_technician_info(self, technician_id):
        '''
        Получить информацию о техническом специалисте
        https://ui.servicedeskplus.com/APIDocs3/index.html#get-a-technician
        '''
        return self.get_data(f'technicians/{technician_id}')

    def add_technician(self, input_data):
        '''
        Добавить технического специалиста
        см. документацию для input_data
        https://ui.servicedeskplus.com/APIDocs3/index.html#add-a-technician
        '''
        return self.post_data('technicians', input_data)

    def update_technician(self, technician_id, input_data):
        '''
        Обновить информацию о техническом специалисте
        см. документацию для input_data
        https://ui.servicedeskplus.com/APIDocs3/index.html#update-a-technician
        '''
        return self.put_data(f'technicians/{technician_id}', input_data)
    
    def delete_technician(self, technician_id):
        '''
        Удалить технического специалиста
        https://ui.servicedeskplus.com/APIDocs3/index.html#delete-a-technician
        '''
        return self.delete_data(f'technicians/{technician_id}')

    def change_technician_as_user(self, technician_id):
        '''
        Сделать технического специалиста пользователем
        см. документацию для input_data
        https://ui.servicedeskplus.com/APIDocs3/index.html#update-a-technician
        '''
        return self.put_data(f'technicians/change_as_user?ids={technician_id}')
    
    # request_type
    def get_all_request_types_data(self, input_data=None):
        '''
        Эта операция извлекает все типы заявок.
        '''
        if not input_data:
            input_data = { "list_info": {"row_count": 2,
                                         "start_index": 0,
                                         "sort_field": "id",
                                         "sort_order": "asc",
                                         "get_total_count": True}}
        return self.get_data('request_types')

    def add_request_types(self, type_name, description, is_deleted=False):
        '''
        Эта операция позволяет добавить тип заявок.
        '''
        input_data = {"request_type": {"name": type_name,
                                       "description": description,
                                       "deleted": is_deleted}}
        return self.post_data('request_types', input_data)
    
    def get_request_type_data(self, request_type_id):
        '''
        Эта операция извлекает сведения о типе заявки.
        '''
        return self.get_data(f'request_types/{request_type_id}')
    
    def update_request_type(self, request_type_id, type_name, description, is_deleted=False):
        '''
        Эта операция позволяет обновить тип заявки.
        '''
        input_data = {"request_type": {"name": type_name,
                                       "description": description,
                                       "deleted": is_deleted}}
        return self.put_data(f'request_types/{request_type_id}', input_data)

    def delete_request_type(self, request_type_id):
        '''
        Эта операция позволяет удалить тип заявки.
        '''
        return self.delete_data(f'request_types/{request_type_id}')

    # closure code
    def get_all_request_closure_codes_data(self, input_data=None):
        '''
        Эта операция извлекает все коды закрытия заявок.
        '''
        if not input_data:
            input_data = { "list_info": {"row_count": 2,
                                         "start_index": 0,
                                         "sort_field": "id",
                                         "sort_order": "asc",
                                         "get_total_count": True}}
        return self.get_data('request_closure_codes')

    def add_request_closure_codes(self, closure_code_name, description, is_deleted):
        '''
        Эта операция позволяет добавить код закрытия заявки.
        '''
        input_data = {"request_closure_code": {"name": closure_code_name,
                                               "description": description,
                                               "deleted": is_deleted}}
        return self.post_data('request_closure_codes', input_data)

    def get_closure_code_data_data(self, request_closure_code_id):
        '''
        Эта операция извлекает сведения о коде закрытия заявки.
        '''
        return self.get_data(f'request_closure_codes/{request_closure_code_id}')
    
    def update_closure_code(self, request_closure_code_id, closure_code_name, description, is_deleted=False):
        '''
        Эта операция позволяет обновить код закрытия заявки.
        '''
        input_data = {"request_closure_code": {"name": closure_code_name,
                                              "description": description,
                                              "deleted": is_deleted}}
        return self.put_data(f'request_closure_codes/{request_closure_code_id}', input_data)

    def delete_closure_code(self, request_closure_code_id):
        '''
        Эта операция позволяет удалить тип заявки.
        '''
        return self.delete_data(f'request_closure_codes/{request_closure_code_id}')
    
    # tags
    def get_all_tags_data(self, input_data=None):
        '''
        Эта операция извлекает все теги.
        '''
        if not input_data:
            input_data = { "list_info": {"row_count": 2,
                                         "start_index": 0,
                                         "sort_field": "id",
                                         "sort_order": "asc",
                                         "get_total_count": True}}
        return self.get_data('tags')

    def get_tag_data(self, tag_id):
        '''
        Эта операция извлекает сведения о теге
        '''
        return self.get_data(f'tags/{tag_id}')

    def add_tag(self, tag_name):
        '''
        Эта операция позволяет добавлять теги.
        '''
        input_data = {"tags": [{"name": tag_name}]}
        return self.post_data(f'tags', input_data)

    def update_tag(self, tag_id, tag_name):
        '''
        Эта операция позволяет обновить тег
        '''
        input_data = {"tags": [{"name": tag_name}]}
        return self.post_data(f'tags/{tag_id}', input_data)
    
    # Тут закончились методы указанные в документациях

    def set_telegram_id_in_sd(self, user_id, telegram_id):
        input_data = {"user": {"user_udf_fields": {"udf_long_8760": str(telegram_id)}}}
        return self.update_user(user_id, input_data)
