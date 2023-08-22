---
title: "Power Apps Test Engine YAML format (preview)"
description: Describes the YAML format for test following the same guidelines as Power Fx.
author: jt000
ms.author: jasontre
ms.date: 08/11/2023
ms.reviewer: jdaly
ms.topic: article
contributors:
 - JimDaly
---

# Power Apps Test Engine YAML format (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Tests are defined in YAML following the same guidelines as Power Fx does. [Learn more about the Power Fx YAML formula grammar](/power-platform/power-fx/yaml-formula-grammar).

View the [PowerApps-TestEngine/samples](https://github.com/microsoft/PowerApps-TestEngine/tree/main/samples) folder for detailed examples.

## YAML schema definition

| Property | Description |
|---|---|
| [test](#test) | Defines one test suite, the test cases in the test suite and configuration specific to the test suite |
| [testSettings](#testsettings) | Defines settings for the test suite that are reused across multiple test cases |
| [environmentVariables](#environment-variables)| Defines variables that could potentially change as the app is ported across different environments |

## test

Used to define one test.

### test YAML schema definition

| Property | Required | Description |
|---|---|---|
| `testSuiteName` | Yes | The name of the test suite |
| `testSuiteDescription` | No | Additional information describes what the test suite does |
| `persona` | Yes | The user that is logged in to perform the test. Must match a persona listed in the [Users](#users) section | 
| `appLogicalName` | Yes | The logical name of the app that is to be launched. It can be obtained from the solution. For canvas apps, you need to add it to a solution to obtain it |
| `appId` | No | The ID of the app that is to be launched. Required and used only when app logical name isn't present. App ID should be used only for canvas apps that aren't in the solution
| `networkRequestMocks` | No | Defines network request mocks needed for the test |
| `testCases` | Yes | Defines test cases in the test suite. Test cases contained in test suites are run sequentially. The app state is persisted across all test cases in a suite |
| `onTestCaseStart` | No | Defines the steps that need to be triggered for every test case in a suite before the case begins executing |
| `onTestCaseComplete` | No | Defines the steps that need to be triggered for every test case in a suite after the case finishes executing |
| `onTestSuiteComplete` | No | Defines the steps that need to be triggered after the suite finishes executing |

#### test NetworkRequestMocks

| Property | Required | Description |
|---|---|---|
| `requestURL` | Yes | The request URL that gets mock response. Glob patterns are accepted |
| `responseDataFile` | Yes | A text file with the mock response content. All text in this file is read as the response |
| `method` | No | The request's method (GET, POST, etc.) |
| `headers` | No | A list of header fields in the request in the format of [fieldName: fieldValue] |
| `requestBodyFile` | No | A text file with the request body. All text in this file is read as the request body |

For optional properties, if no value is specified, the routing applies to all. For example, if `method` is null, we send back the mock response whatever the method is as long as the other properties all match.

For Sharepoint/Dataverse/Connector apps, `requestURL` and `method` can be the same for all requests. `x-ms-request-method` and `x-ms-request-url` in  headers may need to be configured in that case to identify different requests.

#### test TestCases

| Property | Required | Description |
|---|---|---|
| `testCaseName` | Yes | The name of the test case, it's used in reporting success and failure |
| `testCaseDescription` | No | Additional information describes what the test case does |
| `testSteps` | Yes | A set of Power FX functions describing the steps needed to perform the test case |

#### test TestSteps

- This can use any existing [Test Engine Power Fx functions](/power-platform/power-fx/overview) functions or [specific test functions](powerfx.md) defined by this framework.
- It should start with a `|` to allow for multiline YAML expressions followed by an `=` sign to indicate that it's a Power Fx expression
- Functions should be separated by a `;`
- Comments can be used and should start with `//`

## testSettings

Used to define settings for the tests in the test plan.

### testSettings YAML schema definition

| Property | Required | Description |
|---|---|---|
| `locale` | Yes | The locale/culture syntax in which the test cases or test steps are written in. See [Global Support in Microsoft Power Fx](/power-platform/power-fx/global) for more information. If unspecified, `CultureInfo.CurrentCulture` is used for the locale by default for parsing the test steps. |
| `browserConfigurations` | Yes | A list of browser configurations to be tested. At least one browser must be specified. |
| `recordVideo` | No | Default is false. If set to true, a video recording of the test is captured. |
| `headless` | No | Default is true. If set to false, the browser shows up during test execution. |
| `timeout` | No |Timeout value in milliseconds. Default is 30,000 milliseconds (30s). If any operation takes longer than the timeout limit, it ends the test in a failure. |
| `filePath` | No |  The file path to a separate yaml file with all the test settings. If provided, it will **override** all the test settings in the test plan. |

#### testSettings Browser configuration

| Property | Required | Description |
|---|---|---|
| `browser` | Yes | The browser to be launched when testing. Should match the [browsers supported by Playwright](https://playwright.dev/dotnet/docs/browsers). |
| `device` | No | The device to emulate when launching the browser. Should match the [devices supported by Playwright](https://playwright.dev/dotnet/docs/api/class-playwright#playwright-devices)
| `screenHeight` | No | The height of the screen to use when launching the browser. If specified, `screenWidth` must also be specified. |
| `screenWidth` | No | The width of the screen to use when launching the browser. If specified, `screenHeight` must also be specified.|

## Users

To ensure credentials are stored in secure manner, the test definition references users using a persona name. Storing credentials in test plan files isn't supported.

References to the user credentials are located under the `environmentVariables` section as a list of `users`

Example:

```yaml
environmentVariables:
    - users:
        - personaName: "User1"
          emailKey: "user1Email"
          passwordKey: "user1Password"
        - personaName: "User2"
          emailKey: "user2Email"
          passwordKey: "user2Password"
```

The `personaName` is used as part of the test definition to indicate what user to run the test as.

### Supported credentials storage mechanisms

> [!NOTE]
> Multi-factor authentication is not supported.

#### Environment variables

To store credentials as environment variables, you can set it as follows:

```powershell
# In PowerShell - replace variableName and variableValue with the correct values
$env:variableName = "variableValue"
```

In the YAML, two properties need to be defined to indicate that this user's credentials are stored in environment variables:

- `emailKey`: The environment variable used to store the user's email.
- `passwordKey`: The environment variable used to store the user's password.

Example YAML:

```yaml
    - personaName: "User1"
      emailKey: "user1Email"
      passwordKey: "user1Password"
```

Example PowerShell to set user credentials based on YAML:

```powershell
$env:user1Email = "someone@example.com"
$env:user1Password = "fake password"
```

### See also

[Power Apps Test Engine overview (preview)](overview.md)   
[Power Apps Test Engine Power Fx functions (preview)](powerfx.md)   

[!INCLUDE [footer-banner](../../includes/footer-banner.md)]

