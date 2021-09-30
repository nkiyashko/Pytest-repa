{
  "id": "ed4a32d5-1ea8-45ea-b7d2-fb4feb65d8bf",
  "version": "2.0",
  "name": "Test2",
  "url": "https://auth.cloudike.com",
  "tests": [{
    "id": "2d6d329f-c56c-428b-89c0-29b7fa304edd",
    "name": "login",
    "commands": [{
      "id": "80321a97-8cf9-44c3-abf0-09e9612435a0",
      "comment": "",
      "command": "open",
      "target": "/?ticket_id=ef35d705668c4d6dbf2fb4ed71ebdfb7",
      "targets": [],
      "value": ""
    }, {
      "id": "5f9f9cc9-7ebb-47a6-b429-0addf7b9f475",
      "comment": "",
      "command": "setWindowSize",
      "target": "1440x900",
      "targets": [],
      "value": ""
    }, {
      "id": "89f8b639-0112-4e5e-a792-806740dde9f2",
      "comment": "",
      "command": "type",
      "target": "css=.ng-valid",
      "targets": [
        ["css=.ng-valid", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "nkiyashko@asdco.ru"
    }, {
      "id": "a6f84215-0427-4a53-9e8b-a8f875a87bb0",
      "comment": "",
      "command": "type",
      "target": "css=.form-control:nth-child(1)",
      "targets": [
        ["css=.form-control:nth-child(1)", "css:finder"],
        ["xpath=//input[@name='password']", "xpath:attributes"],
        ["xpath=//app-form-password/div/input", "xpath:position"]
      ],
      "value": "500875875g"
    }, {
      "id": "627c972b-1671-4b46-b99d-f2921f005703",
      "comment": "",
      "command": "click",
      "target": "css=.btn-primary",
      "targets": [
        ["css=.btn-primary", "css:finder"],
        ["xpath=//div[3]/button", "xpath:position"],
        ["xpath=//button[contains(.,'Sign in')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "aa961a65-1f4f-4f04-88fa-1c72ab69af02",
      "comment": "",
      "command": "click",
      "target": "css=.user-menu__host:nth-child(1) .user-menu__login-text",
      "targets": [
        ["css=.user-menu__host:nth-child(1) .user-menu__login-text", "css:finder"],
        ["xpath=//div[3]/div/div/cl-user-menu/div/div/span", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "35276383-bd5c-4cd3-8440-1fc28c8f6fdb",
      "comment": "",
      "command": "click",
      "target": "css=.open .user-menu__item:nth-child(2) .user-menu__link-text",
      "targets": [
        ["css=.open .user-menu__item:nth-child(2) .user-menu__link-text", "css:finder"],
        ["xpath=//div[3]/div/div/cl-user-menu/div/div[2]/ul/li[2]/a/span", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "eda03570-e9ee-4bc0-8393-b45a696b0f2e",
      "comment": "",
      "command": "type",
      "target": "css=.form-control:nth-child(2)",
      "targets": [
        ["css=.form-control:nth-child(2)", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "nkiyashko@asdco.ru"
    }]
  }],
  "suites": [{
    "id": "61130349-0063-4e4b-8f55-29d0c94a1466",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": []
  }],
  "urls": ["https://auth.cloudike.com/"],
  "plugins": []
}