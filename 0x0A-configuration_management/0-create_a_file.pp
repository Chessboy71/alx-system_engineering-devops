#this file creates a new fils 

file { '/tmp/school':
  ensure  => 'present',
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}

