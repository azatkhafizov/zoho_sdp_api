from .sdp_api_core import SDP

class Contract(SDP):
    def get_all_contracts_data(self, input_data=None):
        '''
        Просмотреть все контракты
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'contracts', input_data)
    
    def get_contract_data(self, contract_id):
        '''
        Просмотреть информацию о контракте
        ''' 
        return self.get_data(f'contracts/{contract_id}')
    
    def add_contract(self, input_data):
        '''
        Добавить контракт
        см. input_data в доках к api
        '''
        return self.post_data(f'contracts', input_data)
    
    def update_contract(self, contract_id, input_data):
        '''
        Изменить контракт
        см. input_data в доках к api
        '''
        return self.put_data(f'contracts/{contract_id}', input_data)
    
    def renew_contract(self, contract_id, input_data):
        '''
        Продлить контракт
        см. input_data в доках к api
        '''
        return self.post_data(f'contracts/{contract_id}/renew_contract', input_data)
    
    def contract_owner_send_email(self, contract_id, subject, description):
        '''
        Эта операция позволяет отправить электронное письмо владельцу контракта.
        '''
        input_data = {"notification": {"description": description,"subject": subject}}
        return self.post_data(f'contracts/{contract_id}/email_owner', input_data)
    
    def contract_owner_send_email(self, contract_id, subject, description):
        '''
        Эта операция позволяет отправить электронное письмо поставщику контракта.
        '''
        input_data = {"notification": {"description": description,"subject": subject}}
        return self.post_data(f'contracts/{contract_id}/email_vendor', input_data)
    
    def delete_contract(self, contract_id):
        '''
        Удалить контракт
        '''
        return self.put_data(f'contracts/{contract_id}')
    
    # Тут закончились методы указанные в документациях