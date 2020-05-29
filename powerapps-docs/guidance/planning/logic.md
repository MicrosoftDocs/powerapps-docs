Where to place logic - Canvas apps, Model Driven Apps, Common Data Service or Power Automate flows?
===================================================================================================

Your app will have business logic, such as data validation (using the right
format for an email address, for example), calculations, selecting the next
process step based on data, enabling a button when all required fields have
data, and so forth. This article explains some considerations for deciding where
to place the logic in your system.

Power Apps - Canvas Apps
------------------------

You set logic in Canvas apps using formulas.

All of the formula logic is processed on the device the app is run on. The more
complex the logic is, the more processing power the device will require to be
able to handle all of the logic.

To keep the app performant, you should consider the following when placing logic
in Canvas apps:

-   Use in situations where immediate change visible on the screen is required

-   Use only simple logic and avoid complex formulas with dozens of lines

-   Limit to a few data connectors in a formula

-   Avoid using logic to manipulate or transform data

-   Avoid processing multiple records at a time (for example, avoid using ForAll)

[Learn more about formulas in Canvas
apps](../../maker/canvas-apps/working-with-formulas).

Power Apps – Model-Driven Apps
------------------------------

Model-driven apps provide several ways to run logic. There are four types of
logic using low-code methods that are aimed for all developers:

-   Business Process Flows

-   Workflows

-   Actions

-   Business Rules

Additionally, for pro-developers:

-   Client-side scripting

-   API development

-   Using code with web resources

All of these options run on the device that runs the apps. Consider
placing logic in Model-driven apps if:

-   Logic needs to be run on the device

-   The logic requires multiple entities (tables)

-   You need sophisticated logic that is not available with out of the box
    features

In general, if you are making apps with complex logic, consider using
Model-driven apps instead of trying to do everything using Canvas apps.

[Learn more about business logic in Model-driven
apps](../../maker/model-driven-apps/guide-staff-through-common-tasks-processes).

Power Automate flows
--------------------

For use cases where there is complex logic to run, you need multiple connectors
or you don’t want the user to wait for the action to finish, Power Automate
flows is a good option to run logic. Consider Power Automate flows
if:

-   Logic needs to run across multiple connectors

-   You are creating an approval process

-   Producing output in another format

-   You want to reduce dependency on device-side processing power

[Learn more about Power
Automate](https://docs.microsoft.com/power-automate/).

Common Data Service
-------------------

You can set logic in Common Data Service so that all of the logic is run in the
service rather than the devices. This makes the app more performant and also
makes the logic independent of the apps and flows to ensure data is used in a
particular way.

For example, if you want to require that address is input for all applications
and flows that use the Account entity, you should set this logic in Common Data
Service rather than in each app and flow.

There are several ways of applying logic to Common Data Service. Using low code,
you can set up things such as autonumbering fields, calculated fields, and
roll-up fields. For pro-developers, you can apply business logic using code by
creating a plugin, or developing workflow extensions.

[Learn more about applying business logic in Common Data
Service](../../maker/common-data-service/cds-processes).
