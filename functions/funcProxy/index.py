# -*- coding: utf-8 -*-
import logging
import fc2
import json


def handler(event, context):
  logger = logging.getLogger()

  creds = context.credentials
  client = fc2.Client(
    endpoint='https://%s.%s.fc.aliyuncs.com' % (context.account_id, context.region),
    accessKeyID=creds.access_key_id,
    accessKeySecret=creds.access_key_secret,
    securityToken=creds.security_token or '')
  
  evt = json.loads(event)
  response = client.invoke_function(evt.get('serviceName'), evt.get('functionName'), event, headers={'x-fc-invocation-type': 'Async'})
  logger.info(response.data)

  return {'status': 'async invoked %s/%s' % (evt.get('serviceName'), evt.get('functionName'))}