This application implements a client program and a server programthat communicate with each other using TCP sockets.

The server process hosts a key-value store that clients can interact with. Specific interactions include the following:

- Storing key/value pairs into the store.
- Retrieving key/value pairs from the store
- Listing the key set and list the value set.



#### Key-Value store

key: the name of the item

Value, which is the actual content of the item.

A key-value store provides the following basic functions:

| **Function**    | **Description**                                              |
| --------------- | ------------------------------------------------------------ |
| get(key)        | Gets the value of the corresponding key from the key-value store |
| put(key, value) | Updates the value of the corresponding key in the key-value store or create a new pair of key value in the key value store if the key doesn’t currently exist. |
| mappings        | Retrieve all the key-value pairs from the key-value store    |
| keyset          | Retrieve all the keys from the key-value store.              |
| values          | Retrieve all the values from the key-value store.            |
| help            | Allows clients to list all the available functions provided by the server. |
| bye             | Terminates the process.                                      |



#### Client-Server Interactions 

The client program can interact with the server from command line interfaces. 

The server process will be started in the terminal first by running "python server.py".

We assume that this service is running on a fixed port number, e.g. 50000, that is known by the client. Then the client program should be invoked in another terminal window by executing "python client.py".

After this, the client program asks for the IP address or hostname of the server that* user should type in. If the IP address or hostname is valid, the client should see the following messages:

> python client.py
>
>  Welcome to the KeyValue Service Client
>
> Enter the IP address or Hostname of the server: localhost
>
> Please wait while I connect you...

Once a connection is established, the client should receive a welcoming message from the server and prints it on the screen. Meanwhile, a prompt will show up for the user to enter commands.

All user commands are entered on a single line. The client stays in a loop reading a command typed by the user, sending the command to the server, and reading and displaying the response. The client terminates after it receives bye command from the user.

Following is a sample interaction between the client and the server, as seen from the client’s side:

> *python client.py*
>
> *Welcome to the KeyValue Service Client*
>
> *Enter the IP address or Hostname of the server: localhost*
>
> *Please wait while I connect you...*
>
> *Welcome to the KeyValue Service*
>
> *KeyValue Service> help*
>
> *help*
>
> *get key*
>
> *put key value*
>
> *values*
>
> *keyset*
>
> *mappings*
>
> *bye*
>
> *KeyValue Service> mappings*
>
> *a 1*
>
> *aaa a 4*
>
> *b 2*
>
> *KeyValue Service> put aaa a 5*
>
> *Ok.*
>
> *KeyValue Service> mappings*
>
> *a 1*
>
> *aaa a 5*
>
> *b 2*
>
> *KeyValue Service> get aaa a*
>
> *5*
>
> *KeyValue Service> keyset*
>
> *[a, aaa a, b]*
>
> *KeyValue Service> values*
>
> *[1, 5, 2]*
>
> *KeyValue Service> bye*
>
> *See you later.*
>
> 



