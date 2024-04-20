# Puppet manifest to install Flask version 2.1.0 using pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Notify the execution of the command so it's visible

exec { 'flask_version':
  command   => '/usr/bin/flask --version',
  path      => ['/usr/bin'],
  logoutput => true,
  require   => Package['flask'],
}
