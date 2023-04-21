# This Puppet manifest will install the puppet-flask

package { 'python3-pip':
  ensure => installed,
}
exec { 'install-flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin',
  creates => '/usr/local/bin/flask',
}
