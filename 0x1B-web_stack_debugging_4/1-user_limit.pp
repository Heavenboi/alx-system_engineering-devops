# This manifest increases the open file
# descriptor limit for the holberton user

exec { 'change-os-configuration-for-holberton-user':
  command => 'sed -i "/holberton/d" /etc/security/limits.conf',
  path    => ['/usr/bin', '/bin']
}

