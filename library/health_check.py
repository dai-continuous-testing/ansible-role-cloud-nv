#!/usr/bin/python

import time
import socket

try:
    # python3
    import urllib.request as urllib_request
    import urllib.error as urllib_error
except ImportError:
    # python2
    import urllib2 as urllib_request
    import urllib2 as urllib_error

from ansible.module_utils.basic import AnsibleModule

def check_server_status(url, headers, expected_status, timeout, expected_regexp):

    try:
        req = urllib_request.Request(url, headers=headers)
        resp = urllib_request.urlopen(req, timeout=timeout)

    except urllib_error.HTTPError as e:
        if e.code == expected_status:
            return {
                "msg": "OK",
                "success": True,
                "url": url,
                "expected_status": expected_status,
                "actual_status": e.code
            }

        else:
            return {
                "msg": 'Expected status %d, actual: %d' % (expected_status, e.code),
                "success": False,
                "url": url,
                "expected_status": expected_status,
                "actual_status": e.code
            }

    except (urllib_error.URLError, socket.error) as e:
        return {
            "msg": 'URLError: %s' % str(e),
            "success": False,
            "url": url,
            "expected_status": expected_status
        }

    if resp.getcode() != expected_status:
        return {
            "msg": 'Expected status %d, actual: %d' % (expected_status, resp.getcode()),
            "success": False,
            "url": url,
            "expected_status": expected_status,
            "actual_status": resp.getcode()
        }

    try:
        content = resp.read()
    except:
        content = ""

    return {
        "msg": "OK",
        "success": True,
        "url": url,
        "expected_status": expected_status,
        "actual_status": resp.getcode(),
        "content": content
    }

def main():
    
    module_args = dict(
        url=dict(required=True, type='str'),
        headers=dict(required=False, type='dict', default=None),
        initial_delay=dict(required=False, type='int', default=0),
        delay_between_tries=dict(required=False, type='int', default=5),
        max_retries=dict(required=False, type='int', default=10),
        timeout=dict(request=False, type='int', default=10),
        expected_status=dict(request=False, type='int', default=200),
        expected_regexp=dict(request=False, default=None)
    )
    
    module = AnsibleModule(
        argument_spec=module_args
    )

    url = module.params['url']
    headers = module.params['headers'] or {}
    initial_delay = module.params['initial_delay']
    delay_between_tries = module.params['delay_between_tries']
    max_retries = module.params['max_retries']
    timeout = module.params['timeout']
    expected_status = module.params['expected_status']
    expected_regexp = module.params['expected_regexp']

    time.sleep(initial_delay)
    
    for attempt in range(max_retries):
        
        if attempt != 0:
            time.sleep(delay_between_tries)
        
        result = check_server_status(
                url=url, 
                headers=headers, 
                timeout=timeout,
                expected_status=expected_status,
                expected_regexp=expected_regexp)
        
        if result["success"]:
            module.exit_json(failed_attempts=attempt)
    
    else:
        module.fail_json(msg='Maximum attempts reached: ' + result["msg"],
                         failed_attempts=attempt)

if __name__ == '__main__':
    main()
