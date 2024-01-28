import json
import mimetypes
import os
try:
    import requests
except:
    os.system('pip install requests')

try:
    from requests_toolbelt.multipart.encoder import MultipartEncoder
except:
    os.system('pip install requests-toolbelt')

class SDP():

    def __init__(self, api_key, api_url_base):
        '''
        api_url_base должен в себе содержать url до /api/v3
        Например https://sd-exemple.ru/api/v3
        '''
        assert '/api/v3' in api_url_base, 'Не правильный URL для API'
        self.api_key = api_key
        self.api_url_base = api_url_base
        self.headers = {f"authtoken": self.api_key, "Content-Type": "application/json"}

    def get_data(self, api_method: str(), input_data: dict()=None):
        '''
        Для выполнения HTTP GET запросов и получения json ответа
        '''
        if input_data:
            params = {"input_data":json.dumps(input_data, ensure_ascii=False)}
        else:
            params = None
        return requests.get(self.api_url_base+'/'+api_method, headers=self.headers, params=params).json()
            
    def get_content_data(self, api_method: str(), input_data: dict()=None):
        '''
        Для выполнения HTTP GET запросов с получением контента
        '''
        if input_data:
            params = {"input_data":json.dumps(input_data, ensure_ascii=False)}
        else:
            params = None
        return requests.get(self.api_url_base+'/'+api_method, headers=self.headers, params=params).content
            
    def post_data(self, api_method: str(), input_data: dict()=None):
        '''
        Для выполнения HTTP POST запросов и получения json ответа
        '''
        if input_data:
            params = {"input_data":json.dumps(input_data, ensure_ascii=False)}
        else:
            params = None
        return requests.post(self.api_url_base+'/'+api_method, headers=self.headers, params=params).json()
            
    def put_data(self, api_method: str(), input_data: dict()=None):
        '''
        Для выполнения HTTP PUT запросов и получения json ответа
        '''
        if input_data:
            params = {"input_data":json.dumps(input_data, ensure_ascii=False)}
        else:
            params = None
        return requests.put(self.api_url_base+'/'+api_method, headers=self.headers, params=params).json()
            
    def delete_data(self, api_method: str(), input_data: dict()=None):
        '''
        Для выполнения HTTP DELETE запросов и получения json ответа
        '''
        if input_data:
            params = {"input_data":json.dumps(input_data, ensure_ascii=False)}
        else:
            params = None
        return requests.delete(self.api_url_base+'/'+api_method, headers=self.headers, params=params).json()

    def send_file(self, file_path, method, http_method='post'):
        '''
        Для выполнения скачивания файла. Файл скачается на указанный file_path.
        В method нужно указать href url после /api/v3. Например: requests/{request_id}/attachments/{attachment_id}/download
        В http_method можно указать 2 варианта put или post
        '''
        file_name = file_path.split(os.path.sep)[-1]
        mimetype = mimetypes.guess_type(file_path)[0]
        data = MultipartEncoder(fields={'input_file': (file_name, open(file_path, 'rb'), mimetype)})
        headers = self.headers
        headers['Content-Type'] = data.content_type
        if http_method == 'post':
            return requests.post(self.api_url_base+'/'+method, headers=self.headers, data=data).json()
        elif http_method == 'put':
            return requests.put(self.api_url_base+'/'+method, headers=self.headers, data=data).json()
        else:
            return {"res": 'Not supported http_method'}