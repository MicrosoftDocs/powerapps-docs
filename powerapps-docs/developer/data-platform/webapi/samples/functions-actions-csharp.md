---
title: "Web API Functions and Actions Sample (C#) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample demonstrates how to call bound and unbound functions and actions, including custom actions, using the Microsoft Dataverse Web API and C#"
ms.custom: ""
ms.date: 07/15/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: b14a8bff-bf05-412c-89f6-ba7b503dcb51
caps.latest.revision: 13
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Web API Functions and Actions Sample (C#)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This sample demonstrates how to call bound and unbound functions and actions, including custom actions, using the Microsoft Dataverse Web API.  
  
> [!NOTE]
> This sample implements the operations detailed in the [Web API Functions and Actions Sample](../web-api-functions-actions-sample.md). This sample also uses the [CDSWebApiService](cdswebapiservice.md) class methods for messaging, performance enhancements, and error processing.

## Prerequisites

Prerequisites for all Dataverse Web API C# samples are detailed in the [Prerequisites](../web-api-samples-csharp.md#bkmk_prerequisites) section of the parent topic [Web API Samples (C#)](../web-api-samples-csharp.md).  
  
## How to run this sample

Go to the [PowerApps-Samples](https://github.com/Microsoft/PowerApps-Samples) GitHub repository, clone or download the samples repository, and extract its contents into a local folder. Navigate to the cds/webapi/C#/FunctionsAndActions folder. This folder should contain the following files:  
  
|File|Purpose/Description|  
|----------|--------------------------|  
|Program.cs|Contains the primary source code for this sample.|  
|App.config|The application configuration file, which contains placeholder Dataverse server connection information. This file is shared with several of the Web API samples in the repo. If you configure connection information for one sample, you can run the other samples with the same configuration.|
|FunctionsAndActions.sln <br />FunctionsAndActions.csproj <br />Packages.config <br />AssemblyInfo.cs|The standard Visual Studio 2019 solution, project, NuGet package configuration, and assembly information files for this sample.|  
|WebAPIFunctionsandActions_1_0_0_0_managed.zip|A custom managed solution containing two custom actions called by this sample.|  
  
Next, use the following procedure to run this sample.  

1. Using Dynamics 365 Customer Engagement (**Settings** > **Solutions**) or Power Apps (**Solutions**), import the provided solution (.zip) file into your testing environment.
  
1. Locate and double-click on the solution file, FunctionsAndActions.sln, to load the solution into Visual Studio. Build the **FunctionsAndActions** solution.  This should automatically download and install all the required NuGet packages that are either missing or need to be updated.  
  
1. Edit the application configuration file, App.config, to specify connection information for your Dataverse server.  
  
1. Build and run the **FunctionsAndActions** project from within Visual Studio.  All sample solutions are configured to run in debug mode by default.  
  
## Code listing

 `Program.cs` partial listing
  
```csharp  
sing System;
using System.Collections.Generic;
using System.Configuration;
using System.Net;

namespace PowerApps.Samples
{
    /// <summary>
    /// This program demonstrates use of functions and actions with the 
    /// Power Platform data service Web API.
    /// </summary>
    /// <remarks>Be sure to fill out App.config with your test environment information
    /// and import the provided managed solution into your test environment using the web app
    /// before running this program.</remarks>
    /// <see cref="Https://docs.microsoft.com/powerapps/developer/data-platform/webapi/samples/functions-actions-csharp"/>
    public class Program
    {
        public static void Main()
        {
            Console.Title = "Function and Actions demonstration";

            // Track entity instance URIs so those records can be deleted prior to exit.
            Dictionary<string, Uri> entityUris = new Dictionary<string, Uri>();
            
            try
            {
                // Get environment configuration information from the connection string in App.config.
                ServiceConfig config = new ServiceConfig(
                    ConfigurationManager.ConnectionStrings["Connect"].ConnectionString);

                // Use the service class that handles HTTP messaging, error handling, and
                // performance optimizations.
                using (CDSWebApiService svc = new CDSWebApiService(config))
                {
                    // Create any entity instances required by the program code that follows
                    CreateRequiredRecords(svc, entityUris);

                    #region Call an unbound function with no parameters
                    Console.WriteLine("\n* Call an unbound function with no parameters.");

                    // Retrieve the current user's full name from the WhoAmI function:
                    Console.Write("\tGetting information on the current user..");
                    JToken currentUser = svc.Get("WhoAmI");

                    // Obtain the user's ID and full name
                    JToken user = svc.Get("systemusers(" + currentUser["UserId"] + ")?$select=fullname");

                    Console.WriteLine("completed.");
                    Console.WriteLine("\tCurrent user's full name is '{0}'.", user["fullname"]);
                    #endregion Call an unbound function with no parameters

                    #region Call an unbound function that requires parameters
                    Console.WriteLine("\n* Call an unbound function that requires parameters");

                    // Retrieve the code for the specified time zone
                    int localeID = 1033;
                    string timeZoneName = "Pacific Standard Time";

                    // Define the unbound function and its parameters
                    string[] uria = new string[] {
                        "GetTimeZoneCodeByLocalizedName",
                        "(LocalizedStandardName=@p1,LocaleId=@p2)",
                        "?@p1='" + timeZoneName + "'&@p2=" + localeID };

                    // This would also work:
                    // string[] uria = ["GetTimeZoneCodeByLocalizedName", "(LocalizedStandardName='" + 
                    //    timeZoneName + "',LocaleId=" + localeId + ")"]; 

                    JToken localizedName = svc.Get(string.Join("", uria));
                    string timeZoneCode = localizedName["TimeZoneCode"].ToString();

                    Console.WriteLine(
                        "\tThe time zone '{0}' has the code '{1}'.", timeZoneName, timeZoneCode);
                    #endregion Call an unbound function that requires parameters

                    #region Call a bound function   
                    Console.WriteLine("\n* Call a bound function");

                    // Retrieve the total time (minutes) spent on all tasks associated with 
                    // incident "Sample Case".
                    string boundUri = entityUris["Sample Case"] +
                        @"/Microsoft.Dynamics.CRM.CalculateTotalTimeIncident()";

                    JToken cttir = svc.Get(boundUri);
                    string totalTime = cttir["TotalTime"].ToString();

                    Console.WriteLine("\tThe total duration of tasks associated with the incident " +
                        "is {0} minutes.", totalTime);
                    #endregion Call a bound function 

                    #region Call an unbound action that requires parameters
                    Console.WriteLine("\n* Call an unbound action that requires parameters");

                    // Close the existing opportunity "Opportunity to win" and mark it as won.
                    JObject opportClose = new JObject()
                    {
                        { "subject", "Won Opportunity" },
                        { "opportunityid@odata.bind", entityUris["Opportunity to win"] }
                    };

                    JObject winOpportParams = new JObject()
                    {
                        { "Status", "3" },
                        { "OpportunityClose", opportClose }
                    };

                    JObject won = svc.Post("WinOpportunity", winOpportParams);

                    Console.WriteLine("\tOpportunity won.");
                    #endregion Call an unbound action that requires parameters

                    #region Call a bound action that requires parameters
                    Console.WriteLine("\n* Call a bound action that requires parameters");

                    // Add a new letter tracking activity to the current user's queue.
                    // First create a letter tracking instance.
                    JObject letterAttributes = new JObject()
                    {
                        {"subject", "Example letter" },
                        {"description", "Body of the letter" }
                    };

                    Console.Write("\tCreating letter 'Example letter'..");

                    Uri letterUri = svc.PostCreate("letters", letterAttributes);
                    entityUris.Add("Example letter", letterUri);

                    Console.WriteLine("completed.");

                    //Retrieve the ID associated with this new letter tracking activity.
                    JToken letter = svc.Get(letterUri + "?$select=activityid,subject");
                    string letterActivityId = (string)letter["activityid"];

                    // Retrieve the URL to current user's queue.
                    string myUserId = (string)currentUser["UserId"];

                    JToken queueRef = svc.Get("systemusers(" + myUserId + ")/queueid/$ref");
                    string myQueueUri = (string)queueRef["@odata.id"];

                    //Add the letter activity to current user's queue, then return its queue ID.
                    JObject targetUri = JObject.Parse(
                      @"{activityid: '" + letterActivityId + @"', '@odata.type': 'Microsoft.Dynamics.CRM.letter' }");

                    JObject addToQueueParams = new JObject()
                    {
                        { "Target", targetUri }
                    };

                    string queueItemId = (string)svc.Post(
                        myQueueUri + "/Microsoft.Dynamics.CRM.AddToQueue", addToQueueParams)["QueueItemId"];

                    Console.WriteLine("\tLetter 'Example letter' added to current user's queue.");
                    Console.WriteLine("\tQueueItemId returned from AddToQueue action: {0}", queueItemId);
                    #endregion Call a bound action that requires parameters

                    #region Call a bound custom action that requires parameters
                    Console.WriteLine("\n* Call a bound custom action that requires parameters");

                    // Add a note to a specified contact. Uses the custom action sample_AddNoteToContact, which
                    // is bound to the contact to annotate, and takes a single param, the note to add. It also  
                    // returns the URI to the new annotation. 

                    JObject note = JObject.Parse(
                        @"{NoteTitle: 'Sample note', NoteText: 'The text content of the note.'}");
                    string actionUri = entityUris["Jon Fogg"].ToString() + "/Microsoft.Dynamics.CRM.sample_AddNoteToContact";

                    JObject contact = svc.Post(actionUri, note);
                    Uri annotationUri = new Uri(svc.BaseAddress + "annotations(" + contact["annotationid"] + ")");
                    entityUris.Add((string)note["NoteTitle"], annotationUri);

                    Console.WriteLine("\tA note with the title '{0}' was created and " +
                        "associated with the contact 'Jon Fogg'.", note["NoteTitle"]);
                    #endregion Call a bound custom action that requires parameters

                    #region Call an unbound custom action that requires parameters
                    Console.WriteLine("\n* Call an unbound custom action that requires parameters");

                    // Create a customer of the specified type, using the custom action sample_CreateCustomer,
                    // which takes two parameters: the type of customer ('account' or 'contact') and the name of 
                    // the new customer.
                    string customerName = "New account customer (sample)";
                    JObject customerAttributes = JObject.Parse(
                        @"{CustomerType: 'account', AccountName: '" + customerName + "'}");

                    JObject response = svc.Post("sample_CreateCustomer", customerAttributes);
                    Console.WriteLine("\tThe account '" + customerName + "' was created.");

                    // Because the CreateCustomer custom action does not return any data about the created instance, 
                    // we must query the customer instance to figure out its URI.
                    JToken customer = svc.Get("accounts?$filter=name eq 'New account customer (sample)'&$select=accountid&$top=1");
                    Uri customerUri = new Uri(svc.BaseAddress + "accounts(" + customer["value"][0]["accountid"] + ")");
                    entityUris.Add( customerName, customerUri );

                    // Try to call the same custom action with invalid parameters, here the same name is
                    // not valid for a contact. (ContactFirstname and ContactLastName parameters are  
                    // required when CustomerType is contact.
                    customerAttributes = JObject.Parse(
                        @"{CustomerType: 'contact', AccountName: '" + customerName + "'}");

                    try
                    {
                        customerUri = svc.PostCreate("sample_CreateCustomer", customerAttributes);
                        Console.WriteLine("\tCall to the custom CreateCustomer action succeeded, which was not expected.");
                    }
                    catch (AggregateException e)
                    {
                        Console.WriteLine("\tCall to the custom CreateCustomer action did not succeed (as was expected).");
                        foreach (Exception inner in (e as AggregateException).InnerExceptions)
                        { Console.WriteLine("\t  -" + inner.Message); }
                    }
                    #endregion Call an unbound custom action that requires parameters

                    DeleteEntityRecords(svc, entityUris);
                }
            }
            catch (Exception e)
            {
                Console.BackgroundColor = ConsoleColor.Red; // Highlight exceptions
                if ( e is AggregateException )
                {
                    foreach (Exception inner in (e as AggregateException).InnerExceptions)
                    { Console.WriteLine("\n" + inner.Message); }
                }
                else if ( e is ServiceException)
                {
                    var ex = e as ServiceException;
                    Console.WriteLine("\nMessage send response: status code {0}, {1}",
                        ex.StatusCode, ex.ReasonPhrase);
                }
                Console.ReadKey(); // Pause terminal
            }
        }
    }
}
```

### See also

[Use the Dataverse Web API](../overview.md)<br />
[Use Web API functions](../use-web-api-functions.md)<br />
[Use Web API actions](../use-web-api-actions.md)<br />
[Web API Samples](../web-api-samples.md)<br />
[Web API Functions and Actions Sample](../web-api-functions-actions-sample.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
