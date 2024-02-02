# Increases the amount of traffic handled by the Nginx server.

# Increase the ULIMIT of the default file
exec { 'fix-for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Reload Nginx
exec { 'nginx-reload':
  command => 'nginx reload',
  path    => '/etc/init.d/'
}
