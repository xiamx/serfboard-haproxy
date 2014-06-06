import jinja2
template_dir = "./templates"
loader = jinja2.FileSystemLoader(template_dir)
j2 = jinja2.Environment(loader=loader, trim_blocks=True)

haproxy_template = j2.get_template("haproxy.j2")

class Server:
    def __init__(self, name, address, options):
        self.name = name
        self.address = address
        self.options = options


beef = Server("beef", "192.0.1.3:80", "maxconn 40")
chicken = Server("chicken", "192.0.1.2:80", "maxconn 40")
temp_vars = { "servers": [beef, chicken] }
outputText = haproxy_template.render( temp_vars )
print outputText
