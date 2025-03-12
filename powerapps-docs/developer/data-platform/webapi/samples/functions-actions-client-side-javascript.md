---
title: "Web API Functions and Actions Sample (Client-side JavaScript) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample demonstrates how to perform bound and unbound functions and actions, including custom actions, using the Microsoft Dataverse Web API and client-side JavaScript."
ms.date: 03/30/2025
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
  - Mattp123
---

# Web API Functions and Actions Sample (Client-side JavaScript)

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This sample demonstrates how to perform bound and unbound functions and actions, including custom actions, using the Microsoft Dataverse Web API using client-side JavaScript.

> [!NOTE]
> This sample implements the operations detailed in the [Web API Functions and Actions Sample](../web-api-functions-actions-sample.md) and uses the common client-side JavaScript constructs described in [Web API Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md)


[!INCLUDE [cc-web-api-spa-javascript-code-sample-note](../../includes/cc-web-api-spa-javascript-code-sample-note.md)]

## Prerequisites

This sample has the same prerequisites as [Quick Start Web API with client-side JavaScript and Visual Studio Code](../quick-start-js-spa.md#prerequisites). To run this sample, you should complete the quick start first. You can use the same application registration information for that sample to run this sample.

TODO: Create an include of steps to register the sample.
Include it here? Or in [Web API Data operations Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md)

## FunctionsAndActions.js

```javascript
import { Util } from "../scripts/Util.js";
import { DataverseWebAPI as dv } from "../scripts/DataverseWebAPI.js";
export class FunctionsAndActions {
  /**
   * @type {dv.Client}
   * @private
   */
  #client; // The DataverseWebAPIClient.Client instance
  #container; // The container element to display messages
  #entityStore = []; // Store for created records to delete at the end of the sample
  #util; // Util instance for utility functions
  #whoIAm; // The current user's information
  #isSystemAdminFunctionSolutionId = null; // ID of the SystemAdminFunction solution
  #name = "Functions and actions"; // Name of the sample

  // Constructor to initialize the client, container, and utility helper functions
  constructor(client, container) {
    this.#client = client;
    this.#container = container;
    this.#util = new Util(container);
  }

  // Public functions to set up, run, and clean up data created by the sample
  async SetUp() {
    // Clear the container
    this.#container.replaceChildren();
    this.#util.appendMessage(this.#name + " sample started");
    // Get the current user's information
    try {
      this.#whoIAm = await this.#client.WhoAmI();

      const contosoConsulting = {
        accountcategorycode: 1,
        address1_addresstypecode: 3,
        address1_city: "Redmond",
        address1_country: "USA",
        address1_line1: "123 Maple St.",
        address1_name: "Corporate Headquarters",
        address1_postalcode: "98000",
        address1_shippingmethodcode: 4,
        address1_stateorprovince: "WA",
        address1_telephone1: "555-1234",
        customertypecode: 3,
        description: "Contoso is a business consulting company.",
        emailaddress1: "info@contoso.com",
        industrycode: 7,
        name: "Contoso Consulting",
        numberofemployees: 150,
        ownershipcode: 2,
        preferredcontactmethodcode: 2,
        telephone1: "(425) 555-1234",
      };

      const contosoConsultingId = await this.#client.Create(
        "accounts",
        contosoConsulting
      );
      this.#entityStore.push({
        entitySetName: "accounts",
        id: contosoConsultingId,
        entityName: "account",
        name: contosoConsulting.name,
      });
    } catch (error) {
      this.#util.showError(error.message);
    }

    this.#isSystemAdminFunctionSolutionId =
      await this.#getIsSystemAdminFunctionSolutionId();
    if (!this.#isSystemAdminFunctionSolutionId) {
      this.#util.appendMessage(
        "IsSystemAdmin Function solution is not installed. Installing it now... "
      );
      // Install the IsSystemAdmin Function solution
      await this.#installIsSystemAdminFunctionSolution();

      // Try to retrieve the ID after installing the solution
      this.#isSystemAdminFunctionSolutionId =
        await this.#getIsSystemAdminFunctionSolutionId();
      if (this.#isSystemAdminFunctionSolutionId) {
        this.#entityStore.push({
          entitySetName: "solutions",
          id: this.#isSystemAdminFunctionSolutionId,
          entityName: "solution",
          name: "IsSystemAdmin Function",
        });
        this.#util.appendMessage(
          "Installed IsSystemAdminFunction solution and added it to the entity store:"
        );
      } else {
        this.#util.showError(
          "Failed to install retrieve the ID of the  IsSystemAdminFunction solution."
        );
      }
    } else {
      this.#util.appendMessage(
        "IsSystemAdmin Function solution is already installed."
      );
    }

    // Create account to share
    const accountToShare = {
      name: "Account to Share",
    };

    try {
      const accountToShareId = await this.#client.Create(
        "accounts",
        accountToShare
      );
      this.#entityStore.push({
        entitySetName: "accounts",
        id: accountToShareId,
        entityName: "account",
        name: accountToShare.name,
      });
    } catch (error) {
      this.#util.showError(
        "Couldn't create the account record for sharing:" + error.message
      );
    }
  }
  // Run the sample
  async Run() {
    try {
      this.#util.appendMessage("<h2>1: Unbound Function WhoAmI</h2>");
      await this.#whoAmIExample();
      this.#util.appendMessage("<h2>2: Unbound Function FormatAddress</h2>");
      await this.#formatAddressExample();
      this.#util.appendMessage("<h2>3: Unbound Function InitializeFrom</h2>");
      await this.#initializeFromExample();
      this.#util.appendMessage(
        "<h2>4: Unbound Function RetrieveCurrentOrganization</h2>"
      );
      await this.#retrieveCurrentOrganizationExample();
      this.#util.appendMessage(
        "<h2>5: Unbound Function RetrieveTotalRecordCount</h2>"
      );
      await this.#retrieveTotalRecordCountExample();
      this.#util.appendMessage(
        "<h2>6: Bound Function IsSystemAdmin custom API</h2>"
      );
      await this.#isSystemAdminExample();
      this.#util.appendMessage("<h2>7: Unbound Action GrantAccess</h2>");
      await this.#grantAccessExample();
      this.#util.appendMessage("<h2>8: Bound Action AddPrivilegesRole</h2>");
      await this.#addPrivilegesRoleExample();
    } catch (error) {
      this.#util.showError(error.message);
      // Try to clean up even if an error occurs
      await this.CleanUp();
    }
  }
  // Clean up the created records
  async CleanUp() {
    if (this.#entityStore.length === 0) {
      this.#util.appendMessage("No records to delete");
      return;
    }

    this.#util.appendMessage("<h2>9: Delete sample records</h2>");
    this.#util.appendMessage("Deleting the records created by this sample:");

    let deleteMessageList = document.createElement("ul");
    this.#container.append(deleteMessageList);

    for (const item of this.#entityStore) {
      try {
        await this.#client.Delete(item.entitySetName, item.id);
        const message = document.createElement("li");
        message.textContent = `Deleted ${item.entityName} ${item.name}`;
        deleteMessageList.append(message);
      } catch (e) {
        const message = document.createElement("li");
        message.textContent = `Failed to delete ${item.entityName} ${item.name}`;
        message.className = "error";
        deleteMessageList.append(message);
      }
    }

    // Set the entity store to an empty array
    this.#entityStore = [];
    this.#util.appendMessage(this.#name + " sample completed.");
    this.#util.appendMessage("<a href='#'>Go to top</a>");
  }

  //#region Section 0: Install Solution in Setup

  async #getIsSystemAdminFunctionSolutionId() {
    try {
      const records = await this.#client.RetrieveMultiple(
        "solutions",
        "$select=solutionid&$filter=uniquename eq 'IsSystemAdminFunction'"
      );

      if (records.value.length === 0) {
        return null;
      }
      return records.value[0].solutionid;
    } catch (error) {
      this.#util.showError(
        `Failed to retrieve IsSystemAdminFunction solution ID: ${error.message}`
      );
    }
  }

  async #installIsSystemAdminFunctionSolution() {
    const url = new URL(
      "/solution/IsSystemAdminFunction_1_0_0_0_managed.zip",
      window.location.href
    );

    const response = await fetch(url);
    const arrayBuffer = await response.arrayBuffer();
    const byteArray = new Uint8Array(arrayBuffer);
    // Convert byte array to base64 encoded string
    const base64String = btoa(String.fromCharCode(...byteArray));

    const request = new dv.WebAPIRequest("POST", "ImportSolution", null, {
      OverwriteUnmanagedCustomizations: false,
      PublishWorkflows: false,
      CustomizationFile: base64String,
      ImportJobId: "00000000-0000-0000-0000-000000000000",
    });

    try {
      await this.#client.SendRequest(request);
    } catch (error) {
      this.#util.showError(
        `Failed to install the IsSystemAdminFunction solution: ${error.message}`
      );
    }
  }

  //#endregion Section 0: Install Solution in Setup

  //#region Section 1: Unbound Function WhoAmI
  // Demonstrates calling the WhoAmI function
  async #whoAmIExample() {
    try {
      // Invoke the WhoAmI function
      let whoAmIRequest = new dv.WebAPIRequest("GET", "WhoAmI");

      const whoAmIResponse = await this.#client.SendRequest(whoAmIRequest);
      let message = [
        "<a target='_blank' href='https://learn.",
        "microsoft.com/power-apps/developer/data-platform/webapi/reference/",
        "whoami'>WhoAmI function</a> returns the current user's information ",
        "with the properties of the <a target='_blank' href='https://learn.",
        "microsoft.com/power-apps/developer/data-platform/webapi/reference/",
        "whoamiresponse'>WhoAmIResponse complex type</a>:",
      ];

      this.#util.appendMessage(message.join(""));
      const table = this.#util.createTable(whoAmIResponse.body);
      this.#container.appendChild(table);
    } catch (e) {
      this.#util.showError(`Failed to call WhoAmI: ${e.message}`);
      throw e;
    }
  }
  //#endregion Section 1: Unbound Function WhoAmI

  //#region Section 2: Unbound Function FormatAddress

  async #formatAddressExample() {
    // Function to generate aliases and parameter assignment
    // for a function where all the parameter types are strings.
    function generateStringAliasesAndAssignments(object) {
      const keys = Object.keys(object);
      const values = Object.values(object);

      // Generate aliases
      const aliases = keys
        .map((key, index) => `${key}=@p${index + 1}`)
        .join(",");

      // Generate assigned values
      const assignedValues = keys
        .map((key, index) => `@p${index + 1}='${values[index]}'`)
        .join("&");

      return { aliases, assignedValues };
    }

    // Define the address object
    const address1 = {
      Line1: "123 Maple St.",
      City: "Seattle",
      StateOrProvince: "WA",
      PostalCode: "98007",
      Country: "USA",
    };

    // Call the FormatAddress function
    try {
      const { aliases, assignedValues } =
        generateStringAliasesAndAssignments(address1);
      const formatAddressRequest = new dv.WebAPIRequest(
        "GET",
        `FormatAddress(${aliases})`,
        assignedValues
      );
      const response = await this.#client.SendRequest(formatAddressRequest);

      let message = [
        "<a target='_blank' href='https://learn.",
        "microsoft.com/power-apps/developer/data-platform/webapi/reference/",
        "formataddress'>FormatAddress function</a> returns a formatted address ",
        "with the properties of the <a target='_blank' href='https://learn.",
        "microsoft.com/power-apps/developer/data-platform/webapi/reference/",
        "formataddressresponse'>FormatAddressResponse complex type</a>:",
      ];

      this.#util.appendMessage(message.join(""));

      this.#util.appendMessage(
        `<strong>Formatted US Address:</strong><div style="white-space: pre-line;">${response.body.Address}</div>`
      );
    } catch (error) {
      this.#util.showError(`Failed to format address1: ${error.message}`);
    }

    // Define a new  address object
    const address2 = {
      Line1: "1-2-3 Sakura",
      City: "Nagoya",
      StateOrProvince: "Aichi",
      PostalCode: "455-2345",
      Country: "JAPAN",
    };

    try {
      const { aliases, assignedValues } =
        generateStringAliasesAndAssignments(address2);
      const formatAddressRequest = new dv.WebAPIRequest(
        "GET",
        `FormatAddress(${aliases})`,
        assignedValues
      );
      const response = await this.#client.SendRequest(formatAddressRequest);

      this.#util.appendMessage(
        `<strong>Formatted Japan Address:</strong><div style="white-space: pre-line;">${response.body.Address}</div>`
      );
    } catch (error) {
      this.#util.showError(`Failed to format address2: ${error.message}`);
    }
  }

  //#endregion Section 2: Unbound Function FormatAddress

  //#region Section 3: Unbound Function InitializeFrom

  async #initializeFromExample() {
    // Get the account ID for Contoso Consulting created in SetUp
    const contosoAccountId = this.#entityStore.find(
      (item) => item.name === "Contoso Consulting"
    ).id;

    const aliases = [
      "EntityMoniker=@p1",
      "TargetEntityName=@p2",
      "TargetFieldType=@p3",
    ].join(",");

    const assignedValues = [
      `@p1={'@odata.id':'accounts(${contosoAccountId})'}`,
      "@p2='account'",
      "@p3=Microsoft.Dynamics.CRM.TargetFieldType'ValidForCreate'",
    ].join("&");

    const intializeFromRequest = new dv.WebAPIRequest(
      "GET",
      `InitializeFrom(${aliases})`,
      assignedValues
    );

    // Will set the data for the new record.
    let newaccount = null;
    try {
      const response = await this.#client.SendRequest(intializeFromRequest);

      let message = [
        "The <a target='_blank' href='https://learn.",
        "microsoft.com/power-apps/developer/data-platform/webapi/reference/",
        "initializefrom'>InitializeFrom function</a> returns a <a target='_blank' href='https://learn.microsoft.com/power-apps/developer/data-platform/webapi/reference/crmbaseentity'>crmbaseentity</a>",
        " object with the following properties that ",
        "provide default values copied from the source record:",
      ];

      this.#util.appendMessage(message.join(""));

      newaccount = response.body;
      const table = this.#util.createTable(newaccount, false);
      this.#container.appendChild(table);
    } catch (error) {
      this.#util.showError(`Failed to initialize from: ${error.message}`);
    }

    if (newaccount) {
      // Create a new account using the initialized values
      newaccount.name = "Contoso Consulting Chicago Branch";
      newaccount.address1_city = "Chicago";
      newaccount.address1_line1 = "456 Elm St.";
      newaccount.address1_name = "Chicago Branch Office";
      newaccount.address1_postalcode = "60007";
      newaccount.address1_stateorprovince = "IL";
      newaccount.address1_telephone1 = "(312) 555-3456";
      newaccount.numberofemployees = 12;

      // Remove the ownerid@odata.bind property from the new account object
      // if it exists. This will only occur if this column is mapped.
      // This column should not be mapped.
      // The calling user will be set as the owner of the new record.
      if (newaccount["ownerid@odata.bind"]) {
        delete newaccount["ownerid@odata.bind"];
      }

      // Converts object properties to an array of strings
      // that can be used with $select.
      function getSelectablePropertyNames(obj) {
        const result = {};
        for (const key in obj) {
          if (obj.hasOwnProperty(key)) {
            if (!key.startsWith("@")) {
              if (key.endsWith("@odata.bind")) {
                const newKey = "_" + key.replace(/@odata\.bind$/, "_value");
                result[newKey] = obj[key];
              } else {
                result[key] = obj[key];
              }
            }
          }
        }
        return Object.keys(result);
      }

      // Transform the object to remove @odata.bind properties
      const columns = getSelectablePropertyNames(newaccount);

      try {
        const contosoChicago = await this.#client.CreateRetrieve(
          "accounts",
          newaccount,
          `$select=${columns.join(",")}`
        );
        this.#entityStore.push({
          entitySetName: "accounts",
          id: contosoChicago.accountid,
          entityName: "account",
          name: newaccount.name,
        });

        this.#util.appendMessage(
          `New ${contosoChicago.name} account record created.`
        );
        const table = this.#util.createTable(contosoChicago, true);
        this.#container.appendChild(table);
      } catch (error) {
        this.#util.showError(
          `Failed to create new record using payload from initializeFrom message: ${error.message}`
        );
      }
    }
  }

  //#endregion Section 3: Unbound Function InitializeFrom

  //#region Section 4: Unbound Function RetrieveCurrentOrganization

  async #retrieveCurrentOrganizationExample() {
    try {
      const retrieveCurrentOrganizationRequest = new dv.WebAPIRequest(
        "GET",
        "RetrieveCurrentOrganization(AccessType=@p1)",
        "@p1=Microsoft.Dynamics.CRM.EndpointAccessType'Default'"
      );

      const response = await this.#client.SendRequest(
        retrieveCurrentOrganizationRequest
      );

      let message = [
        "<a target='_blank' ",
        "href='https://learn.microsoft.com/power-apps/developer/data-platform/webapi/reference/retrievecurrentorganization'>",
        "RetrieveCurrentOrganization function</a> returns the current organization information with the properties of the ",
        "<a target='_blank' href='https://learn.microsoft.com/power-apps/developer/data-platform/webapi/reference/retrievecurrentorganizationresponse'>",
        "RetrieveCurrentOrganizationResponse complex type</a>. The <strong>Details</strong> property contains the following information:",
      ];

      this.#util.appendMessage(message.join(""));
      const table = this.#util.createTable(response.body.Detail);
      this.#container.appendChild(table);
    } catch (error) {
      this.#util.showError(
        `Failed to retrieve current organization: ${error.message}`
      );
    }
  }
  //#endregion Section 4: Unbound Function RetrieveCurrentOrganization

  //#region Section 5: Unbound Function RetrieveTotalRecordCount

  async #retrieveTotalRecordCountExample() {
    let message = [
      "<a target='_blank' ",
      "href='https://learn.microsoft.com/power-apps/developer/data-platform/webapi/reference/retrievetotalrecordcount'>",
      "RetrieveTotalRecordCount function</a> returns the current organization information with the properties of the ",
      "<a target='_blank' href='https://learn.microsoft.com/power-apps/developer/data-platform/webapi/reference/retrievetotalrecordcountresponse'>",
      "RetrieveTotalRecordCountResponse  complex type</a>. The <strong>EntityRecordCountCollection</strong> property contains the following information:",
    ];
    this.#util.appendMessage(message.join(""));

    const RetrieveTotalRecordCountRequest = new dv.WebAPIRequest(
      "GET",
      "RetrieveTotalRecordCount(EntityNames=@p1)",
      "@p1=['account','contact']"
    );

    try {
      const response = await this.#client.SendRequest(
        RetrieveTotalRecordCountRequest
      );

      this.#util.appendMessage(
        "The number of records for each table according to RetrieveTotalRecordCount:"
      );

      const keys = response.body.EntityRecordCountCollection.Keys;
      const values = response.body.EntityRecordCountCollection.Values;

      const data = {};
      for (let i = 0; i < keys.length; i++) {
        data[keys[i]] = values[i];
      }

      const table = this.#util.createTable(data, false);
      this.#container.appendChild(table);
    } catch (error) {
      this.#util.showError(
        `Failed to retrieve total record count: ${error.message}`
      );
    }
  }

  //#endregion Section 5: Unbound Function RetrieveTotalRecordCount

  //#region Section 6: Bound Function IsSystemAdmin custom API

  async #isSystemAdminExample() {
    let startMessage = [
      "The <strong>sample_IsSystemAdmin</strong> function is a ",
      "custom API that checks if the user has the system administrator role. ",
      "It is bound to the system user table and returns a boolean value ",
      "indicating whether the user is a system administrator.",
      "<br />",
      "This function is contained within a solution called ",
      "<strong>IsSystemAdminFunction</strong> that is installed if it isn't found ",
      "when the samples starts, and is deleted at the end of the sample if it was installed.",
      "The sample calls the <strong>sample_IsSystemAdmin</strong> function for the ",
      "first 10 enabled interactive users in the system who do not have a # ",
      "character in their name and are enabled.",
      "<a target='_blank' href='https://learn.microsoft.com/power-apps/developer/",
      "data-platform/org-service/samples/issystemadmin-customapi-sample-plugin'> ",
      "Learn more about how this custom API was created</a>.",
    ];

    this.#util.appendMessage(startMessage.join(""));

    // Check if the IsSystemAdminFunction solution is installed
    if (!this.#isSystemAdminFunctionSolutionId) {
      this.#util.showError("IsSystemAdminFunction solution is not installed.");
      return;
    }

    // Get top 10 user records that don't start with # character
    const records = await this.#client.RetrieveMultiple(
      "systemusers",
      [
        "$select=systemuserid,fullname",
        "$filter=not contains(fullname,'%23') and accessmode eq 0",
        "$top=10",
      ].join("&")
    );

    // Check if each user is a system admin
    const checkPromises = records.value.map((record) =>
      this.#checkIsSystemAdmin(record)
    );
    const results = await Promise.all(checkPromises);

    let message = [];

    results.forEach(({ record, isSystemAdmin }) => {
      let item = [
        "<li>",
        record.fullname,
        isSystemAdmin ? " <strong>HAS</strong> " : " does not have ",
        "the system administrator role.",
        "</li>",
      ];
      message.push(item.join(""));
    });

    this.#util.appendMessage(message.join(""), null, "ul");
  }

  async #checkIsSystemAdmin(record) {
    if (!record || !record.systemuserid) {
      this.#util.showError("Invalid record or systemuserid.");
      return { record, isSystemAdmin: false };
    }

    const request = new dv.WebAPIRequest(
      "GET",
      `systemusers(${record.systemuserid})/Microsoft.Dynamics.CRM.sample_IsSystemAdmin`
    );

    try {
      const response = await this.#client.SendRequest(request);
      return { record, isSystemAdmin: response.body.HasRole };
    } catch (error) {
      this.#util.showError(
        `Failed to check IsSystemAdmin for user ${record.systemuserid}: ${error.message}`
      );
      return { record, isSystemAdmin: false };
    }
  }
  //#endregion Section 6: Bound Function IsSystemAdmin custom API

  //#region Section 7: Unbound Action GrantAccess

  async #grantAccessExample() {
    const startMessage = [
      "Use the <a target='_blank' ",
      "href='https://learn.microsoft.com/power-apps/developer/data-platform/webapi/reference/grantaccess'>GrantAccess action</a> ",
      "to grant access rights to a record for a principal, which means a user or team. ",
      "This unbound action requires a reference to the record using the <strong>Target</strong> parameter. ",
      "The <strong>PrincipalAccess</strong> parameter contains data about the principal and the access rights to be granted ",
      "using a ",
      "<a target='_blank' ",
      "href='https://learn.microsoft.com/power-apps/developer/data-platform/webapi/reference/principalaccess'>PrincipalAccess complex type</a> ",
      "instance.",
    ].join("");

    this.#util.appendMessage(startMessage);

    // Get the ID for "Account to Share" account record created in SetUp
    const accountToShareId = this.#entityStore.find(
      (item) => item.name === "Account to Share"
    ).id;

    // Get an enabled, interactive user other than current user
    let otherUser = null;
    try {
      const records = await this.#client.RetrieveMultiple(
        "systemusers",
        [
          "$select=systemuserid,fullname",
          [
            "$filter=systemuserid ne ",
            this.#whoIAm.UserId,
            " and isdisabled eq false",
            " and accessmode eq 0",
            " and not startswith(fullname,'%23')",
          ].join(""),
          "$top=1",
        ].join("&")
      );

      if (records.value.length > 0) {
        otherUser = records.value[0];
      } else {
        this.#util.showError(
          "No other enabled interactive users found in the system. Can't demonstrate the GrantAccess action."
        );
        return;
      }
    } catch (error) {
      this.#util.showError(`Failed to retrieve other user: ${error.message}`);
    }

    if (otherUser && accountToShareId) {
      const accessRights = await this.#retrievePrincipalAccessRequest(
        otherUser.systemuserid,
        accountToShareId
      );

      // Display the access rights
      this.#util.appendMessage(
        [
          otherUser.fullname,
          " has the following access rights to the account record: ",
          accessRights,
        ].join("")
      );

      // Show if the user has DeleteAccess rights
      this.#util.appendMessage(
        [
          otherUser.fullname,
          accessRights.includes("DeleteAccess") ? " has " : " does not have ",
          "DeleteAccess rights to the account record.",
        ].join("")
      );

      // Give them DeleteAccess rights if they don't have it
      if (!accessRights.includes("DeleteAccess")) {
        // Prepare the body for the GrantAccess request
        const grantAccessBody = {
          Target: {
            accountid: accountToShareId,
            "@odata.type": "Microsoft.Dynamics.CRM.account",
          },
          PrincipalAccess: {
            Principal: {
              systemuserid: otherUser.systemuserid,
              "@odata.type": "Microsoft.Dynamics.CRM.systemuser",
            },
            AccessMask: "DeleteAccess",
          },
        };
        // Compose the request
        const grantAccessRequest = new dv.WebAPIRequest(
          "POST",
          "GrantAccess",
          null,
          grantAccessBody
        );

        try {
          // Send the GrantAccess request
          await this.#client.SendRequest(grantAccessRequest);
          this.#util.appendMessage(
            `Granted DeleteAccess rights to ${otherUser.fullname} for the account record.`
          );
        } catch (error) {
          this.#util.showError(`Failed to grant access: ${error.message}`);
        }

        // Retrieve the updated access rights
        const updatedAccessRights = await this.#retrievePrincipalAccessRequest(
          otherUser.systemuserid,
          accountToShareId
        );

        if (updatedAccessRights.includes("DeleteAccess")) {
          this.#util.appendMessage(
            `${otherUser.fullname} DeleteAccess rights to the account record is confirmed.`
          );
        } else {
          this.#util.appendMessage(
            `${otherUser.fullname} still does not have DeleteAccess rights to the account record.`
          );
        }
      } else {
        this.#util.appendMessage(
          `${otherUser.fullname} already has DeleteAccess rights to the account record.`
        );
      }
    }
  }

  /**
   * Retrieves the principal access rights for a given system user and account.
   *
   * @param {string} systemUserId - The ID of the system user.
   * @param {string} accountid - The ID of the account.
   * @returns {Promise<string>} A promise that resolves to the access rights of the principal.
   * @throws Will throw an error if the request fails.
   * @private
   */
  async #retrievePrincipalAccessRequest(systemUserId, accountid) {
    const request = new dv.WebAPIRequest(
      "GET",
      `systemusers(${systemUserId})/Microsoft.Dynamics.CRM.RetrievePrincipalAccess(Target=@p1)`,
      `@p1={ '@odata.id':'accounts(${accountid})'}`
    );

    try {
      const response = await this.#client.SendRequest(request);
      return response.body.AccessRights;
    } catch (error) {
      this.#util.showError(
        `Failed to retrieve principal access for user ${systemUserId} and account ${accountid}: ${error.message}`
      );
    }
  }

  //#endregion Section 7: Unbound Action GrantAccess

  //#region Section 8: Bound Action AddPrivilegesRole

  async #addPrivilegesRoleExample() {
    const startMessage = [
      "Use the <a target='_blank' href='https://learn.microsoft.",
      "com/power-apps/developer/data-platform/webapi/reference/",
      "addprivilegesrole'>AddPrivilegesRole action</a> to add privileges to a security role. ",
      "This action is bound to the <a target='_blank' href='htt",
      "ps://learn.microsoft.com/power-apps/developer/data-platfo",
      "rm/webapi/reference/role'>role entity type</a>. ",
      "The <strong>Target</strong> parameter contains a reference to the record.",
      "The <strong>Privileges</strong> parameter contains data ",
      "about the privileges to be added.",
      "Use a collection of <a target='_blank' href='https://lea",
      "rn.microsoft.com/power-apps/developer/data-platform/webap",
      "i/reference/roleprivilege'>RolePrivilege complex type</a> ",
      "instances. to set the privileges.",
      "RolePrivilege are added to the role in the context of a business unit, in this case the user's business unit. ",
      "Each RolePrivilege must have a <strong>Depth</strong> assigned using <a targ",
      "et='_blank' href='https://learn.microsoft.com/power-apps/",
      "developer/data-platform/webapi/reference/privilegedepth'>",
      "PrivilegeDepth enum type</a> values.",
      "The Depth value is set to <strong>Basic</strong> in this ",
      "sample.",
    ].join("");
    this.#util.appendMessage(startMessage);

    // Create a security role to add privileges to
    const role = {
      "businessunitid@odata.bind": `businessunits(${
        this.#whoIAm.BusinessUnitId
      })`,
      name: "Test Role",
    };

    let roleId = null;
    try {
      roleId = await this.#client.Create("roles", role);
      // To delete later
      this.#entityStore.push({
        entitySetName: "roles",
        id: roleId,
        entityName: "role",
        name: role.name,
      });

      this.#util.appendMessage(`Created a security role named ${role.name}.`);
    } catch (error) {
      this.#util.showError(`Failed to create security role: ${error.message}`);
    }

    if (roleId) {
      try {
        // Show the current privileges for the role
        await this.#showRolePrivileges(roleId, role.name);
      } catch (error) {
        this.#util.showError(error.message);
      }

      // Retrieve the prvCreateAccount and prvReadAccount privileges

      try {
        const privileges = await this.#client.RetrieveMultiple(
          "privileges",
          [
            "$select=name",
            "$filter=name eq 'prvCreateAccount' or name eq 'prvReadAccount'",
          ].join("&")
        );

        let rolePrivileges = [];

        privileges.value.forEach((privilege) => {
          rolePrivileges.push({
            BusinessUnitId: this.#whoIAm.BusinessUnitId,
            Depth: "Basic",
            PrivilegeId: privilege.privilegeid,
            PrivilegeName: privilege.name,
          });
        });

        // Create the request

        const addPrivilegesRoleRequest = new dv.WebAPIRequest(
          "POST",
          `roles(${roleId})/Microsoft.Dynamics.CRM.AddPrivilegesRole`,
          null,
          { Privileges: rolePrivileges }
        );

        // Send the request to add the privileges
        try {
          await this.#client.SendRequest(addPrivilegesRoleRequest);

          this.#util.appendMessage(
            `Added the 'prvCreateAccount' and 'prvReadAccount' privileges to the ${role.name} security role:`
          );

          try {
            // Show the updated privileges for the role
            await this.#showRolePrivileges(roleId, role.name);
          } catch (error) {
            this.#util.showError(error.message);
          }
        } catch (error) {
          this.#util.showError(
            `Failed to add privileges to the security role: ${error.message}`
          );
        }
      } catch (error) {
        this.#util.showError(
          `Failed to retrieve 'prvCreateAccount' and 'prvReadAccount' privileges: ${error.message}`
        );
      }
    } else {
      this.#util.showError(
        "Failed to create security role. Cannot add privileges."
      );
      return;
    }
  }

  async #showRolePrivileges(roleId, name) {
    // Get the roles currently associated with the role

    try {
      const rolePrivileges = await this.#client.RetrieveMultiple(
        `roles(${roleId})/roleprivileges_association`,
        "$select=name"
      );

      this.#util.appendMessage(
        `The ${name} security role has the following ${rolePrivileges.value.length} privileges:`
      );
      let list = [];
      rolePrivileges.value.forEach((privilege) => {
        list.push(`<li>${privilege.name}</li>`);
      });
      this.#util.appendMessage(list.join(""), null, "ul");
    } catch (error) {
      throw new Error(
        `Failed to retrieve privileges for role ${roleId}: ${error.message}`
      );
    }
  }

  //#endregion Section 8: Bound Action AddPrivilegesRole
}
```



### See also

[Use the Dataverse Web API](../overview.md)<br />
[Use Web API functions](../use-web-api-functions.md)<br />
[Use Web API actions](../use-web-api-actions.md)<br />
[Web API Samples](../web-api-samples.md)<br />
[Web API Functions and Actions Sample](../web-api-functions-actions-sample.md)<br />
[Web API Functions and Actions Sample (C#)](webapiservice-functions-and-actions.md)<br />
[Web API Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md)<br />
[Web API Basic Operations Sample (Client-side JavaScript)](basic-operations-client-side-javascript.md)<br />
[Web API Query Data Sample (Client-side JavaScript)](query-data-client-side-javascript.md)<br />
[Web API Conditional Operations Sample (Client-side JavaScript)](conditional-operations-client-side-javascript.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
