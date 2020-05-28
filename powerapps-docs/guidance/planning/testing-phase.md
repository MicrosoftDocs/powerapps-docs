Testing Phase
=============

Now that your app is built, the next step is to start testing out the app. In
this section you will learn about the basics of how testing should be carried
out.

Types of tests
--------------

### Unit tests

Unit test is a test used to check whether a specific function or a feature of
your app is working correctly.

### End-to-end tests

End-to-end tests are used to check whether the overall solution runs correctly.
This is important because even if all unit tests are correctly functioning, the
integration between two units could potentially fail. The tests are done by
following a *test scenario* close to the use case of the actual business
process.

### User acceptance tests (UAT)

User acceptance test (UAT) is a test done by the **user** of the app instead of
the maker. This test is to ensure what has been built by the makers matches the
requirements initially requested by the user.

Tips:

-   Test with the real end users

-   Try to choose users with diversity in terms of IT skill levels. This will
    allow you to gain variety of different feedback

-   Don’t give the user instructions; see if they can understand the app
    intuitively

-   Observe how they navigate the app without assistance & see where to improve
    the design

-   When the user is stuck on a screen, ask them to explain what their
    expectation was

-   Try out different devices to make sure the test cases behave the same

-   Ideally, test the app in the actual environment / location if using offline
    capabilities

-   Ask your users to try to “break” your app, such as by entering unusual
    characters in text fields

-   Users will typically test “the happy path” (the path a user takes when
    everything is going perfectly); ask them to also test scenarios such as
    canceling an expense report instead of submitting it, or denying an expense
    report instead of approving it.

Your users may not be familiar with testing software. Let them know what kind of
feedback you are looking for. It’s often helpful to provide a template for
“bugs” to make sure testers explain exactly what they were doing, what happened,
what they expected to happen instead, and any relevant information about their
testing environment (such as device type and browser).

It is natural and OK for the user to request changes to the specifications or
ask for additional requirements. These requests should be recorded in the
feature list described in [Prioritizing features and
requests](https://review.docs.microsoft.com/en-us/powerapps/guidance/envisioning-design-prioritize-features)
section.

Creating test cases and scenarios
---------------------------------

In order to write comprehensive test scenarios and test cases, you should refer
back to the Planning and Design phases to make sure you test all the important
scenarios.

First step is to write the unit tests. Make sure you break down the tests to
each feature or function. The test cases for unit tests should be listed like
the table below:

| **Test Case No.** | **Description of test**                              | **Inputs to test with** | **Expected Result**                          | **Result** |
|-------------------|------------------------------------------------------|-------------------------|----------------------------------------------|------------|
| 1-1               | Submit order details from form                       | Order No. 16516         | Order is successfully submitted              |            |
| 1-2               | Check PDF is generated and is attached to the record | N/A                     | PDF file attached to the record              |            |
| 1-3               | Check email notification is sent to user             | test\@contoso.com       | Email is received by the specified recipient |            |

Tools to help you test (Canvas Apps)
------------------------------------

### Power Apps Test Studio (Experimental)

For testing inside Canvas apps, there is a tool built-in called Power Apps Test
studio that allows you to write, organize, and automate tests for canvas apps.
The Power Apps test studio should be used when setting up a unit test to ensure
features and functions are correctly functioning. You can find more information
about it in [the test Studio
documentation](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/test-studio).

### Monitor (Experimental)

When you are testing for performance issues, Monitor allows you to check the
network activity similar to a network trace in the browser. For details on the
Monitor tool, have a look at this [blog post: “Introducing Monitor to debug apps
and improve
performance](https://powerapps.microsoft.com/en-us/blog/introducing-monitor-to-debug-apps-and-improve-performance/)”.

Tools to help you test (Model-driven Apps)
------------------------------------------

### EasyRepro

EasyRepro is the tool provided for Dynamics 365 and Power Apps Model-driven
apps. It not only provides the testing tool but also has over 200+ sample test
cases to help you speed up the testing process. You can find more information
about it in [this blog post: "EasyRepro automated testing
framework"](https://powerapps.microsoft.com/en-us/blog/easyrepro-automated-testing-framework-june-update-is-now-available/)
and also access to [the EasyRepro GitHub
repository](https://github.com/Microsoft/EasyRepro).

### Solution Checker

Solution Checker is a tool that checks whether the solution you have created is healthy. You
can quickly review issues and see recommended fixes. For more information, have
a look at [the Solution Checker
documentation](https://docs.microsoft.com/en-us/powerapps/maker/common-data-service/use-powerapps-checker).
