### cmpe273-lab3 
### SJSU ID:012566333 (Premal Dattatray Samale)
### Description: Implement sending "Hello World" from client to server via UDP using Twisted Lib.Answer to this question: "What happened when you send message from client in Multicast UDP when server is not available?" 



Requirement :Twisted lib.
             Python version: 3.5 is used
            
### Question: 
    What happened when you send message from client in Multicast UDP 
    when server is not available?"
### Answer:  
    When multicast message is sent from client and server is not available,below things happened
    1.  All listeners on the multicast address including the client received message.But in this case 
        server is not available so server did not receive message.
    2.  Client did not provide notification of undelivered message.
    3.  Also client in multicast UDP did not show any error message related to the server unavailibility.
               








