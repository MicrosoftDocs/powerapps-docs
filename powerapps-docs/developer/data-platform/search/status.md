---
title: "Dataverse Search status (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use Dataverse search status to check the status of Dataverse search." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 10/20/2023
ms.reviewer: jdaly
ms.topic: article
author: mspilde # GitHub ID
ms.author: mspilde # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
---
# Dataverse Search status

Use search status to know:

- Whether search is enabled.
- Which tables and columns are enabled for search.

#### [SDK for .NET](#tab/sdk)

```csharp
static void CheckSearchStatus(IOrganizationService service) {
   try
   {     
      OrganizationResponse searchStatusResponse = service.Execute(new OrganizationRequest("searchstatus"));
  
      string responseString = searchStatusResponse.Results["response"];

      Console.WriteLine(responseString);
      //Expect that this value is an escaped string containing JSON that must be parsed
   }
   catch (FaultException<OrganizationServiceFault> osf)
   {
      Console.WriteLine($"OrganizationServiceFault:{osf.Message}");
      // Fails here, Due to plug-in in Custom API?

      /*
      ErrorCode: 0x80048D0A IsvAbortedInternalServerError
      Message: Object reference not set to an instance of an object.
      
      */
   }
   catch (Exception ex) {

      Console.WriteLine($"Exception:{ex.Message}");
   }      
}
```

**Output**

```
OutputSearchStatus START

        Status: Provisioned
        LockboxStatus: Disabled
        CMKStatus: Disabled
        Entity Status Results:

                entitylogicalname: account
                objecttypecode: 1
                primarynamefield: name
                lastdatasynctimestamp: 1555508!10/16/2023 02:21:59
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:00
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        accountid        indexfieldname:a_0
                        accountnumber    indexfieldname:a0w
                        address1_city    indexfieldname:a0x
                        createdon        indexfieldname:i_0
                        emailaddress1    indexfieldname:a0y
                        entityimage_url  indexfieldname:h_0
                        modifiedon       indexfieldname:j_0
                        name     indexfieldname:d_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        primarycontactid         indexfieldname:a0z
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        telephone1       indexfieldname:a12
                        telephone2       indexfieldname:a13
                        versionnumber    indexfieldname:e_0


                entitylogicalname: activitymimeattachment
                objecttypecode: 1001
                primarynamefield: filename
                lastdatasynctimestamp: 1555512!10/16/2023 02:32:21
                lastprincipalobjectaccesssynctimestamp:
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        activitymimeattachmentid         indexfieldname:a_0
                        activitysubject  indexfieldname:a14
                        body     indexfieldname:l_0
                        filename         indexfieldname:d_0
                        mimetype         indexfieldname:a15
                        objectid         indexfieldname:a16
                        objecttypecode   indexfieldname:a19
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: annotation
                objecttypecode: 5
                primarynamefield: subject
                lastdatasynctimestamp: 1555508!10/16/2023 02:22:02
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:02
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        annotationid     indexfieldname:a_0
                        createdon        indexfieldname:i_0
                        documentbody     indexfieldname:k_0
                        filename         indexfieldname:a00
                        isdocument       indexfieldname:a01
                        mimetype         indexfieldname:a03
                        modifiedon       indexfieldname:j_0
                        notetext         indexfieldname:a04
                        objectid         indexfieldname:a05
                        objecttypecode   indexfieldname:a08
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        subject  indexfieldname:d_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: appointment
                objecttypecode: 4201
                primarynamefield: subject
                lastdatasynctimestamp: 1555508!10/16/2023 02:22:01
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:01
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        activityid       indexfieldname:a_0
                        createdon        indexfieldname:i_0
                        formattedscheduledend    indexfieldname:a1a
                        formattedscheduledstart  indexfieldname:a1b
                        instancetypecode         indexfieldname:a1c
                        location         indexfieldname:a1e
                        modifiedon       indexfieldname:j_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        regardingobjecttypecode  indexfieldname:a1f
                        scheduledend     indexfieldname:a1g
                        scheduledstart   indexfieldname:a1h
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        subject  indexfieldname:d_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: botcomponent
                objecttypecode: 10089
                primarynamefield: name
                lastdatasynctimestamp: 1555499!10/16/2023 02:08:10
                lastprincipalobjectaccesssynctimestamp: 1504570!10/16/2023 02:08:10
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        botcomponentid   indexfieldname:a_0
                        createdon        indexfieldname:i_0
                        filedata         indexfieldname:a09
                        modifiedon       indexfieldname:j_0
                        name     indexfieldname:d_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: contact
                objecttypecode: 2
                primarynamefield: fullname
                lastdatasynctimestamp: 1555508!10/16/2023 02:22:01
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:01
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        address1_city    indexfieldname:a0a
                        address1_telephone1      indexfieldname:a0b
                        contactid        indexfieldname:a_0
                        createdon        indexfieldname:i_0
                        emailaddress1    indexfieldname:a0c
                        entityimage_url  indexfieldname:h_0
                        firstname        indexfieldname:a0d
                        fullname         indexfieldname:d_0
                        lastname         indexfieldname:a0e
                        middlename       indexfieldname:a0f
                        mobilephone      indexfieldname:a0g
                        modifiedon       indexfieldname:j_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        parentcustomerid         indexfieldname:a0h
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        telephone1       indexfieldname:a0k
                        versionnumber    indexfieldname:e_0


                entitylogicalname: email
                objecttypecode: 4202
                primarynamefield: subject
                lastdatasynctimestamp: 1555512!10/16/2023 02:32:20
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:32:21
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        acceptingentityid        indexfieldname:a0l
                        activityid       indexfieldname:a_0
                        attachmentopencount      indexfieldname:a0o
                        createdon        indexfieldname:i_0
                        linksclickedcount        indexfieldname:a0p
                        modifiedon       indexfieldname:j_0
                        opencount        indexfieldname:a0q
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        regardingobjectid        indexfieldname:a0r
                        regardingobjecttypecode  indexfieldname:a0u
                        replycount       indexfieldname:a0v
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        subject  indexfieldname:d_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: fax
                objecttypecode: 4204
                primarynamefield: subject
                lastdatasynctimestamp: 1555508!10/16/2023 02:22:02
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:02
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        activityid       indexfieldname:a_0
                        createdby        indexfieldname:a1w
                        createdon        indexfieldname:i_0
                        modifiedon       indexfieldname:j_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        prioritycode     indexfieldname:a1z
                        regardingobjectid        indexfieldname:a21
                        regardingobjecttypecode  indexfieldname:a24
                        scheduledend     indexfieldname:a25
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        subject  indexfieldname:d_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: goal
                objecttypecode: 9600
                primarynamefield: title
                lastdatasynctimestamp: 1555508!10/16/2023 02:22:03
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:03
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        actualstring     indexfieldname:a26
                        createdon        indexfieldname:i_0
                        entityimage_url  indexfieldname:h_0
                        fiscalperiod     indexfieldname:a27
                        fiscalyear       indexfieldname:a29
                        goalenddate      indexfieldname:a2b
                        goalid   indexfieldname:a_0
                        goalownerid      indexfieldname:a2c
                        goalstartdate    indexfieldname:a2f
                        inprogressstring         indexfieldname:a2g
                        metricid         indexfieldname:a2h
                        modifiedon       indexfieldname:j_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        parentgoalid     indexfieldname:a2k
                        percentage       indexfieldname:a2n
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        targetstring     indexfieldname:a2o
                        title    indexfieldname:d_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: knowledgearticle
                objecttypecode: 9953
                primarynamefield: title
                lastdatasynctimestamp: 1555508!10/16/2023 02:22:03
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:03
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        articlepublicnumber      indexfieldname:a3w
                        content  indexfieldname:a3x
                        createdby        indexfieldname:a3y
                        createdon        indexfieldname:i_0
                        createdonbehalfby        indexfieldname:a41
                        description      indexfieldname:a44
                        isinternal       indexfieldname:a45
                        islatestversion  indexfieldname:a47
                        isprimary        indexfieldname:a49
                        isrootarticle    indexfieldname:a4b
                        keywords         indexfieldname:a4d
                        knowledgearticleid       indexfieldname:a_0
                        knowledgearticleviews    indexfieldname:a4e
                        languagelocaleid         indexfieldname:a4f
                        majorversionnumber       indexfieldname:a4i
                        minorversionnumber       indexfieldname:a4j
                        modifiedby       indexfieldname:a4k
                        modifiedon       indexfieldname:j_0
                        msdyn_contentstore       indexfieldname:a4n
                        msdyn_externalreferenceid        indexfieldname:a4o
                        msdyn_ingestedarticleurl         indexfieldname:a4p
                        msdyn_integratedsearchproviderid         indexfieldname:a4q
                        msdyn_isingestedarticle  indexfieldname:a4t
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        owningteam       indexfieldname:a4v
                        owninguser       indexfieldname:a4y
                        parentarticlecontentid   indexfieldname:a51
                        previousarticlecontentid         indexfieldname:a54
                        rating   indexfieldname:a57
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        subjectid        indexfieldname:a58
                        title    indexfieldname:d_0
                        transactioncurrencyid    indexfieldname:a5b
                        versionnumber    indexfieldname:e_0


                entitylogicalname: letter
                objecttypecode: 4207
                primarynamefield: subject
                lastdatasynctimestamp: 1555508!10/16/2023 02:22:02
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:02
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        activityid       indexfieldname:a_0
                        createdby        indexfieldname:a3m
                        createdon        indexfieldname:i_0
                        modifiedon       indexfieldname:j_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        prioritycode     indexfieldname:a3p
                        regardingobjectid        indexfieldname:a3r
                        regardingobjecttypecode  indexfieldname:a3u
                        scheduledend     indexfieldname:a3v
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        subject  indexfieldname:d_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: metric
                objecttypecode: 9603
                primarynamefield: name
                lastdatasynctimestamp: 1555508!10/16/2023 02:22:01
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:01
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        amountdatatype   indexfieldname:a3h
                        createdon        indexfieldname:i_0
                        isamount         indexfieldname:a3j
                        metricid         indexfieldname:a_0
                        modifiedon       indexfieldname:j_0
                        name     indexfieldname:d_0
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: msdyn_kbattachment
                objecttypecode: 10113
                primarynamefield: msdyn_filename
                lastdatasynctimestamp: 1555512!10/16/2023 02:32:21
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:32:21
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        createdon        indexfieldname:i_0
                        modifiedon       indexfieldname:j_0
                        msdyn_fileattachment     indexfieldname:a1i
                        msdyn_filename   indexfieldname:d_0
                        msdyn_kbattachmentid     indexfieldname:a_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: mspcat_catalogsubmissionfiles
                objecttypecode: 10293
                primarynamefield: mspcat_name
                lastdatasynctimestamp: 1555508!10/16/2023 02:22:02
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:02
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        createdon        indexfieldname:i_0
                        modifiedon       indexfieldname:j_0
                        mspcat_catalogsubmissionfilesid  indexfieldname:a_0
                        mspcat_name      indexfieldname:d_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: phonecall
                objecttypecode: 4210
                primarynamefield: subject
                lastdatasynctimestamp: 1555508!10/16/2023 02:22:01
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:01
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        activityid       indexfieldname:a_0
                        createdby        indexfieldname:a2z
                        createdon        indexfieldname:i_0
                        modifiedon       indexfieldname:j_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        prioritycode     indexfieldname:a32
                        regardingobjectid        indexfieldname:a34
                        regardingobjecttypecode  indexfieldname:a37
                        scheduledend     indexfieldname:a38
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        subject  indexfieldname:d_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: powerpagecomponent
                objecttypecode: 10239
                primarynamefield: name
                lastdatasynctimestamp: 1555512!10/16/2023 02:32:20
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:32:20
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        createdon        indexfieldname:i_0
                        modifiedon       indexfieldname:j_0
                        name     indexfieldname:d_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        powerpagecomponentid     indexfieldname:a_0
                        searchcontent    indexfieldname:a1v
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: recurringappointmentmaster
                objecttypecode: 4251
                primarynamefield: subject
                lastdatasynctimestamp: 1555508!10/16/2023 02:22:05
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:05
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        activityid       indexfieldname:a_0
                        createdon        indexfieldname:i_0
                        modifiedon       indexfieldname:j_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        regardingobjecttypecode  indexfieldname:a3l
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        subject  indexfieldname:d_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: socialactivity
                objecttypecode: 4216
                primarynamefield: subject
                lastdatasynctimestamp: 1555508!10/16/2023 02:22:04
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:05
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        activityid       indexfieldname:a_0
                        community        indexfieldname:a1j
                        createdon        indexfieldname:i_0
                        modifiedon       indexfieldname:j_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        postfromprofileid        indexfieldname:a1l
                        prioritycode     indexfieldname:a1o
                        regardingobjectid        indexfieldname:a1q
                        regardingobjecttypecode  indexfieldname:a1t
                        sentimentvalue   indexfieldname:a1u
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        subject  indexfieldname:d_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: socialprofile
                objecttypecode: 99
                primarynamefield: profilename
                lastdatasynctimestamp: 1555508!10/16/2023 02:22:04
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:04
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        blocked  indexfieldname:a39
                        community        indexfieldname:a3b
                        createdon        indexfieldname:i_0
                        customerid       indexfieldname:a3d
                        modifiedon       indexfieldname:j_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        profilefullname  indexfieldname:a3g
                        profilename      indexfieldname:d_0
                        socialprofileid  indexfieldname:a_0
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        versionnumber    indexfieldname:e_0


                entitylogicalname: task
                objecttypecode: 4212
                primarynamefield: subject
                lastdatasynctimestamp: 1555508!10/16/2023 02:22:04
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:04
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        activityid       indexfieldname:a_0
                        createdby        indexfieldname:a2p
                        createdon        indexfieldname:i_0
                        modifiedon       indexfieldname:j_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        prioritycode     indexfieldname:a2s
                        regardingobjectid        indexfieldname:a2u
                        regardingobjecttypecode  indexfieldname:a2x
                        scheduledend     indexfieldname:a2y
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        subject  indexfieldname:d_0
                        versionnumber    indexfieldname:e_0


OutputSearchStatus END
```

#### [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/data/v9.2/searchstatus HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

```

The `response` property returned by <xref:Microsoft.Dynamics.CRM.searchstatusResponse?text=searchstatusResponse ComplexType> is an escaped string containing JSON data. The `status` property value can be either: `notprovisioned`, `provisioninginprogress`, or `provisioned`.

When not provisioned, you should get a response like this:

**Response**

```http
HTTP/1.1 200 OK

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchstatusResponse",
  "response": "{\"value\":{\"status\":\"notprovisioned\",\"lockboxstatus\":\"Unknown\"}}"
}
```

When search is enabled, there is more data that describes the search status for the org.

**Response**

```http
HTTP/1.1 200 OK

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchstatusResponse",
  "response": "{\"value\":{\"entitystatusresults\":[{\"entitylogicalname\":\"account\",\"objecttypecode\":1,\"primarynamefield\":\"name\",\"lastdatasynctimestamp\":\"73630169!09/12/2022 14:26:14\",\"lastprincipalobjectaccesssynctimestamp\":\"72969347!09/12/2022 14:26:14\",\"entitystatus\":\"EntitySyncComplete\",\"searchableindexedfieldinfomap\":{\"emailaddress1\":{\"indexfieldname\":\"a3x\"},\"address1_city\":{\"indexfieldname\":\"a3y\"},\"modifiedon\":{\"indexfieldname\":\"j_0\"},\"telephone1\":{\"indexfieldname\":\"a3z\"},\"statecode\":{\"indexfieldname\":\"f_0\"},\"primarycontactid\":{\"indexfieldname\":\"a40\"},\"statuscode\":{\"indexfieldname\":\"g_0\"},\"createdon\":{\"indexfieldname\":\"i_0\"},\"entityimage_url\":{\"indexfieldname\":\"h_0\"},\"industrycode\":{\"indexfieldname\":\"a43\"},\"name\":{\"indexfieldname\":\"d_0\"},\"owningbusinessunit\":{\"indexfieldname\":\"c_0\"},\"crdcb_testrollupfield\":{\"indexfieldname\":\"a45\"},\"ownerid\":{\"indexfieldname\":\"b_0\"},\"accountnumber\":{\"indexfieldname\":\"a46\"},\"telephone2\":{\"indexfieldname\":\"a47\"},\"versionnumber\":{\"indexfieldname\":\"e_0\"},\"accountid\":{\"indexfieldname\":\"a_0\"},\"crdcb_throwawaydate\":{\"indexfieldname\":\"a48\"},\"crdcb_budget\":{\"indexfieldname\":\"a8f\"}}}, 
  
  <Information on other tables removed for brevity> 
  
  ],\"status\":\"provisioned\",\"lockboxstatus\":\"Disabled\",\"cmkstatus\":\"Disabled\"}}"
}
```

When unescaped, the JSON of the `response` property looks like this:

```json
{
  "value": {
    "entitystatusresults": [
      {
        "entitylogicalname": "account",
        "objecttypecode": 1,
        "primarynamefield": "name",
        "lastdatasynctimestamp": "73630169!09/12/2022 14:26:14",
        "lastprincipalobjectaccesssynctimestamp": "72969347!09/12/2022 14:26:14",
        "entitystatus": "EntitySyncComplete",
        "searchableindexedfieldinfomap": {
          "emailaddress1": { "indexfieldname": "a3x" },
          "address1_city": { "indexfieldname": "a3y" },
          "modifiedon": { "indexfieldname": "j_0" },
          "telephone1": { "indexfieldname": "a3z" },
          "statecode": { "indexfieldname": "f_0" },
          "primarycontactid": { "indexfieldname": "a40" },
          "statuscode": { "indexfieldname": "g_0" },
          "createdon": { "indexfieldname": "i_0" },
          "entityimage_url": { "indexfieldname": "h_0" },
          "industrycode": { "indexfieldname": "a43" },
          "name": { "indexfieldname": "d_0" },
          "owningbusinessunit": { "indexfieldname": "c_0" },
          "ownerid": { "indexfieldname": "b_0" },
          "accountnumber": { "indexfieldname": "a46" },
          "telephone2": { "indexfieldname": "a47" },
          "versionnumber": { "indexfieldname": "e_0" },
          "accountid": { "indexfieldname": "a_0" }
        }
      },

  <Information on other tables removed for brevity> 

    ],
    "status": "provisioned",
    "lockboxstatus": "Disabled",
    "cmkstatus": "Disabled"
  }
}
```

The `entitystatusresults` contains information about each table configured for search. For each table, the `searchableindexedfieldinfomap` tells you which columns are included in search for that table. The `indexfieldname` property is for internal use only.

- `lockboxstatus` refers to the Power Platform Customer Lockbox. More information: [Securely access customer data using Customer Lockbox in Power Platform (preview)](/power-platform/admin/about-lockbox)
- `cmkstatus` refers to whether the environment has a customer managed key. More information: [Manage the encryption key](/power-platform/admin/manage-encryption-key)


#### [Search 2.0 endpoint](#tab/search)

**Request**

```http
GET [Organization URI]/api/search/v2.0/status HTTP/1.1
```

The response from the `search/v2.0/status` endpoint is the same as the Web API.

---


### See also

[Search for Dataverse records](overview.md)<br />
[Dataverse Search query](query.md)<br />
[Dataverse Search suggest](suggest.md)<br />
[Dataverse Search autocomplete](autocomplete.md)<br />
[Dataverse Search statistics](statistics.md)<br />
[Dataverse legacy search](legacy.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]