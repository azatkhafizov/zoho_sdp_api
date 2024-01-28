from .sdp_api_core import SDP

class Asset(SDP):

    def get_all_assets_data(self, input_data=None):
        '''
        Просмотреть все активы
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'assets', input_data)
    
    def get_asset_data(self, asset_id):
        '''
        Просмотреть данные об активе
        '''
        return self.get_data(f'assets/{asset_id}')
    
    def add_asset(self, input_data):
        '''
        Добавить актив
        см. input_data в доках к api
        '''
        return self.post_data(f'assets', input_data)
    
    def update_asset(self, asset_id, input_data):
        '''
        Изменить информации в активе
        см. input_data в доках к api
        '''
        return self.put_data(f'assets/{asset_id}', input_data)
    
    def delete_asset(self, asset_id):
        '''
        Удалить актив
        '''
        return self.delete_data(f'assets/{asset_id}')
    
    def get_asset_metainfo(self):
        '''
        Получить метаинформацию об активах
        '''
        return self.get_data(f'assets/metainfo')
    
    def copy_asset(self, asset_id, number_copies=1):
        '''
        Копировать актив
        '''
        input_data = {"copy": {"number_copies": str(number_copies)}}
        return self.post_data(f'assets/{asset_id}/copy', input_data)
    
    def configure_depreciation_asset(self, asset_id, input_data):
        '''
        Настройка амортизации актива.
        см. input_data в доках к api
        '''
        return self.post_data(f'assets/{asset_id}/configure_depreciation', input_data)
    
    # workstation
    def get_all_workstations_data(self, input_data=None):
        '''
        Просмотреть все рабочие станции
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'workstations', input_data)
    
    def get_workstation_data(self, workstation_id):
        '''
        Просмотреть данные об рабочей станции
        '''
        return self.get_data(f'workstations/{workstation_id}')
    
    def add_workstation(self, input_data):
        '''
        Добавить рабочюю станцию
        см. input_data в доках к api
        '''
        return self.post_data(f'workstations', input_data)
    
    def update_workstation(self, workstation_id, input_data):
        '''
        Эта операция позволяет обновить рабочую станцию.
        см. input_data в доках к api
        '''
        return self.put_data(f'workstations/{workstation_id}', input_data)
    
    def delete_workstation(self, workstation_id):
        '''
        Удалить актив
        '''
        return self.delete_data(f'workstations/{workstation_id}')
    
    def get_workstation_metainfo(self):
        '''
        API Metainfo предоставляет метаданные дополнительных полей рабочей станции, 
        идентификатора дополнительных полей актива и атрибутов CI. 
        Атрибуты CI рабочей станции можно добавить и обновить, 
        передав идентификатор типа продукта в качестве аргумента этому API
        '''
        return self.get_data(f'workstations/metainfo')
    
    def copy_workstation(self, workstation_id, number_copies=1):
        '''
        Копировать актив
        '''
        input_data = {"copy": {"number_copies": str(number_copies)}}
        return self.post_data(f'workstations/{workstation_id}/copy', input_data)
    
     # Тут закончились методы указанные в документациях