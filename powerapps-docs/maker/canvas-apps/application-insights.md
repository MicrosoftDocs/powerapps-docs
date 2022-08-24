---
title: Analyze telemetry of a canvas app using Application Insights
description: Learn about how to analyze app telemetry of canvas apps using Application Insights.
author: mattgon
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 08/23/2022
ms.subservice: canvas-maker
ms.author: austinj
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
  - maustinjones 
  - mattgon
---

# Analyze telemetry of a canvas app using Application Insights

You can connect your app with [Application Insights](/azure/azure-monitor/app/app-insights-overview), a feature of [Azure Monitor](/azure/azure-monitor/overview). Application Insights includes powerful analytics tools to help you diagnose issues and to understand what users actually do with your app. 

With your app connected to Applications Insights, you can collect information to help you drive better business decisions and improve the quality of your apps.

In this quickstart, you'll instrument a canvas app called Kudos. This helps you explore, discover telemetry concepts, and apply them to your own canvas apps. The sample Kudos app is part of a suite of employee engagement apps available for download from [Employee Experience Starter Kit](https://powerapps.microsoft.com/blog/powerapps-employee-experience-starter-kit).

## Prerequisites

- You must have access to the [Azure portal](https://portal.azure.com).
- You must have the permissions to [create Azure resources](/azure/role-based-access-control/quickstart-assign-role-user-portal).

### Optional

- Download and install the Kudos app from [Employee Experience Starter Kit](https://powerapps.microsoft.com/blog/powerapps-employee-experience-starter-kit). You can also use an existing app instead.

## Create an Application Insights resource

Before you can send telemetry for an app, you'll need to create an Application Insights resource to store the events.

1. Sign in to the [Azure portal](https://portal.azure.com/).

1. Search for Application Insights:

    ![Application Insights.](./media/application-insights/azureappinsights.png "Application Insights")

1. Create an Application Insights resource:

    ![Add an Application Insights resource.](./media/application-insights/azureappinsights-add.png "Add an Application Insights resource")

1. Enter the appropriate values and select **Review + create**. For more details, read [Create an Application Insights resource](/azure/azure-monitor/app/create-new-resource). 

    ![Create a resource.](./media/application-insights/createresource.png "Create a resource")

1. After the Application Insights instance is created, you'll see the instance overview. Copy the **Instrumentation Key**. You'll need this key to configure your app.

    ![Copy Instrumentation Key.](./media/application-insights/instrumentation-key.png "Copy Instrumentation Key")

## Connect your app to Application Insights

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from the left navigation. From the list of apps, select the **Kudos** app and then select **Edit**:

    ![Edit Kudos app.](./media/application-insights/edit-kudos-app.png "Edit Kudos app")

    > [!NOTE]
    > You can also [create](open-and-run-a-sample-app.md) a new app or [edit](edit-app.md) any existing app instead.

1. Select the **App** object from the left navigation tree view and paste the **Instrumentation Key**:

    ![Add Instrumentation Key.](./media/application-insights/add-instrumentation-key.png "Add Instrumentation Key")

1. **Save** and **Publish** your app.

1. **Play** the published app and browse through different screens. 

As you browse through different screens, events are automatically logged to Application Insights, including the usage details such as:

- Where the app is accessed from.
- Which devices are used.
- The browser types used.

> [!IMPORTANT]
> You must play the published app to send events to Application Insights. Events are not sent to Application Insights when you preview the app in Power Apps Studio.

## View events in Application Insights

1. Sign in to the [Azure portal](https://portal.azure.com/) and open the Application Insights resource you created [earlier](#create-an-application-insights-resource).

1. Scroll down in the left navigation pane and select **Users** under the **Usage** section. 

    > [!NOTE]
    > **Users** view shows usage details of the app, such as:
    > - Number of users who viewed the app.
    > - Number of sessions by the users for the app.
    > - Number of events logged for the app.
    > - Operating systems and browser version details of the users.
    > - Region and location of the users.
    > 
    > For more details, read [Users, sessions, and events analysis in Application Insights](/azure/azure-monitor/app/usage-segmentation).

1. Select one of the user sessions to drill into specific details. You can see information such as the session length and the screens visited:

    ![Usage details for users.](./media/application-insights/appinsights-users.gif "Usage details for users")

1. Select the **Events** view in left navigation pane under the **Usage** section. You can see a summary of all the screens viewed across all app sessions:

    ![Event details for the app.](./media/application-insights/appInsights-events.gif "Event details for the app")

> [!TIP]
> Some of the additional Application Insights features you can use are:  
> - [Funnels](/azure/azure-monitor/app/usage-funnels)
> - [Cohorts](/azure/azure-monitor/app/usage-cohorts)
> - [Impact analysis](/azure/azure-monitor/app/usage-impact)
> - [Retention analysis](/azure/azure-monitor/app/usage-retention)
> - [Usage flows](/azure/azure-monitor/app/usage-flows)

## Create custom trace events

You can write custom traces directly to Application Insights and start to analyze information specific to your scenario. [Trace](./functions/function-trace.md) function allows you to collect:

- Granular usage information for controls on the screens.
- Which specific users are accessing your app.
- What errors occur.

Tracing can also help diagnose issues because you can send a trail of information as your users browse through your app and perform different actions.

There are three severities for trace messages when sending custom trace information to Application Insights from your app:

- Information
- Warning
- Error

Depending on your scenario, you can choose to send a trace message with the appropriate severity. You can query the data and take specific actions based on the message severity.

> [!NOTE]
> If you are logging any personnel data, you will need to consider any data compliance obligations, such as GDPR, that you might also need to implement.

You'll now update your app and create a new component to collect feedback on each screen of the app. You'll write the events to Application Insights.

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Select **Apps** from the left navigation. From the list of apps, select the **Kudos** app and then select **Edit**.

    > [!NOTE]
    > You can also [create](open-and-run-a-sample-app.md) a new app or [edit](edit-app.md) any existing app instead.

1. Select the **Components** option on the **Tree view**:

    ![Components.](./media/application-insights/new-component.png "Components")

1. Select **New component**, and then resize the width to 200 and height to 75:

    ![Height and width.](./media/application-insights/resize-component.png "Height and width")

1. Select **Insert** from the menu and then select **Icons** to add *Emoji - Frown* and *Emoji - Smile*:

    ![Add icons.](./media/application-insights/add-icons.png "Add icons")

1. Select **New custom property** to create a custom property:

    ![Create custom property.](./media/application-insights/create-custom-property.png "Create custom property")

1. Enter property *Name* and *Display name* such as *FeedbackSceen*.

1. Enter property *Description*.

1. Select **Property type** as **Input** and **Data type** as **Screen**:

    ![Custom property.](./media/application-insights/custom-input-property.png "Custom property")

    > [!NOTE]
    > Input property allows you to capture the screen name and its component so that you can log this information to Application Insights.

1. Select the component on the **Tree View**, select **More actions** (**...**), and then select **Rename** to rename the component with a meaningful name such as *FeedbackComponent*.

    ![Rename component and icons.](./media/application-insights/rename-component-icons.png "Rename component and icons")

1. Select the icons, select **More actions** (**...**), and then select **Rename** to rename the icons with meaningful names, such as *FrownIcon* and *SmileIcon*.

1. Select **FrownIcon**, select the **OnSelect** property, and then enter the following expression in the formula bar:

    ```powerapps-dot
    Trace(
       "App Feedback",
       TraceSeverity.Information,
           {
             UserName: User().FullName,
             UserEmail: User().Email,
             Screen: FeedbackComponent.FeedbackScreen.Name,
             FeedbackValue: "-1"
           }
         );
    Notify("Thanks for you feedback!");
    ```

    ![Frown icon formula.](./media/application-insights/frownicon-formula.png "Frown icon formula")

    > [!NOTE]
    > The formula expression sends *UserName*, *UserEmail*, *Screen*, and the *Feedback* (with the value *-1*) to Application Insights.

1. Select **SmileIcon**, select the **OnSelect** property, and then enter the following expression in the formula bar:
    
    ```powerapps-dot
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
    ```

1. Add the component to one of the screens in your app:

    ![Add feedback component.](./media/application-insights/add-feedback-component.png "Add feedback component")

1. Select **Save** and then select **Publish** to save and publish your app.

1. Play the published app, and send a smile and a frown feedback from your screens.

    > [!IMPORTANT]
    > You must play the published app to send events to Application Insights. Events are not sent to Application Insights when you preview the app in Power Apps Studio.

    ![Play published app.](./media/application-insights/play-published-app.png "Play published app")

## Analyze data in Application Insights

You can now begin to analyze the data you sent using the [Trace](#create-custom-trace-events) function from your app in Application Insights.

1. Sign in to the [Azure portal](https://portal.azure.com/) and open the Application Insights resource you created [earlier](#create-an-application-insights-resource):

    ![Select Application Insights.](./media/application-insights/select-app-insights.png "Select Application Insights")

1. Select **Logs** under **Monitoring** from the left navigation pane:

    ![Select Logs.](./media/application-insights/select-logs.png "Select Logs")

1. Enter the following query and select **Run**. The feedback received from your app is returned:

    ```kusto
    traces
    | where message == "App Feedback"
    | order by timestamp
    ```

    ![View app feedback.](./media/application-insights/view-app-feedback.png "View app feedback")

1. Select a row in the results and expand the *customDimensions* field. 

    The values for **Screen**, **UserName**, **UserEmail**, and **FeedbackValue** for the **OnSelect** event of the smile or frown icon in your component have been recorded. <br>
    There are also some additional values recorded for each event sent to Application Insights, such as the **appId**, **appName**, and **appSessionId**.

    ![Expand custom dimensions.](./media/application-insights/expand-custom-dimensions.png "Expand custom dimensions")

1. With the following example query, you can extend the properties of the JSON custom dimensions and project the columns in the results view.

    ```kusto
    traces
        | extend customdims = parse_json(customDimensions)
        | where message == "App Feedback"
        | project timestamp
            , message
            , AppName = customdims.['ms-appName']
            , AppId = customdims.['ms-appId']
            , FeedbackFrom = customdims.UserEmail
            , Screen = customdims.Screen
            , FeedbackValue = customdims.FeedbackValue
        | order by timestamp desc
    ```

    ![Extend customDimensions query.](./media/application-insights/custom-dimensions-extend-query.png "Extend customDimensions query")

    > [!TIP]
    > *Log queries* are extremely powerful. You can use them to join multiple tables, aggregate large amounts of data, and perform complex operations. For more information, read [Log queries](/azure/azure-monitor/log-query/log-query-overview).

## Monitor unhandled errors (experimental)

[This section contains pre-release documentation and is subject to change.]

> [!IMPORTANT]
> - This is an experimental feature.
> - Experimental features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

Errors occurring during app runtime cannot always be anticipated and planned for. Unhandled Power Fx formula errors are reported to users as banner messages during runtime. These errors can also be reported to Application Insights to help understand frequency and severity without reliance on app users reporting issues. More proactive measures can also be put in place by [setting up real-time alerts](/azure/azure-monitor/app/availability-alerts) when runtime errors occur.

### Enable error passing to Application Insights

You'll need to enable the setting that allows Power Apps to pass the unhandled runtime errors to Azure Application Insights.

> [!WARNING]
> Enabling this setting may incur additional costs related to the storage of Application Insights logs.

To enable error passing, go to **Settings > Upcoming features > Experimental > Pass errors to Azure Application Insights** while keeping your canvas app open for editing.

:::image type="content" source="media/application-insights/pass-error-feature.png" alt-text="Enable Pass errors to Azure Application Insights setting.":::

Upon publishing the app, unhandled runtime errors are now reported to Application Insights.

### Error events in App Insights

Unhandled Power Fx errors experienced by end users at app runtime will be reported to the **traces** table. Unhandled errors can be identified and distinguished from other error events by the event message "Unhandled error". The "severityLevel" dimension of these events will be 3 (TraceSeverity.Error).

Detailed error messages are provided in the "errors" dimension of the *customDimension* property. In situations where  multiple errors occurred during the same operation, these errors will be consolidated in the "errors" dimension of a single trace event. These error messages are the same as reported in [Monitor](/power-apps/maker/monitor-canvasapps) during a live debug session.

This example query identifies unhandled errors and expands all error messages included in the trace event:

```kusto
traces
    | where message == "Unhandled error"
    | extend customdims = parse_json(customDimensions)
    | extend errors = parse_json(tostring(customdims.['errors']))
    | mv-expand errors
    | project timestamp
        , itemId //unique identifier for the trace event
        , AppName = customdims.['ms-appName']
        , AppId = customdims.['ms-appId']
        , errors = errors.['Message']
    | order by timestamp desc
```

:::image type="content" source="media/application-insights/kusto.png" alt-text="Sample output for example query.":::

## Correlation tracing (experimental)

[This section contains pre-release documentation and is subject to change.]

> [!IMPORTANT]
> - This is an experimental feature.
> - Experimental features aren’t meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

Connections to external data and services are fundamental to most apps. Correlation tracing enables the generation and propagation of context information to enable the joining of telemetry across a canvas app and its connections (see limitations below). As an example, your app may call into a custom connector that in turn calls an Azure Function or other REST API. Correlation tracing allows you to correlate actions taken within the app with the underlying API calls across tiers. This can be useful in troubleshooting.

Canvas app correlation tracing is an implementation of context tracing follows [W3C specification](https://www.w3.org/TR/trace-context/).

### Enable Correlation Tracing

> [!WARNING]
> Enabling this setting may incur additional costs related to the storage of Application Insights logs.

To enable the Correlation Tracing feature, go to **Settings > Upcoming features > Experimental > Enable Azure Application Insights correlation tracing** while keeping your canvas app open for editing.

:::image type="content" source="media/application-insights/correlation-tracing.png" alt-text="Enable Azure Application Insights correlation tracing.":::

Upon publishing the app, correlation tracing will now be enabled in Application Insights.

### Limitations

- Correlation tracing is currently enabled for custom connectors. Other connector types are not yet supported.
- HTTP requests are only captured in App Insights if the connected service [is also instrumented with App Insights](/azure/azure-monitor/app/app-insights-overview).

### Using correlation tracing

When enabled, correlation tracing adds a new telemetry event in the **dependencies** table of the canvas app's App Insights instance. This event is recorded at the time a response from a network call (for supported connectors) is received. Dependency events capture details of the network call, including the request and response headers, response status code, and duration of the call.

:::image type="content" source="media/application-insights/correlation-dependencies.png" alt-text="Sample event logged in the dependencies table.":::

If the connected service is also instrumented with App Insights, an additional telemetry event capturing the request is generated in the **requests** table of the service's App Insights instance. Some Azure Services, such as Azure Functions can be instrumented without any coding from the Azure portal. Both the canvas app (or multiple apps) and connected services can be instrumented with the same App Insights instance.

:::image type="content" source="media/application-insights/correlation-requests.png" alt-text="Sample event logged in the requests table.":::

Network calls for supported connectors can be joined with other telemetry on the "operation_Id" dimension. This example query shows a network call being made alongside trace events emitted during an app session.

```kusto
traces | union dependencies | union requests | union pageViews | union customEvents
| project timestamp
    , itemType
    , name
    , operation_Name
    , message
    , severityLevel
    , customDimensions
    , operation_Id
    , operation_ParentId
| where operation_Id == "0a7729e3e83c4e4d93cb4f51149f73b9" //placeholder operation_Id, replace
| order by timestamp asc
```

:::image type="content" source="media/application-insights/correlation-output.png" alt-text="Sample output for example query.":::
  
## Export data to Power BI

You can export your Application Insights data and query results to Power BI for analysis and data presentation.

1. Sign in to the [Azure portal](https://portal.azure.com/) and open the Application Insights resource you created [earlier](#create-an-application-insights-resource):

1. Select **Logs** under **Monitoring** from the left navigation pane:

1. From the log analytics query window, select the **Export** drop-down menu.

1. Select the **Export to Power BI (M query)** option. This will download a Power BI query file to your machine:

    ![Export Power BI query.](./media/application-insights/export-powerbi-query.png "Export Power BI query")

1. Open the downloaded file in a text editor and copy the query to the clipboard.

1. Open Power BI.

1. Select the **Get Data** drop-down menu in the **Home** ribbon and then select  **Blank query**:

    ![Power BI blank query.](./media/application-insights/powerbi-blank-query.png "Power BI blank query")

1. In the query window, select **Advanced Editor**. Paste the query from step 5 into the window, select **Done**, and then select **Close & Apply**:

    ![Power BI advance query.](./media/application-insights/powerbi-advance-query.png "Power BI advance query")

1. You can also create charts and visualizations in Power BI to represent feedback received in your app, as well as make data-based decisions and actions.

    ![Charts and visualizations.](./media/application-insights/powerbi-feedback.png "Charts and visualizations")

## Default Trace event context and dimensions

A set of default dimensions is also added to the *customDimensions* property on each Trace event. These dimensions can be used to identify the application and application sessions the events occurred in. If you log additional custom data using the trace function, they'll also appear in the custom dimensions.

| Dimension Name  | Represents                                            |
|-----------------|-------------------------------------------------------|
| ms-appId | The Application ID of the app that sent the event. |
| ms-appname | The Application name of the app that sent the event. |
| ms-appSessionId | The application session ID. This value may not be populated is some scenarios. When available, this value overrides the standard App Insights sessionID dimension. |
| ms-tenantID | The unique identifier of the tenant where the application is published. |
| ms-environmentId | The name of the environment where the application is published. |
| userId | A unique identifier for the end-user associated with the session. |
| ms-duration | An imputed value measuring the time it takes for a user to navigate from one screen to another. This value overrides the standard App Insights PageView duration dimension. |
| sessionId | A session ID that can be used to correlate all events associated with a single application session. This value will always be present and is recommended for understanding unique session count. This value is taken from the player's session ID and is shown when viewing the session details while playing the app. Session ID might sometimes get a default, random, and unique Application Insights generated value. This default value isn't reliable and doesn't correlate with any app-specific parameters. |
| Duration | An imputed value measuring the time it takes for a user to navigate from one screen to another. This value is the same as the duration reported by the ms-duration dimension. |
| ms-isTest | Indicates if the session is associated with the Test Studio test runner. |
| ms-currentScreenName | The name of the page an end user is navigating from (present for page navigation events). |
| ms-targetScreenName | The name of the page an end user is navigating to (present for page navigation events). |

## Unsupported scenarios

App Insights doesn't support the following scenarios.

- Offline and mobile apps/player events (both Android and iOS) aren't captured.
- Network requests and errors aren't captured.  
- GCC and non-public clouds aren't supported.

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
