import os
from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='upload', renderer='templates/upload.html')
def upload_view(request):
    return {}

@view_config(route_name='upload_file', request_method='POST')
def upload_file(request):
    upload_dir = 'path/to/upload/directory'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    file = request.POST['file']
    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, 'wb') as f:
        f.write(file.file.read())

    return Response('File uploaded successfully')
