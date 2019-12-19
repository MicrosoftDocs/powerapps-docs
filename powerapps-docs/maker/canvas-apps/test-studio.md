---
title: Test Studio for testing canvas app | Microsoft Docs
description: Describes Test Studio with overview, terminology, best practices and limitations.
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 11/18/2019
ms.author: aheaney
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Test Studio (experimental) 

Build end-to-end UI tests for your Canvas app using Test Studio. Maintain your app quality by continually validating your app works as expected when new changes or updates are deployed. 

## Overview

Testing is an important part of the Software Development Life Cycle (SDLC). Testing can help ensure the quality of the app you are delivering to your end-users. It can identify bugs or defects early in the release process and provides you an opportunity to fix these issues and make your app more reliable before releasing changes to your users. Depending on the size and usage of your app, manual testing of your changes may be enough. However, as your app grows in complexity and usage, you might want to begin thinking about a test strategy and ensuring mistakes in your app development get identified early and that they do not impact your end-user or customer productivity. If your app is mission-critical, even a small mistake can have a big impact on the day-to-day work of your end-users, and testing can help minimize the risk and prevent work-stoppages in your organization or for your customers. 

As you add or change features in your app, you need to perform tests against existing features to validate functionality has not been impacted. This can result in the testing cycle of your app becoming longer. Soon, regression testing your app may be longer than the time spent to develop new features. In fast paced development, thoroughly testing every feature in your app becomes a bottleneck to releasing your software. One option to reduce the test cycle time, and time spent on regression testing, is test automation. Test automation can help you test your app with minimal effort as each new version of your app is released, expand the test coverage of your app, save time spent on testing, and also identify those critical issues fast and early in your release process. 

Power Apps Test Studio is a low-code solution to write, organize and automate tests for your canvas apps. With Test Studio, tests are written using familiar Power Apps expressions or you can use a recorder to save every interaction and automatically generate the expressions for you. When you have written a test, you can play it back within the Test Studio to validate they are working as expected. When you are ready, you can also run the tests in a web browser and build the automated tests into your app deployment process. 

![Test Studio](./media/test-studio/test-studio.png)

> [!NOTE]
> This feature is still experimental and we recommend you use it to write tests for non-production apps. For more information, see [Experimental and preview features](working-with-experimental-preview.md).

## Test Studio Terminology

If you are new to testing, and before we begin to show you how to write tests for a sample app using Power Apps Test Studio, it’s important to understand some test terminology and some key testing concepts that we will be referencing in this article, primarily Test Cases, Test Suites and Test Assertions.

### Test Cases

Test cases are made up of a series of instructions or actions, called test steps. Test cases are executed to validate your app, or specific features in your app, are working as you expect. For example, I would like to validate that my expenses can only be submitted when they have an actual cost associated. A test case can help verify this condition or requirement is always met. 

In the Test Studio, test steps are written using the Power Apps expression language. Test expressions can consist of the same functions that are available to you when building your app, as well as additional expressions to support automated testing in your apps. 

### Test Suites

Test suites are used to organize, categorize or group your test cases together. As the number of test cases in your application grows, you may want to organize the test cases in specific features or functionality that make sense to you. For example, if I have an expense app, you may have a set of test cases to validate submitting expense reports, which you can organize into an Expense Creation test suite. You also may have another test suite that focuses just on Expense Approvals. 

In the Test Studio, test cases contained in test suites are run sequentially and the app state is persisted across all test cases in a suite. For example, if you have a test case that completes on Screen 5 in your app, the next test case in your test suite will begin running from Screen 5. This allow you to break down a complex test scenario into multiple test cases within a single suite, and the state is shared across all test cases. If your second test case expects to begin at the start screen of the App, you can navigate to the start screen as the first step in your test case. It’s important to remember that the App is not reloaded at the beginning of every test case in a test suite when planning your test execution. 

### Test Assertions

Every test case should have an expected result. To validate the expected result of a test against the actual result of your test, you can write Test assertions. An assertion is an expression that evaluates to true or false in the test. If the expression returns false, the test case will fail. 

In the expense app example above, you could write an assertion to validate that Expense reports cannot be created when an expense line items has a $0 cost associated. 

## Best practices

1. **Determine which test cases should be automated.**

    It’s difficult to automate all tests and we are not proposing that you rely on test automation completely. Manual testing in addition to test automation should be completed. Tests best suited to automation are

    - Repetitive tests.
    - High business impact functionality tests.
    - Features that are stable and not undergoing significant change.
    - Features that require multiple data sets. 
    - Manual testing that takes significant time and effort. 


2. **Keep test cases small.** 

    While a single test case can support testing all functionality in your app, we recommend that you avoid writing a monolithic test case and try to divide it into multiple test cases. Each test case could test a specific feature or functionality in your app.  If you have a single large test case which is testing multiple features, a failed assertion means the test case will fail and other functionality in your app will not get tested. Using multiple test cases contained in test suite will allow other functionality to get tested regardless if a previous test case failed. Using this strategy will also make it easier to update or modify and isolate test failures.


3. **Keep expressions to a single test action.**

    A test action can contain multiple expressions. Large multi-action test expressions for a single step may impact your ability to debug and isolate any test failures. A test step which contains multiple actions should be divided into one or more test steps containing single actions or expressions, as this would help you identify and troubleshoot issues faster.  


4. **Every test case should have an expected result.**

    Each test case should have 1 or more expected results. Test assertions should be used to validate the expected outcome(s) of your test against the actual outcome(s). Multiple assertions can be written for a single test case. 

5. **Use Test suites.**

    For maintenance, group or categorize similar test cases together and provide descriptions to describe the purpose and expected results of your test. 

## Known limitations

Blow are some known limitations you might encounter when writing tests. We are working to provide full control coverage in Power Apps Test Studio, but some controls are not yet supported.

- Components.   
- Code components written in the Power Apps Component Framework. 
- Nested galleries. 
- Controls not listed in this article are not supported.
- Person type columns in SharePoint.


