---
title: Testing Phase - Planning a Power Apps project | Microsoft Docs
description: Now that your app is built, the next step is to start testing it. You'll learn the basics of testing an app and discover Power Apps testing tools.
author: taiki-yoshida
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/16/2020
ms.subservice: guidance
ms.author: tayoshi
ms.reviewer: kathyos

---

# Testing phase

Now that your app is built, the next step is to start testing it. In
this section you'll learn the basics of how testing should be carried
out.

## Types of tests

### Unit tests

A *unit test* is used to check whether a specific function or feature of
your app is working correctly.

### End-to-end tests

*End-to-end tests* are used to check whether the overall solution runs correctly.
This is important because even if all unit tests function correctly, the
integration between two units can potentially fail. These tests are done by
following a test scenario that's close to the use case of the actual business
process.

### User acceptance tests

A *user acceptance test* (UAT) is done by the user of the app instead of
the maker. This test is to ensure that what has been built by the makers matches the
requirements initially requested by the user.

Here are some tips for getting good results from UATs:

- Test with the real users.

- Try to choose users with diversity in terms of IT skill levels. This way, you can get a variety of feedback.

- Don't give the user instructions; see whether they can understand the app
    intuitively.

- Observe how they navigate the app without assistance, and see where you can improve
    the design.

- When the user is stuck on a screen, ask them to explain what their
    expectation was.

- Try out different devices to make sure the test cases behave the same.

- Ideally, test the app in the user's actual environment or location if the app uses offline
    capabilities.

- Ask your users to try to "break" your app, such as by entering unusual
    characters in text fields.

- Users will typically test the "happy path" (the path a user takes when
    everything is going perfectly); ask them to also test scenarios such as
    canceling an expense report instead of submitting it, or denying an expense
    report instead of approving it.

Your users might not be familiar with testing software. Let them know what kind of
feedback you're looking for. It's often helpful to provide a template for
"bugs" to make sure testers explain exactly what they were doing, what happened,
what they expected to happen instead, and any relevant information about their
testing environment (such as device type and browser).

It's natural and OK for the user to request changes to the specifications or
ask for additional features. These requests should be recorded in the
feature list described in [Prioritizing features and requests](prioritizing-features.md).

## Creating test cases and scenarios

To write comprehensive test scenarios and test cases, you should refer
back to the [Planning phase](planning-phase.md) and [Designing phase](designing-phase.md) sections to make sure you test all the important
scenarios.

The first step is to write the unit tests. Make sure you break the tests down to
each feature or function. The test cases for unit tests should be listed like
the table below:

| Test case No. |   Description of test                                    |   Inputs to test with   |   Expected result                            |   Result   |
|---------------|----------------------------------------------------------|-------------------------|----------------------------------------------|------------|
| 1-1           | Submit order details from a form                         | Order No. 16516         | Order is successfully submitted              |            |
| 1-2           | Check that a PDF is generated and attached to the record | N/A                     | PDF file is attached to the record           |            |
| 1-3           | Check email notification is sent to user                 | test\@contoso.com       | Email is received by the specified recipient |            |

## Tools to help you test canvas apps

### Power Apps Test Studio (experimental)

For testing inside canvas apps, you can use a built-in tool named Power Apps Test
Studio to write, organize, and automate tests for canvas apps. More information:
[Test Studio (experimental)](../../maker/canvas-apps/test-studio.md)

### Azure Monitor (experimental)

When you're testing for performance issues, you can use Monitor to check
network activity, similar to a network trace in the browser. For details about the
Monitor tool, see the blog post [Introducing Monitor to debug apps and improve performance](https://powerapps.microsoft.com/blog/introducing-monitor-to-debug-apps-and-improve-performance/).

## Tools to help you test model-driven apps

### EasyRepro

EasyRepro is the tool provided for Dynamics 365 and Power Apps model-driven
apps. It not only includes a testing tool but also has over 200 sample test
cases to help you speed up the testing process. For more information,
see the blog post [EasyRepro automated testing
framework](https://powerapps.microsoft.com/blog/easyrepro-automated-testing-framework-june-update-is-now-available/),
and access it at the [EasyRepro GitHub
repository](https://github.com/Microsoft/EasyRepro).

### Solution checker

The solution checker is a tool that checks whether the solution you've created is healthy. You
can quickly review issues and see recommended fixes. More information: [Use solution checker to validate your model-driven apps in Power Apps](../../maker/data-platform/use-powerapps-checker.md)

> [!div class="nextstepaction"]
> [Next step: Publish and share the app](discoverability.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]