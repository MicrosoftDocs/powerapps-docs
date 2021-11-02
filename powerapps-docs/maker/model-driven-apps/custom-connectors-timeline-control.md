---
title: Use custom connectors with the timeline in Power Apps | MicrosoftDocs
description: "Learn how to use custom connectors to bring your own data, such as records, to the timeline in Power Apps."
ms.custom: ""
ms.date: 11/2/2021
ms.reviewer: "matp"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
author: "lalexms"
ms.subservice: mda-maker
ms.author: "laalexan"
manager: "kvivek"
tags: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---


# Use custom connectors with the timeline control

Custom connectors is a feature that provides a way for developers to surface information such as Dataverse table rows, external data sources, and so forth, as records entries within the TimelineWallControl component. It allows for a broader set of scenarios in addition to the existing out-of-box notes, posts, and activities.

For information about configuring and using the timeline, see the following topics:

- [Use timeline](/powerapps/user/add-activities)
- [Configure timeline](set-up-timeline-control.md)
- [Timeline record card configuration](set-up-timeline-control.md#display-a-custom-table-in-a-timeline)

Records that are configured within custom connectors are a JavaScript web resource that conforms to the IRecordSource interface. The name of a web resource, along with the constructor (name including namespace), and optional JSON web resource path, can be added as a UClientRecordSourcesJSON parameter configuration within FormXML.

```json
<UClientRecordSourcesJSON>
  {"recordSources": [{
    "name": "new_SecondaryRecordSource", 
    "constructor": "SampleNamespace.SecondaryRecordSource"}]
  }
</UClientRecordSourcesJSON>
```

TimelineWallControl is expected to load the JavaScript web resource and then create the instance of IRecordSource from the configured constructor.

The IRecordSource is then initialized (init), with a request for pages of records (getRecordsData), and a request for the UX representation of a single record (getRecordUX).

The response from requesting records is persisted to minimize the number of record requests that occur within multi-session scenarios.

## Scope

Custom connectors is supported within single-session and multi-session table forms in Unified Interface client model apps.

### Out of scope
The following functionality isn't available for the custom connectors feature:
- Offline and offline-by-default scenarios
- Dashboards
- Locations where TimelineWallControl isn't available (such as converged apps, canvas apps, portals, custom pages, and so forth)

## Known limitations

The configured web resources aren't formally declared as dependencies to the form. This means that exporting a form won't automatically export the web resources and they'd need to be added to that export manually. In addition, it can be easy to accidentally delete these web resources.

## Develop a record source

When developing a record source, make sure to follow these practices:

- Ensure that you're retrieving data securely. The Unified Interface security model considers JS and JSON web resources as untrusted, and thus, such resources shouldn't contain tokens or secrets in them, as they'd be stored in plain text.
- If the data is within Dataverse, use the context object from init behavior to make requests into Dataverse. Calls into Dataverse from context have requests proxied through a secure iframe. This is how out-of-box record sources within TimelineWallControl retrieve data.
- If the data is outside of Dataverse, use existing mechanisms from the platform to retrieve external data.
- Locally test changes by using Fiddler: Improve the agility of development and debugging of JavaScript web resources by using Fiddler AutoResponder. More information: [Script web resource development using Fiddler AutoResponder](/powerapps/developer/model-driven-apps/streamline-javascript-development-fiddler-autoresponder).
- Reduce the risk of XSS attacks: The risk of XSS attacks occurs when adding/binding HTML to the DOM. Use plain text whenever possible to reduce this risk. If HTML is required, you must sanitize this content before adding it to the record.
- Follow general best practices for client scripting. More information: [Client scripting in model-driven apps](/powerapps/developer/model-driven-apps/clientapi/client-scripting-best-practices)
- Ensure inclusive design practices, including the usage of automated testing tools such as Accessibility Insights.

## Solution sample

You can get started with a [custom connectors solution sample](/powerapps-samples/tree/master/model-driven-apps/custom-connectors/SecondaryRecordSource/solution) that has the "SecondaryRecordSource" web resource, which is configured for "Account for Interactive Experiences" and "Account for Multisession Experiences" forms.

### See also

[Use timeline](/powerapps/user/add-activities)<br>
[Configure timeline](set-up-timeline-control.md)<br>
[Timeline record card configuration](set-up-timeline-control.md#display-a-custom-table-in-a-timeline)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
