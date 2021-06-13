# How to customize the Issue Reporting app

The Issue Reporting Power App template for Microsoft Teams is designed to be a
complete app experience but allow makers to easily extend it for their own
purposes. In this guide we will go over how to customize the Issue Reporting app
in Power Apps in Microsoft Teams.

Before you can customize the app, you must install it from the Teams store. You
can get the app at <https://aka.ms/TeamsIssueReporting> .

Once the app is installed you can then customize the app using the following
steps

# Opening Power Apps app in Microsoft Teams

1.  In Microsoft Teams, select the **…** button from the left menu.

2.  Type **Power Apps** in the search field.

    ![](media/34b78dbbc16206691ae83bd7e295324a.png)

3.  Select the Power Apps app from the list to open the app. Power Apps will
    open inside of teams

4.  Right click on the **Power Apps** logo and select **Pin** to lock the app to
    the side menu so it is easy to get to in the future.

| ![](media/378e9ccb5b2952d6156f29c03b12e06b.png) |   |
|-------------------------------------------------|---|

1.  It is recommended that you “pop out” Power Apps so that if you need to
    navigate somewhere else in Microsoft Teams you won’t lose your app
    configuration. To pop out the Power Apps app, right mouse click on the Power
    Apps logo and select **Pop out app**.

![](media/3ed835bbfe3a1599ede28e8d9587e268.png)

1.  Now that you have loaded the Power Apps app, select **Build**.

![](media/0d034b5046f496651172b75d89670462.png)

1.  This screen will show all the teams that have Power Apps installed in them.

2.  Select the team in which you installed the Issue Reporting app.

3.  Select **Installed apps.** This will show all apps installed in the Team.

4.  Issue Reporting solution includes two apps: **Issue Reporting** for users to
    report issues, and **Manage issues** for managers to use to analyze issue
    reporting history and create or modify Issue templates.

5.  Select **See more** in the **Issue Reporting** tile.

    ![Graphical user interface, application Description automatically
    generated](media/7c8d162b00f816d7b0b42cf019ca7eef.png)

6.  You will now see all of the apps, tables, flows, and chatbots in the Team.

    ![Graphical user interface, application Description automatically
    generated](media/f03d4d5b0082790b4af1401fc7abf751.png)

## Extend the Issue Reporting data model

If you are modifying or adding any fields to your app, you will want to first
update or add these columns in their Dataverse tables. In this section we will
explore the data model for Issue Reporting and how to modify it in Power Apps in
Microsoft Teams. Below is the data model for Issue Reporting.

### ![](media/1edaebe007f0fb052f6340b09a6b14a9.png)

Before modifying the fields, you need to first decide where the fields you want
to add should go. What are the users doing when they should see or interact with
these fields?

-   **Issue Report**

    Issues refer to a problem or trouble being faced by the Users. Information
    such as the Name, Issue category, issue template, Planner Task ID, due date,
    assigned user and description are stored in the Issue reports table.

    An issue can be related only to a single Category and Template.

-   **Issue Report Category**

    Categories are used to group similar kind of issues. Details such as the
    Name, category icon, Planner Bucket ID are stored in the Issue Report
    Categories table. A Category can have multiple Issues and Issue Templates
    associated to it.

-   **Issue Report Templates**

    Issue templates have predefined questions that must be answered by the users
    while creating an issue which helps us in understanding it better. Details
    such as the Due Date, Category the user to whom the tasks should be
    assigned, the primary contact information are stored in the Issue Report
    Templates table. There can be multiple questions and issues related to an
    Issue template. When an Issue Category is selected, the questions asked on
    the issue report form are based on the template.

-   **Issue Report Questions**

    Questions are part of the Issue Templates which help in explaining the issue
    in a better way. Details such as the Issue template and the sequence are
    stored in the Issue Report Questions table. There can be multiple questions
    in an Issue template

-   **Issue Report Settings**

    Settings are used to store configurations for the app, including the Team
    and Planner Ids for where to log issues as Planner Tasks.

-   **Issue Report User Setting**

    User settings are used to store user preferences pertaining to seeing the
    Power Apps splash screen every time they login to the app. There is one
    record for each user.

-   **Issue Report Photo**

    This table has been included to hold photos for issues. This is currently
    not used in the app but is provided for easy extension.

## Issue Reporting Screens

From the list of apps, chatbots, flows, and tables, select the **Issue
Reporting** app.

![Graphical user interface, text, application Description automatically
generated](media/b96bcff99c1b9a74f27081ee1509771a.png)

Now that Issue Reporting is open in Power Apps in Microsoft Teams, select the
**Tree View**.

![](media/fc3c6dc8c74bc43a913746718654a62e.png)

From the Tree View you can see the screens included in the app. Clicking the
arrow to the left of a screen will expand the contents of the screen, giving you
access to the components of the screen, including galleries, buttons, text
labels, and text input controls.

The following are the screens in Issue reporting:

| **Screen**                  | **Description**                                                                                                                                                                      |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Landing Screen              | This screen displays an image the the app title as the app is loading.                                                                                                               |
| Hidden Admin Screen         | This is a helper screen for admins to try and understand the way that theming works in the app and support for dark mode and high contrast. This screen is not visible to app users. |
| Insights Screen             | This is the first screen that users see, which provides insight to the number of issues created and providing access for users to navigate to the issue report screen.               |
| Issue Report Screen         | This screen is the form that users complete to create an issue.                                                                                                                      |
| Issue Stats Screen          | This screen displays the quantity of issues by status.                                                                                                                               |
| Template Selection Screen   | This screen is the list of category templates from which a user selects when creating an issue.                                                                                      |
| Assignment Selection Screen | This screen is where the user searches for and selects the user to whom the issue should be assigned.                                                                                |
| Issue Submission Screen     | This screen is the confirmation message when an issue has been submitted.                                                                                                            |
| Settings Missing Screen     | This screen is displayed if a user attempts to open the app without first configuring the Microsoft Planner location.                                                                |
| Tasks Access Denied Screen  | This screen is displayed if a user attempts to submit an issue when they do not have access to the Planner instance that the app is configured to use.                               |

## Manage Issue Screens

Now let’s look at the screens in the **Manage Issues** app:

1.  In the Power Apps app, select the **Build** tab

2.  Select the team in which you installed the Issue Reporting app.

3.  Select **Installed apps.** This will show all apps installed in the Team.

4.  Select **Manage issues** in the **Issue Reporting** tile.

    ![](media/8aeeb9a564a6d76035847d36a30e25f8.png)

5.  Manage issues will open in the designer.

6.  Select the **Tree view** and review the screens in the Manage Issues app.

![](media/19c181a698afcf23d5f594e1f462bb4e.png)

The following are the screens in the Manage Issues app:

| **Screen**               | **Description**                                                                                                                                                                                                      |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Landing Screen           | Displays an image and the app name as the app loads                                                                                                                                                                  |
| Hidden Admin Screen      | This screen is not visible to users of the app--it is designed to make it easy for makers to simulate scenarios within the designer. For example you can toggle dark mode on and see how the app looks in dark mode. |
| Insights Screen          | The primary screen of the app, shows a summary of issues created by status and navigate to the task view in Planner.                                                                                                 |
| Issue Templates Screen   | From this screen, managers can add or modify issue categories and create issue templates.                                                                                                                            |
| Settings Screen          | Screen from which an administrator can manage user settings like restricting the manage app to Owner or selecting the Team and Planner where tasks will be created.                                                  |
| About Screen             | Scree that displays more details about the app.                                                                                                                                                                      |
| Incorrect Context Screen | This screen displays when a user tries to launch the app outside of Microsoft Teams or in mobile.                                                                                                                    |

## Common customization scenarios:

In this section we discuss common customization/extension scenarios for Issue
Reporting, and where you would make these changes

### Add logo to launch screen

If you want to modify the loading screen of the Issue reporting loading screen,
such as adding your logo to it, you would make this change in the **Landing
Screen** of the **Issue Reporting**  app.

### Automate task assignment

To automate task assignment, you would update the formula for create issue on
the **Issue Report** screen of the **Issue reporting** app, or use a Power
Automate flow. See **Add business logic for automated task assignment** (insert
link).

### Modify app purpose

Issue Reporting can be used as a starting point for any kind of scenario where a
requestor submits an item for someone else to work on or resolve. It could be
modified into a ticket management system like a helpdesk request system or a
work order tracking system. See an example of modifying the purpose of the app
in **Convert issue reporting app to a work order management app** (insert link).

### Integrate with other task management system

The Power Platform includes connectors to multiple task scheduling applications,
such as Microsoft To-do, Jira, and Trello. Using Power Automate, you can
integrate tasks created in Issue Reporting with other task management systems
than Planner. This app can also be combined with other apps, such as
[**Inspection.**](../../../../../Downloads/Docs/aka.ms/teamsinspection)

### Add additional fields to populate when a task is created

Manage issues populates the most common fields used in Planner when creting a
task, such as Description, Title, and Assigned to; however, you may want to
populate additional fields or change the way the fields are mapped. To modify
this logic you would update the formula for creating issues on the **Issue
Report** screen of the **Issue reporting** app. See **Add urgency flag to
reported issues** (insert link) for an example of adding a field in Issue
Reporting to designate urgent issues.

## Publish changes

When you are done making modifications to the apps, select **Save** to save your
changes**.**

>   ![](media/06b7b0f0659349e2f14e73181d19c48b.png)

-   To preview your changes, click the
    ![](media/4e3f450e832033c418a717c40f48f91c.png) button

    -   The app will launch in preview mode, where you can test the user
        experience when running the app

    -   To exit preview mode, press **Escape** on your keyboard or click the
        **X** in the upper right corner

![](media/15e4d4a6d569e5dee8706aa89311aa63.png)

-   To publish your app changes, click the
    ![](media/8d74091f0d73cc7758738c538e16bf8f.png) button

-   Publishing the app makes your changes visible to users of the app

-   A dialog will open confirming that you want to publish

    ![](media/7abe9b759d131416c74024250e126d7b.png)

-   To change app settings, such as icon and background color, click **Edit
    details**

-   To publish the app, click **Next**

-   On the next screen, confirm the channel you want the app to appear. You can
    add to other channels in the Team by pressing the **+** button

    ![](media/9c738bae1da8579dd1159a250f9bfd1f.png)

-   To complete publishing your changes, Click **Save and close**

## Customization considerations

Before modifying the Issue reporting app, consider the following items:

-   Where are my table customizations? Columns and tables added by you will go
    to **built by this team** section of the Power Apps app. You can also add
    new tables in the **See all** area.

![Graphical user interface, application, Teams Description automatically
generated](media/ddbd94d33295118be728bf160829b745.png)

-   Changes made to an app will be added as a new version of the app. If you get
    a new version from store, your customizations will not be overridden. You
    will get a new version that has the latest features, but the new version
    will not be published.

    For example, if you add a field called **urgent** to the issue report
    screen, then you install the latest version from the Teams store, your
    urgent field will still be visible in the app after the upgrade.

    ![Graphical user interface, application, Teams Description automatically
    generated](media/41b309ff976b41599884466c55f54ef9.png)

    ![Graphical user interface, application, Teams Description automatically
    generated](media/690aa704014f9a582d4c0896c9673d3f.png)

Figure 1 After upgrading the solution your current app version will still be
"live."

>   The updated version of the app is available from the version history of the
>   app. Selecting **Details** from the app list will display the versions of
>   the app and allow you to publish the new version.

>   ![Graphical user interface, application, Teams Description automatically
>   generated](media/963dc49d3863c3cba80a3570f7848036.png)

-   When customizing the app, pop out the Power Apps app in Teams so you don’t
    lose your changes when you navigate to other parts of Microsoft Teams.

-   The app theming has been developed to support dark and high contrast mode in
    Microsoft Teams. Changing the fill color of screens may break dark and high
    contrast modes
