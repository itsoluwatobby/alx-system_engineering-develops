# A puppet manuscript to debug why Apache is returning 500 error

$edit_file = '/var/www/html/wp-settings.php'

#replace line containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${edit_file}",
  path    => ['/bin','/usr/bin']
}
