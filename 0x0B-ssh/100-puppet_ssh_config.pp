# Define SSH client configuration file path
$ssh_config_file = '/etc/ssh/ssh_config'

# Enusre SSH client configuration to use the private key ~/.ssh/school
file_line { 'Declare identity file':
  ensure => present,
  path   => $ssh_config_file,
  line   => '	IdentityFile ~/.ssh/school',
  match  => '^#>\s*IdentifyFile\s+~/.ssh/school$',
}

# Enusre SSH client configuration to use the private key ~/.ssh/school
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => $ssh_config_file,
  line   => '   PasswordAuthentication no',
  match  => '^#>\s*PasswordAuthentication\s+no$',
}
