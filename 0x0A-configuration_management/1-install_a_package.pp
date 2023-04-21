# This Puppet manifest will install the puppet-flask

package { 'puppet-flask':
  ensure   => '2.1.0',
  provider => 'gem',
}
