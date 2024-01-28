from .sdp_api_core import SDP


class Solutions(SDP):
    def get_all_solutions_data(self, input_data=None):
        '''
        Эта операция поможет вам просмотреть все существующие решения в приложении.
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": 10,
                                        "start_index": 1,
                                        "get_total_count": True,
                                        "sort_field": "topic"}}
        return self.get_data(f'solutions', input_data)
    
    def get_solution_data(self, solution_id):
        '''
        Просмотреть информацию о контракте
        ''' 
        return self.get_data(f'solutions/{solution_id}')
    
    def add_solution(self, input_data):
        '''
        Эта операция поможет вам добавить новое решение.
        см. input_data в доках к api
        '''
        return self.post_data(f'solutions', input_data)
    
    def update_solution(self, solution_id, input_data):
        '''
        Эта операция поможет вам обновить существующее решение.
        см. input_data в доках к api
        '''
        return self.put_data(f'solutions/{solution_id}', input_data)
    
    def delete_solution(self, solution_id):
        '''
        Эта операция поможет вам удалить существующее решение по solution_id.
        '''
        return self.delete_data(f'solutions/{solution_id}')
    
    def solution_approve(self, solution_id, operation_comment):
        '''
        Эта операция поможет вам утвердить существующее решение.
        '''
        input_data = {"solution": {"operation_comment": operation_comment}}
        return self.put_data(f'solutions/{solution_id}/approve', input_data)
    
    def solution_reject(self, solution_id, operation_comment):
        '''
        Эта операция поможет вам отклонить утверждение существующего решения.
        '''
        input_data = {"solution": {"operation_comment": operation_comment}}
        return self.put_data(f'solutions/{solution_id}/reject', input_data)
    
    def solution_like(self, solution_id):
        '''
        Эта операция поможет лакнуть решение.
        '''
        return self.put_data(f'solutions/{solution_id}/like')
    
    def solution_removelike(self, solution_id):
        '''
        Чтобы удалить лайк (или) неприязнь к решению
        '''
        return self.put_data(f'solutions/{solution_id}/removelike')
    
    def solution_reacted_users(self, solution_id):
        '''
        Эта операция поможет вам просмотреть понравившихся и не понравившихся пользователей решения.
        '''
        return self.get_data(f'solutions/{solution_id}/reacted_users')
    
    # topic
    def get_all_topics_data(self, input_data=None):
        '''
        Эта операция поможет вам просмотреть все существующие темы в приложении.
        ''' 
        if not input_data:
            input_data = {"list_info": {"row_count": "3", "start_index": "1"}}
        return self.get_data(f'topics', input_data)
    
    def get_topic_data(self, topic_id):
        '''
        Эта операция поможет вам просмотреть существующую тему по topic_id.
        ''' 
        return self.get_data(f'topics/{topic_id}')
    
    def add_topic(self, input_data):
        '''
        Эта операция поможет вам добавить новую тему
        см. input_data в доках к api
        '''
        return self.post_data(f'topics', input_data)
    
    def update_topic(self, topic_id, input_data):
        '''
        Эта операция поможет вам переименовать тему.
        см. input_data в доках к api
        '''
        return self.put_data(f'topics/{topic_id}', input_data)
    
    def delete_topic(self, topic_id):
        '''
        Эта операция поможет вам удалить существующую тему по topic_id
        '''
        return self.delete_data(f'topics/{topic_id}')
    
    def topic_change_parent(self, topic_id, parent_topic_id):
        '''
        Эта операция поможет вам изменить родительскую тему.
        '''
        input_data = { "topic": {"parent": {"id": str(parent_topic_id)}}}
        return self.put_data(f'topics/{topic_id}', input_data)

    def topic_change_parent(self, topic_id):
        '''
        Эта операция поможет вам удалить родительский элемент и переместить 
        дочерний элемент в качестве родительского элемента темы.
        '''
        input_data = { "topic": {"parent": None}}
        return self.put_data(f'topics/{topic_id}', input_data)