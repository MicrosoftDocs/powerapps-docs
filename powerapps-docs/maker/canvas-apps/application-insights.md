# Analyze app telemetry using Application Insights

You can connect your app with [Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview), a feature of [Azure Monitor](https://docs.microsoft.com/azure/azure-monitor/overview). Application Insights is an extensible Application Performance Management (APM) service for developers and DevOps professionals.

With your app connected to Applications Insights, you can collect
information to help you drive better business decisions and improve the quality of your apps.

In this quickstart, you'll instrument a canvas app called Kudos. This helps you explore, discover telemetry concepts and apply them to your own canvas
apps. The sample Kudos app is part of a suite of employee engagement apps
available for download from [Employee Experience Starter
Kit](https://powerapps.microsoft.com/blog/powerapps-employee-experience-starter-kit).

## Prerequisites

- You must have access to [Azure Portal](https://portal.azure.com).
- You must have the permissions to [create Azure resources](https://docs.microsoft.com/azure/role-based-access-control/quickstart-assign-role-user-portal).
- Optional: 
    - Download and install Kudos app from [Employee Experience Starter
Kit](https://powerapps.microsoft.com/blog/powerapps-employee-experience-starter-kit).
    - You can also use an existing app.

## Create an Application Insights resource

Before you can send telemetry for an app, you will need to create an Azure
Application Insights resource to store the events.

1. Sign in to the [Azure portal](https://portal.azure.com/).

1. Search for Application Insights:

    ![Azure Application Insights](media/azureappinsights.png)

1. Create an Application Insights resource:

    ![Add a Azure Application Insights resource](media/azureappinsights-add.png)

1. Enter the appropriate values and select **Review + create**. For more details, read [Create an Application Insights resource](https://docs.microsoft.com/azure/azure-monitor/app/create-new-resource). 

    ![Create a resource](media/createresource.png)

1. After the Application Insights instance is created, you'll see the instance overview. Copy the **Instrumentation Key**. You'll need this key to configure your app.

    ![Copy Instrumentation Key](media/instrumentation-key.png)

## Connect your app to Application Insights

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from the left navigation. From the list of apps, select the **Kudos** app and then select **Edit**:

    ![Edit Kudos App](media/edit-kudos-app.png)

    > [!NOTE]
    > You can also [create](open-and-run-a-sample-app.md) a new app or [edit](edit-app.md) any existing app instead.

1. Select **App** object from the left navigation tree view and paste the **Instrumentation Key**:

    ![Add Instrumentation Key](media/add-instrumentation-key.png)

1. **Save** & **Publish** your app.

1. **Play** the published app and browse through different screens. 

As you browse through different screens, events are automatically logged to Application Insights including the usage details such as:

- Where the app is accessed from.
- Which are the devices used.
- The browser types used.

> [!IMPORTANT]
> You must play the published app to send events to Application
Insights. Events are not sent to Application Insights when you preview the
app in Power Apps Studio.

## View events in Application Insights

1. Sign in to the [Azure portal](https://portal.azure.com/) and open the Application Insights resource you created [earlier](#create-an-application-insights-resource).

1. Scroll down in the left navigation pane and select **Users** under the **Usage** section. 

    > [!NOTE]
    > **Users** view shows usage details of the app, such as:
    > 
    > - Number of users that viewed the app.
    > - Number of sessions by the users for the app.
    > - Number of events logged for the app.
    > - Operating systems and browser version details of the users.
    > - Region and location of the users.
    > 
    > For more details, read [Users, sessions, and events analysis in Application Insights](https://docs.microsoft.com/azure/azure-monitor/app/usage-segmentation).

1. Select one of the user sessions to drill into specific details. You can see information such as the session length and the screens visited:

    ![Usage details for users](media/appinsights-users.gif)

1. Select the **Events** view in left navigation pane under **Usage** section. You can see a summary of all the screens viewed across all app sessions:

    ![Event details for the app](media/appInsights-events.gif)

> [!TIP]
> Some of the additional Application Insights features you can use are:  
> - [**Funnels**](https://docs.microsoft.com/azure/azure-monitor/app/usage-funnels)
> - [**Cohorts**](https://docs.microsoft.com/azure/azure-monitor/app/usage-cohorts)
> - [**Impact analysis**](https://docs.microsoft.com/en-us/azure/azure-monitor/app/usage-impact)
> - [**Retention analysis**](https://docs.microsoft.com/azure/azure-monitor/app/usage-retention)
> - [**Usage flows**](https://docs.microsoft.com/azure/azure-monitor/app/usage-flows)

## Create custom trace events

You can write custom traces directly to Application Insights and start to analyze information specific to your scenario. [Trace](https://docs.microsoft.com/powerapps/maker/canvas-apps/functions/function-trace) function allows you to collect:

- Granular usage information for controls on the screens.
- Which specific users are accessing your app.
- What errors occur.

Tracing can also help diagnose issues as you can send a trail of information as your users browse through your app and perform different actions.

When sending custom trace information to Application Insights from your app,
there are 3 severities you can associate with the trace message. These
severities are Information, Warning or Error. Depending on your scenario, you
can choose to send trace message with either of these severities, so you query
the data and take specific actions based on the message severity.

**Note**: If you are logging any personnel data, you will need to consider any
data compliance obligations, such as GDPR, that you may also need to implement. 

You will now update your app and create a new component to gather customer
feedback on each screen of the app. You will write the events to App Insights.

1.  Select the components option in the Tree view

![A screenshot of a cell phone Description automatically generated](media/6546b89d737b92f7317edfc26aad4804.png)

1.  Create a New component and resize the width and height

![A screenshot of a cell phone Description automatically generated](media/4eae9c80e22cdfcd14f78b8071c363ee.png)

1.  Add a smile and frown icon to the component

![A screenshot of a social media post Description automatically generated](media/087d0df17fba50c8b6e4f18f572acc85.png)

1.  Create a new custom input property using the screen data type. This allows
    us to capture the screen name the component is placed on, and we can log
    this information to Application Insights.

![A screenshot of a cell phone Description automatically generated](media/da3f1dddda108473f505ca9598e6fb75.png)

1.  Rename the component and icons.

![A screenshot of a cell phone Description automatically generated](media/753671f65a0786af697db03c195c951b.png)

1.  Select the FrownIcon and enter the below expression in the OnSelect event of
    the control. As well as the Trace message, we will send the User name,
    email, the screen the feedback was received on and a feedback value of -1 to
    indicate the frown to App Insights.

>   Trace(

>   "App Feedback",

>   TraceSeverity.Information,

>   {

>   UserName: User().FullName,

>   UserEmail: User().Email,

>   Screen: FeedbackComponent.FeedbackScreen.Name,

>   FeedbackValue: "-1"

>   }

>   );

>   Notify("Thanks for you feedback!");

![A screenshot of a social media post Description automatically generated](media/196035c955068fed0667773318b31fde.png)

1.  Select the SmileIcon and enter the below expression in the OnSelect event of
    the control. For the smile, we will send a feedback value of 1.

Trace(

"App Feedback",

TraceSeverity.Information,

{

UserName: User().FullName,

UserEmail: User().Email,

Screen: FeedbackComponent.FeedbackScreen.Name,

FeebackValue: "1"

}

);

Notify("Thanks for you feedback!");

1.  Add the component to one of the screens in your application.

![A screenshot of a social media post Description automatically generated](media/9e675ab1b619e24030a6835132273abf.png)

1.  Save & Publish your app.

2.  Play the published app and send a Smile and Frown feedback from your
    screens.

\*\* Note: Telemetry events will only get sent to Application Insights when you
play the published app. Playing the preview app in the Studio will not send
events to Application Insights.

![A screenshot of a cell phone Description automatically generated](media/faf6dc92e7372593c8c009347e4bbe5a.png)

Analyze the information in App Insights

You can now begin to analyze the information you sent using the Trace function
from your application in App Insights.

1.  Sign in to the [Azure portal](https://portal.azure.com/)

2.  Select the App Insights resource you created earlier

![A screenshot of a computer Description automatically generated](media/0ae9a50a8fc0b142da873c574d4d4a38.png)

1.  Select Logs in the left tree menu.

![A screenshot of a social media post Description automatically generated](media/16cbc2b8fb2cfe3b75b133937e83ea1e.png)

1.  Type the below query and select Run. The feedback received from your app are
    returned.

![A screenshot of a social media post Description automatically generated](media/9229bc871d9fe8f1c46f829d3fe67ab0.png)

1.  Select a row in the results and expand the custom dimensions field. The
    values for Screen, UserName, UserEmail and FeedbackValue for the OnSelect
    event of the smile or frown icon in your component have being recorded.
    There are also some additional values recorded for each event sent to
    Application Insights, such as the AppId, AppName and AppSessionId.

![A screenshot of a social media post Description automatically generated](media/c52dd2ea4d94082ce1032376ea3e0399.png)

1.  Using the below query, you can extend the properties of the JSON custom
    dimensions and present them columns in the results view.

    Log queries are extremely powerful, and you can use them to join multiple
    tables, aggregate large amounts of data and perform complex operations. You
    can learn more about Log
    queries [here](https://docs.microsoft.com/en-us/azure/azure-monitor/log-query/log-query-overview). 

traces

\| extend customdims = parse_json(customDimensions)

\| where message == "App Feedback"

\| project timestamp

, message

, AppName = customdims.['ms-appName']

, AppId = customdims.['ms-appId']

, FeedbackFrom = customdims.UserEmail

, Screen = customdims.Screen

, FeedbackValue = customdims.FeedbackValue

\| order by timestamp desc

![A screenshot of a social media post Description automatically generated](media/c489903a35fe02d39f1b8467abf1e1af.png)

Export the information to Power BI

You can also export your Application Insights data and query results to Power BI
for further analysis and data presentation to stakeholders.

1.  From the log analytics query window, select export.

2.  Select "Export to Power BI (M query)" option. This download a Power BI query
    file to your machine. Open the file and copy the query.

![A screenshot of a social media post Description automatically generated](media/fb45b10cf5ed2b4ec683ac9aa2c7803a.png)

1.  Open Power BI.

2.  Select "Get Data" and "Blank Query" menu option.

![A screenshot of a cell phone Description automatically generated](media/ac6f1be345b6bbbc5cbad7002cc6f0f0.png)

1.  In the query window, select "Advanced editor". Paste the query from step 2
    into the window and select "Done" followed by "Close & Apply".

![A screenshot of a social media post Description automatically generated](media/5c3bc2f7be5ad75cfee2bb8f31f6999e.png)

1.  With my data, I can create charts and visualizations in Power BI to
    represent feedback received in my app, and make data-based decisions and
    actions.

![](media/c5743349347f61ad5215440e625453ad.png)

Default event context and dimensions

In order to track what a user does over time, Application Insights needs an ID
for each user or session. The following IDs are included in every trace or
screen view event sent.

| Event property | Represents                                                 |
|----------------|------------------------------------------------------------|
| User_Id        | The AAD user object id of the end user of the application. |
| Session_Id     | The Power Apps player session id.                          |

In addition to these properties, a set of default dimensions are also added to
the customDimensions property on each event. These can be used to identify the
application and application sessions the events occurred in. If you log addition
custom data using the trace function, they will also appear in the custom
dimensions.

| Dimension Name  | Represents                                            |
|-----------------|-------------------------------------------------------|
| ms-appId        | The Application Id of the app that sent the event     |
| ms-appName      | The Application name of the app that sent the event   |
| ms-tenantId     | The Tenant Id related to the app that sent the event. |
| ms-isTest       | If the event was sent during the execution of a test. |
| ms-appSessionId | The application session Id.                           |

 
