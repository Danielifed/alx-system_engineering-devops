# This Puppet manifest will kill the process named killmenow

exec { 'process kill killmenow':
  path    => '/usr/bin/',
  command => 'pkill -f killmenow',
}
