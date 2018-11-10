You can create a client for a specific CDS environment and not provide the user any options about which environment they can connect with. Only valid users for that specific environment can use your client.

If you want people using your client to be able to connect to any CDS environment they have access to you could prompt them to enter the URL for their environment, but this is not recommended. Each user may have access to multiple CDS environments. Users may not know or remember the URL for their environment. Expecting people to enter this URL is bound to frustrate users. 

Instead, your client should provide a list of each of the available environments based on the user’s credentials. If there is more than one environment available, your application should prompt the user to choose which environment they want to connect with.

With CDS for Apps, server and organization allocation may change as part of datacenter management and load balancing. Therefore, a discovery service provides a way to discover which server is serving an instance at a given time.