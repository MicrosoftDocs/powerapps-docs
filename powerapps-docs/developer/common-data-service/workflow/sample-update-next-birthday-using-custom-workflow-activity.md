---
title: "Sample: Update next birthday using a custom workflow activity (Common Data Service for Apps) | Microsoft Docs"
description: "The sample demonstrates workflow activity returns the next birthday. Use this in a workflow that sends a birthday greeting to a customer. "
ms.custom: ""
ms.date: 06/16/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "samples"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 1cff83b0-1f7b-4ddb-a2af-b85f9f785529
caps.latest.revision: 21
author: "JimDaly"
ms.author: "jdaly"
manager: "amyla"
---
# Sample: Update next birthday using a custom workflow activity

Download the complete sample here [Custom workflow activities sample](https://code.msdn.microsoft.com/Custom-Workflow-Activities-eee57285). 

## Prerequisites

[!INCLUDE [sdk-prerequisite](../../../includes/sdk-prerequisite.md)]
  
## Requirements 
 
The following custom field must exist for this custom workflow activity to work:  
  
-   `Contact`.`new_nextbirthday`  
  
## Demonstrates  
 The following sample workflow activity returns the next birthday. Use this in a workflow that sends a birthday greeting to a customer.  
  
## Example  

```csharp
using System;
using System.Activities;
using System.Collections;
using System.Reflection;

using Microsoft.Xrm.Sdk;
using Microsoft.Xrm.Sdk.Messages;
using Microsoft.Xrm.Sdk.Query;
using Microsoft.Xrm.Sdk.Workflow;

namespace Microsoft.Crm.Sdk.Samples
{
    /// <summary>
    /// Activity will return the next upcoming birthday that has just passed
    /// 
    /// If this year's birthday has not yet occurred, it will return this year's birthday
    /// Otherwise, it will return the birthday for next year
    /// 
    /// A workflow can timeout when on this date
    /// </summary>
    [Persist]
    public sealed partial class ReleaseScenario_UpdateNextBirthday : CodeActivity
    {
        protected override void Execute(CodeActivityContext executionContext)
        {
            IWorkflowContext context = executionContext.GetExtension<IWorkflowContext>();

            //Create an Organization Service
            IOrganizationServiceFactory serviceFactory = executionContext.GetExtension<IOrganizationServiceFactory>();
            IOrganizationService service = serviceFactory.CreateOrganizationService(context.InitiatingUserId);

            //Retrieve the contact id
            Guid contactId = this.Contact.Get(executionContext).Id;

            //Create the request
            RetrieveRequest request = new RetrieveRequest();
            request.ColumnSet = new ColumnSet(new string[] { "birthdate" });
            request.Target = new EntityReference(EntityName.Contact, contactId);

            //Retrieve the entity to determine what the birthdate is set at
            Entity entity = (Entity)((RetrieveResponse)service.Execute(request)).Entity;

            //Extract the date out of the entity
            DateTime? birthdate;
            if (entity.Contains(ContactAttributes.Birthdate))
            {
                birthdate = (DateTime?)entity[ContactAttributes.Birthdate];
            }
            else
            {
                birthdate = null;
            }

            //Check to see if the current birthday is set. We don't want the activity to fail if the birthdate is not set
            if (birthdate == null)
            {
                return;
            }

            //Calculate the next birthdate. Encapsulated in a methdo so that the method can be used in the test case for verification purposes
            DateTime nextBirthdate = CalculateNextBirthday(birthdate.Value);

            //Update the next birthday field on the entity
            Entity updateEntity = new Entity(EntityName.Contact);
            updateEntity.Id = contactId;
            updateEntity["new_nextbirthday"] = nextBirthdate;

            service.Update(updateEntity);
        }

        //Define the properties
        [RequiredArgument]
        [Input("Update Next Birthdate for")]
        [ReferenceTarget("contact")]
        public InArgument<EntityReference> Contact { get; set; }

        private DateTime CalculateNextBirthday(DateTime birthdate)
        {
            DateTime nextBirthday = new DateTime(birthdate.Year, birthdate.Month, birthdate.Day);

            //Check to see if this birthday occurred on a leap year
            bool leapYearAdjust = false;
            if (nextBirthday.Month == 2 &amp;&amp; nextBirthday.Day == 29)
            {
                //Sanity check, was that year a leap year
                if (DateTime.IsLeapYear(nextBirthday.Year))
                {
                    //Check to see if the current year is a leap year
                    if (!DateTime.IsLeapYear(DateTime.Now.Year))
                    {
                        //Push the date to March 1st so that the date arithmetic will function correctly
                        nextBirthday = nextBirthday.AddDays(1);
                        leapYearAdjust = true;
                    }
                }
                else
                {
                    throw new Exception("Invalid Birthdate specified", new ArgumentException("Birthdate"));
                }
            }

            //Calculate the year difference
            nextBirthday = nextBirthday.AddYears(DateTime.Now.Year - nextBirthday.Year);

            //Check to see if the date was adjusted
            if (leapYearAdjust &amp;&amp; DateTime.IsLeapYear(nextBirthday.Year))
            {
                nextBirthday = nextBirthday.AddDays(-1);
            }

            return nextBirthday;
        }
    }

    public sealed partial class ReleaseScenario_MessageName : CodeActivity
    {
        protected override void Execute(CodeActivityContext executionContext)
        {
            IWorkflowContext context = executionContext.GetExtension<IWorkflowContext>();

            //Set the variable
            MessageName.Set(executionContext, context.MessageName);
        }

        //Define the properties
        [Output("Message Name")]
        public OutArgument<string> MessageName { get; set; }
    }

    /// <summary>
    /// Calculates the credit score based on the SSN and name. 
    /// </summary>
    /// <remarks>
    /// This depends on a custom entity called Loan Application and customizations to Contact.
    /// 
    /// Loan Application requires the following properties:
    /// <list>
    ///		<item>Schema Name: new_loanapplication</item>
    ///		<item>Attribute: new_loanapplicationid as the primary key</item>
    ///		<item>Attribute: new_creditscore of type int with min of 0 and max of 1000 (if it is to be updated)</item>
    ///		<item>Attribute: new_loanamount of type money with default min/max</item>
    ///		<item>Customize the form to include the attribute new_loanapplicantid</item>
    /// </list>
    /// 
    /// Contact Requires the following customizations
    /// <list>
    ///		<item>Attribute: new_ssn as nvarchar with max length of 15</item>
    ///		<item>One-To-Many Relationship with these properties:
    ///			<list>
    ///				<item>Relationship Definition Schema Name: new_loanapplicant</item>
    ///				<item>Relationship Definition Related Entity Name: Loan Application</item>
    ///				<item>Relationship Atttribute Schema Name: new_loanapplicantid</item>
    ///				<item>Relationship Behavior Type: Referential</item>
    ///			</list>
    ///		</item>
    /// </list>
    /// 
    /// The activity takes, as input, a EntityReference to the Loan Application and a boolean indicating whether new_creditscore should be updated to the credit score.
    /// </remarks>
    /// <exception cref=">ArgumentNullException">Thrown when LoanApplication is null</exception>
    /// <exception cref=">ArgumentException">Thrown when LoanApplication is not a EntityReference to a LoanApplication entity</exception>
    public sealed partial class RetrieveCreditScore : CodeActivity
    {
        private const string CustomEntity = "new_loanapplication";

        protected override void Execute(CodeActivityContext executionContext)
        {
            //Check to see if the EntityReference has been set
            EntityReference loanApplication = this.LoanApplication.Get(executionContext);
            if (loanApplication == null)
            {
                throw new InvalidOperationException("Loan Application has not been specified", new ArgumentNullException("Loan Application"));
            }
            else if (loanApplication.LogicalName != CustomEntity)
            {
                throw new InvalidOperationException("Loan Application must reference a Loan Application entity",
                    new ArgumentException("Loan Application must be of type Loan Application", "Loan Application"));
            }

            //Retrieve the CrmService so that we can retrieve the loan application
            IWorkflowContext context = executionContext.GetExtension<IWorkflowContext>();
            IOrganizationServiceFactory serviceFactory = executionContext.GetExtension<IOrganizationServiceFactory>();
            IOrganizationService service = serviceFactory.CreateOrganizationService(context.InitiatingUserId);

            //Retrieve the Loan Application Entity
            Entity loanEntity;
            {
                //Create a request
                RetrieveRequest retrieveRequest = new RetrieveRequest();
                retrieveRequest.ColumnSet = new ColumnSet(new string[] { "new_loanapplicationid", "new_loanapplicantid" });
                retrieveRequest.Target = loanApplication;

                //Execute the request
                RetrieveResponse retrieveResponse = (RetrieveResponse)service.Execute(retrieveRequest);

                //Retrieve the Loan Application Entity
                loanEntity = retrieveResponse.Entity as Entity;
            }

            //Retrieve the Contact Entity
            Entity contactEntity;
            {
                //Create a request
                EntityReference loanApplicantId = (EntityReference)loanEntity["new_loanapplicantid"];

                RetrieveRequest retrieveRequest = new RetrieveRequest();
                retrieveRequest.ColumnSet = new ColumnSet(new string[] { "fullname", "new_ssn", "birthdate" });
                retrieveRequest.Target = loanApplicantId;

                //Execute the request
                RetrieveResponse retrieveResponse = (RetrieveResponse)service.Execute(retrieveRequest);

                //Retrieve the Loan Application Entity
                contactEntity = retrieveResponse.Entity as Entity;
            }

            //Retrieve the needed properties
            string ssn = (string)contactEntity["new_ssn"];
            string name = (string)contactEntity[ContactAttributes.FullName];
            DateTime? birthdate = (DateTime?)contactEntity[ContactAttributes.Birthdate];
            int creditScore;

            //This is where the logic for retrieving the credit score would be inserted
            //We are simply going to return a random number
            creditScore = (new Random()).Next(0, 1000);

            //Set the credit score property
            this.CreditScore.Set(executionContext, creditScore);

            //Check to see if the credit score should be saved to the entity
            //If the value of the property has not been set or it is set to true
            if (null != this.UpdateEntity &amp;&amp; this.UpdateEntity.Get(executionContext))
            {
                //Create the entity
                Entity updateEntity = new Entity(loanApplication.LogicalName);
                updateEntity["new_loanapplicationid"] = loanEntity["new_loanapplicationid"];
                updateEntity["new_creditscore"] = this.CreditScore.Get(executionContext);

                //Update the entity
                service.Update(updateEntity);
            }
        }

        //Define the properties
        [Input("Loan Application")]
        [ReferenceTarget(CustomEntity)]
        public InArgument<EntityReference> LoanApplication { get; set; }

        [Input("Update Entity's Credit Score")]
        [Default("true")]
        public InArgument<bool> UpdateEntity { get; set; }

        [Output("Credit Score")]
        [AttributeTarget(CustomEntity, "new_creditscore")]
        public OutArgument<int> CreditScore { get; set; }
    }
}
```
  
### See also

[Custom Workflow Activities (Workflow Assemblies)](custom-workflow-activities-workflow-assemblies.md)<br />
[Sample: Calculate a Credit Score with a Custom Workflow Activity](sample-calculate-credit-score-custom-workflow-activity.md)<br />
[Add Metadata to a Custom Workflow Activity](add-metadata-custom-workflow-activity.md)<br />
<xref:Microsoft.Xrm.Sdk.Workflow.IWorkflowContext>