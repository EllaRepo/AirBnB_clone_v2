# sets up web servers for the deployment of web_static

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; sudo service nginx start',
  before   => Exec['create directories'],
}

exec {'create directories':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test/ ; sudo mkdir -p /data/web_static/shared/',
  before   => Exec['html file'],
}

exec {'html file':
  provider => shell,
  command  => 'echo "Hello Web Server!" | sudo tee /data/web_static/releases/test/index.html',
  before   => Exec['symbolic link'],
}

exec {'symbolic link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before   => Exec['add location'],
}

exec {'add location':
  provider => shell,
  command  => 'sudo sed -i \'38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\' /etc/nginx/sites-available/default',
  before   => Exec['restart Nginx'],
}

exec {'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  before   => File['owner']
}

file {'owner':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}
