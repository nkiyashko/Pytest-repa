var = {
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
  }, {
    "id": "94c4ffb3-043c-4c8b-84fd-e17db70f4d1e",
    "name": "negative login",
    "commands": [{
      "id": "6c257fce-1082-4ce2-8fb4-c2c1d2f3ca16",
      "comment": "",
      "command": "open",
      "target": "/?ticket_id=6a40429394414c96a408dbb83ab17400",
      "targets": [],
      "value": ""
    }, {
      "id": "94188944-4e3a-4e31-afeb-1742fb60f6d1",
      "comment": "",
      "command": "setWindowSize",
      "target": "1440x900",
      "targets": [],
      "value": ""
    }, {
      "id": "1d62eff1-5eb8-4777-a2d1-d91f365c63a0",
      "comment": "",
      "command": "click",
      "target": "css=.form-control:nth-child(2)",
      "targets": [
        ["css=.form-control:nth-child(2)", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "448fcb1a-2a1a-42aa-96c0-9290ffb67d08",
      "comment": "",
      "command": "type",
      "target": "css=.form-control:nth-child(2)",
      "targets": [
        ["css=.form-control:nth-child(2)", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "nkiyashko"
    }, {
      "id": "bbffdb84-0b3e-497e-860d-fd4ea25f1300",
      "comment": "",
      "command": "type",
      "target": "css=.ng-untouched",
      "targets": [
        ["css=.ng-untouched", "css:finder"],
        ["xpath=//input[@name='password']", "xpath:attributes"],
        ["xpath=//app-form-password/div/input", "xpath:position"]
      ],
      "value": "500875875g"
    }, {
      "id": "f7d5bdec-66c7-4c79-8c8c-887b3ea153e6",
      "comment": "",
      "command": "click",
      "target": "css=.form-control:nth-child(2)",
      "targets": [
        ["css=.form-control:nth-child(2)", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b980f186-dd9a-4098-a0f8-4047854fd37a",
      "comment": "",
      "command": "type",
      "target": "css=.form-control:nth-child(2)",
      "targets": [
        ["css=.form-control:nth-child(2)", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "nkiyashko@"
    }, {
      "id": "c01b0417-7746-44c3-aa21-56422cbec32b",
      "comment": "",
      "command": "click",
      "target": "css=.form-control:nth-child(2)",
      "targets": [
        ["css=.form-control:nth-child(2)", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "5c964da6-2214-47b4-8c7a-d5a13d5ea2e5",
      "comment": "",
      "command": "type",
      "target": "css=.form-control:nth-child(2)",
      "targets": [
        ["css=.form-control:nth-child(2)", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "nkiyashko@gmail"
    }, {
      "id": "b43bb3ed-a27b-4f27-922d-2fe655177eb3",
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
      "id": "958256f1-37c5-4c81-a186-8cf293940b62",
      "comment": "",
      "command": "mouseOver",
      "target": "css=.btn-primary",
      "targets": [
        ["css=.btn-primary", "css:finder"],
        ["xpath=//div[3]/button", "xpath:position"],
        ["xpath=//button[contains(.,'Sign in')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "289f4c52-b6d2-4781-b567-00f28f1a389d",
      "comment": "",
      "command": "mouseOut",
      "target": "css=.btn-primary",
      "targets": [
        ["css=.btn-primary", "css:finder"],
        ["xpath=//div[3]/button", "xpath:position"],
        ["xpath=//button[contains(.,'Sign in')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "3fb77c59-c2b0-45fc-97f6-c532c51057e9",
      "comment": "",
      "command": "click",
      "target": "css=.form-control:nth-child(2)",
      "targets": [
        ["css=.form-control:nth-child(2)", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "66fff076-15ed-4b7c-8822-d9b2d4728b43",
      "comment": "",
      "command": "click",
      "target": "css=.form-control:nth-child(2)",
      "targets": [
        ["css=.form-control:nth-child(2)", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "d1b0a2c7-e0ee-4493-807b-b5807f1c8353",
      "comment": "",
      "command": "type",
      "target": "css=.form-control:nth-child(2)",
      "targets": [
        ["css=.form-control:nth-child(2)", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "nkiyashkogmail.com"
    }, {
      "id": "55392e09-f889-41f8-bb91-142a4353c836",
      "comment": "",
      "command": "click",
      "target": "css=.form-control:nth-child(2)",
      "targets": [
        ["css=.form-control:nth-child(2)", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "e21e9b5d-c029-465f-84bb-7829d2551df1",
      "comment": "",
      "command": "type",
      "target": "css=.form-control:nth-child(2)",
      "targets": [
        ["css=.form-control:nth-child(2)", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "nkiyashko@gmail.com"
    }, {
      "id": "2d3c4d5a-d461-4904-bbc9-aa89b395dc7b",
      "comment": "",
      "command": "click",
      "target": "css=.form-control:nth-child(1)",
      "targets": [
        ["css=.form-control:nth-child(1)", "css:finder"],
        ["xpath=//input[@name='password']", "xpath:attributes"],
        ["xpath=//app-form-password/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "606fbb9a-1849-406d-8a90-11dc3dbcf386",
      "comment": "",
      "command": "click",
      "target": "css=.form-control:nth-child(1)",
      "targets": [
        ["css=.form-control:nth-child(1)", "css:finder"],
        ["xpath=//input[@name='password']", "xpath:attributes"],
        ["xpath=//app-form-password/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "f338deae-1f12-4335-ac44-a4b86d458faa",
      "comment": "",
      "command": "type",
      "target": "css=.form-control:nth-child(1)",
      "targets": [
        ["css=.form-control:nth-child(1)", "css:finder"],
        ["xpath=//input[@name='password']", "xpath:attributes"],
        ["xpath=//app-form-password/div/input", "xpath:position"]
      ],
      "value": "500875875"
    }, {
      "id": "3e8081d1-4f38-4de4-b8a1-9d894bc452bc",
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
      "id": "e22ae837-bb9c-4eb6-afdf-e64ce94e9def",
      "comment": "",
      "command": "mouseOver",
      "target": "css=.btn-primary",
      "targets": [
        ["css=.btn-primary", "css:finder"],
        ["xpath=//div[3]/button", "xpath:position"],
        ["xpath=//button[contains(.,'Sign in')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "5e713950-9d93-4b2f-bcd9-f649d678dd53",
      "comment": "",
      "command": "mouseOut",
      "target": "css=.btn-primary",
      "targets": [
        ["css=.btn-primary", "css:finder"],
        ["xpath=//div[3]/button", "xpath:position"],
        ["xpath=//button[contains(.,'Sign in')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "401453bf-0354-451f-b4e5-3feaa3309869",
      "comment": "",
      "command": "click",
      "target": "css=.form-control:nth-child(1)",
      "targets": [
        ["css=.form-control:nth-child(1)", "css:finder"],
        ["xpath=//input[@name='password']", "xpath:attributes"],
        ["xpath=//app-form-password/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b59a5e97-f32a-41c0-ae53-968148c191da",
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
      "id": "34f975d4-2807-406f-99ce-295635b2913e",
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
      "id": "f2a2619c-3e95-4c7a-80a0-ac77bb24566a",
      "comment": "",
      "command": "click",
      "target": "css=.icon use",
      "targets": [
        ["css=.icon use", "css:finder"]
      ],
      "value": ""
    }, {
      "id": "3b8c6b1a-f2ad-456e-a6b1-cd15f42d5fb4",
      "comment": "",
      "command": "click",
      "target": "css=.form-control:nth-child(2)",
      "targets": [
        ["css=.form-control:nth-child(2)", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "a3c68812-ec80-4a61-ad24-06615c2d6aa8",
      "comment": "",
      "command": "type",
      "target": "css=.form-control:nth-child(2)",
      "targets": [
        ["css=.form-control:nth-child(2)", "css:finder"],
        ["xpath=//input[@type='email']", "xpath:attributes"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "nkiyashko@asdco.ru"
    }, {
      "id": "f84977da-fcf9-4ae9-b8cb-8d9ba5334bad",
      "comment": "",
      "command": "click",
      "target": "css=.btn-primary",
      "targets": [
        ["css=.btn-primary", "css:finder"],
        ["xpath=//div[3]/button", "xpath:position"],
        ["xpath=//button[contains(.,'Sign in')]", "xpath:innerText"]
      ],
      "value": ""
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