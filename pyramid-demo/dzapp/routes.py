from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    
    config.add_route('upload', '/upload')
    config.add_route('upload_file', '/upload_file')
    config.scan()
    
    return config.make_wsgi_app()
