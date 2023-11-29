# Terminates a running process called "killmenow"
exec { 'pkill -f killmenow':
  path => 'usr/bin/:usr/local/bin/:/bin/'
}
