# allow a maximum of 500 file descriptors and then restart the Nginx service
exec { 'change-ulimit-for-nginx':
  command => 'sed -i "/^ULIMIT/c ULIMIT=\"-n 500\"" /etc/default/nginx; service nginx restart',
  path    => ['/usr/bin', '/bin']
}

