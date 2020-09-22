A task with function resource can **wait for callback** as well.

```

% fun deploy
using template: template.yml
using region: cn-hangzhou
using accountId: ***********3637
using accessKeyId: ***********FPbL
using timeout: 60

Collecting your services information, in order to caculate devlopment changes...

Resources Changes(Beta version! Only FC resources changes will be displayed):

┌────────────────────────┬──────────────────────────────┬────────┬──────────┐
│ Resource               │ ResourceType                 │ Action │ Property │
├────────────────────────┼──────────────────────────────┼────────┼──────────┤
│ WaitForCallbackService │ Aliyun::Serverless::Service  │ Add    │ Policies │
├────────────────────────┼──────────────────────────────┼────────┼──────────┤
│ funcProxy              │ Aliyun::Serverless::Function │ Modify │ CodeUri  │
├────────────────────────┼──────────────────────────────┼────────┼──────────┤
│ workflowCallback       │ Aliyun::Serverless::Function │ Modify │ CodeUri  │
└────────────────────────┴──────────────────────────────┴────────┴──────────┘

? Please confirm to continue. Yes
Waiting for flow WaitForCallbackWorkflow to be deployed...
flow WaitForCallbackWorkflow deploy success

Waiting for service WaitForCallbackService to be deployed...
service WaitForCallbackService deploy success

% aliyun fnf StartExecution --FlowName WaitForCallbackWorkflow --Input '{"serviceName": "WaitForCallbackService", "functionName": "workflowCallback"}'
{
        "FlowDefinition": "version: v1\ntype: flow\nsteps:\n  - type: task\n    name: test\n    resourceArn: 'acs:fc:::services/WaitForCallbackService/functions/funcProxy'\n    pattern: waitForCallback\n    inputMappings:\n      - target: serviceName\n        source: $input.serviceName\n      - target: functionName\n        source: $input.functionName\n      - target: taskToken\n        source: $context.task.token\n    retry:\n      - errors:\n          - FC.ResourceThrottled\n          - FC.ResourceExhausted\n          - FC.InternalServerError\n          - FC.Unknown\n          - FnF.TaskTimeout\n        intervalSeconds: 1\n        maxAttempts: 10\n        multiplier: 1.5\n        maxIntervalSeconds: 10\n",
        "FlowName": "WaitForCallbackWorkflow",
        "Input": "{\"serviceName\": \"WaitForCallbackService\", \"functionName\": \"workflowCallback\"}",
        "Name": "69f71f89-3329-42c4-b508-b41617432db1",
        "Output": "",
        "RequestId": "4d8f018a-0d50-df04-78c6-f8a0379b8724",
        "StartedTime": "2020-09-22T23:43:40.073Z",
        "Status": "",
        "StoppedTime": ""
}

% aliyun fnf DescribeExecution --FlowName WaitForCallbackWorkflow  --ExecutionName 69f71f89-3329-42c4-b508-b41617432db1
{
        "FlowDefinition": "version: v1\ntype: flow\nsteps:\n  - type: task\n    name: test\n    resourceArn: 'acs:fc:::services/WaitForCallbackService/functions/funcProxy'\n    pattern: waitForCallback\n    inputMappings:\n      - target: serviceName\n        source: $input.serviceName\n      - target: functionName\n        source: $input.functionName\n      - target: taskToken\n        source: $context.task.token\n    retry:\n      - errors:\n          - FC.ResourceThrottled\n          - FC.ResourceExhausted\n          - FC.InternalServerError\n          - FC.Unknown\n          - FnF.TaskTimeout\n        intervalSeconds: 1\n        maxAttempts: 10\n        multiplier: 1.5\n        maxIntervalSeconds: 10\n",
        "FlowName": "WaitForCallbackWorkflow",
        "Input": "{\"serviceName\": \"WaitForCallbackService\", \"functionName\": \"workflowCallback\"}",
        "Name": "69f71f89-3329-42c4-b508-b41617432db1",
        "Output": "{\"status\":\"report task with token: djEjV2FpdEZvckNhbGxiYWNrV29ya2Zsb3cjNjlmNzFmODktMzMyOS00MmM0LWI1MDgtYjQxNjE3NDMyZGIxIzIjUzFkeElzZElram44ZEIrUktla2F3cnNJcEkwPQ==\"}",
        "RequestId": "37c901a8-3802-53c2-5f3a-5a30759941d8",
        "StartedTime": "2020-09-22T23:43:40.073Z",
        "Status": "Succeeded",
        "StoppedTime": "2020-09-22T23:43:54.511Z"
}

```