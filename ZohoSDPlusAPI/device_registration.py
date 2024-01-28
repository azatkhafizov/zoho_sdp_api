from .sdp_api_core import SDP


class DeviceRegistration(SDP):

    def register_device(self, input_data):
        '''
        Эта операция помогает зарегистрировать устройство для push-уведомлений.
        см. input_data в доках к api
        '''
        return self.post_data(f'mobile_devices', input_data)
    
    def unregister_device(self, registration_id):
        '''
        Эта операция помогает зарегистрировать устройство для push-уведомлений.
        см. input_data в доках к api
        '''
        return self.post_data(f'mobile_devices/{registration_id}')