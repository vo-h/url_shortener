from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'', 'url_shortener.urls', name=' '),
    host(r'admin', 'app.urls_admin', name='admin'),
)