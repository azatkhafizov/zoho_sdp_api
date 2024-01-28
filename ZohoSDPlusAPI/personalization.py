from .sdp_api_core import SDP


class Personalization(SDP):

    def add_personalization(self, input_data):
        '''
        Добавить персонализацию
        см. input_data в доках к api
        '''
        return self.post_data(f'personalizations', input_data)
    
    def get_personalization(self, registration_id):
        '''
        Посмотреть персонализацию
        '''
        return self.get_data(f'personalizations')