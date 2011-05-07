from django.shortcuts import render_to_response
import sys, socket, os, platform

def getipaddrs(hostname):
    result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
    return [x[4][0] for x in result]

def home(request):
    hostinfo = {}
    osinfo = {}
    platforminfo = {}
    envinfo = os.environ

    osinfo['sys.platform'] = sys.platform
    osinfo['os.name'] = os.name
    osinfo['hostname'] = socket.gethostname()
    osinfo['fully-qualified-name'] = socket.getfqdn(osinfo['hostname'])
    osinfo['os.uname'] = os.uname()
    
    try:
        hostinfo['ips'] = ", ".join(getipaddrs(osinfo['hostname']))
    except socket.gaierror, e:
        hostinfo['ips'] = None
    
    platforminfo['machine'] = platform.machine()
    platforminfo['node'] = platform.node()
    platforminfo['platform'] = platform.platform(aliased=0, terse=0)
    platforminfo['processor'] = platform.processor()
    platforminfo['architecture'] = platform.architecture()
    platforminfo['python_build'] = platform.python_build()
    platforminfo['python_version'] = platform.python_version()
    platforminfo['python_compiler'] = platform.python_compiler()
    platforminfo['python_branch'] = platform.python_branch()
    platforminfo['python_implementation'] = platform.python_implementation()
    platforminfo['python_revision'] = platform.python_revision()
    platforminfo['python_version_tuple'] = platform.python_version_tuple()
    platforminfo['release'] = platform.release()
    platforminfo['system'] = platform.system()
    platforminfo['version'] = platform.version()
    platforminfo['system_alias'] = platform.system_alias(platforminfo['system'], platforminfo['release'], platforminfo['version'])
    platforminfo['uname'] = platform.uname()
    platforminfo['linux_distribution'] = platform.linux_distribution()
    
    return render_to_response("home.html", {'request': request, 'osinfo': osinfo, 'hostinfo': hostinfo, 'envinfo': envinfo, 'platforminfo': platforminfo})
