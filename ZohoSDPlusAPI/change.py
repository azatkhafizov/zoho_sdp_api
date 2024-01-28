import os

from .sdp_api_core import SDP

class Change(SDP):
    
    def get_all_changes_data(self, input_data=None):
        '''
        Эта операция поможет вам получить изменения списка.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/changes/change.html#get-list-change
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'changes', input_data)
    
    def get_change_data(self, change_id):
        '''
        Эта операция поможет вам получить изменения.
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/changes/change.html#get-change
        '''
        return self.get_data(f'changes/{change_id}')
    
    def add_change(self, input_data):
        '''
        Эта операция поможет вам добавить новое изменение.
        см. input_data в доках к api
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/changes/change.html#add-change
        '''
        return self.post_data(f'changes', input_data)
    
    def update_change(self, change_id, input_data):
        '''
        Эта операция поможет вам отредактировать или обновить изменение.
        см. input_data в доках к api
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/changes/change.html#edit-change
        '''
        return self.put_data(f'changes/{change_id}', input_data)

    def delete_change(self, change_id):
        '''
        Эта операция поможет вам удалить изменение (окончательное удаление).
        https://www.manageengine.com/products/service-desk/sdpod-v3-api/changes/change.html#delete-change
        '''
        return self.delete_data(f'changes/{change_id}')
    
    def delete_to_trash_change(self, change_id):
        '''
        Эта операция поможет вам удалить изменение в корзину.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/changes/change.html#trash-a-change
        '''
        return self.delete_data(f'changes/{change_id}/move_to_trash')
    
    def restore_change_a_trash(self, change_id):
        '''
        Эта операция поможет вам восстановить изменение с корзины
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/changes/change.html#restore-a-change
        '''
        return self.put_data(f'changes/{change_id}/restore_from_trash')
    
    def pickup_change(self, change_id):
        '''
        Взять измение от имени текущего технического специалиста под которым сгенерирован API token
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/changes/change.html#pickup-change
        '''
        return self.put_data(f'changes/pickup?ids={change_id}')
    
    def assign_change_owner(self, change_id, change_owner_id):
        '''
        Назначить владельца измения 
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/changes/change.html#assign-change
        '''
        input_data = {"change": {"change_owner": {"id": str(change_owner_id)}}}
        return self.put_data(f'changes/assign?ids={change_id}', input_data)
    
    def assign_change_iniciator(self, change_id, change_iniciator_id):
        '''
        Назначить владельца инициатора
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/changes/change.html#assign-change
        '''
        input_data = {"change": {"change_requester": {"id": str(change_iniciator_id)}}}
        return self.put_data(f'changes/assign?ids={change_id}', input_data)
    
    def assign_change_manager(self, change_id, change_manager_id):
        '''
        Назначить менеджера измения 
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/changes/change.html#assign-change
        '''
        input_data = {"change": {"change_manager": {"id": str(change_manager_id)}}}
        return self.put_data(f'changes/assign?ids={change_id}', input_data)

    def close_change(self, change_id, comment, status):
        '''
        Эта операция поможет вам отредактировать или обновить изменение.
        см. input_data в доках к api
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/changes/change.html#close-a-change
        '''
        input_data = {"comment": comment, "status": status}
        return self.put_data(f'changes/{change_id}/close_change', input_data)
    
    def copy_change(self, change_id):
        '''
        Копирует данное изменение и создает новое изменение.
        '''
        return self.post_data(f'changes/{change_id}/copy')
    
    def get_change_summary_data(self, change_id):
        '''
        Эта операция позволяет получить сводную информацию об изменениях.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/changes/change.html#get-summary
        '''
        return self.get_data(f'changes/summary?ids={change_id}')
    
    def get_meta_info_for_change_add(self):
        '''
        Эта операция позволяет вам получить метаинформацию операции добавления изменения.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/changes/change.html#meta-info-for-change-add
        '''
        return self.get_data(f'changes/metainfo')
    
    def get_meta_info_for_change_edit(self, change_id):
        '''
        Эта операция позволяет вам получить метаинформацию об операции редактирования.
        https://www.manageengine.com/products/service-desk/sdpop-v3-api/changes/change.html#meta-info-for-change-edit
        '''
        return self.get_data(f'changes/{change_id}/metainfo')
    
    # change attachment
    def get_all_change_attachments_data(self, change_id):
        '''
        Просмотреть все вложения к изменению
        ''' 
        return self.get_data(f'changes/{change_id}/attachments')
    
    def get_change_attachment_data(self, change_id, attachment_id):
        '''
        Просмотреть информацию о вложени в изменении
        ''' 
        return self.get_data(f'changes/{change_id}/attachments/{attachment_id}')
    
    def download_change_attachment(self, change_id, attachment_id, saved_file_patch=os.getcwd()):
        '''
        Эта операция используется для скачивания определенного вложения по изменению
        '''
        attachment_file_list = self.get_all_change_attachments_data(change_id)
        file_name = 'file'
        for at in attachment_file_list['attachments']:
            if at['id'] == str(attachment_id):
                file_name = at['name']
        content_data = self.get_content_data(f'changes/{change_id}/attachments/{attachment_id}/download')
        with open(os.path.join(saved_file_patch, file_name), 'wb') as file:
            file.write(content_data)
        return {"saved_in": saved_file_patch}

    def delete_change_attachment(self, change_id, attachment_id):
        '''
        Удалить вложение с изменения
        ''' 
        return self.delete_data(f'changes/{change_id}/attachments/{attachment_id}')
    
    def add_change_attachment_and_associate(self, change_id, file_path):
        '''
        Эта операция используется для добавления и связывания вложения с изменением.
        '''
        return self.send_file(file_path, f'changes/{change_id}/_upload', http_method='put')
    
    # change type
    
    def get_all_changes_types_data(self, input_data=None):
        '''
        Подробную информацию обо всех доступных типах изменения.
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'change_types', input_data)
    
    def get_change_type_data(self, change_types_id):
        '''
        Вы можете просмотреть подробную информацию о типе изменения.
        '''
        return self.get_data(f'change_types/{change_types_id}')
    
    def add_change_type(self, description, name, color, inactive:bool()=False):
        '''
        Эта операция поможет вам добавить новый тип измения
        '''
        input_data = { "change_type": {"description": description,
                                       "name": name,
                                       "color": color,
                                       "inactive": inactive}}
        return self.post_data(f'change_types', input_data)
    
    def update_change_type(self, change_types_id, description=None, name=None, color=None, inactive:bool()=None):
        '''
        Эта операция поможет вам отредактировать или обновить информацию о типе изменения.
        '''
        input_data = {"change_type": {"id": str(change_types_id)}}
        if description != None:
            input_data["change_type"]["description"] = description
        if name != None:
            input_data["change_type"]["name"] = name
        if color != None:
            input_data["change_type"]["color"] = color
        if inactive != None:
            input_data["change_type"]["inactive"] = inactive
        return self.put_data(f'change_types/{change_types_id}', input_data)

    def delete_change_type(self, change_types_id):
        '''
        Эта операция поможет вам удалить тип изменения
        '''
        return self.delete_data(f'change_types/{change_types_id}')
    
    # reason for change
    def get_all_changes_reasons_data(self, input_data=None):
        '''
        Подробную информацию обо всех доступных причинах изменения
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'reasons_for_change', input_data)
    
    def get_change_reason_data(self, change_reasons_id):
        '''
        Вы можете просмотреть подробную информацию о конкретной причине изменения
        '''
        return self.get_data(f'reasons_for_change/{change_reasons_id}')
    
    def add_change_reason(self, description, name, inactive:bool()=False):
        '''
        Эта операция поможет вам добавить новую причину изменения
        '''
        input_data = { "reason_for_change": {"description": description,
                                             "name": name,
                                             "inactive": inactive}}
        return self.post_data(f'reasons_for_change', input_data)
    
    def update_change_reason(self, change_reasons_id, description=None, name=None, inactive:bool()=None):
        '''
        Эта операция поможет вам отредактировать или обновить информацию о причине изменения.
        '''
        input_data = {"reason_for_change": {"id": str(change_reasons_id)}}
        if description != None:
            input_data["reason_for_change"]["description"] = description
        if name != None:
            input_data["reason_for_change"]["name"] = name
        if inactive != None:
            input_data["reason_for_change"]["inactive"] = inactive
        return self.put_data(f'reasons_for_change/{change_reasons_id}', input_data)

    def delete_change_reason(self, change_reasons_id):
        '''
        Эта операция поможет вам удалить причину изменения
        '''
        return self.delete_data(f'reasons_for_change/{change_reasons_id}')
    
    # change status
    def get_all_changes_statuses_data(self, input_data=None):
        '''
        Подробную информацию обо всех доступных статусах изменения
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'change_statuses', input_data)
    
    def get_change_status_data(self, change_status_id):
        '''
        Вы можете просмотреть подробную информацию о конкретном статусе изменения
        '''
        return self.get_data(f'change_statuses/{change_status_id}')
    
    def add_change_status(self, description, name, stage_id, inactive:bool()=False):
        '''
        Эта операция поможет вам добавить новую статус изменения
        '''
        input_data = { "change_status": {"description": description,
                                         "name": name,
                                         "inactive": inactive,
                                         "stage": {"id": stage_id},}}
        return self.post_data(f'change_statuses', input_data)
    
    def update_change_status(self, change_status_id, stage_id=None, description=None, name=None, inactive:bool()=None):
        '''
        Эта операция поможет вам отредактировать или обновить информацию о статусе изменения.
        '''
        input_data = {"change_status": {"id": str(change_status_id)}}
        if stage_id != None:
            input_data["change_status"]["stage_id"] = stage_id
        if description != None:
            input_data["change_status"]["description"] = description
        if name != None:
            input_data["change_status"]["name"] = name
        if inactive != None:
            input_data["change_status"]["inactive"] = inactive
        return self.put_data(f'change_statuses/{change_status_id}', input_data)

    def delete_change_status(self, change_status_id):
        '''
        Эта операция поможет вам удалить статус изменения
        '''
        return self.delete_data(f'change_statuses/{change_status_id}')
    
    # change stage
    def get_all_changes_stages_data(self, input_data=None):
        '''
        Подробную информацию обо всех доступных статусах изменения
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'change_stages', input_data)
    
    def get_change_stage_data(self, change_stage_id):
        '''
        Вы можете просмотреть подробную информацию о конкретном этапе изменения
        '''
        return self.get_data(f'change_stages/{change_stage_id}')
    
    def add_change_stage(self, input_data):
        '''
        Эта операция поможет вам добавить новый этап изменения
        input_data см. в доках к API
        '''
        return self.post_data(f'change_stages', input_data)
    
    def update_change_status(self, change_stage_id, input_data):
        '''
        Эта операция поможет вам отредактировать или обновить информацию о этапе изменения.
        input_data см. в доках к API
        '''
        return self.put_data(f'change_stages/{change_stage_id}', input_data)
    
    # change role
    def get_all_changes_roles_data(self, input_data=None):
        '''
        Подробную информацию обо всех доступных ролях изменения
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'change_roles', input_data)
    
    def get_change_role_data(self, change_roles_id):
        '''
        Вы можете просмотреть подробную информацию о конкретной роле изменения
        '''
        return self.get_data(f'change_roles/{change_roles_id}')
    
    def add_change_role(self, input_data):
        '''
        Эта операция поможет вам добавить новую роль изменения
        input_data см. в доках к API
        '''
        return self.post_data(f'change_roles', input_data)
    
    def update_change_role(self, change_roles_id, input_data):
        '''
        Эта операция поможет вам отредактировать или обновить информацию о роле изменения.
        input_data см. в доках к API
        '''
        return self.put_data(f'change_roles/{change_roles_id}', input_data)

    def delete_change_role(self, change_roles_id):
        '''
        Эта операция поможет вам удалить роль изменения
        '''
        return self.delete_data(f'change_roles/{change_roles_id}')
    
    # change risk
    def get_all_changes_risks_data(self, input_data=None):
        '''
        Подробную информацию обо всех доступных рисках изменения
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'risks', input_data)
    
    def get_change_risk_data(self, risks_id):
        '''
        Вы можете просмотреть подробную информацию о конкретном риске изменения
        '''
        return self.get_data(f'risks/{risks_id}')
    
    def add_change_risk(self, description, name, inactive:bool()=False):
        '''
        Эта операция поможет вам добавить новый риск изменения
        '''
        input_data = { "risk": {"description": description,
                                "name": name,
                                "inactive": inactive}}
        return self.post_data(f'risks', input_data)
    
    def update_change_risk(self, change_risk_id, description=None, name=None, inactive:bool()=None):
        '''
        Эта операция поможет вам отредактировать или обновить информацию о риске изменения.
        '''
        input_data = {"risk": {"id": str(change_risk_id)}}
        if description != None:
            input_data["risk"]["description"] = description
        if name != None:
            input_data["risk"]["name"] = name
        if inactive != None:
            input_data["risk"]["inactive"] = inactive
        return self.put_data(f'risks/{change_risk_id}', input_data)

    def delete_change_risk(self, change_risk_id):
        '''
        Эта операция поможет вам удалить риск изменения
        '''
        return self.delete_data(f'risks/{change_risk_id}')
    
    # change closure code
    def get_all_changes_closure_codes_data(self, input_data=None):
        '''
        Подробную информацию обо всех доступных кодах закрытия изменения
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'change_closure_codes', input_data)
    
    def get_change_closure_code_data(self, change_closure_codes_id):
        '''
        Вы можете просмотреть подробную информацию о конкретном коде закрытия изменения
        '''
        return self.get_data(f'change_closure_codes/{change_closure_codes_id}')
    
    def add_change_closure_code(self, description, name, inactive:bool()=False):
        '''
        Эта операция поможет вам добавить новый код закрытия изменения
        '''
        input_data = { "change_closure_codes": {"description": description,
                                                "name": name,
                                                "inactive": inactive}}
        return self.post_data(f'change_closure_codes', input_data)
    
    def update_change_closure_code(self, change_closure_codes_id, description=None, name=None, inactive:bool()=None):
        '''
        Эта операция поможет вам отредактировать или обновить информацию о коде закрытия изменения.
        '''
        input_data = {"change_closure_codes": {"id": str(change_closure_codes_id)}}
        if description != None:
            input_data["change_closure_codes"]["description"] = description
        if name != None:
            input_data["change_closure_codes"]["name"] = name
        if inactive != None:
            input_data["change_closure_codes"]["inactive"] = inactive
        return self.put_data(f'change_closure_codes/{change_closure_codes_id}', input_data)

    def delete_change_closure_code(self, change_closure_codes_id):
        '''
        Эта операция поможет вам удалить код закрытия изменения
        '''
        return self.delete_data(f'change_closure_codes/{change_closure_codes_id}')
    
    # change CAB
    def get_all_changes_cabs_data(self, input_data=None):
        '''
        Подробную информацию обо всех доступных консультативных советах по изменениям
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'cabs', input_data)
    
    def get_change_cab_data(self, cabs_id):
        '''
        Вы можете просмотреть подробную информацию о конкретном консультативном совете по изменению
        '''
        return self.get_data(f'cabs/{cabs_id}')
    
    def add_change_cab(self, input_data):
        '''
        Эта операция поможет вам добавить новый код закрытия изменения
        input_data см. в доках к API
        '''
        return self.post_data(f'cabs', input_data)
    
    def update_change_cab(self, cabs_id, input_data):
        '''
        Эта операция поможет вам отредактировать или обновить информацию о консультативном совете по изменениям.
        input_data см. в доках к API
        '''
        return self.put_data(f'cabs/{cabs_id}', input_data)

    def delete_change_cab(self, cabs_id):
        '''
        Эта операция поможет вам удалить консультативный совет по изменения
        '''
        return self.delete_data(f'cabs/{cabs_id}')
    
    # change closure rule
    def get_all_changes_closure_rules_data(self, input_data=None):
        '''
        Подробную информацию обо всех доступных правилах закрытия по изменениям
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'change_closure_rules', input_data)
    
    def update_change_closure_rule(self, change_closure_rules_id, input_data):
        '''
        Эта операция поможет вам отредактировать или обновить информацию о правиле закрытия изменения.
        input_data см. в доках к API
        '''
        return self.put_data(f'change_closure_rules/{change_closure_rules_id}', input_data)
    
    # change to change role
    def get_all_changes_to_change_roles_data(self, change_id, input_data=None):
        '''
        Подробную информацию обо всех доступных консультативных настройках ролей в изменении
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'changes/{change_id}/roles', input_data)
    
    def get_change_to_change_role_data(self, change_id, change_to_change_role_id):
        '''
        Вы можете просмотреть подробную информацию о конкретном настройке ролей в изменении
        '''
        return self.get_data(f'changes/{change_id}/roles/{change_to_change_role_id}')
    
    def add_a_role_assignments_in_a_change(self, change_id, input_data):
        '''
        Эта операция поможет вам добавить новые ролия для изменения
        input_data см. в доках к API
        '''
        return self.post_data(f'changes/{change_id}/roles', input_data)

    def delete_a_role_assignment_from_a_change(self, change_id, change_to_change_role_id):
        '''
        Эта операция поможет вам удалить назначенные роли в изменении
        '''
        return self.delete_data(f'changes/{change_id}/roles/{change_to_change_role_id}')
    
    # change downtime
    def get_all_changes_downtimes_data(self, change_id, input_data=None):
        '''
        Подробную информацию обо всех простоях по изменениям
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'changes/{change_id}/downtimes', input_data)
    
    def get_change_downtime_data(self, change_id, downtime_id):
        '''
        Вы можете просмотреть подробную информацию о конкретном простое по изменению
        '''
        return self.get_data(f'changes/{change_id}/downtimes/{downtime_id}')
    
    def add_change_downtime(self, change_id, input_data):
        '''
        Эта операция поможет вам добавить новый простой по изменению
        input_data см. в доках к API
        '''
        return self.post_data(f'changes/{change_id}/downtimes', input_data)
    
    def update_change_downtime(self, change_id, downtime_id, input_data):
        '''
        Эта операция поможет вам отредактировать или обновить информацию о простое в изменении
        input_data см. в доках к API
        '''
        return self.put_data(f'changes/{change_id}/downtimes/{downtime_id}', input_data)

    def delete_change_downtime(self, change_id, downtime_id):
        '''
        Эта операция поможет вам удалить простой в изменении
        '''
        return self.delete_data(f'changes/{change_id}/downtimes/{downtime_id}')
    
    def copy_schedule_times_to_actual_times_of_a_downtime_for_change(self, change_id, downtime_id ):
        '''
        Скопировать запланированное время в фактическое время простоя
        '''
        return self.put_data(f'changes/{change_id}/downtimes/copy_scheduled_to_actual?ids={downtime_id}')
    
    def meta_info_for_change_downtime_add(self):
        '''
        Вы можете просмотреть подробную информацию о конкретном простое по изменению
        '''
        return self.get_data(f'changes/downtimes/metainfo')
    
    def meta_info_for_change_downtime_edit(self, change_id, downtime_id):
        '''
        Вы можете просмотреть подробную информацию о конкретном простое по изменению
        '''
        return self.get_data(f'changes/{change_id}/downtimes/{downtime_id}/metainfo')
    
    # change status comment
    def get_changes_status_comments_on_stage_data(self, change_id, stage_id, input_data=None):
        '''
        Подробную информацию о комментариях в указанном этапе в изменении
        ''' 
        if not input_data:
            input_data = {"list_info": {"search_fields": {"stage.id": str(stage_id)}}}
        return self.get_data(f'changes/{change_id}/downtimes', input_data)
    
    # change descriptive field
    def get_all_changes_descriptive_fields_data(self, change_id):
        '''
        Подробную информацию обо всех описательныий полей в изменении
        ''' 
        return self.get_data(f'changes/{change_id}/descriptive_fields')
    
    def get_change_descriptive_field_data(self, change_id, plan_id):
        '''
        Вы можете просмотреть подробную информацию описании поля изменении
        '''
        return self.get_data(f'changes/{change_id}/descriptive_fields/{plan_id}')
    
    def get_change_back_out_plan_field(self, change_id):
        '''
        Вы можете просмотреть подробную информацию описании полей плана возврата для изменения
        '''
        return self.get_data(f'changes/{change_id}/back_out_plan')
    
    def get_change_roll_out_plan_field(self, change_id):
        '''
        Вы можете просмотреть подробную информацию описании полей плана отката для изменения
        '''
        return self.get_data(f'changes/{change_id}/roll_out_plan')
    
    def get_change_checklist_field(self, change_id):
        '''
        Вы можете просмотреть подробную информацию описании полей для чеклиста в изменения
        '''
        return self.get_data(f'changes/{change_id}/checklist')
    
    def get_change_review_details_field(self, change_id):
        '''
        Вы можете просмотреть подробную информацию описании полей для review в изменения
        '''
        return self.get_data(f'changes/{change_id}/review_details')
    
    def get_change_impact_details_field(self, change_id):
        '''
        Вы можете просмотреть подробную информацию описании полей для влияний в изменения
        '''
        return self.get_data(f'changes/{change_id}/impact_details')
    
    def get_change_close_details_field(self, change_id):
        '''
        Вы можете просмотреть подробную информацию описании полей для закрытия в изменения
        '''
        return self.get_data(f'changes/{change_id}/close_details')
    
    def update_change_any_descriptive_field(self, change_id, plan_id, input_data):
        '''
        Эта операция поможет обновить любое поле описание изменения
        input_data см. в доках к API
        '''
        return self.put_data(f'changes/{change_id}/descriptive_fields/{plan_id}', input_data)
    
    def update_change_back_out_plan_field(self, change_id, plan_id, input_data):
        '''
        Эта операция поможет вам отредактировать или обновить поля плана возврата для измекнения.
        input_data см. в доках к API
        '''
        return self.put_data(f'changes/{change_id}/back_out_plan/{plan_id}', input_data)
    
    def update_change_roll_out_plan_field(self, change_id, plan_id, input_data):
        '''
        Эта операция поможет вам отредактировать или обновить поля плана отката для измекнения.
        input_data см. в доках к API
        '''
        return self.put_data(f'changes/{change_id}/roll_out_plan/{plan_id}', input_data)
    
    def update_change_checklist_field(self, change_id, plan_id, input_data):
        '''
        Эта операция поможет вам отредактировать или обновить поля чеклиста для измекнения.
        input_data см. в доках к API
        '''
        return self.put_data(f'changes/{change_id}/checklist/{plan_id}', input_data)
    
    def update_change_review_details_field(self, change_id, plan_id, input_data):
        '''
        Эта операция поможет вам отредактировать или обновить поля review для измекнения.
        input_data см. в доках к API
        '''
        return self.put_data(f'changes/{change_id}/review_details/{plan_id}', input_data)
    
    def update_change_impact_details_field(self, change_id, plan_id, input_data):
        '''
        Эта операция поможет вам отредактировать или обновить поля влияния для измекнения.
        input_data см. в доках к API
        '''
        return self.put_data(f'changes/{change_id}/impact_details/{plan_id}', input_data)
    
    def update_change_close_details_field(self, change_id, plan_id, input_data):
        '''
        Эта операция поможет вам отредактировать или обновить поля детали закрытия для измекнения.
        input_data см. в доках к API
        '''
        return self.put_data(f'changes/{change_id}/close_details/{plan_id}', input_data)
    
    def get_changes_meta_info_for_descriptive_field_add(self):
        '''
        Метаинформация для добавления описательного поля
        '''
        return self.get_data(f'changes/descriptive_fields/metainfo')
    
    def get_changes_meta_info_for_descriptive_field_edit(self, change_id, descritpive_field_id):
        '''
        Метаинформация для описательного редактирования полей
        '''
        return self.get_data(f'changes/{change_id}/descriptive_fields/{descritpive_field_id}/metainfo')
    
    # change associations
    def get_all_requests_initiated_by_change(self, change_id, input_data=None):
        '''
        Получить все ассоциированные заявки с изменением инициализированные изменением
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'changes/{change_id}/initiated_requests', input_data)
    
    def associate_a_request_initiated_by_change(self, change_id, request_id):
        '''
        Ассоциировать заявку с изменением иницированный изменением
        '''
        input_data = {"request_caused_by_change": {"request": {"id": str(request_id)}}}
        return self.post_data(f'changes/{change_id}/initiated_requests', input_data)

    def diassociate_a_request_initiated_by_change(self, change_id, request_id):
        '''
        Диассоциировать заявку с изменением иницированный изменением
        '''
        input_data = {"request_caused_by_change": {"request": {"id": str(request_id)}}}
        return self.delete_data(f'changes/{change_id}/initiated_requests', input_data)
    
    def get_all_requests_that_initiated_change(self, change_id, input_data=None):
        '''
        Получить все ассоциированные заявки инициализированные заявкой
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'changes/{change_id}/initiated_by_requests', input_data)
    
    def associate_a_request_that_initiated_change(self, change_id, request_id):
        '''
        Ассоциировать заявку с изменением иницированный заявкой
        '''
        input_data = {"request_caused_by_change": {"request": {"id": str(request_id)}}}
        return self.post_data(f'changes/{change_id}/initiated_by_requests', input_data)

    def diassociate_a_request_that_initiated_change(self, change_id, request_id):
        '''
        Диассоциировать заявку с изменением иницированный заявкой
        '''
        input_data = {"request_caused_by_change": {"request": {"id": str(request_id)}}}
        return self.delete_data(f'changes/{change_id}/initiated_by_requests', input_data)
    
    def get_all_problems_associated_to_change(self, change_id, input_data=None):
        '''
        Получить все ассоциированные проблемы с изменением
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'changes/{change_id}/problems', input_data)
    
    def associate_problem_with_change(self, change_id, problem_id):
        '''
        Ассоциировать проблему с изменением
        '''
        input_data = {"change_problem_association": {"problem": {"id": str(problem_id)}}}
        return self.post_data(f'changes/{change_id}/problems', input_data)

    def diassociate_a_request_that_initiated_change(self, change_id, problem_id):
        '''
        Диассоциировать проблему с изменением
        '''
        input_data = {"change_problem_association": {"problem": {"id": str(problem_id)}}}
        return self.delete_data(f'changes/{change_id}/problems', input_data)
    
    def get_all_projects_associated_to_change(self, change_id, input_data=None):
        '''
        Получить все ассоциированные проекты с изменением
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'changes/{change_id}/projects', input_data)
    
    def associate_project_with_change(self, change_id, problem_id, initiated_by):
        '''
        Ассоциировать проект с изменением
        initiated_by должен быть или "change" или "projects"
        '''
        input_data = {"change_project_association": {"project": {"id": str(problem_id)},  "initiated_by": initiated_by}}
        return self.post_data(f'changes/{change_id}/projects', input_data)

    def diassociate_a_project_that_initiated_change(self, change_id, problem_id):
        '''
        Диассоциировать проект с изменением
        '''
        input_data = {"change_project_association": {"project": {"id": str(problem_id)}}}
        return self.delete_data(f'changes/{change_id}/projects', input_data)
    
    # change note
    def get_all_notes_data_of_change(self, change_id, input_data=None):
        '''
        Просмотреть все примечания в изменении
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'changes/{change_id}/notes', input_data)
    
    def get_note_data_of_change(self, change_id, notes_id):
        '''
        Просмотреть примечание в изменении
        ''' 
        return self.get_data(f'changes/{change_id}/notes/{notes_id}')
    
    def add_note_to_change(self, change_id, description):
        '''
        Добавить примечание в изменении
        ''' 
        input_data = {"note": {"description": description}}
        return self.post_data(f'changes/{change_id}/notes', input_data)
    
    def update_note_to_change(self, change_id, note_id, description):
        '''
        Изменить примечание в изменении
        ''' 
        input_data = {"note": {"description": description}}
        return self.put_data(f'changes/{change_id}/notes/{note_id}', input_data)
    
    def delete_note_to_change(self, change_id, note_id):
        '''
        Удалить примечание в изменении
        ''' 
        return self.delete_data(f'changes/{change_id}/notes/{note_id}')
    
    # change attachment field
    def get_all_change_attachments_fields(self, change_id):
        '''
        Просмотреть все вложения к изменении
        ''' 
        return self.get_data(f'changes/{change_id}/attachment_fields')
    
    def get_change_attachment_fields(self, change_id, attachment_id):
        '''
        Просмотреть информацию о вложении в изменении
        ''' 
        return self.get_data(f'changes/{change_id}/attachment_fields/{attachment_id}')
    
    def meta_info_for_attachment_field_add(self):
        '''
        Метаинформация для добавления поля вложения
        ''' 
        return self.get_data(f'changes/attachment_fields/metainfo')
    
    def meta_info_for_attachment_field_edit(self, change_id, attachment_field_id):
        '''
        Метаинформация для добавления поля вложения
        ''' 
        return self.get_data(f'changes/{change_id}/attachment_fields/{attachment_field_id}/metainfo')
    
    # change notification
    def get_all_change_notifications_data(self, change_id):
        '''
        Просмотреть все уведомления к изменении
        ''' 
        return self.get_data(f'changes/{change_id}/notifications')
    
    def get_change_notification_data(self, change_id, notification_id):
        '''
        Просмотреть информацию о уведомлении в изменении
        ''' 
        return self.get_data(f'changes/{change_id}/notifications/{notification_id}')
    
    def change_send_notification(self, change_id,input_data):
        '''
        Отправить уведомление для изменения
        input_data см. в доках к API
        ''' 
        return self.post_data(f'changes/{change_id}/notifications', input_data)
    
    # change template
    def get_all_change_templates_data(self, input_data=None):
        '''
        Просмотреть все шаблоны к изменениям
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'change_templates')
    
    def get_change_template_data(self, template_id, input_data=None):
        '''
        Просмотреть шаблон к изменении
        input_data см. в доках к API
        ''' 
        if not input_data:
            input_data = {"include": ["all_stages"]}
        return self.get_data(f'change_templates/{template_id}')
    
    # change template role
    def get_all_change_template_role_assignments(self, change_templates_id, input_data=None):
        '''
        Просмотреть все назначения роли шаблона изменения
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_fields": [{"field": "id", "order": "asc"}]}}
        return self.get_data(f'change_templates/{change_templates_id}/roles', input_data)
    
    def get_change_template_role_assignment(self, change_templates_id, roles_id):
        '''
        Просмотр назначения роли шаблона изменения
        ''' 
        return self.get_data(f'change_templates/{change_templates_id}/roles/{roles_id}')
    
    # change release association
    def get_change_release_associations(self, change_id):
        '''
        Получить релизы ассоцианные с изменением
        ''' 
        return self.get_data(f'changes/{change_id}/releases')
    
    def associate_change_to_release(self, change_id, release_id):
        '''
        Ассоциировать изменение с релизом
        ''' 
        input_data = {"releases": [{"release": {"id": str(release_id)}}]}
        return self.post_data(f'changes/{change_id}/releases', input_data)
    
    def diassociate_change_to_release(self, change_id, release_id):
        '''
        Ассоциировать изменение с релизом
        ''' 
        input_data = {"releases": [{"release": {"id": str(release_id)}}]}
        return self.delete_data(f'changes/{change_id}/releases', input_data)
    
    # Тут закончились методы указанные в документациях